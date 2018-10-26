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
