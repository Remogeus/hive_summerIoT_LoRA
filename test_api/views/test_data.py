"""
{
    "_meta":
    {
        "status":"SUCCESS",
        "count":1
    },
    "records":
    [
        {
            "devEUI":"4786E6ED00350042",
            "projectId":"TEST",
            "description":"Testovací teplotní čidlo",
            "model":"RHF1S001",
            "vendor":"Rising HF"
        }
    ]
}
"""

test_data_error = {
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

test_data_msg_ok = {
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
