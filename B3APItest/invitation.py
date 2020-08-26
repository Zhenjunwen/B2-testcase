# coding=utf-8
import json
from B3APItest.API_test import RunMain
from log import out_log
from B3APItest.signature import get_signture
import configparser

cf = configparser.ConfigParser()
#配置文件路径
cf.read("F:\mohu-test\config.cfg")

B3_url = cf.get("url","url")
token_wen = cf.get('token','token_wen')
token_junxin = cf.get('token','token_junxin')
token_guoliang= cf.get('token',"token_guoliang")
H5_apikey =cf.get("Apikey","H5_apikey")
H5_apisecret =cf.get("Apikey","H5_apisecret")
sys_apikey =cf.get("Apikey","sys_apikey")
sys_apisecret =cf.get("Apikey","sys_apisecret")
Android_apikey =cf.get("Apikey","Android_apikey")
Android_apisecret =cf.get("Apikey","Android_apisecret")
IOS_apikey =cf.get("Apikey","IOS_apikey")
IOS_apisecret =cf.get("Apikey","IOS_apisecret")

def invitation_my_stats(token):
    #获取我的邀请统计信息
    url = "%s/api/v1/invitation/my_stats" % B3_url
    body={
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def invitation_my_records(token,page_number,page_size):
    #获取我的邀请记录
    url = "%s/api/v1/invitation/my_records" % B3_url
    body={
        "token":token,
        "page_number":page_number,
        "page_size":page_size

    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))


if __name__ == "__main__":
    invitation_my_stats(token="98233aec2a4ebe527ba4139dcbf533e8")