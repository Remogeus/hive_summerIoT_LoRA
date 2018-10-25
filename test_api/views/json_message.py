from django.http import JsonResponse
from time import localtime, strftime

from .config_api import payload
from .test_data import test_data_error, test_data_msg_ok
from .status_messages import net_status, char_status
from .conversion import uncomp_weight, temp_compensation


def message(request):
    payload['stop'] = strftime("%Y-%m-%dT%H:%M%S", localtime())
    payload['limit'] = 10
    hive_message = test_data_msg_ok
    # hive_message = test_data_error
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
        hive_humid = [int(messages[i][2], 16) for i in range(data_count)]
        status = [bin(int(messages[i][13], 16)) for i in range(data_count)]

        frame_id = [int(messages[i][1] + messages[i][0], 16)
                    for i in range(data_count)]
        hive_temp = [int(messages[i][3] + messages[i][2], 16) / 10
                     for i in range(data_count)]
        pressure = [int(messages[i][6] + messages[i][5], 16)
                    for i in range(data_count)]
        bat_volt = [int(messages[i][12] + messages[i][11], 16) / 1000
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
