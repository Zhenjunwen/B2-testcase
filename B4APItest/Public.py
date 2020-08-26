# coding=utf-8
import json
from API_test import RunMain
from log import out_log
from B4APItest.signature import get_signture
import configparser
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

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


#公共分类
def common_contract_limit(symbol="",contract_type=""):
    #合约交易-获取合约下单及持仓限制
    url = "%s/api/v1/futures/common/contract_limit" % B4_url
    params = {
        "symbol":symbol,                #合约品种，默认全部
        "contract_type":contract_type   #合约类型，取值范围：this_week=当周 next_week=次周 quarter=季度 next_quarter=次季度 不传或传空字符串则默认为全部
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_contract(symbol=""):
    #合约交易-获取平台合约信息
    url = "%s/api/v1/futures/common/contracts" % B4_url
    params = {
        "symbol": symbol,  # 合约品种，默认全部
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_contract_fee_rate(symbol=""):
    #合约交易-获取合约手续费费率
    url = "%s/api/v1/futures/common/fee_rate" % B4_url
    params = {
        "symbol": symbol,  # 合约品种，默认全部
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_order_limit(symbol="",contract_type=""):
    #合约交易-获取合约持仓量限制
    url = "%s/api/v1/futures/common/order_limit" % B4_url
    params = {
        "symbol":symbol,                #合约品种，默认全部
        "contract_type":contract_type   #合约类型，取值范围：this_week=当周 next_week=次周 quarter=季度 next_quarter=次季度 不传或传空字符串则默认为全部
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_position_limit(symbol="",contract_type=""):
    #合约交易-获取合约持仓量限制
    url = "%s/api/v1/futures/common/position_limit" % B4_url
    params = {
        "symbol":symbol,                #合约品种，默认全部
        "contract_type":contract_type   #合约类型，取值范围：this_week=当周 next_week=次周 quarter=季度 next_quarter=次季度 不传或传空字符串则默认为全部
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_effective_contracts(symbol=""):
    #合约交易-获取平台合约简要信息
    url = "%s/api/v1/futures/common/effective_contracts" % B4_url
    params = {
        "symbol": symbol,  # 合约品种，默认全部
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,params), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_contract_price_limit(contract_code):
    #合约交易-获取合约最高最低限价
    url = "%s/api/v1/futures/common/contract_price_limit" % B4_url
    params = {
        "contract_code": contract_code,
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_contracts_symbols():
    #合约交易-获取平台合约品种
    url = "%s/api/v1/futures/common/symbols" % B4_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_adjust_factor(symbol=""):
    #合约交易-获取平台阶梯调整系数
    url = "%s/api/v1/futures/common/adjust_factor" % B4_url
    params = {
        "symbol": symbol,  # 合约品种，默认全部
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_timestamp():
    #获取系统当前时间
    url = "%s/api/v1/common/timestamp" % B4_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_symbols():
    #获取所有交易对
    url = "%s/api/v1/common/symbols" % B4_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_get_currencys():
    #获取所有币种及对应的主链
    url = "%s/api/v1/common/get_currencys" % B4_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_currencys():
    #获取所有币种
    url = "%s/api/v1/common/currencys" % B4_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_partitions():
    #获取所有交易区
    url = "%s/api/v1/common/partitions" % B4_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def common_get_tradePairs(partition=""):
    #获取所有交易对及最新成交涨跌信息
    url = "%s/api/v1/common/get_tradePairs" % B4_url
    params={
        "partition":partition
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret,params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

#banner
def banner_get_list(size,platform,language=""):
    #获取Banner列表
    url = "%s/api/v1/banner/get_list" % B4_url
    params = {
        "size":size,            #获取的记录数
        "platform":platform,    #终端类型，1=移动端 2=PC端
        "language":language
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(PC_apikey, PC_apisecret,params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

#公告
def announcement_get_list(page_number,page_size,platform,language=""):
    #获取公告列表
    url = "%s/api/v1/announcement/get_list" % B4_url
    params = {
        "page_number":page_number,
        "page_size":page_size,
        "platform":platform,
        "language":language
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret,params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def announcement_get_info(id):
    #获取公告列表
    url = "%s/api/v1/announcement/get_info" % B4_url
    params = {
        "id":id
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret,params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

#系统参数
def parameter_get_otc_config():
    #获取C2C交易配置参数
    url = "%s/api/v1/parameter/get_otc_config" % B4_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def parameter_get_tradePair_config():
    #获取交易对配置参数
    url = "%s/api/v1/parameter/get_tradePair_config" % B4_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def parameter_get_currency_parameters():
    #获取币种配置参数
    url = "%s/api/v1/parameter/get_currency_parameters" % B4_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def parameter_get_otc_countries():
    #获取开放C2C交易的国家和地区
    url = "%s/api/v1/parameter/get_otc_countries" % B4_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def parameter_get_registration_countries():
    #获取开放注册的国家和地区
    url = "%s/api/v1/parameter/get_registration_countries" % B4_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def parameter_get_currency_config(symbol,chain_id=""):
    #获取指定币种的配置参数
    url = "%s/api/v1/parameter/get_currency_config" % B4_url
    params = {
        "symbol":symbol,
        "chain_id":chain_id     #币种所归属的主链ID，仅当币种为多主链币种（如USDT）时该字段必填
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret,params), method='GET')
    out_log(url,send_msg=params,response_msg=json.dumps(run.response).encode("utf8"))
    print(run.response)

def parameter_get_top_tradePairs(size):
    #获取排序展示的交易对
    url = "%s/api/v1/parameter/get_top_tradePairs" % B4_url
    params = {
        "size":size
    }
    run = RunMain(url=url, params=params, data=None,
                  headers=get_signture(IOS_apikey, IOS_apisecret,params), method='GET')
    out_log(url,send_msg=params,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # common_contract_limit(symbol="", contract_type="")
    # common_contract(symbol="")
    # common_contract_fee_rate(symbol="")
    # common_order_limit(symbol="", contract_type="")
    # common_position_limit(symbol="", contract_type="")
    # common_effective_contracts(symbol="")
    # common_contract_price_limit(contract_code="BTC_20200828")
    # common_contracts_symbols()
    # common_adjust_factor(symbol="")
    # common_timestamp()
    # common_symbols()
    # common_get_currencys()
    # common_currencys()
    # common_partitions()
    # common_get_tradePairs(partition="")
    # banner_get_list(size="1", platform="2", language="")
    # announcement_get_list(page_number="1", page_size="5", platform="1", language="zh")
    # announcement_get_info(id="1")
    # parameter_get_otc_config()
    # parameter_get_tradePair_config()
    # parameter_get_currency_parameters()
    # parameter_get_otc_countries()
    # parameter_get_registration_countries()
    # parameter_get_currency_config(symbol='BTC', chain_id="1")
    # parameter_get_top_tradePairs(size="2")
    pass