from time import localtime, strftime

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

def dev_status(status):
    possible_status = {
    0: 'invalid status',
    1: 'charged',
    2: 'charging',
    3: 'discharged'
    }
    return possible_status.get(status & 0x03)

def net_status(status):
    possible_status = {
    0: 'initialized',
    4: 'joining',
    8: 'joined',
    12: 'join failed'
    }
    return possible_status.get(status & 0x0c)

"""test_data_dev = {
    "_meta": {
        "status": "ERROR",
        "count": 1
    },
    "records": {
        "errorCode": 404,
        "userMessage": "Not Found.",
        "devMessage": "That route was not found on the server.",
        "more": "Check route for misspellings.",
        "applicationCode": "N1000"
    }
}

hive_device = test_data_dev
if hive_device["_meta"]["status"] == "ERROR":
    print({
        "data_is_valid": False,
        "error_code": hive_device["records"]["errorCode"],
        "user_msg": hive_device["records"]["userMessage"],
        "dev_msg": hive_device["records"]["devMessage"],
        "msg_more": hive_device["records"]["more"],
        "app_code": hive_device["records"]["applicationCode"]
    }
    )
else:
"""
payload['stop'] = strftime("%Y-%m-%dT%H:%M:%S", localtime())
payload['limit'] = 10
print(payload)

