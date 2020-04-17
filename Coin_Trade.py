#coding=utf-8

import json
from API_test import RunMain
import time
from B2_C2C_api import get_signture
from log import out_log
from login_register import user_login

# B2_url = "http://192.168.0.22:12024" #孙骞
B3_url = "https://api.b3dev.xyz" #B3dev
# B2_url = "http://api.b2sim.xyz" #B2sim
B2_url = "http://api.b2dev.xyz" #B2dev
# B2_url = "http://api.b2sit.xyz" #B2sit
# token_junxin = user_login("2","13826284310","111111")  # 俊鑫token
token_wen = "7893e454c38358872bb9fbcbb78f965c"  # 俊文token
# sys_token = "2da373f6d5ffc1f6a42120eb5a893adb" #B2后台token
H5_apikey = "sUY7qsoHudTrw2Ct"
H5_apisecret = "gEq76SZv"
sys_apikey = "5S7NukaMpMVW8U4Z"
sys_apisecret = "p0fbgZI0"
Android_apikey = "qbmkIS55ptjBhZFp"
Android_apisecret = "7M1H4mXA"
IOS_apikey = "oStkKLmJ5Q8S4n3b"
IOS_apisecret = "gKByU6HC"


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
        "side":side,
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
    add_orders("30d0514b553963855d5fa3b0e2347250",0,1.5,"0","web","BTC-USDT")
    # add_orders("f2cc54246712804f5fe554e20bba0477",8745.26,0.1005,"1","web","BTC-USDT")
    # add_orders("683973377ae5c92d3e1bbecc87beec2d",7238.41,0.1005+0.01,"0","web","BTC-USDT")
    # get_open_orders(token="683973377ae5c92d3e1bbecc87beec2d")
    last_trade(symbol="BTC-USDT")
    # market(symbol="BTC-USDT", precision="1")
    # history_trade("BTC-USDT","50")
