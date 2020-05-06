# coding=utf-8
import traceback
import json
import requests
from API_test import RunMain
import time
from log import out_log
from login_register import user_login
from signature import get_signture
import demjson


# B3_url = "http://192.168.0.22:12024" #孙骞
B3_url = "https://api.b3dev.xyz" #B3dev
# B3_url = "http://api.B3sit.xyz" #B3sit
# B3_url = "http://api.B3sim.xyz" #B3sim
token_junxin = "f59d910a722302fe3b0b6a0542351cce"  # 俊鑫token
token_wen = "08cf9ab4a68819bddb381da4cdc311eb"  # 俊文token
token_guoliang = "bc3200619901095b749e2c49adff5f5e" #国亮token
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

def futures_contract_price_limit(contract_code):
    #3639-期货合约-获取合约最高最低限价
    url = "%s/api/v1/futures/common/contract_price_limit" % B3_url
    params = {
        "contract_code":contract_code #合约代码
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_common_effective_contracts():
    #3630-期货合约-获取平台生效的合约
    url = "%s/api/v1/futures/common/effective_contracts" % B3_url
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

def futures_account_position_info(token,symbol):
    #3621-获取用户账户及持仓信息
    url = "%s/api/v1/futures/account_position_info" % B3_url
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
    return json.loads(run.response)

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
    if json.loads(run.response)["code"] == 1000:
        order_id = json.loads(run.response)["data"]["order_id"]
        print("单号："+order_id,
              "下单数量:"+quantity,
              "下单价格:"+price,
              "杠杆倍数:"+lever,
              "交易方向:"+direction
              )
    else:
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

def futures_open_orders(token,page_number,page_size,symbol=None,contract_code=None):
    #3369-获取当前委托
    url = "%s/api/v1/futures/order/open_orders" % B3_url
    body={
        "token":token,
        "page_number":page_number,
        "page_size":page_size,
        "symbol":symbol,              #合约品种，默认全部，不与contract_code同时生效，contract_code存在时优先使用contract_code
        "contract_code":contract_code #合约代码，默认全部，不与symbol同时生效，contract_code存在时优先使用contract_code
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_close_orders(token,page_number,page_size,state,contract_code=None,symbol=None):
    #3378-获取历史委托
    url = "%s/api/v1/futures/order/close_orders" % B3_url
    body={
        "token":token,
        "page_number":page_number,
        "page_size":page_size,
        "state":state,                  #订单状态，取值范围：filled=已成交，cancelled=已撤销，不传或传空字符串则为全部
        "symbol":symbol,                #合约品种，默认全部，不与contract_code同时生效，contract_code存在时优先使用contract_code
        "contract_code":contract_code   #合约代码，默认全部，不与symbol同时生效，contract_code存在时优先使用contract_code
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

def futures_cancel_by_symbol(token,symbol):
    #3504-撤销指定合约品种的全部订单
    url = "%s/api/v1/futures/order/cancel_by_symbol" % B3_url
    body = {
        "token":token,
        "symbol":symbol
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='POST')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_cancel_by_contract_code(token,contract_code):
    #3504-撤销指定合约代码的全部订单
    url = "%s/api/v1/futures/order/cancel_by_contract_code" % B3_url
    body = {
        "token":token,
        "contract_code":contract_code   #合约代码：BTC——20200417
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='POST')
    # out_log(url,response_msg=json.loads(run.response))
    print(demjson.decode(run.response))

def futures_batch_cancel(token,order_ids):
    #3603-批量撤销订单
    url = "%s/api/v1/futures/order/batch_cancel" % B3_url
    body = {
        "token":token,
        "order_ids":order_ids   #多个订单号拼接字符串，以,分隔，最大数量：10
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='POST')
    out_log(url,response_msg=json.loads(run.response))
    print(demjson.decode(run.response))

#期货合约行情
def futures_index_price(symbol):
    #获取指数价格
    url = "%s/v2/futures/market/index_price" % B3_url
    body = {
        "symbol":symbol
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_market_depth(contract_code):
    #获取市场深度数据
    url = "%s/api/v1/futures/market/depth" % B3_url
    body = {
        "contract_code":contract_code #合约代码
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='GET')
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
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='GET')
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
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='GET')
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
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='GET')
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
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='GET')
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
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_position_limit(token,symbol=None,contract_type=None):
    #3486-获取用户下单量限制
    url = "%s/api/v1/futures/contract/position_limit" % B3_url
    body = {
        "token":token,
        "symbol":symbol,
        "contract_type":contract_type
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='POST')
    out_log(url,response_msg=json.loads(run.response))
    print(demjson.decode(run.response))

