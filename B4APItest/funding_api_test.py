# coding=utf-8
import json
from API_test import RunMain
from log import out_log
from B4APItest.signature import get_signture
import configparser

cf = configparser.ConfigParser()
# 配置文件路径
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

def funding_activity_activities(page_size,page_number,symbol=""):
    # 8418-获取所有进行中的活动
    url = "%s/api/v1/funding/activity/activities" % B4_url
    params = {
        "symbol":symbol,
        "page_size":page_size,
        "page_number":page_number
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret), method='GET')
    out_log(url, send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def funding_activity_detail(activity_id):
    # 8427-获取活动详情
    url = "%s/api/v1/funding/activity/detail" % B4_url
    params = {
        "activity_id":activity_id
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret), method='GET')
    out_log(url, send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def funding_activity_participate(token,activity_id,activity_code):
    # 8436-参与活动
    url = "%s/api/v1/funding/activity/participate" % B4_url
    body = {
        "token": token,
        "activity_id":activity_id,
        "activity_code":activity_code
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def funding_activity_participated_activities(token,symbol,page_number,page_size):
    # 8445-获取我参与的活动
    url = "%s/api/v1/funding/activity/participated_activities" % B4_url
    body = {
        "token": token,
        "symbol":symbol,
        "page_number":page_number,
        "page_size":page_size
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def funding_activity_participated_detail(token,activity_id):
    # 8454-获取我参与的活动详情
    url = "%s/api/v1/funding/activity/participated_detail" % B4_url
    body = {
        "token": token,
        "activity_id":activity_id,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def funding_activity_exit(token,activity_id):
    # 8463-申请退出活动
    url = "%s/api/v1/funding/activity/exit" % B4_url
    body = {
        "token": token,
        "activity_id":activity_id,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def funding_activity_switch(token,activity_id):
    # 8481-切换活动为进行中
    url = "%s/api/v1/funding/activity/switch" % B4_url
    body = {
        "token": token,
        "activity_id":activity_id,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # 8418-获取所有进行中的活动
    # funding_activity_activities(symbol="BTC",page_size="10", page_number="1")

    #获取活动详情
    # funding_activity_detail(activity_id="0")

    #8436-参与活动
    # funding_activity_participate(token="ed37c795681f4c4a0b514926704a8714", activity_id="15", activity_code="fAeeGg")

    #获取我参与的活动
    # funding_activity_participated_activities(token=token_wen,symbol="BTC",page_number="1",page_size="10")

    #获取我参与的活动详情
    # funding_activity_participated_detail(token=token_wen, activity_id="6")

    #申请退出活动
    # funding_activity_exit(token=token_wen, activity_id="13")

    #切换活动为进行中
    funding_activity_switch(token="8f195c7bdfb47bfbd15321f4d7f5c694", activity_id="15")
    pass