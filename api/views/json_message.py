from django.http import JsonResponse
from time import localtime, strftime

import requests

from .config_api import payload, url_message
from .status_messages import net_status, char_status
from .conversion import uncomp_weight, temp_compensation


def message(request):
    payload['stop'] = strftime("%Y-%m-%dT%H:%M%S", localtime())
    payload['limit'] = 10
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
        work_data = [[record['time'], record['payloadHex']]
                     for record in hive_message['records']]

        timestamps = [i[0] for i in work_data]

        msg_len = len(work_data[0][1]) // 2
        messages = [i[1][j:j + 2]
                    for i in work_data for j in range(0, len(i[1]), 2)]
        messages = [messages[i:i + msg_len]
                    for i in range(0, len(messages), msg_len)]

        """
        Yes, I know, the whole next section is for changing endianess of
        parts of a message, but it is easier to realise in what format are
        data returned (hint: it's string) and then use Python's strenght in
        manipulation this data type
        """
        hive_humid = [int(messages[i][4], 16) for i in range(data_count)]
        status = [bin(int(messages[i][13], 16)) for i in range(data_count)]

        frame_id = [int(''.join(reversed(message[i][:2])), 16)
                    for i in range(data_count)]
        hive_temp = [int(''.join(reversed(message[i][2:4])), 16) / 10
                     for i in range(data_count)]
        pressure = [int(''.join(reversed(message[i][5:7])), 16)
                    for i in range(data_count)]
        bat_volt = [int(''.join(reversed(message[i][11:13])), 16) / 1000
                    for i in range(data_count)]

        weight = [
            uncomp_weight(
                int(''.join(reversed(messages[i][7:11])), 16),
            ) for i in range(data_count)
        ]
        hive_weight = [temp_compensation(
            weight[i], hive_temp[i]) for i in range(data_count)]

        return_data = {
            'time': [timestamps[i] for i in range(data_count)],
            'frame_id': [frame_id[i] for i in range(data_count)],
            'temperature': [hive_temp[i] for i in range(data_count)],
            'humidity': [hive_humid[i] for i in range(data_count)],
            'pressure': [pressure[i] for i in range(data_count)],
            'hive_weight': [hive_weight[i] for i in range(data_count)],
            'bat_voltage': [bat_volt[i] for i in range(data_count)],
            'device_status': [char_status(status[i]) for i in range(data_count)],
            'network_status': [net_status(status[i]) for i in range(data_count)]
        }
        return_data = [dict(zip(return_data.keys(), i))
                       for i in zip(*return_data.values())]

        return JsonResponse(return_data, safe=False, json_dumps_params={'indent': 4})
