import hashlib
import time
import urllib


def get_signture(apikey,apisecret,playload=""):
    t = time.time()
    timestamp = str(int(round(t * 1000)))
    dic = {
        'apikey': apikey,
        'apisecret': apisecret,
        'timestamp': timestamp,
    }
    dic.update(playload)
    param = ''

    for key in sorted(dic):
        param += str(key) + '=' + str(dic[key]) + '&'
    param = param[:-1]
    keyUrlString = urllib.parse.quote(param).upper()
    sig_str = keyUrlString + apisecret + 'BB3EX'
    signature = str(hashlib.sha256(sig_str.encode('utf-8')).hexdigest()).upper()
    return signature