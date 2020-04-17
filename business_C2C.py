# coding=utf-8
import traceback
import json
from API_test import RunMain
import time
from log import out_log
from login_register import user_login
from signature import get_signture

# B3_url = "http://192.168.0.22:12024" #孙骞
B3_url = "https://api.b3dev.xyz" #B3dev
# B2_url = "http://api.b2dev.xyz" #B2dev
# B2_url = "http://api.b2sit.xyz" #B2sit
# B2_url = "http://api.b2sim.xyz" #B2sim
token_junxin = "17d740ce53869ceb3dce06e943e88488"  # 俊鑫token
token_wen = "5ba6901e5f74a3e42935a5386e473a88"  # 俊文token
sys_token = "81a5463a4c317f4ed6c5a10183d8f40c" #B2后台token
H5_apikey = "sUY7qsoHudTrw2Ct"
H5_apisecret = "gEq76SZv"
sys_apikey = "5S7NukaMpMVW8U4Z"
sys_apisecret = "p0fbgZI0"
Android_apikey = "qbmkIS55ptjBhZFp"
Android_apisecret = "7M1H4mXA"
IOS_apikey = "oStkKLmJ5Q8S4n3b"
IOS_apisecret = "gKByU6HC"

def apply(token,symbol,amount):
    #提交商户认证
    url = "%s/api/v1/business/apply"% B3_url
    body = {
        "token":token,
        "certificate_front":"e6ec529ba185279aa0adcf93e645c7cd.jpg",
        "certificate_back":"469bba0a564235dfceede42db14f17b0.jpg",
        "certificate_handheld":"509e1a7dd584d7de15b20fc52e0e2e8d.jpg",
        "symbol":symbol,
        "amount":amount #USDT:1500,BTC:0.2
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))

def get_info(token):
    #获取提交的商户认证信息
    url = "%s/api/v1/business/get_info"% B3_url
    body = {
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))


def add_deposit(token,symbol,amount,user_id):
    #商户认证-增加商户保证金
    url = "%s/api/v1/admin/business/add_deposit"% B3_url
    body = {
        "token":token,
        "symbol":symbol,
        "amount":amount,
        "user_id":user_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(sys_apikey, sys_apisecret, body), method='POST')
    print(json.loads(run.response))

def reduce_deposit(token,symbol,amount,user_id):
    #商户认证-减少商户保证金
    url = "%s/api/v1/admin/business/reduce_deposit"% B3_url
    body = {
        "token":token,
        "symbol": symbol,
        "amount": amount,
        "user_id": user_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(sys_apikey, sys_apisecret, body), method='POST')
    print(json.loads(run.response))

def quit_business(token,remark=""):
    #退出商户认证
    url = "%s/api/v1/business/quit"% B3_url
    body = {
        "token":token,
        "remark":remark
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))

def quit_validate(token):
    #获取商户退出条件的符合情况
    url = "%s/api/v1/business/quit_validate"% B3_url
    body = {
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))

if __name__ == "__main__":
    get_info(token_wen)
    quit_validate(token_wen)
    # apply(token="e8032b945d69bea5425a72e2c991cfef", symbol="BTC", amount="0.3")
    # quit_validate(token_wen)
    # add_deposit(token=sys_token, symbol="BTC", amount="0.12345678", user_id="125487")
    # quit_business(token=token_wen)
    # reduce_deposit(token="5960f1eea9ba394863603b85a1aca851", symbol="BTC", amount="0.3", user_id="126319")