test_data_msg = {
    "_meta":
    {
        "status": "SUCCESS",
        "count": 11
    },
    "records": [
        {
            "time": "2016-06-15T16:17:31.851+02:00",
            "devEUI": "4786E6ED00350042",
            "fPort": 8,
            "fCntUp": 9538,
            "aDRbit": 1,
            "fCntDn": 0,
            "payloadHex": "b4af4aa698d6574a6b4e2e5661ee",
            "micHex": "79b30671",
            "lrcid": "00000065",
            "lrrRSSI": -106.000000,
            "lrrSNR": 0.000000,
            "spFact": 12,
            "subBand": "G1",
            "channel": "LC1",
            "devLrrCnt": 1,
            "lrrid": "29000049",
            "lrrLAT": 50.120018,
            "lrrLON": 14.501301,
            "lrrs": [
                {
                    "Lrrid": "29000049",
                    "LrrRSSI": -106.000000,
                    "LrrSNR": 0.000000,
                }
            ]
        },
        {
            "time": "2016-06-15T16:17:31.851+02:00",
            "devEUI": "4786E6ED00350042",
            "fPort": 8,
            "fCntUp": 9538,
            "aDRbit": 1,
            "fCntDn": 0,
            "payloadHex": "2400c7003ada03b4312602730f06",
            "micHex": "79b30671",
            "lrcid": "00000065",
            "lrrRSSI": -106.000000,
            "lrrSNR": 0.000000,
            "spFact": 12,
            "subBand": "G1",
            "channel": "LC1",
            "devLrrCnt": 1,
            "lrrid": "29000049",
            "lrrLAT": 50.120018,
            "lrrLON": 14.501301,
            "lrrs": [
                {
                    "Lrrid": "29000049",
                    "LrrRSSI": -106.000000,
                    "LrrSNR": 0.000000,
                }
            ]
        },
        {
            "time": "2016-06-15T16:17:31.851+02:00",
            "devEUI": "4786E6ED00350042",
            "fPort": 8,
            "fCntUp": 9538,
            "aDRbit": 1,
            "fCntDn": 0,
            "payloadHex": "2400c7003ada03b4312602730f09",
            "micHex": "79b30671",
            "lrcid": "00000065",
            "lrrRSSI": -106.000000,
            "lrrSNR": 0.000000,
            "spFact": 12,
            "subBand": "G1",
            "channel": "LC1",
            "devLrrCnt": 1,
            "lrrid": "29000049",
            "lrrLAT": 50.120018,
            "lrrLON": 14.501301,
            "lrrs": [
                {
                    "Lrrid": "29000049",
                    "LrrRSSI": -106.000000,
                    "LrrSNR": 0.000000,
                }
            ]
        },
        {
            "time": "2016-06-15T16:17:31.851+02:00",
            "devEUI": "4786E6ED00350042",
            "fPort": 8,
            "fCntUp": 9538,
            "aDRbit": 1,
            "fCntDn": 0,
            "payloadHex": "2400c7003ada03b4312602730f09",
            "micHex": "79b30671",
            "lrcid": "00000065",
            "lrrRSSI": -106.000000,
            "lrrSNR": 0.000000,
            "spFact": 12,
            "subBand": "G1",
            "channel": "LC1",
            "devLrrCnt": 1,
            "lrrid": "29000049",
            "lrrLAT": 50.120018,
            "lrrLON": 14.501301,
            "lrrs": [
                {
                    "Lrrid": "29000049",
                    "LrrRSSI": -106.000000,
                    "LrrSNR": 0.000000,
                }
            ]
        },
        {
            "time": "2016-06-15T16:17:31.851+02:00",
            "devEUI": "4786E6ED00350042",
            "fPort": 8,
            "fCntUp": 9538,
            "aDRbit": 1,
            "fCntDn": 0,
            "payloadHex": "2400c7003ada03b4312602730f09",
            "micHex": "79b30671",
            "lrcid": "00000065",
            "lrrRSSI": -106.000000,
            "lrrSNR": 0.000000,
            "spFact": 12,
            "subBand": "G1",
            "channel": "LC1",
            "devLrrCnt": 1,
            "lrrid": "29000049",
            "lrrLAT": 50.120018,
            "lrrLON": 14.501301,
            "lrrs": [
                {
                    "Lrrid": "29000049",
                    "LrrRSSI": -106.000000,
                    "LrrSNR": 0.000000,
                }
            ]
        },
        {
            "time": "2016-06-15T16:17:31.851+02:00",
            "devEUI": "4786E6ED00350042",
            "fPort": 8,
            "fCntUp": 9538,
            "aDRbit": 1,
            "fCntDn": 0,
            "payloadHex": "2400c7003ada03b4312602730f09",
            "micHex": "79b30671",
            "lrcid": "00000065",
            "lrrRSSI": -106.000000,
            "lrrSNR": 0.000000,
            "spFact": 12,
            "subBand": "G1",
            "channel": "LC1",
            "devLrrCnt": 1,
            "lrrid": "29000049",
            "lrrLAT": 50.120018,
            "lrrLON": 14.501301,
            "lrrs": [
                {
                    "Lrrid": "29000049",
                    "LrrRSSI": -106.000000,
                    "LrrSNR": 0.000000,
                }
            ]
        },
        {
            "time": "2016-06-15T16:17:31.851+02:00",
            "devEUI": "4786E6ED00350042",
            "fPort": 8,
            "fCntUp": 9538,
            "aDRbit": 1,
            "fCntDn": 0,
            "payloadHex": "2400c7003ada03b4312602730f09",
            "micHex": "79b30671",
            "lrcid": "00000065",
            "lrrRSSI": -106.000000,
            "lrrSNR": 0.000000,
            "spFact": 12,
            "subBand": "G1",
            "channel": "LC1",
            "devLrrCnt": 1,
            "lrrid": "29000049",
            "lrrLAT": 50.120018,
            "lrrLON": 14.501301,
            "lrrs": [
                {
                    "Lrrid": "29000049",
                    "LrrRSSI": -106.000000,
                    "LrrSNR": 0.000000,
                }
            ]
        },
        {
            "time": "2016-06-15T16:17:31.851+02:00",
            "devEUI": "4786E6ED00350042",
            "fPort": 8,
            "fCntUp": 9538,
            "aDRbit": 1,
            "fCntDn": 0,
            "payloadHex": "2400c7003ada03b4312602730f09",
            "micHex": "79b30671",
            "lrcid": "00000065",
            "lrrRSSI": -106.000000,
            "lrrSNR": 0.000000,
            "spFact": 12,
            "subBand": "G1",
            "channel": "LC1",
            "devLrrCnt": 1,
            "lrrid": "29000049",
            "lrrLAT": 50.120018,
            "lrrLON": 14.501301,
            "lrrs": [
                {
                    "Lrrid": "29000049",
                    "LrrRSSI": -106.000000,
                    "LrrSNR": 0.000000,
                }
            ]
        },
        {
            "time": "2016-06-15T16:17:31.851+02:00",
            "devEUI": "4786E6ED00350042",
            "fPort": 8,
            "fCntUp": 9538,
            "aDRbit": 1,
            "fCntDn": 0,
            "payloadHex": "2400c7003ada03b4312602730f09",
            "micHex": "79b30671",
            "lrcid": "00000065",
            "lrrRSSI": -106.000000,
            "lrrSNR": 0.000000,
            "spFact": 12,
            "subBand": "G1",
            "channel": "LC1",
            "devLrrCnt": 1,
            "lrrid": "29000049",
            "lrrLAT": 50.120018,
            "lrrLON": 14.501301,
            "lrrs": [
                {
                    "Lrrid": "29000049",
                    "LrrRSSI": -106.000000,
                    "LrrSNR": 0.000000,
                }
            ]
        },
        {
            "time": "2016-06-15T16:17:31.851+02:00",
            "devEUI": "4786E6ED00350042",
            "fPort": 8,
            "fCntUp": 9538,
            "aDRbit": 1,
            "fCntDn": 0,
            "payloadHex": "2400c7003ada03b4312602730f09",
            "micHex": "79b30671",
            "lrcid": "00000065",
            "lrrRSSI": -106.000000,
            "lrrSNR": 0.000000,
            "spFact": 12,
            "subBand": "G1",
            "channel": "LC1",
            "devLrrCnt": 1,
            "lrrid": "29000049",
            "lrrLAT": 50.120018,
            "lrrLON": 14.501301,
            "lrrs": [
                {
                    "Lrrid": "29000049",
                    "LrrRSSI": -106.000000,
                    "LrrSNR": 0.000000,
                }
            ]
        },
        {
            "time": "2016-06-15T16:17:31.851+02:00",
            "devEUI": "4786E6ED00350042",
            "fPort": 8,
            "fCntUp": 9538,
            "aDRbit": 1,
            "fCntDn": 0,
            "payloadHex": "2500c7003ada03b4312602730f09",
            "micHex": "79b30671",
            "lrcid": "00000065",
            "lrrRSSI": -106.000000,
            "lrrSNR": 0.000000,
            "spFact": 12,
            "subBand": "G1",
            "channel": "LC1",
            "devLrrCnt": 1,
            "lrrid": "29000049",
            "lrrLAT": 50.120018,
            "lrrLON": 14.501301,
            "lrrs": [
                {
                    "Lrrid": "29000049",
                    "LrrRSSI": -106.000000,
                    "LrrSNR": 0.000000,
                }
            ]
        },
    ]
}
hive_message = test_data_msg
"""       if hive_message["_meta"]["status"] == 'ERROR':
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
        else:"""
