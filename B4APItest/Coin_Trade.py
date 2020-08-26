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



def top_trades():
    #获取市场Top买卖信息
    url = "%s/api/v1/market/top_trades" % B4_url
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
    url = "%s/api/v1/transaction/add_order" % B4_url
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

def cancel_order(token,order_id):
    #撤销订单
    url = "%s/api/v1/transaction/cancel_order" % B4_url
    body={
        "token":token,
        "order_id":order_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))


def get_open_orders(token,page_number="1",page_size="10",symbol=""):
    #获取当前订单
    url = "%s/api/v1/transaction/get_open_orders" % B4_url
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

def get_close_orders(token,page_number="1",page_size="10",symbol=""):
    #获取历史订单
    url = "%s/api/v1/transaction/get_close_orders" % B4_url
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

def get_trade_detail(token,order_id):
    #获取订单成交明细
    url = "%s/api/v1/transaction/get_trade_detail" % B4_url
    body={
        "token":token,
        "order_id":order_id,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_order_detail(token,order_id):
    #获取订单详情
    url = "%s/api/v1/transaction/get_order_detail" % B4_url
    body={
        "token":token,
        "order_id":order_id,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # top_trades()
    # add_orders(token=token_wen,price=7753.12,quantity=0.1,side="0",source="app",symbol="BTC-USDT")
    # add_orders(token="53f002f0241422f375d380ff2090a016",price=9745.26,quantity=0.1005,side="0",source="web",symbol="BTC-USDT")
    # add_orders("683973377ae5c92d3e1bbecc87beec2d",7238.41,0.1005+0.01,"0","web","BTC-USDT")
    # get_open_orders(token=token_wen)
    # last_trade(symbol="BTC-USDT")
    # market(symbol="BTC-USDT", precision="1")
    # history_trade("BTC-USDT","50")
    # cancel_order(token=token_wen, order_id="5166541")
    # get_close_orders(token=token_wen, page_number="1", page_size="10", symbol="")
    # get_order_detail(token=token_wen, order_id="5166655")
    pass