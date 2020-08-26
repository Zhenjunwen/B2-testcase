#coding=utf-8

import json
from API_test import RunMain
from log import out_log
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

def notification_delete(token,id):
    #删除消息
    url = "%s/api/v1/notification/delete" % B4_url
    body = {
        "token":token,
        "id":id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='POST')
    out_log(url,body,json.loads(run.response))
    print(json.loads(run.response))

def notification_read(token,id):
    #标记消息为已读
    url = "%s/api/v1/notification/read" % B4_url
    body = {
        "token":token,
        "id":id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='POST')
    out_log(url,body,json.loads(run.response))
    print(json.loads(run.response))

def notification_get_list(token,page_number="1",page_size="10"):
    #获取我的所有消息
    url = "%s/api/v1/notification/get_list" % B4_url
    body = {
        "token":token,
        "page_number":page_number,
        "page_size":page_size
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='POST')
    out_log(url,body,json.loads(run.response))
    print(json.loads(run.response))

def notification_get_unread_num(token):
    #获取我的未读消息数量
    url = "%s/api/v1/notification/get_unread_num" % B4_url
    body = {
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='POST')
    out_log(url,body,json.loads(run.response))
    print(json.loads(run.response))

def notification_clear(token):
    #清空全部消息
    url = "%s/api/v1/notification/clear" % B4_url
    body = {
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='POST')
    out_log(url,body,json.loads(run.response))
    print(json.loads(run.response))



if __name__ == "__main__":
    # notification_delete(token=token_wen, id="1")
    # notification_read(token=token_wen, id="2")
    # notification_get_list(token=token_wen)
    # notification_get_unread_num(token=token_wen)
    # notification_clear(token=token_wen)
    pass