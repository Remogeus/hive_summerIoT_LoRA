from django.http import JsonResponse
from django.http import HttpResponse
from time import localtime, strftime

import requests

"""
Calibration values taken from the manual for the device, found on
https://pripoj.me/wp-content/uploads/2017/08/Payload.pdf
"""
calibration_index = 65536
zero_offset = 514.3
beta0 = 0.022

# Payload with user token
payload = {
    'token': 'yjHRpdbhce4VdJ43kTJ0RwqYpbIqQJDR'
}


# URLs for communication with API
url_device = 'api.pripoj.me/device/get'
url_message = 'api.pripoj.me/message/get/'


def temp_compensation(weight, temperature):
    """ temp_compensation(weight, temperature)

        Returns a compensated weight of the hive, according to
        https://pripoj.me/wp-content/uploads/2017/08/Payload.pdf

        Parameters: @weight - float, uncompensated weight of the hive_name
                    @temperature - float, hive temperature aquired from sensor
        Returns:    float - compensated weight
    """
    return weight - (temperature * beta0)


def uncomp_weight(adc_readout):
    """ uncomp_weight(adc_readout)

        Returns a uncompensated weight of the hive from the readings of the ADC,
        according to https://pripoj.me/wp-content/uploads/2017/08/Payload.pdf

        Parameters: @adc_readout - int, raw uncalibrated load cell ADC readout
        Returns:    float - uncompensated weight
    """
    return (adc_readout / calibration_index) - zero_offset


def char_status(status):
    """ char_status(status)

        Returs charging status of the device

        Parameters: @status - integer, device status aquired from sensor
        Returns:    string - charging status
    """
    possible_status = {
    0: 'invalid status',
    1: 'charged',
    2: 'charging',
    3: 'discharged'
    }
    return possible_status.get(status & 0x03)


def net_status(status):
    """ net_status(status)

        Returs network join status of the device

        Parameters: @status - integer, device status aquired from sensor
        Returns:    string - network join status
    """
    possible_status = {
    0: 'initialized',
    4: 'joining',
    8: 'joined',
    12: 'join failed'
    }
    return possible_status.get(status & 0x0c)


def device(request):
    hive_device = requests.get(url_device, params=payload).json()
    if hive_device['_meta']['status'] == 'ERROR':
        return JsonResponse(
        {
            'data_is_valid': False,
            'error_code': hive_device['records']['errorCode'],
            'user_msg': hive_device['records']['userMessage'],
            'dev_msg': hive_device['records']['devMessage'],
            'msg_more': hive_device['records']['more'],
            'app_code': hive_device['records']['applicationCode']
        },
        safe=False,
        json_dumps_params={'indent': 4}
    )
    else:
        for i in hive_device['records']:
            vendor = i['vendor']
            if vendor == 'Beepad':
                return JsonResponse(
                    {
                        'data_is_valid': True,
                        'project_id': i['projectId'],
                        'dev_eui': i['devEUI'],
                        'desc': i['description'],
                        'model': i['model'],
                        'vendor': vendor
                    },
                    safe=False,
                    json_dumps_params={'indent': 4}
                )
                url_message += i['devEUI']


def message(request):
    payload[0]['stop'] = strftime("%Y-%m-%dT%H:%M%S", localtime())
    payload[0]['limit'] = 10
    hive_message = requests.get(url_message, params=payload).json()
    """
    testing if the data are valid, if not, error flag 'data_is_valid' is set
    to False and then in jQuery this is used to replace whole webpage with
    an error message
    """
       if hive_message['_meta']['status'] == 'ERROR':
            return JsonResponse(
                {
                    'data_is_valid': False,
                    'error_code': hive_message['records']['errorCode'],
                    'user_msg': hive_message['records']['userMessage'],
                    'dev_msg': hive_message['records']['devMessage'],
                    'msg_more': hive_message['records']['more'],
                    'app_code': hive_message['records']['applicationCode']
                },
                safe=False,
                json_dumps_params={'indent': 4}
            )
        else:
            data_count = int(hive_message['_meta']['count'])
            work_data = [[record['time'], record['payloadHex']] for record in hive_message['records']]

            msg_len = len(work_data[0][1])//2
            messages = [i[1][j:j+2] for i in work_data for j in range(0, len(i[1]), 2)]
            messages = [messages[i:i+msg_len] for i in range(0, len(messages), msg_len)]
            """
            Yes, I know, the whole next section is for changing endianess of
            parts of a message, but it is easier to realise in what format are
            data returned (hint: it's string) and then use Python's strenght in
            manipulation this data type
            """
            hive_humid = [int(messages[i][2], 16) for i in range(0, data_count)]
            status = [bin(int(messages[i][13], 16)) for i in range(0, data_count)]

            frame_id = [int(messages[i][1] + messages[i][0], 16) for i in range(0, data_count)]
            hive_temp = [int(messages[i][3] + messages[i][2], 16)/10 for i in range(0, data_count)]
            pressure = [int(messages[i][6] + messages[i][5], 16) for i in range(0, data_count)]
            bat_volt = [int(messages[i][12] + messages[i][11], 16)/1000 for i in range(0, data_count)]

            weight = [uncomp_weight(int(messages[i][10] + messages[i][9] +
                                        messages[i][8] + messages[i][7], 16)) for i in range(0, data_count)]
            hive_weight = [temp_compensation(weight[i], hive_temp[i]) for i in range(0, data_count)]

            for i in range(0, data_count):
                return JsonResponse(
                {
                    'time': work_data[i][0],
                    'frame_id': frame_id[i],
                    'temperature': hive_temp[i],
                    'humidity': hive_humid[i],
                    'pressure': pressure[i],
                    'hive_weight': hive_weight[i],
                    'bat_voltage': bat_volt[i],
                    'device_status': char_status(status[i]),
                    'network_status': net_status(status[i])
                },
                safe=False,
                json_dumps_params={'indent': 4}
                )
