# coding=utf-8
import traceback
import json
from API_test import RunMain
import time
from log import out_log
from login_register import user_login
from signature import get_signture

# B3_url = "http://192.168.0.22:12024" #孙骞
B3_url = "https://api.b3dev.xyz" #B3dev
# B3_url = "http://api.B3sit.xyz" #B3sit
# B3_url = "http://api.B3sim.xyz" #B3sim
token_junxin = "17d740ce53869ceb3dce06e943e88488"  # 俊鑫token
token_wen = "7893e454c38358872bb9fbcbb78f965c"  # 俊文token
sys_token = "2da373f6d5ffc1f6a42120eb5a893adb" #B3后台token
H5_apikey = "alLzET7dFLYN5ONg"
H5_apisecret = "rpoEwZeM"
sys_apikey = "4NHMhvsQ15TFNyVO"
sys_apisecret = "h8eiT26J"
Android_apikey = "ctyD04PtGMIsJtNZ"
Android_apisecret = "41DwD4ST"


def futures_get_contracts():
    #3279-获取合约基本配置
    url = "%s/api/v1/futures/contract/contract_config" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(run.response)

def futures_common_get_contracts():
    #期货合约-3270-获取当前生效的合约
    url = "%s/api/v1/futures/common/contracts" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_common_get_contract(contract_code):
    #期货合约-3288-获取指定合约信息
    url = "%s/api/v1/futures/common/contract" % B3_url
    body={
        "contract_code":contract_code
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,body), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_get_adjust_factor():
    #期货合约-3306-获取平台阶梯调整系数
    url = "%s/api/v1/futures/common/adjust_factor" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_get_assets(token):
    #3252-获取合约账户资产
    url = "%s/api/v1/futures/account/assets" % B3_url
    body={
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_get_asset(token,symbol):
    #3261-获取合约账户指定币种资产
    url = "%s/api/v1/futures/account/asset" % B3_url
    body={
        "token":token,
        "symbol":symbol
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))


def futures_transfer_fund(token,symbol,amount,side):
    #3243-账户资产划转
    url = "%s/api/v1/futures/account/transfer_fund" % B3_url
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

def futures_get_position_limit(token,symbol,contract_type):
    #3315-获取用户持仓量限制
    url = "%s/api/v1/futures/contract/position_limit" % B3_url
    body={
        "token":token,
        "symbol":symbol,
        "contract_type":contract_type #合约类型，1=当周 2=次周 3=季度 4=次季度 0=全部 默认为全部
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_get_order_limit(token,symbol,contract_type):
    #3324-获取用户下单数量限制
    url = "%s/api/v1/futures/contract/order_limit" % B3_url
    body={
        "token":token,
        "symbol":symbol,
        "contract_type":contract_type #合约类型，1=当周 2=次周 3=季度 4=次季度 0=全部 默认为全部
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def futures_get_fee_rate(token,symbol):
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

def futures_add_order(token,contract_code,side,quantity,price,lever,source):
    #3342-合约下单
    url = "%s/api/v1/futures/order/place" % B3_url
    body={
        "token":token,
        "contract_code":contract_code,  #合约代号
        "side":side,                    #交易方向，0=卖出平仓 1=卖出开仓 2=买入平仓 3=买入开仓
        "quantity":quantity,            #下单数量
        "price":price,                  #下单价格，0=按对手价下单
        "lever":lever,                  #杠杆倍数
        "source":source                 #订单来源，取值范围：app | web
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # futures_get_adjust_factor(symbol="BTC")
    # futures_common_get_contract(contract_code="BTC_20200417")
    # futures_common_get_contracts()
    futures_get_contracts()
    # pass
