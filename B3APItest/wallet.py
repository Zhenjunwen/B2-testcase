#coding=utf-8
import hashlib
import json
from B3APItest.API_test import RunMain
from B3APItest.C2C_api import get_signture
from B3APItest.DB_config import DB
from log import out_log
from B3APItest.login_register import send_sms
import configparser

cf = configparser.ConfigParser()
#配置文件路径
cf.read("F:\mohu-test\configfile\config.cfg")
B3_url = cf.get("url","url")
token_wen = cf.get('token','token_wen')
token_junxin = cf.get('token','token_junxin')
token_guoliang=cf.get('token',"token_guoliang")
H5_apikey =cf.get("Apikey","H5_apikey")
H5_apisecret =cf.get("Apikey","H5_apisecret")
sys_apikey =cf.get("Apikey","sys_apikey")
sys_apisecret =cf.get("Apikey","sys_apisecret")
Android_apikey =cf.get("Apikey","Android_apikey")
Android_apisecret =cf.get("Apikey","Android_apisecret")
IOS_apikey =cf.get("Apikey","IOS_apikey")
IOS_apisecret =cf.get("Apikey","IOS_apisecret")


def get_address(token,symbol,chain_id):
    # 获取充币地址
    url = "%s/api/v1/wallet/get_address" % B3_url
    body = {
        "token": token,
        "symbol": symbol,
        "chain_id": chain_id,#	币种所归属的主链ID
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def withdraw(token,symbol,amount,address,password,account,chain_id):
    #提币
    url = "%s/api/v1/wallet/withdraw" % B3_url
    password = str(hashlib.sha256(password.encode('utf-8')).hexdigest()).upper()
    db = DB('mysql.b3dev.xyz', 3306, 'b3_api', 'fGFcqRkHC5D2z^b^', 'b3')  # B3devDB
    # db = DB('mysql.b2dev.xyz', 3306, 'b2_cc', 'EV0Yom7L5l4r', 'biso')  # devDB
    # db = DB('mysql.b2sit.xyz', 3306, 'b2_cc', '7iD5uXtW84tG', 'biso') #sitDB
    # db = DB('mysql.b2sim.xyz', 3306, 'b2_cc', '30iAc2sF8UZa', 'biso') #simDB
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

def get_withdrawal_list(token,symbol,page_number="1",page_size="10"):
    # 获取提币记录
    url = "%s/api/v1/wallet/get_withdrawal_list" % B3_url
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

def cancel_withdraw(token,record_id):
    # 取消提币
    url = "%s/api/v1/wallet/cancel_withdraw" % B3_url
    body = {
        "token": token,
        "record_id": record_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def transfer_fund(token,symbol,amount,side):
    # 资金划转
    url = "%s/api/v1/wallet/transfer_fund" % B3_url
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

def get_transfer_list(token,page_number,page_size,symbol=""):
    # 获取资金划转记录
    url = "%s/api/v1/wallet/get_transfer_list" % B3_url
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

def get_asset_c2c(token):
    # 获取C2C账户指定币种资产
    url = "%s/api/v1/wallet/get_assets_c2c" % B3_url
    body = {
        "token": token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_assets(token):
    # 获取币币账户币种资产
    url = "%s/api/v1/wallet/get_assets" % B3_url
    body = {
        "token": token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def validate_token(token):
    # 检验token是否有效
    url = "%s/api/v1/user/validate_token" % B3_url
    body = {
        "token": token
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def KYC(token,name,certificate_type,certificate_no):
    # KYC实名认证
    url = "%s/api/v1/authentication/kyc" % B3_url
    body = {
        "token": token,
        "name":name,
        "certificate_type":certificate_type,
        "certificate_no":certificate_no
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def validate_address(symbol,chain_id,address):
    # 验证提币地址是否合法
    url = "%s/api/v1/wallet/validate_address" % B3_url
    body = {
        "symbol": symbol,
        "chain_id":chain_id,
        "address":address,
    }
    run = RunMain(url=url, params=body, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='GET')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def total_assets(token,type,quote_currency=""):
    # 5205-获取账户折合总资产
    url = "%s/api/v1/wallet/total_assets" % B3_url
    body = {
        "token": token,
        "type":type,    #资产类型，取值范围：：1=币币资产  2=法币资产  4=合约资产，可组合使用
        "quote_currency":quote_currency    #计价币种，取值范围：USD | CNY，默认值：USD
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_recharge_list(token,symbol,page_number="1",page_size="10"):
    # 5205-获取账户折合总资产
    url = "%s/api/v1/wallet/get_recharge_list" % B3_url
    body = {
        "token": token,
        "symbol":symbol,
        "page_number":page_number,
        "page_size":page_size

    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_recharge_detail(token,record_id):
    # 5205-获取账户折合总资产
    url = "%s/api/v1/wallet/get_recharge_detail" % B3_url
    body = {
        "token": token,
        "record_id":record_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # get_recharge_detail(token=token_junxin, record_id='1853')
    # get_recharge_list(token=token_junxin, symbol="USDT", page_number="1", page_size="10")
    # get_withdrawal_list(token=token_wen, symbol="ETH")
    # withdraw(token=token_wen, symbol="ETH", amount="0.05", address="0x769539b4937d4dEE08b363a2135679Fc8baE5772", password="123456", account="15521057551", chain_id="2")
    # cancel_withdraw(token=token_wen, record_id="6")
    # get_asset_c2c(token_wen)
    # validate_token(token_wen)
    # transfer_fund(token_wen, symbol="USDT", amount="90", side="1")
    # transfer_fund(token_wen, symbol="USDT", amount="90", side="0")
    # transfer_fund(token_wen, symbol="-btc", amount="1", side="1")
    # transfer_fund(token_wen, symbol="BTC", amount="1", side="0")
    # get_transfer_list(token=token_wen, page_number="1", page_size="20", symbol="")
    # KYC(token="f80dfb7a06668d567282da239609c73d",name="甄俊壕",certificate_type="2",certificate_no="440682199710064034")
    # validate_address(symbol="EOS", chain_id="2", address="0x769539b4937d4dEE08b363a2135679Fc8baE5772")
    total_assets(token=token_wen, type="7", quote_currency="USD")
