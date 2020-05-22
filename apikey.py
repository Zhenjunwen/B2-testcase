# coding=utf-8
import traceback
import json
import requests
from API_test import RunMain
import time
from log import out_log
from apikey_signature import get_signture

import configparser

cf = configparser.ConfigParser()
#配置文件路径
cf.read("F:\mohu-test\config.cfg")
B3_url = cf.get("url","url")
token_wen = cf.get('token','token_wen')
token_junxin = cf.get('token','token_junxin')
token_guoliang=cf.get('token',"token_guoliang")
H5_apikey =cf.get("Apikey","H5_apikey")
H5_apisecret =cf.get("Apikey","H5_apisecret")
sys_apikey =cf.get("Apikey","sys_apikey")
sys_apisecret =cf.get("Apikey","sys_apisecret")
Android_apikey =cf.get("Apikey","Android_apikey")
Android_apisecret =cf.get("Apikey","Android_apisecret")
IOS_apikey =cf.get("Apikey","IOS_apikey")
IOS_apisecret =cf.get("Apikey","IOS_apisecret")

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