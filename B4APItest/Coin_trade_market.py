# coding=utf-8
import json
from API_test import RunMain
from log import out_log
from B4APItest.signature import get_signture
import demjson
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

def market_get_order_detail(symbol,scale,size):
    #获取市场K线数据
    url = "%s/api/v1/market/history/kline" % B4_url
    params={
        "symbol":symbol,
        "scale":scale,
        "size":size
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret, params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def market_get_top_trades(symbol,size):
    #获取市场Top买卖数据
    url = "%s/api/v1/market/top_trades" % B4_url
    params={
        "symbol":symbol,
        "size":size
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret, params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def market_get_last_trade(symbol):
    #获取市场最新成交涨跌数据
    url = "%s/api/v1/market/last_trade" % B4_url
    params={
        "symbol":symbol,
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret, params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def market_get_depth(symbol):
    #获取市场最新成交涨跌数据
    url = "%s/api/v1/market/depth" % B4_url
    params={
        "symbol":symbol,
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret, params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def market_get_history_trade(symbol,size):
    #获取市场近期成交记录
    url = "%s/api/v1/market/history/trade" % B4_url
    params={
        "symbol":symbol,
        "size":size
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret, params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def market_get_depth_merged(symbol,precision):
    #获取指定价格聚合精度的市场深度数据
    url = "%s/api/v1/market/depth/merged" % B4_url
    params={
        "symbol":symbol,
        "precision":precision
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret, params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # market_get_order_detail(symbol="BTC-USDT", scale="1", size="100")
    # market_get_top_trades(symbol="BTC-USDT", size="50")
    # market_get_last_trade(symbol="BTC-USDT")
    # market_get_depth(symbol="BTC-USDT")
    # market_get_history_trade(symbol="BTC-USDT", size="20")
    # market_get_depth_merged(symbol="BTC-USDT", precision="-1")
    pass
