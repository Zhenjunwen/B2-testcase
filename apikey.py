# coding=utf-8
import traceback
import json
import requests
from API_test import RunMain
import time
from log import out_log
from login_register import user_login
from apikey_signature import get_signture

# B3_url = "http://192.168.0.22:12024" #孙骞
B3_url = "https://api.b3dev.xyz" #B3dev
H5_apikey = "sUY7qsoHudTrw2Ct"
H5_apisecret = "gEq76SZv"
sys_apikey = "5S7NukaMpMVW8U4Z"
sys_apisecret = "p0fbgZI0"
Android_apikey = "qbmkIS55ptjBhZFp"
Android_apisecret = "7M1H4mXA"
IOS_apikey = "oStkKLmJ5Q8S4n3b"
IOS_apisecret = "gKByU6HC"

def futures_common_get_contracts(apikey,apisecret,symbol,amount,side):
    #apikey用户资产划转
    url = "%s/merchant/api/v1/futures/account/transfer" % B3_url
    t = time.time()
    timestamp = str(int(round(t * 1000)))
    sign_body = {
        "symbol": symbol,
        "amount": amount,
        "side": side,
    }
    sign = get_signture(apikey=apikey,apisecret=apisecret,playload=sign_body)
    # print(sign)
    body = {
        "symbol":symbol,
        "amount":amount,
        "side":side,
        "timestamp":timestamp,
        "apikey":apikey,
        "sign":sign
    }
    run = RunMain(url=url, params=None, data=body,
                  headers="", method='POST')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    futures_common_get_contracts(apikey="173e3d0b-dff4-4b39-913b-04c5fb57f3e0",apisecret="IiwA2rTxsL7fbHJw",symbol="BTC", amount="5000", side="1")