data_count = int(hive_message['_meta']['count'])
work_data = [[record['time'], record['payloadHex']] for record in hive_message['records']]

msg_len = len(work_data[0][1])//2
messages = [i[1][j:j+2] for i in work_data for j in range(0, len(i[1]), 2)]
messages = [messages[i:i+msg_len] for i in range(0, len(messages), msg_len)]

hive_humid = [int(messages[i][2], 16) for i in range(0, data_count)]
status = [int(messages[i][13], 16) for i in range(0, data_count)]

frame_id = [int(messages[i][1] + messages[i][0], 16) for i in range(0, data_count)]
hive_temp = [int(messages[i][3] + messages[i][2], 16)/10 for i in range(0, data_count)]
pressure = [int(messages[i][6] + messages[i][5], 16) for i in range(0, data_count)]
bat_volt = [int(messages[i][12] + messages[i][11], 16)/1000 for i in range(0, data_count)]

weight = [uncomp_weight(int(messages[i][10] + messages[i][9] +
                            messages[i][8] + messages[i][7], 16)) for i in range(0, data_count)]
hive_weight = [temp_compensation(weight[i], hive_temp[i]) for i in range(0, data_count)]

print(net_status(status[2]))
print(hive_humid)
print(status)

print(frame_id)
print(hive_temp)
print(pressure)
print(bat_volt)

print(hive_weight)

"""frame_id = [int(((i[1])[2:4] + (i[1])[:2]), 16) for i in work_data]
temperature = [int(((i[1])[6:8] + (i[1])[4:6]), 16)/10 for i in work_data]
humidity = [int(((i[1])[10:12] + (i[1])[4:6]), 16)/10 for i in work_data]
print(frame_id)
print(temperature)"""
