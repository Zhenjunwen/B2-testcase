#coding=utf-8
import hashlib
import json
from API_test import RunMain
import time
from B2_C2C_api import get_signture
from DB_config import DB
from log import out_log
from login_register import send_sms, user_login

# B2_url = "http://192.168.0.22:12024" #孙骞
B2_url = "http://api.b2dev.xyz" #B2dev
# B2_url = "http://api.b2sit.xyz"  # B2sit
# B2_url = "http://api.b2sim.xyz" #B2sim
token_junxin = "80fe2d99db7b256063b80874fedc05cf"  # 俊鑫token
token_wen = "b41a6ec802efad9856b5862b13a2fbbd"  # 俊文token
# sys_token = "2da373f6d5ffc1f6a42120eb5a893adb" #B2后台token
H5_apikey = "alLzET7dFLYN5ONg"
H5_apisecret = "rpoEwZeM"
sys_apikey = "4NHMhvsQ15TFNyVO"
sys_apisecret = "h8eiT26J"
sys_token = "01f9936ad43a673e517dd4712c9b38e9"#B2dev

def get_address(token,symbol,chain_id):
    # 获取充币地址
    url = "%s/api/v1/wallet/get_address" % B2_url
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
    url = "%s/api/v1/wallet/withdraw" % B2_url
    password = str(hashlib.sha256((password + "BSOEXSS").encode('utf-8')).hexdigest()).upper()
    # db = DB('192.168.0.120', 3306, 'tars2', '#k6tYIA4KrYfFU0y', 'biso') #内网DB
    db = DB('mysql.b2dev.xyz', 3306, 'b2_cc', 'EV0Yom7L5l4r', 'biso')  # devDB
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
    url = "%s/api/v1/wallet/transfer_fund" % B2_url
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

def get_asset_c2c(token):
    # 获取C2C账户指定币种资产
    url = "%s/api/v1/wallet/get_assets_c2c" % B2_url
    body = {
        "token": token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def get_assets(token):
    # 获取币币账户币种资产
    url = "%s/api/v1/wallet/get_assets" % B2_url
    body = {
        "token": token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def validate_token(token):
    # 检验token是否有效
    url = "%s/api/v1/user/validate_token" % B2_url
    body = {
        "token": token
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def KYC(token,name,certificate_type,certificate_no):
    # KYC实名认证
    url = "%s/api/v1/authentication/kyc" % B2_url
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
    get_asset_c2c(token_wen)
    # validate_token(token_wen)
    # transfer_fund(token_junxin, symbol="BTC", amount="100", side="1")
    # KYC(token_wen,"甄俊壕","2","440682199710064034")
