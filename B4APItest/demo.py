# coding=utf-8
import json
from B3APItest.API_test import RunMain
from log import out_log
from B3APItest.signature import get_signture
import time
import configparser
from B3APItest.futures import futures_transfer_fund,futures_add_order,futures_account_position_info

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

def demo_run():
    #俊鑫划转2个币
    futures_transfer_fund(token=token_junxin, symbol="BTC", amount="2", side="1")
    #俊文划转0.2个币
    futures_transfer_fund(token=token_wen, symbol="BTC", amount="0.2", side="1")
    #俊文下单（做空爆仓）
    futures_add_order(token=token_wen,contract_code="BTC_20200626",direction="sell_open",quantity="367",price="9185.12",lever="20",source="web")
    #俊鑫吃单
    futures_add_order(token=token_junxin,contract_code="BTC_20200626",direction="buy_open",quantity="367",price="9185.12",lever="20",source="web")
    #俊鑫爆仓价格
    futures_add_order(token=token_junxin,contract_code="BTC_20200626",direction="buy_open",quantity="1",price="9988.12",lever="20",source="web")
    futures_add_order(token=token_junxin, contract_code="BTC_20200626", direction="sell_open", quantity="1",price="9988.12", lever="20", source="web")
    time.sleep(5)
    #俊文划转0.2个币
    futures_transfer_fund(token=token_wen, symbol="BTC", amount="0.2", side="1")
    # 俊文下单（做多爆仓）
    futures_add_order(token=token_wen, contract_code="BTC_20200626", direction="buy_open", quantity="363",price="9085.12", lever="20", source="web")
    # 俊鑫吃单
    futures_add_order(token=token_junxin, contract_code="BTC_20200626", direction="sell_open", quantity="363",price="9085.12", lever="20", source="web")
    #俊鑫爆仓价格
    futures_add_order(token=token_junxin, contract_code="BTC_20200626", direction="sell_open", quantity="1",price="8000.12", lever="20", source="web")
    futures_add_order(token=token_junxin, contract_code="BTC_20200626", direction="buy_open", quantity="1",price="8000.12", lever="20", source="web")
    time.sleep(5)
    # 俊文划转0.2个币
    futures_transfer_fund(token=token_wen, symbol="BTC", amount="0.2", side="1")
    #俊文下单（做空爆仓）
    futures_add_order(token=token_wen,contract_code="BTC_20200626",direction="sell_open",quantity="370",price="9266.12",lever="20",source="web")
    #俊鑫吃单
    futures_add_order(token=token_junxin,contract_code="BTC_20200626",direction="buy_open",quantity="370",price="9266.12",lever="20",source="web")
    #俊鑫爆仓
    futures_add_order(token=token_junxin, contract_code="BTC_20200626", direction="buy_open", quantity="1",price="9988.12", lever="20", source="web")
    futures_add_order(token=token_junxin, contract_code="BTC_20200626", direction="sell_open", quantity="1",
                      price="9988.12", lever="20", source="web")
    time.sleep(5)
    # # 俊文划转0.2个币
    # futures_transfer_fund(token=token_wen, symbol="BTC", amount="0.2", side="1")
    # # 俊文下单（做多穿仓爆仓）
    # futures_add_order(token=token_wen, contract_code="BTC_20200626", direction="buy_open", quantity="804",price="20120.12", lever="20", source="web")
    # # 俊鑫吃单
    # futures_add_order(token=token_junxin, contract_code="BTC_20200626", direction="sell_open", quantity="804",price="20120.12", lever="20", source="web")
    # # 俊鑫爆仓价
    # futures_add_order(token=token_junxin, contract_code="BTC_20200626", direction="sell_open", quantity="1",price="9135.12", lever="20", source="web")
    # futures_add_order(token=token_junxin, contract_code="BTC_20200626", direction="buy_open", quantity="1",price="9135.12", lever="20", source="web")
    #俊文划转0.2个币
    futures_transfer_fund(token=token_wen, symbol="BTC", amount="0.2", side="1")
    # 俊文下单（做多爆仓）
    futures_add_order(token=token_wen, contract_code="BTC_20200626", direction="buy_open", quantity="363",price="9285.09", lever="20", source="web")
    # 俊鑫吃单
    futures_add_order(token=token_junxin, contract_code="BTC_20200626", direction="sell_open", quantity="363",price="9285.09", lever="20", source="web")
    #俊鑫爆仓价格
    futures_add_order(token=token_junxin, contract_code="BTC_20200626", direction="sell_open", quantity="1",price="8000.09", lever="20", source="web")
    futures_add_order(token=token_junxin, contract_code="BTC_20200626", direction="buy_open", quantity="1",price="8000.09", lever="20", source="web")

