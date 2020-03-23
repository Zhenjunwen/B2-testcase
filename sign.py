import time
import urllib
import requests
import hashlib

def signed_request(self, method, url, **payload):
    """request a signed url"""
    timestamp = str(int(time.time() * 1000))

    dic = {
        'apikey': self.accessKey,
        'apisecret': self.secretKey,
        'timestamp': timestamp
    }

    dic.update(payload)
    param = ''

    for key in sorted(dic):
        param += str(key) + '=' + str(dic[key]) + '&'
    param = param[:-1]

    keyUrlString = urllib.parse.quote(param).upper()
    sig_str = keyUrlString + self.secretKey + 'BTCSOEX'
    signature = str(hashlib.sha256(sig_str.encode('utf-8')).hexdigest()).upper()

    body = {
        'apikey': self.accessKey,
        'timestamp': timestamp,
        'sign': signature,
    }

    body.update(payload)

    if method == 'POST':
        response = requests.request(method, self.baseUrl + url, json=body)
    elif method == 'GET':
        response = requests.request(method, self.baseUrl + url + param)

    return response