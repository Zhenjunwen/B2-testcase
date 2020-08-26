#coding=utf-8

import json
from B3APItest.API_test import RunMain
from B3APItest.C2C_api import get_signture
from log import out_log
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



def top_trades():
    #获取市场Top买卖信息
    url = "%s/api/v1/market/top_trades" % B3_url
    params = {
        "symbol":"BTC-USDT",
        "size":"20"
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,params,json.loads(run.response))
    print(json.loads(run.response))

def add_orders(token,price,quantity,side,source,symbol):
    #下单
    url = "%s/api/v1/transaction/add_order" % B3_url
    body={
        "token":token,
        "price":str(price),
        "quantity":str(quantity),
        "side":side,                #交易方向 0=卖出 1=买入
        "source":source,
        "symbol":symbol

    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_open_orders(token,page_number="1",page_size="10",symbol=None):
    #用户获取当前最新有效价格
    url = "%s/api/v1/transaction/get_open_orders" % B3_url
    body={
        "token":token,
        "symbol":symbol,
        "page_number":page_number,
        "page_size":page_size,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def last_trade(symbol):
    #获取市场最新成交涨跌信息
    url = "%s/api/v1/market/last_trade" % B3_url
    params={
        "symbol":symbol,
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret, params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def cancel_all_orders(token,symbol):
    #后台一键撤销订单
    url = "%s/api/v1/admin/transaction/cancel_all_orders" % B3_url
    body={
        "token":token,
        "symbol":symbol,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(sys_apikey, sys_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def market(symbol,precision):
    # 获取指定价格聚合度的市场深度数据
    url = "%s/api/v1/market/depth/merged" % B3_url
    body = {
        "symbol": symbol,
        "precision":precision,
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(sys_apikey, sys_apisecret, body), method='GET')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def history_trade(symbol,size):
    # 获取市场近期成交记录
    url = "%s/api/v1/market/history/trade" % B3_url
    body = {
        "symbol": symbol,
        "size":size,
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(sys_apikey, sys_apisecret, body), method='GET')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # cancel_all_orders("72bf0954d984fa25e250f83df1761803", "SOFUN-USDT")
    # top_trades()
    add_orders(token="f80dfb7a06668d567282da239609c73d",price=9753.12,quantity=0.01,side="1",source="web",symbol="BTC-USDT")
    # add_orders(token="53f002f0241422f375d380ff2090a016",price=9745.26,quantity=0.1005,side="0",source="web",symbol="BTC-USDT")
    # add_orders("683973377ae5c92d3e1bbecc87beec2d",7238.41,0.1005+0.01,"0","web","BTC-USDT")
    # get_open_orders(token="683973377ae5c92d3e1bbecc87beec2d")
    # last_trade(symbol="BTC-USDT")
    # market(symbol="BTC-USDT", precision="1")
    # history_trade("BTC-USDT","50")
