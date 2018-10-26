from time import localtime, strftime

"""
Calibration values taken from the manual for the device, found on
https://pripoj.me/wp-content/uploads/2017/08/Payload.pdf
"""
calibration_index = 65536
zero_offset = 514.3
beta0 = 0.022

# Payload with user token
payload = {
    'token': 'yjHRpdbhce4VdJ43kTJ0RwqYpbIqQJDR',
    'limit': 10,
    'stop': strftime("%Y-%m-%dT%H:%M:%S", localtime())
}


# URLs for communication with API
url_message = 'http://api.pripoj.me/message/get/0004A30B001F216B'
