#coding=utf-8

import json
from API_test import RunMain
import time
from B2_C2C_api import get_signture
import hashlib


sunqian_url = "http://192.168.0.22:12024" #孙骞
# B2_url = "http://192.168.0.120:12024"  # B2内网网址
B2_url = "http://api.b2dev.xyz" #B2dev
token_junxin = "17d740ce53869ceb3dce06e943e88488"  # 俊鑫token
token_wen = "7893e454c38358872bb9fbcbb78f965c"  # 俊文token
# sys_token = "2da373f6d5ffc1f6a42120eb5a893adb" #B2后台token
H5_apikey = "alLzET7dFLYN5ONg"
H5_apisecret = "rpoEwZeM"
sys_apikey = "4NHMhvsQ15TFNyVO"
sys_apisecret = "h8eiT26J"
sys_token = "3758757c3f074ca1004b5bed561526c1"#B2dev

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