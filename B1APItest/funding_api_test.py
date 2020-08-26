# coding=utf-8
import json
from API_test import RunMain
from log import out_log
from B1APItest.signature import get_signture
import configparser

cf = configparser.ConfigParser()
# 配置文件路径
cf.read("F:\mohu-test\configfile\B1config.cfg")

B1_url = cf.get("url", "url")
token_wen = cf.get('token', 'token_wen')
token_junxin = cf.get('token', 'token_junxin')
H5_apikey = cf.get("Apikey", "H5_apikey")
H5_apisecret = cf.get("Apikey", "H5_apisecret")
PC_apikey = cf.get("Apikey", "PC_apikey")
PC_apisecret = cf.get("Apikey", "PC_apisecret")

def funding_activity_activities(page_size,page_number,symbol=""):
    # 8418-获取所有进行中的活动
    url = "%s/api/v1/funding/activity/activities" % B1_url
    params = {
        "symbol":symbol,
        "page_size":page_size,
        "page_number":page_number
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(PC_apikey, PC_apisecret,params), method='GET')
    out_log(url, send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def funding_activity_detail(activity_id):
    # 8427-获取活动详情
    url = "%s/api/v1/funding/activity/detail" % B1_url
    params = {
        "activity_id":activity_id
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(PC_apikey, PC_apisecret,params), method='GET')
    out_log(url, send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def funding_activity_participate(token,activity_id):
    # 8436-参与活动
    url = "%s/api/v1/funding/activity/participate" % B1_url
    body = {
        "token": token,
        "activity_id":activity_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(PC_apikey, PC_apisecret, body), method='POST')
    out_log(url, send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def funding_activity_participated_activities(token,symbol,page_number,page_size):
    # 8445-获取我参与的活动
    url = "%s/api/v1/funding/activity/participated_activities" % B1_url
    body = {
        "token": token,
        "symbol":symbol,
        "page_number":page_number,
        "page_size":page_size
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(PC_apikey, PC_apisecret, body), method='POST')
    out_log(url, send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def funding_activity_participated_detail(token,activity_id):
    # 8454-获取我参与的活动详情
    url = "%s/api/v1/funding/activity/participated_detail" % B1_url
    body = {
        "token": token,
        "activity_id":activity_id,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(PC_apikey, PC_apisecret, body), method='POST')
    out_log(url, send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # 8418-获取所有进行中的活动
    # funding_activity_activities(symbol="BTC",page_size="10", page_number="1")

    #获取活动详情
    # funding_activity_detail(activity_id="3")

    #8436-参与活动
    # funding_activity_participate(token="11f8a3da740ca3b0d9fac69ee371b4e9", activity_id="3")

    #获取我参与的活动
    # funding_activity_participated_activities(token=token_wen,symbol="BTC",page_number="1",page_size="10")

    #获取我参与的活动详情
    # funding_activity_participated_detail(token="11f8a3da740ca3b0d9fac69ee371b4e9", activity_id="3")
    pass