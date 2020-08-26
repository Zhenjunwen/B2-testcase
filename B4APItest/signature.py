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
    # print(dic)
    param = ''

    for key in sorted(dic):
        param += str(key) + '=' + str(dic[key]) + '&'
    param = param[:-1]

    keyUrlString = urllib.parse.quote(param).upper()
    sig_str = keyUrlString + apisecret
    # print(sig_str)
    signature = str(hashlib.sha256(sig_str.encode('utf-8')).hexdigest()).upper()
    # print(signature)
    UA = ""
    if dic["apikey"] == "jCwh14Tc89tDJH6l":
        UA = "H5"
    elif dic["apikey"] == "6Ji3P3Yu0tsQaNPu":
        UA = "ARD"
    elif dic["apikey"] == "j6lPYGCeIOwfYrz7":
        UA = "IOS"
    else:
        UA = "PC"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36;B4 %s"%UA,
        "Content-Type": "application/x-www-form-urlencoded",
        "apikey": dic["apikey"],
        "timestamp": str(int(round(t * 1000))),
        "sign": signature
    }
    return headers