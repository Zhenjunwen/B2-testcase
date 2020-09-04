# coding=utf-8
import json
from API_test import RunMain
from B4APItest.signature import get_signture
import configparser

cf = configparser.ConfigParser()
#配置文件路径
cf.read("F:\mohu-test\configfile\B4config.cfg")

B4_url = cf.get("url", "url")
token_wen = cf.get('token', 'token_wen')
token_junxin = cf.get('token', 'token_junxin')
token_guoliang = cf.get('token', "token_guoliang")
H5_apikey = cf.get("Apikey", "H5_apikey")
H5_apisecret = cf.get("Apikey", "H5_apisecret")
PC_apikey = cf.get("Apikey", "PC_apikey")
PC_apisecret = cf.get("Apikey", "PC_apisecret")
Android_apikey = cf.get("Apikey", "Android_apikey")
Android_apisecret = cf.get("Apikey", "Android_apisecret")
IOS_apikey = cf.get("Apikey", "IOS_apikey")
IOS_apisecret = cf.get("Apikey", "IOS_apisecret")


def apply(token,symbol,amount):
    #提交商户认证
    url = "%s/api/v1/business/apply"% B4_url
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
    url = "%s/api/v1/business/get_info"% B4_url
    body = {
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))


def add_deposit(token,symbol,amount,user_id):
    #商户认证-增加商户保证金
    url = "%s/api/v1/admin/business/add_deposit"% B4_url
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
    url = "%s/api/v1/admin/business/reduce_deposit"% B4_url
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
    url = "%s/api/v1/business/quit"% B4_url
    body = {
        "token":token,
        "remark":remark
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))

def quit_validate(token):
    #获取商户退出条件的符合情况
    url = "%s/api/v1/business/quit_validate"% B4_url
    body = {
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))

if __name__ == "__main__":
    # get_info(token_wen)
    # quit_validate(token_wen)
    apply(token=token_wen, symbol="USDT", amount="1500")
    # quit_validate(token_wen)
    # add_deposit(token=sys_token, symbol="BTC", amount="0.12345678", user_id="126378")
    # quit_business(token=token_wen)
    # reduce_deposit(token="5960f1eea9ba394863603b85a1aca851", symbol="BTC", amount="0.3", user_id="126319")