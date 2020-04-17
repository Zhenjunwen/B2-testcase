# coding=utf-8
import traceback
import json
import requests
from API_test import RunMain
import time
from log import out_log
from login_register import user_login
from signature import get_signture

# B3_url = "http://192.168.0.22:12024" #孙骞
B3_url = "https://api.b3dev.xyz" #B3dev
# B3_url = "http://api.B3sit.xyz" #B3sit
# B3_url = "http://api.B3sim.xyz" #B3sim
token_junxin = "f59d910a722302fe3b0b6a0542351cce"  # 俊鑫token
token_wen = "c00691c9af6ba855c015a6231e68e1b7"  # 俊文token
sys_token = "2da373f6d5ffc1f6a42120eb5a893adb" #B3后台token
H5_apikey = "sUY7qsoHudTrw2Ct"
H5_apisecret = "gEq76SZv"
sys_apikey = "5S7NukaMpMVW8U4Z"
sys_apisecret = "p0fbgZI0"
Android_apikey = "qbmkIS55ptjBhZFp"
Android_apisecret = "7M1H4mXA"
IOS_apikey = "oStkKLmJ5Q8S4n3b"
IOS_apisecret = "gKByU6HC"

#公共分类
def futures_common_get_contracts():
    #期货合约-3270-获取当前生效的合约
    url = "%s/api/v1/futures/common/contracts" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_get_adjust_factor():
    #期货合约-3306-获取平台阶梯调整系数
    url = "%s/api/v1/futures/common/adjust_factor" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

#期货合约
def futures_transfer_fund(token,symbol,amount,side):
    #3243-账户资产划转
    url = "%s/api/v1/futures/account/transfer" % B3_url
    body={
        "token":token,
        "symbol":symbol,
        "amount":amount,
        "side":side
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_account_info(token,symbol=None):
    #3252-获取用户账户信息
    url = "%s/api/v1/futures/account_info" % B3_url
    body={
        "token":token,
        "symbol":symbol
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    # r = requests.get(url)
    # print(r.elapsed.total_seconds())
    print(json.loads(run.response))

def futures_get_contracts():
    #3279-获取合约基本配置
    url = "%s/api/v1/futures/contract/contract_config" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_get_fee_rate(token,symbol=None):
    #3333-获取用户手续费费率
    url = "%s/api/v1/futures/contract/fee_rate" % B3_url
    body={
        "token":token,
        "symbol":symbol
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_add_order(token,contract_code,direction,quantity,price,lever,source):
    #3342-合约下单
    url = "%s/api/v1/futures/order/place" % B3_url
    body={
        "token":token,
        "contract_code":contract_code,  #合约代号
        "direction":direction,          #交易方向，取值范围：sell_close=卖出平仓 sell_open=卖出开仓 buy_close=买入平仓 buy_open=买入开仓
        "quantity":quantity,            #下单数量
        "price":price,                  #下单价格，0=按对手价下单
        "lever":lever,                  #杠杆倍数
        "source":source                 #订单来源，取值范围：app | web
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    # r = requests.get(url)
    # print(r.elapsed.total_seconds())
    print(json.loads(run.response))

def futures_order_cancel(token,order_id):
    #3360-撤销订单
    url = "%s/api/v1/futures/order/cancel" % B3_url
    body={
        "token":token,
        "order_id":order_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_open_orders(token,symbol,page_number,page_size):
    #3369-获取当前委托
    url = "%s/api/v1/futures/order/open_orders" % B3_url
    body={
        "token":token,
        "symbol":symbol,
        "page_number":page_number,
        "page_size":page_size
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_close_orders(token,page_number,page_size,symbol=None):
    #3369-获取历史委托
    url = "%s/api/v1/futures/order/close_orders" % B3_url
    body={
        "token":token,
        "symbol":symbol,
        "page_number":page_number,
        "page_size":page_size
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_order_detail(token,order_id):
    #3387-获取委托详情
    url = "%s/api/v1/futures/order/order_detail" % B3_url
    body={
        "token":token,
        "order_id":order_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_trade_detail(token,order_id):
    #3405-获取委托成交明细
    url = "%s/api/v1/futures/order/trade_detail" % B3_url
    body={
        "token":token,
        "order_id":order_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_position_info(token,symbol):
    #3414-获取用户持仓信息
    url = "%s/api/v1/futures/position_info" % B3_url
    body={
        "token":token,
        "symbol":symbol
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    # r = requests.get(url)
    # print(r.elapsed.total_seconds())
    print(json.loads(run.response))

def futures_order_limit(token,symbol,contract_type):
    #3477-获取用户持仓量限制
    url = "%s/api/v1/futures/contract/order_limit" % B3_url
    body={
        "token":token,
        "symbol":symbol,
        "contract_type":contract_type #合约类型，取值范围：this_week=当周 next_week=次周 quarter=季度 next_quarter=次季度 不传或传空字符串则为全部 默认全部
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_get_position_limit(token,symbol,contract_type):
    #3486-获取用户下单量限制
    url = "%s/api/v1/futures/contract/position_limit" % B3_url
    body={
        "token":token,
        "symbol":symbol,
        "contract_type":contract_type #合约类型，取值范围：this_week=当周 next_week=次周 quarter=季度 next_quarter=次季度 不传或传空字符串则为全部 默认全部
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

#期货合约行情
def futures_index_price(symbol):
    #获取指数价格
    url = "%s/v2/futures/market/index_price" % B3_url
    body = {
        "symbol":symbol
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_market_depth(contract_code):
    #获取市场深度数据
    url = "%s/api/v1/futures/market/depth" % B3_url
    body = {
        "contract_code":contract_code #合约代码
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))
    return json.loads(run.response)

def futures_market_depth_merged(contract_code,precision):
    #获取聚合价格精度的市场深度数据
    url = "%s/api/v1/futures/market/depth/merged" % B3_url
    body = {
        "contract_code":contract_code,  #合约代码
        "precision":precision           #价格聚合精度， -2=2位小数，-1=1位小数，0=1位整数，1=2位整数... 以此类推
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))
    return json.loads(run.response)

def futures_market_history_kline(contract_code,period,size):
    #获取市场K线数据
    url = "%s/api/v1/futures/market/history/kline" % B3_url
    body = {
        "contract_code":contract_code,  #合约代码
        "period":period,                #时间粒度，0= 1分钟；1= 5分钟；2= 15分钟；3= 30分钟；4= 60分钟；5：1天
        "size":size                     #要获取的数据条数，最大值：1500
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))
    return json.loads(run.response)

def futures_market_last_trade(contract_code):
    #3450-获取市场最新成交涨跌数据
    url = "%s/api/v1/futures/market/last_trade" % B3_url
    body = {
        "contract_code":contract_code #合约代码
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_market_history_trade(contract_code,size):
    #3459-获取市场近期成交记录
    url = "%s/api/v1/futures/market/history/trade" % B3_url
    body = {
        "contract_code":contract_code, #合约代码
        "size":size                    #要获取的数据条数，最大值：50
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_market_top_trades(contract_code,size):
    #3468-获取市场Top买卖数据
    url = "%s/api/v1/futures/market/top_trades" % B3_url
    body = {
        "contract_code":contract_code, #合约代码
        "size":size                    #要获取的数据条数，取值范围：1~50
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # futures_common_get_contracts()
    futures_get_adjust_factor()
