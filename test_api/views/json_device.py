from django.http import JsonResponse

# from .config_api import url_message
from .test_data import test_data_dev


def device(request):
    hive_device = test_data_dev
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
                # url_message += i['devEUI']
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
