# coding=utf-8
import traceback
import json
import requests
from API_test import RunMain
import time
from log import out_log
from login_register import user_login
from signature import get_signture

# B3_url = "http://192.168.0.22:12024" #孙骞
B3_url = "https://api.b3dev.xyz" #B3dev
# B3_url = "http://api.B3sit.xyz" #B3sit
# B3_url = "http://api.B3sim.xyz" #B3sim
token_junxin = "f59d910a722302fe3b0b6a0542351cce"  # 俊鑫token
token_wen = "c00691c9af6ba855c015a6231e68e1b7"  # 俊文token
sys_token = "2da373f6d5ffc1f6a42120eb5a893adb" #B3后台token
H5_apikey = "sUY7qsoHudTrw2Ct"
H5_apisecret = "gEq76SZv"
sys_apikey = "5S7NukaMpMVW8U4Z"
sys_apisecret = "p0fbgZI0"
Android_apikey = "qbmkIS55ptjBhZFp"
Android_apisecret = "7M1H4mXA"
IOS_apikey = "oStkKLmJ5Q8S4n3b"
IOS_apisecret = "gKByU6HC"

#公共分类
def common_timestamp():
    #获取系统当前时间
    url = "%s/api/v1/common/timestamp" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_symbols():
    #获取所有交易对
    url = "%s/api/v1/common/symbols" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_get_currencys():
    #获取所有币种及对应的主链
    url = "%s/api/v1/common/get_currencys" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_currencys():
    #获取所有币种
    url = "%s/api/v1/common/currencys" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_partitions():
    #获取所有交易区
    url = "%s/api/v1/common/partitions" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_get_tradePairs():
    #获取所有交易对及最新成交涨跌信息
    url = "%s/api/v1/common/get_tradePairs" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

#banner
def banner_get_list(size,platform,language=None):
    #获取Banner列表
    url = "%s/api/v1/banner/get_list" % B3_url
    body = {
        "size":size,
        "platform":platform,
        "language":language
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def announcement_get_list(page_number,page_size,platform,language=None):
    #获取公告列表
    url = "%s/api/v1/announcement/get_list" % B3_url
    body = {
        "page_number":page_number,
        "page_size":page_size	,
        "platform":platform,
        "language":language
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    announcement_get_list(page_number="1", page_size="5", platform="1", language="zh")

