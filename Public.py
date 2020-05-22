# coding=utf-8
import json
from API_test import RunMain
from log import out_log
from signature import get_signture
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

