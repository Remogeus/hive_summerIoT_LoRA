from django.http import JsonResponse

import requests

from .config_api import url_device


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
                url_message += i['devEUI']
