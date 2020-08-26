# coding=utf-8
import json
from API_test import RunMain
from log import out_log
from B3APItest.signature import get_signture
import demjson
import configparser

cf = configparser.ConfigParser()
# 配置文件路径
cf.read("F:\mohu-test\configfile\B3config.cfg")

B3_url = cf.get("url", "url")
token_wen = cf.get('token', 'token_wen')
token_junxin = cf.get('token', 'token_junxin')
token_guoliang = cf.get('token', "token_guoliang")
H5_apikey = cf.get("Apikey", "H5_apikey")
H5_apisecret = cf.get("Apikey", "H5_apisecret")
sys_apikey = cf.get("Apikey", "sys_apikey")
sys_apisecret = cf.get("Apikey", "sys_apisecret")
Android_apikey = cf.get("Apikey", "Android_apikey")
Android_apisecret = cf.get("Apikey", "Android_apisecret")
IOS_apikey = cf.get("Apikey", "IOS_apikey")
IOS_apisecret = cf.get("Apikey", "IOS_apisecret")


# 公共分类
def futures_common_get_contracts(symbol=""):
    # 期货合约-3270-获取当前生效的合约
    url = "%s/api/v1/futures/common/contracts" % B3_url
    params = {
        "symbol": symbol
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_get_adjust_factor(symbol=""):
    # 期货合约-3306-获取平台阶梯调整系数
    url = "%s/api/v1/futures/common/adjust_factor" % B3_url
    params = {
        "symbol": symbol
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_contract_price_limit(contract_code):
    # 3639-期货合约-获取合约最高最低限价
    url = "%s/api/v1/futures/common/contract_price_limit" % B3_url
    params = {
        "contract_code": contract_code  # 合约代码
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_common_effective_contracts(symbol=""):
    # 3630-期货合约-获取平台生效的合约
    url = "%s/api/v1/futures/common/effective_contracts" % B3_url
    params = {
        "symbol": symbol
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


# 期货合约
def futures_transfer_fund(token, symbol, amount, side):
    # 3243-账户资产划转
    url = "%s/api/v1/futures/account/transfer" % B3_url
    body = {
        "token": token,
        "symbol": symbol,
        "amount": amount,
        "side": side
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_account_position_info(token, symbol):
    # 3621-获取用户账户及持仓信息
    url = "%s/api/v1/futures/account_position_info" % B3_url
    body = {
        "token": token,
        "symbol": symbol
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    # r = requests.get(url)
    # print(r.elapsed.total_seconds())
    print(json.loads(run.response))
    return json.loads(run.response)


def futures_get_contracts():
    # 3279-获取合约基本配置
    url = "%s/api/v1/futures/contract/contract_config" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_get_fee_rate(token, symbol=None):
    # 3333-获取用户手续费费率
    url = "%s/api/v1/futures/contract/fee_rate" % B3_url
    body = {
        "token": token,
        "symbol": symbol
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_add_order(token, contract_code, direction, quantity, price, lever, source):
    # 3342-合约下单
    url = "%s/api/v1/futures/order/place" % B3_url
    body = {
        "token": token,
        "contract_code": contract_code,  # 合约代号
        "direction": direction,  # 交易方向，取值范围：sell_close=卖出平仓 sell_open=卖出开仓 buy_close=买入平仓 buy_open=买入开仓
        "quantity": quantity,  # 下单数量
        "price": price,  # 下单价格，0=按对手价下单
        "lever": lever,  # 杠杆倍数
        "source": source  # 订单来源，取值范围：app | web
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        order_id = json.loads(run.response)["data"]["order_id"]
        print("单号：" + order_id,
              "下单数量:" + quantity,
              "下单价格:" + price,
              "杠杆倍数:" + lever,
              "交易方向:" + direction
              )
    else:
        print(json.loads(run.response))


def futures_order_cancel(token, order_id):
    # 3360-撤销订单
    url = "%s/api/v1/futures/order/cancel" % B3_url
    body = {
        "token": token,
        "order_id": order_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_open_orders(token, page_number, page_size, symbol="", contract_code=""):
    # 3369-获取当前委托
    url = "%s/api/v1/futures/order/open_orders" % B3_url
    body = {
        "token": token,
        "page_number": page_number,
        "page_size": page_size,
        "symbol": symbol,  # 合约品种，默认全部，不与contract_code同时生效，contract_code存在时优先使用contract_code
        "contract_code": contract_code  # 合约代码，默认全部，不与symbol同时生效，contract_code存在时优先使用contract_code
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_close_orders(token, page_number, page_size, state=None, contract_code=None, symbol=None):
    # 3378-获取历史委托
    url = "%s/api/v1/futures/order/close_orders" % B3_url
    body = {
        "token": token,
        "page_number": page_number,
        "page_size": page_size,
        "state": state,  # 订单状态，取值范围：filled=已成交，cancelled=已撤销，不传或传空字符串则为全部
        "symbol": symbol,  # 合约品种，默认全部，不与contract_code同时生效，contract_code存在时优先使用contract_code
        "contract_code": contract_code  # 合约代码，默认全部，不与symbol同时生效，contract_code存在时优先使用contract_code
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_order_detail(token, order_id):
    # 3387-获取委托详情
    url = "%s/api/v1/futures/order/order_detail" % B3_url
    body = {
        "token": token,
        "order_id": order_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_trade_detail(token, order_id):
    # 3405-获取委托成交明细
    url = "%s/api/v1/futures/order/trade_detail" % B3_url
    body = {
        "token": token,
        "order_id": order_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_order_limit(token, symbol, contract_type):
    # 3477-获取用户持仓量限制
    url = "%s/api/v1/futures/contract/order_limit" % B3_url
    body = {
        "token": token,
        "symbol": symbol,
        "contract_type": contract_type
        # 合约类型，取值范围：this_week=当周 next_week=次周 quarter=季度 next_quarter=次季度 不传或传空字符串则为全部 默认全部
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_get_position_limit(token, symbol, contract_type):
    # 3486-获取用户下单量限制
    url = "%s/api/v1/futures/contract/position_limit" % B3_url
    body = {
        "token": token,
        "symbol": symbol,
        "contract_type": contract_type
        # 合约类型，取值范围：this_week=当周 next_week=次周 quarter=季度 next_quarter=次季度 不传或传空字符串则为全部 默认全部
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_cancel_by_symbol(token, symbol):
    # 3504-撤销指定合约品种的全部订单
    url = "%s/api/v1/futures/order/cancel_by_symbol" % B3_url
    body = {
        "token": token,
        "symbol": symbol
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_cancel_by_contract_code(token, contract_code):
    # 3504-撤销指定合约代码的全部订单
    url = "%s/api/v1/futures/order/cancel_by_contract_code" % B3_url
    body = {
        "token": token,
        "contract_code": contract_code  # 合约代码：BTC——20200417
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    # out_log(url,response_msg=json.loads(run.response))
    print(demjson.decode(run.response))


def futures_batch_cancel(token, order_ids):
    # 3603-批量撤销订单
    url = "%s/api/v1/futures/order/batch_cancel" % B3_url
    body = {
        "token": token,
        "order_ids": order_ids  # 多个订单号拼接字符串，以,分隔，最大数量：10
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(demjson.decode(run.response))


def futures_financial_records(token, symbol, page_number, page_size, start_date, type=""):
    # 3648-获取用户财务记录
    url = "%s/api/v1/futures/account/financial_records" % B3_url
    body = {
        "token": token,
        "symbol": symbol,
        "page_number": page_number,
        "page_size": page_size,
        "type": type,  # 记录类型，取值范围：转入 | 转出 | 开仓 | 平仓 | 手续费 | 强平，不传或传空字符串则默认为全部
        "start_date": start_date  # 查询起始天数，取值范围：[1, 90]
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(demjson.decode(run.response))


def futures_history_trades(token, page_number, page_size, start_date, contract_code="", direction="", symbol=""):
    # 3783-获取历史成交记录
    url = "%s/api/v1/futures/order/history_trades" % B3_url
    body = {
        "token": token,
        "symbol": symbol,
        "contract_code": contract_code,
        "direction": direction,
        "page_number": page_number,
        "page_size": page_size,
        "start_date": start_date  # 查询起始天数，取值范围：[1, 90]
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(demjson.decode(run.response))


def futures_user_liquidation_orders(token, page_number, page_size, start_date="", contract_code="", direction="",
                                    symbol=""):
    # 6537-获取用户强平订单
    url = "%s/api/v1/futures/order/liquidation_orders" % B3_url
    body = {
        "token": token,
        "symbol": symbol,
        "contract_code": contract_code,
        "direction": direction,  # 交易方向，取值范围：buy_close=买入强平 sell_close=卖出强平，不传或传空字符创则默认为以上全部
        "page_number": page_number,
        "page_size": page_size,
        "start_date": start_date  # 查询起始天数，取值范围：[1, 90]
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(demjson.decode(run.response))


def futures_lighting_close_position(token, contract_code, direction, quantity, source="app"):
    # 6708-闪电平仓下单
    url = "%s/api/v1/futures/order/lighting_close_position" % B3_url
    body = {
        "token": token,
        "contract_code": contract_code,  # 合约代号
        "direction": direction,  # 交易方向，取值范围：buy=买入 sell=卖出
        "quantity": quantity,  # 下单数量
        "source": source  # 订单来源，取值范围：app | web
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        order_id = json.loads(run.response)["data"]["order_id"]
        print("单号：" + order_id,
              "下单数量:" + quantity,
              "交易方向:" + direction
              )
    else:
        print(json.loads(run.response))


def futures_order_trigger_place(token, contract_code, direction, price, quantity, lever, trigger_type, trigger_price,
                                source="app"):
    # 6726-计划委托下单
    url = "%s/api/v1/futures/order/trigger/place" % B3_url
    body = {
        "token": token,
        "contract_code": contract_code,  # 合约代号
        "direction": direction,  # 交易方向，取值范围：buy_open=买入开多 buy_close=买入平空 sell_open=卖出开空 sell_close=卖出平多
        "price": price,  # 下单价格，0=按市价下单
        "quantity": quantity,  # 下单数量
        "source": source,  # 订单来源，取值范围：app | web
        "lever": lever,  # 杠杆倍数
        "trigger_type": trigger_type,  # 触发类型，取值范围：ge=大于等于（最新价比触发价大） le=小于等于（最新价比触发价小）
        "trigger_price": trigger_price  # 触发价格
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        order_id = json.loads(run.response)["data"]["order_id"]
        print("计划委托单号：" + order_id,
              "合约代号：" + contract_code,  # 合约代号
              "交易方向：" + direction,  # 交易方向，取值范围：buy=买入 sell=卖出
              "下单价格：" + price,  # 下单价格，0=按市价下单
              "下单数量：" + quantity,  # 下单数量
              "杠杆倍数：" + lever,  # 杠杆倍数
              "触发类型：" + trigger_type,  # 触发类型，取值范围：ge=大于等于（最新价比触发价大） le=小于等于（最新价比触发价小）
              "触发价格：" + trigger_price  # 触发价格
              )
    else:
        print(json.loads(run.response))


def futures_trigger_cancel(token, order_id):
    # 6735-计划委托撤单
    url = "%s/api/v1/futures/order/trigger/cancel" % B3_url
    body = {
        "token": token,
        "order_id": order_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(demjson.decode(run.response))


def futures_trigger_cancel_by_symbol(token, symbol):
    # 6753-计划委托指定合约品种撤单
    url = "%s/api/v1/futures/order/trigger/cancel_by_symbol" % B3_url
    body = {
        "token": token,
        "symbol": symbol
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(demjson.decode(run.response))


def futures_trigger_cancel_by_contract_code(token, contract_code):
    # 6762-计划委托指定合约代码撤单
    url = "%s/api/v1/futures/order/trigger/cancel_by_contract_code" % B3_url
    body = {
        "token": token,
        "contract_code": contract_code
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(demjson.decode(run.response))


def futures_trigger_open_orders(token, symbol, contract_code, page_number="1", page_size="10"):
    # 6771-获取当前计划委托
    url = "%s/api/v1/futures/order/trigger/open_orders" % B3_url
    body = {
        "token": token,
        "symbol": symbol,
        "contract_code": contract_code,
        "page_number": page_number,
        "page_size": page_size
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(demjson.decode(run.response))


def futures_trigger_close_orders(token, symbol, contract_code, state, direction, start_date="90", page_number="1",
                                 page_size="10"):
    # 6780-获取历史计划委托
    url = "%s/api/v1/futures/order/trigger/close_orders" % B3_url
    body = {
        "token": token,
        "symbol": symbol,
        "contract_code": contract_code,
        "state": state,  # 委托状态，取值范围：succeed=执行成功 failed=执行失败 canceled=已撤销 不传或传空字符串则默认为以上全部
        "direction": direction,
        # 交易方向，取值范围：buy_open=买入开多 buy_close=买入平空 sell_open=卖出开空 sell_close=卖出平多，不传或传空字符串则默认为以上全部
        "start_date": start_date,  # 起始天数，取值范围：[1, 90]，默认值：90
        "page_number": page_number,
        "page_size": page_size
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(demjson.decode(run.response))


# 期货合约行情
def futures_index_price(symbol):
    # 获取指数价格
    url = "%s/v2/futures/market/index_price" % B3_url
    body = {
        "symbol": symbol
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_market_depth(contract_code):
    # 获取市场深度数据
    url = "%s/api/v1/futures/market/depth" % B3_url
    body = {
        "contract_code": contract_code  # 合约代码
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))
    return json.loads(run.response)


def futures_market_depth_merged(contract_code, precision):
    # 获取聚合价格精度的市场深度数据
    url = "%s/api/v1/futures/market/depth/merged" % B3_url
    body = {
        "contract_code": contract_code,  # 合约代码
        "precision": precision  # 价格聚合精度， -2=2位小数，-1=1位小数，0=1位整数，1=2位整数... 以此类推
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))
    return json.loads(run.response)


def futures_market_history_kline(kline_symbol, period, size):
    # 获取市场K线数据
    url = "%s/api/v1/futures/market/history/kline" % B3_url
    body = {
        "kline_symbol": kline_symbol,  # 【更新】合约K线名称，基本格式：合约品种_合约类型，其中合约类型取值范围如下：1=当周 2=次周 3=季度 4=次季度
        "period": period,  # 【更新】时间粒度，取值范围：0= 1分钟；1= 5分钟；2= 15分钟；3= 30分钟；4= 60分钟；5=1天；6=1周；7=1月
        "size": size  # 要获取的数据条数，最大值：1500
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))
    return json.loads(run.response)


def futures_market_last_trade(contract_code):
    # 3450-获取市场最新成交涨跌数据
    url = "%s/api/v1/futures/market/last_trade" % B3_url
    body = {
        "contract_code": contract_code  # 合约代码
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_market_history_trade(contract_code, size):
    # 3459-获取市场近期成交记录
    url = "%s/api/v1/futures/market/history/trade" % B3_url
    body = {
        "contract_code": contract_code,  # 合约代码
        "size": size  # 要获取的数据条数，最大值：50
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_market_top_trades(contract_code, size):
    # 3468-获取市场Top买卖数据
    url = "%s/api/v1/futures/market/top_trades" % B3_url
    body = {
        "contract_code": contract_code,  # 合约代码
        "size": size  # 要获取的数据条数，取值范围：1~50
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_position_limit(token, symbol=None, contract_type=None):
    # 3486-获取用户下单量限制
    url = "%s/api/v1/futures/contract/position_limit" % B3_url
    body = {
        "token": token,
        "symbol": symbol,
        "contract_type": contract_type
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(demjson.decode(run.response))


def futures_liquidation_orders(symbol, direction, start_date="", page_number="", page_size=""):
    # 获取平台强平订单
    url = "%s/api/v1/futures/market/liquidation_orders" % B3_url
    body = {
        "symbol": symbol,
        "direction": direction,  # 交易方向，取值范围：sell_close=卖出强平 buy_close=买入强平
        "start_date": start_date,  # 日期 1-90（默认90天）
        "page_number": page_number,
        "page_size": page_size
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_settlement_history(symbol, page_number="1", page_size="10"):
    # 获取平台交割结算记录
    url = "%s/api/v1/futures/market/settlement_history" % B3_url
    body = {
        "symbol": symbol,
        "page_number": page_number,
        "page_size": page_size
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_risk_risk_reserve(symbol):
    # 查询合约风险准备金余额
    url = "%s/api/v1/futures/market/risk_reserve" % B3_url
    body = {
        "symbol": symbol
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_risk_reserve_info(symbol):
    # 6609-获取合约风险准备金余额和预估分摊比例
    url = "%s/api/v1/futures/market/risk_reserve_info" % B3_url
    body = {
        "symbol": symbol
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_risk_reserve_histroy(symbol, page_number="1", page_size="10"):
    # 6564-获取合约风险准备金余额历史数据
    url = "%s/api/v1/futures/market/risk_reserve_history" % B3_url
    body = {
        "symbol": symbol,
        "page_number": page_number,
        "page_size": page_size

    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_contract_his_open_interest(symbol, period):
    # 平台持仓量查询
    url = "%s/api/v1/futures/market/open_interests" % B3_url
    body = {
        "symbol": symbol,
        "period": period  # 时间周期类型 1小时:"60min"，4小时:"4hour"，12小时:"12hour"，1天:"1day"
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_contract_open_interest(contract_code):
    # 6600-获取合约总持仓量
    url = "%s/api/v1/futures/market/contract_open_interest" % B3_url
    body = {
        "contract_code": contract_code,
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


# 代理商接口
def employee_apply(token, agent_user_id):
    # 3657-提交代理商员工申请
    url = "%s/api/v1/futures/agent/employee/apply" % B3_url
    body = {
        "token": token,
        "agent_user_id": agent_user_id  # 代理商UID
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def employee_details(token):
    # 3666-获取代理商员工申请信息
    url = "%s/api/v1/futures/agent/employee/details" % B3_url
    body = {
        "token": token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def employee_stats(token):
    # 3666-获取代理商推广员邀请统计信息
    url = "%s/api/v1/futures/agent/employee/stats" % B3_url
    body = {
        "token": token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def employee_role_info(token):
    # 3711-获取当前用户的代理商或员工角色信息
    url = "%s/api/v1/futures/agent/role_info" % B3_url
    body = {
        "token": token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


# 邀请
def invitation_my_stats(token):
    # 3756-获取我的邀请统计信息
    url = "%s/api/v1/invitation/my_stats" % B3_url
    body = {
        "token": token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def invitation_my_records(token, page_number, page_size):
    # 3765-获取我的邀请记录
    url = "%s/api/v1/invitation/my_records" % B3_url
    body = {
        "token": token,
        "page_number": page_number,
        "page_size": page_size,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))

#代理商佣金
def commission_records(token, page_number="1", page_size="20",symbol=""):
    # 6852-获取代理商佣金记录
    url = "%s/api/v1/futures/agent/commission_records" % B3_url
    body = {
        "token": token,
        "page_number": page_number,
        "page_size": page_size,
        "symbol":symbol
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def commission_detail(token, record_id):
    # 6861-获取代理商佣金记录详情
    url = "%s/api/v1/futures/agent/commission_detail" % B3_url
    body = {
        "token": token,
        "record_id": record_id,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url, send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))


if __name__ == "__main__":
    # 获取用户财务记录
    # futures_financial_records(token=token_wen, symbol="BTC", page_number="1", page_size="10", start_date="90", type=None)

    # 获取平台合约信息
    # futures_common_get_contracts()
    # 获取平台生效的合约(简易版)
    # futures_common_effective_contracts(symbol="")

    # 获取平台阶梯调整系数
    # futures_get_adjust_factor(symbol="")

    # 获取合约最高最低限价
    # futures_contract_price_limit(contract_code="BTC_20200925")

    # 获取用户手续费费率
    # futures_get_fee_rate(token=token_wen, symbol=None)

    # 获取用户账户及持仓信息
    # futures_account_position_info(token="7dc735bca17f4adb80ec25ac6b5ea8b8", symbol="BTC")

    # 合约下单 0.卖平 1.卖开 16.买平 17.买开
    # futures_add_order(token="3b1a77ae9d2461a98b42e14cd5fdddd0", contract_code="ETH_20200925", direction="buy_open", quantity="10",price="220", lever="20", source="web")
    # futures_add_order(token="df1323b0c892485a355e97b4bdb8078e", contract_code="BTC_20200925", direction="sell_open", quantity="10",price="10000", lever="20", source="web")
    # futures_add_order(token="b9af43c16aff172301ded42f002c82bf",contract_code="BTC_20200626",direction="buy_open",quantity="100",price="9350.55",lever="20",source="web")

    # 闪电平仓
    # futures_lighting_close_position(token="15a66dbf7b9c35a19d621e3bdd55ca50",contract_code ="BTC_20200717", direction="sell_open", quantity="1", source="app")

    # 获取当前委托
    # futures_open_orders(token=token_wen,page_number="1", page_size="10")

    # 获取委托成交明细
    # futures_trade_detail(token=token_wen, order_id="6904344")

    # 获取历史委托
    # futures_close_orders(token=token_wen, page_number="1", page_size="50")

    # 获取委托详情
    # futures_order_detail(token=token_wen, order_id="4441293")

    # 单号撤单
    # futures_order_cancel(token="a53f0b40b844d41df43cda195babe271", order_id="60662")

    # 批量撤单
    # 撤销指定合约品种的全部订单
    # futures_cancel_by_symbol(token=token_wen, symbol="BTC")
    # 撤销指定合约代码的全部订单
    # futures_cancel_by_contract_code(token=token_junxin, contract_code="BTC_20200626")
    # 批量撤销单号订单
    # futures_batch_cancel(token=token_junxin, order_ids="15956408,15956439")

    # 获取历史成交记录
    # futures_history_trades(token=token_wen, page_number="1", page_size="50", start_date="90", contract_code="BTC_20200626", direction="", symbol="")

    # 计划委托下单
    # futures_order_trigger_place(token="15a66dbf7b9c35a19d621e3bdd55ca50", contract_code="BTC_20200717", direction="buy_open", quantity="1",price="9103.32",lever="20", trigger_type="ge", trigger_price="9100.33")

    # 计划委托撤单
    # futures_trigger_cancel(token="b92609f7007acfc2fe94b975e7b4e366", order_id="25")

    # 计划委托指定合约品种撤单
    # futures_trigger_cancel_by_symbol(token=token_wen, symbol="BTC")

    # 计划委托指定合约代码撤单
    # futures_trigger_cancel_by_contract_code(token=token_wen, contract_code="BTC_20200703")

    # 获取当前计划委托
    # futures_trigger_open_orders(token=token_wen, symbol="BTC", contract_code="")

    # 获取历史计划委托
    # futures_trigger_close_orders(token=token_wen, symbol="BTC", contract_code="BTC_20200703", state="canceled", direction="sell_open")

    # 获取深度数据
    # futures_market_depth(contract_code="BTC_20200612")

    # 账户资金划转 0=划转至币币账户 1=划转至合约账户
    # futures_transfer_fund(token="3b1a77ae9d2461a98b42e14cd5fdddd0", symbol="ETH", amount="5", side="1")
    # futures_transfer_fund(token=token_junxin, symbol="BTC", amount="5", side="1")

    # futures_transfer_fund(token="5eb4c2fc44d3a782fa51c8d5c3d99cf7", symbol="ETH", amount="100", side="1")

    # 获取市场最新成交涨跌数据
    # futures_market_last_trade(contract_code="BTC_20200612")

    # 获取市场近期成交记录
    # futures_market_history_trade(contract_code="BTC_20200612", size="50")

    # 获取市场K线数据
    # futures_market_history_kline(kline_symbol="BTC_1", period="7", size="100")

    # 获取指数价
    # futures_index_price(symbol="BTC")

    # 获取用户下单量限制
    # futures_position_limit(token=token_wen)

    # 获取平台强平订单
    # futures_liquidation_orders(symbol="BTC", direction="sell_close",start_date="90",page_number="1", page_size="30")

    # 获取用户强平订单
    # futures_user_liquidation_orders(token=token_wen, page_number="1", page_size="50", start_date="", contract_code="", direction="", symbol="BTC")

    # 获取平台交割结算记录
    # futures_settlement_history(symbol="BTC")

    # 获取合约风险准备金余额和预估分摊比例
    # futures_risk_reserve_info(symbol="BTC")
    # 获取合约风险准备金余额
    # futures_risk_risk_reserve(symbol="BTC")

    # 获取合约风险准备金余额历史数据
    # futures_risk_reserve_histroy(symbol="BTC",start_date="")

    # 平台持仓量查询
    # futures_contract_his_open_interest(symbol="BTC", period="12hour")

    # 获取合约总持仓量
    # futures_contract_open_interest(contract_code="BTC_20200626")

    # 获取用户财务记录
    # futures_financial_records(token=token_junxin, symbol="BTC", page_number="1", page_size="50", start_date="90", type="")

    # 提交代理商员工申请
    # employee_apply(token="4c16c228a453c1d19dee7569bb194f6b", agent_user_id="126379")

    # 获取代理商员工申请信息
    # employee_details(token=token_junxin)

    # 获取代理商推广员邀请统计信息
    # employee_stats(token=token_junxin)

    # 获取当前用户的代理商或员工角色信息
    # employee_role_info(token=token_wen)

    # 获取我的邀请统计信息
    # invitation_my_stats(token=token_wen)

    # 获取我的邀请记录
    # invitation_my_records(token=token_wen, page_number="1", page_size="10")

    #获取代理商佣金记录
    # commission_records(token=token_junxin, page_number="1", page_size="20", symbol="")
    pass