def demo_run2():
    #转入0.2BTC
    # futures_transfer_fund(token=token_wen, symbol="ETH", amount="100", side="1")
    # futures_transfer_fund(token=token_junxin, symbol="ETH", amount="100", side="1")
    for i in range(2):
        # 多单
        futures_add_order(token=token_wen, contract_code="ETH_20200925", direction="buy_open", quantity="20",price="230.58", lever="20", source="app")
        # 多单吃单
        futures_add_order(token=token_junxin, contract_code="ETH_20200925", direction="sell_open", quantity="20", price="230.58",
                          lever="20", source="app")

        # 盈利平仓
        futures_add_order(token=token_wen, contract_code="ETH_20200925", direction="sell_close", quantity="18", price="231.58",
                          lever="20", source="app")
        # 平仓吃单
        futures_add_order(token=token_junxin, contract_code="ETH_20200925", direction="buy_close", quantity="18",
                          price="231.58",
                          lever="20", source="app")
    for i in range(2):
        # 多单
        futures_add_order(token=token_wen, contract_code="ETH_20200925", direction="buy_open", quantity="20",price="232.58", lever="20", source="app")
        # 多单吃单
        futures_add_order(token=token_junxin, contract_code="ETH_20200925", direction="sell_open", quantity="20", price="232.58",
                          lever="20", source="app")

        # 盈利平仓
        futures_add_order(token=token_wen, contract_code="ETH_20200925", direction="sell_close", quantity="18", price="233.58",
                          lever="20", source="app")
        # 平仓吃单
        futures_add_order(token=token_junxin, contract_code="ETH_20200925", direction="buy_close", quantity="18",
                          price="233.58",
                          lever="20", source="app")
        # 平仓吃单
        futures_add_order(token=token_junxin, contract_code="ETH_20200925", direction="buy_close", quantity="2",
                          price="234.58",
                          lever="20", source="app")
        # 盈利平仓
        futures_add_order(token=token_wen, contract_code="ETH_20200925", direction="sell_close", quantity="2",
                          price="234.58",
                          lever="20", source="app")

    # 查询持仓量
    futures_account_position_info(token=token_wen, symbol="ETH")

def demo_run3():
    for i in range(1):
        # 空单
        futures_add_order(token=token_wen, contract_code="ETH_20200925", direction="sell_open", quantity="20",price="234.58", lever="20", source="app")
        # 空单吃单
        futures_add_order(token=token_junxin, contract_code="ETH_20200925", direction="buy_open", quantity="20", price="234.58",
                          lever="20", source="app")

        # 亏损平仓
        futures_add_order(token=token_wen, contract_code="ETH_20200925", direction="buy_close", quantity="18", price="233.58",
                          lever="20", source="app")
        # 平仓吃单
        futures_add_order(token=token_junxin, contract_code="ETH_20200925", direction="sell_close", quantity="18",
                          price="233.58",
                          lever="20", source="app")
    for i in range(1):
        # 多单
        futures_add_order(token=token_wen, contract_code="ETH_20200925", direction="sell_open", quantity="20",price="232.58", lever="20", source="app")
        # 多单吃单
        futures_add_order(token=token_junxin, contract_code="ETH_20200925", direction="buy_open", quantity="20", price="232.58",
                          lever="20", source="app")

        # 盈利平仓
        futures_add_order(token=token_wen, contract_code="ETH_20200925", direction="buy_close", quantity="18", price="231.58",
                          lever="20", source="app")
        # 平仓吃单
        futures_add_order(token=token_junxin, contract_code="ETH_20200925", direction="sell_close", quantity="18",
                          price="231.58",
                          lever="20", source="app")
        # 平仓吃单
        futures_add_order(token=token_junxin, contract_code="ETH_20200925", direction="sell_close", quantity="2",
                          price="230.58",
                          lever="20", source="app")
        # 盈利平仓
        futures_add_order(token=token_wen, contract_code="ETH_20200925", direction="buy_close", quantity="2",
                          price="230.58",
                          lever="20", source="app")

    # 查询持仓量
    futures_account_position_info(token=token_wen, symbol="ETH")

def get_stats(token):
    # 6861-获取代理商佣金记录详情
    url = "https://api.b1dev.xyz/api/v1/invitation/get_stats"
    body = {
        "token": token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # demo_run()
    # print(100*100)
    get_stats(token="5dce196a176a38189c751c30e2c86fed")