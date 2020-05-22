#coding=utf-8
import hashlib
import json
from API_test import RunMain
import time
from C2C_api import get_signture
from DB_config import DB
from log import out_log
from login_register import send_sms
import configparser

cf = configparser.ConfigParser()
#配置文件路径
cf.read("F:\mohu-test\config.cfg")
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



if __name__ == "__main__":
    # withdraw(token="70184cc27a0ed8a4cd75b96ae31b9646", symbol="GK", amount="10", address="2Hbn8bzVx52Ys9E2HpBvzkRztoRHSGXke7X", password="zjw971006", account="15521057551", chain_id="5")
    # get_asset_c2c(token_wen)
    validate_token(token_wen)
    # transfer_fund(token_wen, symbol="USDT", amount="200", side="1")
    # get_transfer_list(token=token_wen, page_number="1", page_size="20", symbol="")
    # KYC(token="f80dfb7a06668d567282da239609c73d",name="甄俊壕",certificate_type="2",certificate_no="440682199710064034")
