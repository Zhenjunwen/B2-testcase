# coding=utf-8
import json
from API_test import RunMain
from log import out_log
from B3APItest.signature import get_signture
import demjson
import configparser

cf = configparser.ConfigParser()
# 配置文件路径
cf.read("F:\mohu-test\configfile\B3config.cfg")

B3_url = cf.get("url", "url")
token_wen = cf.get('token', 'token_wen')
token_junxin = cf.get('token', 'token_junxin')
token_guoliang = cf.get('token', "token_guoliang")
H5_apikey = cf.get("Apikey", "H5_apikey")
H5_apisecret = cf.get("Apikey", "H5_apisecret")
sys_apikey = cf.get("Apikey", "sys_apikey")
sys_apisecret = cf.get("Apikey", "sys_apisecret")
Android_apikey = cf.get("Apikey", "Android_apikey")
Android_apisecret = cf.get("Apikey", "Android_apisecret")
IOS_apikey = cf.get("Apikey", "IOS_apikey")
IOS_apisecret = cf.get("Apikey", "IOS_apisecret")

def favorites_add(token, symbol):
    # 收藏交易对
    url = "%s/api/v1/favorites/add" % B3_url
    body = {
        "token": token,
        "symbol": symbol,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def favorites_remove(token, symbol):
    # 移除收藏交易对
    url = "%s/api/v1/favorites/remove" % B3_url
    body = {
        "token": token,
        "symbol": symbol,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def favorites_list(token):
    # 获取交易对收藏列表
    url = "%s/api/v1/favorites" % B3_url
    body = {
        "token": token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # favorites_add(token=token_wen, symbol="ETH-USDT")
    # favorites_remove(token=token_wen, symbol="BTC-USDT")
    favorites_list(token=token_wen)
    pass