def futures_liquidation_orders(symbol,trade_type,create_date,page_number=None,page_size=None):
    #获取平台强平订单
    url = "%s/v2/futures/market/liquidation_orders" % B3_url
    body = {
        "symbol":symbol,
        "trade_type":trade_type,    #交易类型	1:全部,2: 平多,3: 平空
        "create_date":create_date,   #日期 7，90（7天或者90天）
        "page_number":page_number,
        "page_size":page_size
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_settlement_history(symbol,page_number=None,page_size=None):
    #获取平台交割结算记录
    url = "%s/v2/futures/market/settlement_history" % B3_url
    body = {
        "symbol":symbol,
        "page_number":page_number,
        "page_size":page_size
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_risk_reserve_info(symbol):
    #查询合约风险准备金余额
    url = "%s/v2/futures/market/risk_reserve_info" % B3_url
    body = {
        "symbol":symbol
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_risk_reserve_histroy(symbol,create_date):
    #查询合约风险准备金余额
    url = "%s/v2/futures/market/risk_reserve_histroy" % B3_url
    body = {
        "symbol":symbol,
        "create_date":create_date #	7，90（7天或者90天）
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_contract_his_open_interest(symbol,period):
    #平台持仓量查询
    url = "%s/v2/futures/market/contract_his_open_interest" % B3_url
    body = {
        "symbol":symbol,
        "period":period     #时间周期类型 1小时:"60min"，4小时:"4hour"，12小时:"12hour"，1天:"1day"
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # 获取平台合约信息
    # futures_common_get_contracts()
    # 获取平台生效的合约(简易版)
    # futures_common_effective_contracts()

    #获取平台阶梯调整系数
    # futures_get_adjust_factor()

    #获取合约最高最低限价
    # futures_contract_price_limit(contract_code="BTC_20200501")

    #获取用户账户及持仓信息
    futures_account_position_info(token=token_wen, symbol="BTC")
    # position_unsettled = a["data"]["positions"][0]["position_unsettled"]
    # position_settled = a["data"]["positions"][0]["position_settled"]
    # avg_price_open = a["data"]["positions"][0]["avg_price_open"]
    # settlement_price = a["data"]["positions"][0]["settlement_price"]
    # #持仓张数 = 未结算持仓张数 + 已结算持仓张数
    # position_hold = position_unsettled + position_settled
    # if position_hold == a["data"]["positions"][0]["position_hold"]:
    #     print("True")
    # else:
    #     print(position_hold)
    # #持仓均价 = (未结算持仓张数 * 开仓均价 + 已结算持仓张数 * 结算价格) / (未结算持仓张数 + 已结算持仓张数)
    # avg_price_hold = (position_unsettled*float(avg_price_open)+position_settled*float(settlement_price))/(position_unsettled+position_settled)
    # if avg_price_hold == float(a["data"]["positions"][0]["avg_price_hold"]):
    #     print("True")
    # else:
    #     print(avg_price_hold)

    #合约下单 0.卖平 1.卖开 16.买平 17.买开
    # futures_add_order(token=token_junxin,contract_code="BTC_20200501",direction="buy_close",quantity="7",price="9187.12",lever="10",source="web")
    # futures_add_order(token=token_wen,contract_code="BTC_20200501",direction="sell_close",quantity="62",price="9110.12",lever="10",source="web")

    #获取当前委托
    # futures_open_orders(token=token_wen,page_number="1", page_size="10")

    #获取历史委托
    # futures_close_orders(token=token_guoliang, page_number="1", page_size="50", state="partial_canceled", contract_code="BTC_20200925")

    #获取委托详情
    # futures_order_detail(token=token_guoliang, order_id="3654700")

    #单号撤单
    # futures_order_cancel(token=token_wen, order_id="3696778")

    #批量撤单
    #撤销指定合约品种的全部订单
    # futures_cancel_by_symbol(token=token_wen, symbol="BTC")
    #撤销指定合约代码的全部订单
    # futures_cancel_by_contract_code(token=token_wen, contract_code="BTC_20200501")
    #批量撤销单号订单
    # futures_batch_cancel(token=token_wen, order_ids="115626")

    #获取深度数据
    # futures_market_depth(contract_code="BTC_20200501")

    #账户资金划转 0=划转至币币账户 1=划转至合约账户
    # futures_transfer_fund(token="99bfe311791e9af2df58fe873484022c", symbol="BTC", amount="0.5", side="1")

    # 获取市场最新成交涨跌数据
    #  futures_market_last_trade(contract_code="BTC_20200501")

    # 获取市场K线数据
    # futures_market_history_kline(contract_code="BTC_20200925", period="1", size="100")

    #获取指数价
    # futures_index_price(symbol="ETH")

    #获取用户下单量限制
    # futures_position_limit(token=token_wen)

    #获取平台强平订单
    # futures_liquidation_orders(symbol="BTC", trade_type=1, create_date=7,page_number=None, page_size=None)

    #获取平台交割结算记录
    # futures_settlement_history(symbol="BTC", page_number=None, page_size=None)

    #查询合约风险准备金余额
    # futures_risk_reserve_info(symbol="BTC")

    #平台持仓量查询
    # futures_contract_his_open_interest(symbol="BTC", period="60min")