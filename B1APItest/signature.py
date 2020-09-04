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
    # print(param)
    keyUrlString = urllib.parse.quote(param).upper()
    sig_str = keyUrlString + apisecret + 'BSEX'
    # print(sig_str)
    signature = str(hashlib.sha256(sig_str.encode('utf-8')).hexdigest()).upper()
    # print(signature)
    UA = ""
    if dic["apikey"] == "W6ykKe6I654UMmEO":
        UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36;BiShangEX H5"
    elif dic["apikey"] == "udTnbTv7GqNnUvpC":
        UA = "bsex/(iOS) com.mohu.bsex"
    elif dic["apikey"] == "fkcgD8kGKC6PXjVJ":
        UA = "Android 11"
    else:
        UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36;BiShangEX PC"

    headers = {
        "User-Agent": "%s"%UA,
        "Content-Type": "application/x-www-form-urlencoded",
        "apikey": dic["apikey"],
        "timestamp": str(int(round(t * 1000))),
        "sign": signature
    }
    return headers