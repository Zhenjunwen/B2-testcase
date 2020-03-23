# coding=utf-8
import traceback
import json
from API_test import RunMain
import time
from log import out_log
from login_register import user_login
from signature import get_signture

B2_url = "http://192.168.0.22:12024" #孙骞
# B2_url = "http://api.b2dev.xyz" #B2dev
# B2_url = "http://api.b2sit.xyz" #B2sit
# B2_url = "http://api.b2sim.xyz" #B2sim
token_junxin = "17d740ce53869ceb3dce06e943e88488"  # 俊鑫token
token_wen = "0b88d5881bc7f12dcf76d734a6246b59"  # 俊文token
sys_token = "81a5463a4c317f4ed6c5a10183d8f40c" #B2后台token
H5_apikey = "alLzET7dFLYN5ONg"
H5_apisecret = "rpoEwZeM"
sys_apikey = "4NHMhvsQ15TFNyVO"
sys_apisecret = "h8eiT26J"
Android_apikey = "ctyD04PtGMIsJtNZ"
Android_apisecret = "41DwD4ST"

def apply(token,symbol,amount):
    #提交商户认证
    url_get_tradePair = "%s/api/v1/business/apply"% B2_url
    body = {
        "token":token,
        "certificate_front":"e6ec529ba185279aa0adcf93e645c7cd.jpg",
        "certificate_back":"469bba0a564235dfceede42db14f17b0.jpg",
        "certificate_handheld":"509e1a7dd584d7de15b20fc52e0e2e8d.jpg",
        "symbol":symbol,
        "amount":amount #USDT:1500,BTC:0.2
    }
    run = RunMain(url=url_get_tradePair, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))

def get_info(token):
    #获取提交的商户认证信息
    url_get_tradePair = "%s/api/v1/business/get_info"% B2_url
    body = {
        "token":token,
    }
    run = RunMain(url=url_get_tradePair, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))


def add_deposit(token,symbol,amount,user_id):
    #商户认证-增加商户保证金
    url_get_tradePair = "%s/api/v1/admin/business/add_deposit"% B2_url
    body = {
        "token":token,
        "symbol":symbol,
        "amount":amount,
        "user_id":user_id
    }
    run = RunMain(url=url_get_tradePair, params=None, data=body,
                  headers=get_signture(sys_apikey, sys_apisecret, body), method='POST')
    print(json.loads(run.response))

def reduce_deposit(token,symbol,amount,user_id):
    #商户认证-减少商户保证金
    url_get_tradePair = "%s/api/v1/admin/business/reduce_deposit"% B2_url
    body = {
        "token":token,
        "symbol": symbol,
        "amount": amount,
        "user_id": user_id
    }
    run = RunMain(url=url_get_tradePair, params=None, data=body,
                  headers=get_signture(sys_apikey, sys_apisecret, body), method='POST')
    print(json.loads(run.response))

def quit_business(token,remark=""):
    #退出商户认证
    url_get_tradePair = "%s/api/v1/business/quit"% B2_url
    body = {
        "token":token,
        "remark":remark
    }
    run = RunMain(url=url_get_tradePair, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))

def quit_validate(token):
    #获取商户退出条件的符合情况
    url_get_tradePair = "%s/api/v1/business/quit_validate"% B2_url
    body = {
        "token":token,
    }
    run = RunMain(url=url_get_tradePair, params=None, data=body,
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