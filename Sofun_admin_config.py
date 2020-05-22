#coding=utf-8

import json
from API_test import RunMain
from C2C_api import get_signture
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


def get_tradePair(token,symbol=""):
    #SoFun交易挖矿-获取挖矿交易对列表
    url_get_tradePair = "%s/api/v1/admin/mining/tradePairs"% B2_url
    body = {
        "token":token,
        "page_number":"1",
        "page_size":"100",
        "symbol":symbol
    }
    run = RunMain(url=url_get_tradePair, params=None, data=body,
                  headers=get_signture(sys_apikey, sys_apisecret, body), method='POST')
    print(json.loads(run.response))

def add_tradePair(token,symbol):
    #SoFun交易挖矿-添加支持挖矿的交易对
    url_add_tradePair = "%s/api/v1/admin/mining/tradePair/add"% B2_url
    body = {
        "token":token,
        "symbol":symbol
    }
    run = RunMain(url=url_add_tradePair, params=None, data=body,
                  headers=get_signture(sys_apikey, sys_apisecret, body), method='POST')
    if json.loads(run.response)["code"] == 1000:
        print("SoFun交易挖矿-添加%s交易对成功"%symbol)
    else:
        print(run.response)

def remove_tradePair(token,symbol):
    #SoFun交易挖矿 - 移除指定的挖矿交易对
    url_remove_tradePair = "%s/api/v1/admin/mining/tradePair/remove"% B2_url
    body = {
        "token":token,
        "symbol":symbol
    }
    run = RunMain(url=url_remove_tradePair, params=None, data=body,
                  headers=get_signture(sys_apikey, sys_apisecret, body), method='POST')
    if json.loads(run.response)["code"] == 1000:
        print("SoFun交易挖矿-移除%s交易对成功"%symbol)
    else:
        print(run.response)

if __name__ == "__main__":
    get_tradePair(sys_token)
    add_tradePair(sys_token, "DNC-X-USDT")
    get_tradePair(sys_token)
    # remove_tradePair(sys_token, "TEST-USDT")