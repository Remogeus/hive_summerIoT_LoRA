import json

calibration_index = 65536
zero_offset = 514.3
beta0 = 0.022

payload = {
    'token': 'yjHRpdbhce4VdJ43kTJ0RwqYpbIqQJDR'
}

url_device = 'api.pripoj.me/device/get'
url_message = 'api.pripoj.me/message/get/'


def temp_compensation(weight, temperature):
    return weight - (temperature * beta0)


def uncomp_weight(adc_readout):
    return (adc_readout / calibration_index) - zero_offset


test_data = {
    "_meta": {
        "status": "SUCCESS",
        "count": 10
    },
    "records": [
        {
            "devEUI": "4786E6ED00350042",
            "projectId": "TEST",
            "description": "Testovací teplotní čidlo",
            "model": "RHF1S001",
            "vendor": "Rising HF"
        },
        {
            "devEUI": "4786E6ED00350042",
            "projectId": "TEST",
            "description": "Testovací teplotní čidlo",
            "model": "RHF1S001",
            "vendor": "Rising HF"
        },
        {
            "devEUI": "4786E6ED00350042",
            "projectId": "TEST",
            "description": "Testovací teplotní čidlo",
            "model": "RHF1S001",
            "vendor": "Rising HF"
        },
        {
            "devEUI": "4786E6ED00350042",
            "projectId": "TEST",
            "description": "Testovací teplotní čidlo",
            "model": "RHF1S001",
            "vendor": "Rising HF"
        },
        {
            "devEUI": "4786E6ED00350042",
            "projectId": "TEST",
            "description": "Testovací teplotní čidlo",
            "model": "RHF1S001",
            "vendor": "Rising HF"
        },
        {
            "devEUI": "4786E6ED00350042",
            "projectId": "",
            "description": "Testovací teplotní čidlo",
            "model": "RHF1S001",
            "vendor": "Beepad"
        }
    ]
}

hive_device = test_data
if hive_device["_meta"]["status"] == "ERROR":
    print({
        "data_is_valid": False,
        "error_code": i["records"]["errorCode"],
        "user_msg": i["records"]["userMessage"],
        "dev_msg": i["records"]["devMessage"],
        "msg_more": i["records"]["more"],
        "app_code": i["records"]["applicationCode"]
    }
    )
else:
    for i in hive_device['records']:
        vendor = i["vendor"]
        if vendor == "Beepad":
            print(
                {
                    "data_is_valid": True,
                    "project_id": i["projectId"],
                    "dev_eui": i["devEUI"],
                    "desc": i["description"],
                    "model": i["model"],
                    "vendor": vendor
                },
            )
            url_message += i["devEUI"]
            print(url_message)
"""def message(request):
    payload[0]["stop"] = strftime("%Y-%m-%dT%H:%M%S", localtime())
    payload[0]["limit"] = 10
    hive_message = requests.get(url_message, params=payload).json()
       if hive_message["_meta"]["status"] == 'ERROR':
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
            for record in hive_message['records']:
                timecodes = record['time']
                messages = record['payloadHex']
                """
