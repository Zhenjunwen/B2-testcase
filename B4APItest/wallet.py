#coding=utf-8
import hashlib
import json
from API_test import RunMain
from B4APItest.signature import get_signture
from DB_config import DB
from log import out_log
from B4APItest.login_register import send_sms
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


def get_asset(token,symbol):
    # 获取币币账户指定币种资产
    url = "%s/api/v1/wallet/get_asset" % B4_url
    body = {
        "token": token,
        "symbol": symbol,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def total_assets(token,type,quote_currency=""):
    # 5205-获取账户折合总资产
    url = "%s/api/v1/wallet/total_assets" % B4_url
    body = {
        "token": token,
        "type":type,    #资产类型，取值范围：：1=币币资产  2=法币资产  4=合约资产，可组合使用
        "quote_currency":quote_currency    #计价币种，取值范围：USD | CNY，默认值：USD
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def withdraw(token,symbol,amount,address,password,account,chain_id):
    #提交提币申请
    url = "%s/api/v1/wallet/withdraw" % B4_url
    password = str(hashlib.sha256(password.encode('utf-8')).hexdigest()).upper()
    db = DB('mysql.b4dev.xyz', 3306, 'b4_api', 'eYKRj3Vp@zM0SGWj', 'b4')  # B4devDB
    verification_id = send_sms(sms_type="7", account=account,token=token)
    verification_code = db.query(
        "SELECT verification_code FROM `user_verification_code` WHERE user_account = 86%s ORDER BY code_over_time DESC LIMIT 1" % account)[0][0]
    body={
        "token":token,
        "symbol":symbol,
        "amount":amount,
        "address":address,
        "verification_id":verification_id,
        "verification_code":verification_code,
        "password":password,
        "account":"86%s"%account,
        "chain_id":chain_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_asset_c2c(token,symbol):
    # 获取C2C账户指定币种资产
    url = "%s/api/v1/wallet/get_asset_c2c" % B4_url
    body = {
        "token": token,
        "symbol":symbol
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_assets_c2c(token):
    # 获取C2C账户资产列表
    url = "%s/api/v1/wallet/get_assets_c2c" % B4_url
    body = {
        "token": token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_address(token,symbol,chain_id):
    # 获取充币地址
    url = "%s/api/v1/wallet/get_address" % B4_url
    body = {
        "token": token,
        "symbol": symbol,
        "chain_id": chain_id,#	币种所归属的主链ID
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_recharge_list(token,symbol,page_number="1",page_size="10"):
    # 获取充币记录
    url = "%s/api/v1/wallet/get_recharge_list" % B4_url
    body = {
        "token": token,
        "symbol": symbol,
        "page_number": page_number,
        "page_size":page_size
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_recharge_detail(token,record_id):
    # 获取充币记录详情
    url = "%s/api/v1/wallet/get_recharge_detail" % B4_url
    body = {
        "token": token,
        "record_id":record_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def cancel_withdraw(token,record_id):
    # 取消提币
    url = "%s/api/v1/wallet/cancel_withdraw" % B4_url
    body = {
        "token": token,
        "record_id": record_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_assets(token):
    # 获取币币账户资产列表
    url = "%s/api/v1/wallet/get_assets" % B4_url
    body = {
        "token": token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_withdrawal_list(token,symbol,page_number="1",page_size="10"):
    # 获取提币记录
    url = "%s/api/v1/wallet/get_withdrawal_list" % B4_url
    body = {
        "token": token,
        "symbol": symbol,
        "page_number": page_number,
        "page_size": page_size
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_withdrawal_detail(token,record_id):
    # 获取提币记录详情
    url = "%s/api/v1/wallet/get_withdrawal_detail" % B4_url
    body = {
        "token": token,
        "record_id": record_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_withdrawal_limit(token,symbol,chain_id):
    # 获取提币记录详情
    url = "%s/api/v1/wallet/get_withdrawal_limit" % B4_url
    body = {
        "token": token,
        "symbol": symbol,
        "chain_id":chain_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_transfer_list(token,page_number="1",page_size="10",symbol=""):
    # 获取资金划转记录
    url = "%s/api/v1/wallet/get_transfer_list" % B4_url
    body = {
        "token": token,
        "symbol": symbol,
        "page_number": page_number,
        "page_size": page_size,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_flow_list(token,page_number="1",page_size="10",symbol="",side="",type="",biz_type=""):
    # 获取资产流水记录
    url = "%s/api/v1/wallet/get_flow_list" % B4_url
    body = {
        "token": token,
        "symbol": symbol,
        "page_number": page_number,
        "page_size": page_size,
        "side":side,
        "type":type,
        "biz_type":biz_type
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def transfer_fund(token,symbol,amount,side):
    # 资金划转
    url = "%s/api/v1/wallet/transfer_fund" % B4_url
    body = {
        "token": token,
        "symbol": symbol,
        "amount": amount,
        "side": side, #划转方向， 1=划往C2C账户 0=划往币币账户
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def validate_address(symbol,chain_id,address):
    # 验证提币地址是否合法
    url = "%s/api/v1/wallet/validate_address" % B4_url
    body = {
        "symbol": symbol,
        "chain_id":chain_id,
        "address":address,
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='GET')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # get_asset(token=token_wen, symbol="BTC")
    # total_assets(token=token_wen, type="7", quote_currency="USD")
    # withdraw(token=token_wen, symbol="ETH", amount="0.05", address="0x769539b4937d4dEE08b363a2135679Fc8baE5772", password="123456", account="15521057551", chain_id="2")
    # get_asset_c2c(token=token_wen, symbol="BTC")
    # get_assets_c2c(token=token_wen)
    # get_address(token=token_wen, symbol="ETH", chain_id="2")
    # cancel_withdraw(token=token_wen, record_id="1")
    # get_recharge_detail(token=token_wen, record_id="2")
    # get_assets(token=token_wen)
    # get_withdrawal_list(token=token_wen, symbol="ETH", page_number="1", page_size="10")
    # get_withdrawal_detail(token=token_wen, record_id="7")
    get_withdrawal_limit(token=token_wen, symbol="USDT", chain_id="2")
    # get_transfer_list(token=token_wen,symbol="")
    # transfer_fund(token=token_wen, symbol="BTC", amount="0.1", side="1")
    # validate_address(symbol="ETH", chain_id="2", address="0x769539b4937d4dEE08b363a2135679Fc8baE5772")
    pass