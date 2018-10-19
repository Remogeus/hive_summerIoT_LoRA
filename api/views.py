from django.http import JsonResponse
from django.http import HttpResponse
import requests

# Create your views here.

calibration_index = 65536
zero_offset = 514.3
beta0 = 0.022

payload = {
    'token': 'yjHRpdbhce4VdJ43kTJ0RwqYpbIqQJDR'
}

url_device = 'api.pripoj.me/device/get'
url_message = 'api.pripoj.me/message/get/'

def device(request):
    hive_device = requests.get(url_device, params=payload).json()
    for i in hive_device:
        if i['_meta']['status'] == 'ERROR':
            return JsonResponse(
                {
                    'data_is_valid': False,
                    'error_code': i['records']['errorCode'],
                    'user_msg': i['records']['userMessage'],
                    'dev_msg': i['records']['devMessage'],
                    'msg_more': i['records']['more'],
                    'app_code': i['records']['applicationCode']
                },
                safe=False,
                json_dumps_params={'indent': 4}
            )
            break
        else:
            vendor = i['records']['vendor']
            if vendor == 'Beepad':
                return JsonResponse(
                    {
                        'data_is_valid': True,
                        'project_id': i['records']['projectID'],
                        'dev_eui': i['records']['dev_eui'],
                        'desc': i['records']['description'],
                        'model': i['records']['description'],
                        'desc': i['records']['description'],
                        'vendor': vendor
                    },
                    safe=False,
                    json_dumps_params={'indent': 4}
                )
                url_message += i['records']['dev_eui']

def message(request):
    hive_message = requests.get(url_message, params=payload).json()
        if hive_message['_meta']['status'] == 'ERROR':
                return JsonResponse(
                    {
                        'data_is_valid': False,
                        'error_code': i['records']['errorCode'],
                        'user_msg': i['records']['userMessage'],
                        'dev_msg': i['records']['devMessage'],
                        'msg_more': i['records']['more'],
                        'app_code': i['records']['applicationCode']
                    },
                    safe=False,
                    json_dumps_params={'indent': 4}
                )
        else:
            #toto dokoncit ziskani message z API
