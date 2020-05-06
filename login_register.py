#coding=utf-8

import json
from API_test import RunMain
import time
import hashlib
from DB_config import DB
from log_tool import console_out
from signature import get_signture
from log import out_log
import traceback

# B2_url = "http://192.168.0.22:12024" #孙骞
B3_url = "https://api.b3dev.xyz" #B3dev
B2_url = "http://api.b2dev.xyz" #B2dev
# B2_url = "http://api.b2sit.xyz" #B2sit
# B2_url = "http://api.b2sim.xyz" #B2sim
token_junxin = "17d740ce53869ceb3dce06e943e88488"  # 俊鑫token
token_wen = "08cf9ab4a68819bddb381da4cdc311eb"  # 俊文token
sys_token = "2da373f6d5ffc1f6a42120eb5a893adb" #B2后台token
H5_apikey = "sUY7qsoHudTrw2Ct"
H5_apisecret = "gEq76SZv"
sys_apikey = "5S7NukaMpMVW8U4Z"
sys_apisecret = "p0fbgZI0"
Android_apikey = "qbmkIS55ptjBhZFp"
Android_apisecret = "7M1H4mXA"
IOS_apikey = "oStkKLmJ5Q8S4n3b"
IOS_apisecret = "gKByU6HC"

def send_sms(sms_type,account,dialing_code="86",token="",language="zh"):
    #发送短信验证码-验证码发送成功后服务器返回的验证码ID
    url = "%s/api/v1/send/sms" % B3_url
    body = {
        "type": sms_type,#验证码类型，1=注册 2=登录 3=重置登录密码 4=修改登录密码 5=重置交易密码 6=添加收款方式 7=钱包提现 8=申请ApiKey  9=编辑ApiKey 10=绑定谷歌验证器
        "dialing_code":dialing_code, #区号
        "account":account,
        "token":token, #用户令牌 type > 3时必填
        "language":language #语言，取值："zh"=简体中文, "en"=英文, 默认"zh"
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey,Android_apisecret,body), method='POST')
    out_log(url,body,json.loads(run.response))
    code = json.loads(run.response)["code"]
    # print(json.loads(run.response))
    if code == 1000:
        verification_id = json.loads(run.response)["data"]["verification_id"]
        print(verification_id)
        return verification_id
    elif code == 2994:
        wait_time = json.loads(run.response)["data"]["wait_time"]
        print("重新获取验证需等待%d秒"%wait_time)
    else:
        print(json.loads(run.response))

def register(account,password,verification_id,type="1",dialing_code="86",invitation_code="",platform="2"):
    #注册
    url = "%s/api/v1/user/register" % B3_url
    db = DB('mysql.b3dev.xyz', 3306, 'b3_api', 'fGFcqRkHC5D2z^b^', 'b3')  # B3devDB
    # db = DB('192.168.0.120', 3306, 'tars2', '#k6tYIA4KrYfFU0y', 'biso') #内网DB
    # db = DB('mysql.b2dev.xyz', 3306, 'b2_cc', 'EV0Yom7L5l4r', 'biso') #devDB
    # db = DB('mysql.b2sit.xyz', 3306, 'b2_cc', '7iD5uXtW84tG', 'biso') #sitDB
    # db = DB('mysql.b2sim.xyz', 3306, 'b2_cc', '30iAc2sF8UZa', 'biso') #simDB
    verification_code = db.query("SELECT verification_code FROM `user_verification_code` WHERE user_account = 86%s ORDER BY code_over_time DESC LIMIT 1"%account)[0][0]
    # print(verification_code)
    password = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
    body = {
        "account":account,
        "password":password,
        "verification_id":verification_id, # 验证码发送成功后服务器返回的验证码ID
        "type":type, # 账号类型，1=手机号码 2=邮箱地址
        "dialing_code":dialing_code, # 国际电话区号，仅当type=1 时有效
        "verification_code":verification_code, # 验证码
        "invitation_code":invitation_code, # 邀请码 （非必填）
        "platform":platform # 终端类型，1=移动端 2=PC端
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey,Android_apisecret, body), method='POST')
    out_log(url,body,json.loads(run.response))
    print(password)
    code = json.loads(run.response)["code"]
    if code == 1000:
        token = json.loads(run.response)["data"]["token"]
        return token
    else:
        print(json.loads(run.response))

def login_step1(account,password,type="1",dialing_code="86"):
    url = "%s/api/v1/user/login/step1" % B3_url
    password = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
    body = {
        "type":type, #账号类型，1=手机号码 2=邮箱地址
        "dialing_code":dialing_code, #国际电话区号，仅当type=1 时有效
        "account":account,
        "password":password #SHA256加密后的登录密码
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url,body,json.loads(run.response))
    print(password)
    code = json.loads(run.response)["code"]
    if code == 1000:
        verification_token = json.loads(run.response)["data"]["verification_token"]
        return verification_token
    else:
        print(json.loads(run.response))

def login_step2(verification_token,verification_id,account,platform="2",dialing_code="86"):
    url = "%s/api/v1/user/login/step2" % B3_url
    db = DB('mysql.b3dev.xyz', 3306, 'b3_api', 'fGFcqRkHC5D2z^b^', 'b3')  # B3devDB
    # db = DB('mysql.b2dev.xyz', 3306, 'b2_cc', 'EV0Yom7L5l4r', 'biso')  # devDB
    # db = DB('mysql.b2sit.xyz', 3306, 'b2_cc', '7iD5uXtW84tG', 'biso') #sitDB
    # db = DB('mysql.b2sim.xyz', 3306, 'b2_cc', '30iAc2sF8UZa', 'biso') #simDB
    verification_code = db.query(
        "SELECT verification_code FROM `user_verification_code` WHERE user_account = 86%s ORDER BY code_over_time DESC LIMIT 1" % account)[0][0]
    print(verification_code)
    body = {
        "verification_token":verification_token, # 登录步骤1验证通过后返回的登录验证令牌
        "verification_code":verification_code, # 验证码
        "verification_id" : verification_id, # 验证码发送成功后服务器返回的验证码ID
        "account":dialing_code+account, #账号（国际电话区号+手机号码/邮箱地址）
        "platform":platform #终端类型，1=移动端 2=PC端
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url,body,json.loads(run.response))
    code = json.loads(run.response)["code"]
    if code == 1000:
        token = json.loads(run.response)["data"]["token"]
        return token
    else:
        print(json.loads(run.response))

def user_login(sms_type,account,password):
    verification_token = login_step1(account,password)
    verification_id = send_sms(sms_type,account)
    token = login_step2(verification_token,verification_id,account)
    return token

def user_register(sms_type,account,password):
    verification_id = send_sms(sms_type, account)
    token = register(account=account, password=password, verification_id=verification_id, type="1", dialing_code="86", invitation_code="", platform="2") # SIM邀请码：cKDFHU94，sit：gROQOZ4D dev:7g2VRxQ6
    return token



def validate_login_pwd(token,password):
    #验证登录密码是否正确
    url = "%s/api/v1/user/validate_login_pwd" % B3_url
    password = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
    body={
        "token":token,
        "password":password
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(password)
    print(json.loads(run.response))

def modify_login_pwd(token,password,account):
    #修改登录密码
    url = "%s/api/v1/user/modify_login_pwd" % B3_url
    db = DB('mysql.b3dev.xyz', 3306, 'b3_api', 'fGFcqRkHC5D2z^b^', 'b3')  # B3devDB
    # db = DB('192.168.0.120', 3306, 'tars2', '#k6tYIA4KrYfFU0y', 'biso') #内网DB
    # db = DB('mysql.b2dev.xyz', 3306, 'b2_cc', 'EV0Yom7L5l4r', 'biso') #devDB
    # db = DB('mysql.b2sit.xyz', 3306, 'b2_cc', '7iD5uXtW84tG', 'biso') #sitDB
    # db = DB('mysql.b2sim.xyz', 3306, 'b2_cc', '30iAc2sF8UZa', 'biso') #simDB
    verification_id = send_sms(sms_type="4", account=account, dialing_code="86", token=token, language="zh")
    verification_code = db.query(
        "SELECT verification_code FROM `user_verification_code` WHERE user_account = 86%s ORDER BY code_over_time DESC LIMIT 1" % account)[0][0]
    print(verification_code)
    password = str(hashlib.sha256(password.encode('utf-8')).hexdigest()).upper()
    body={
        "token":token,
        "password":password,
        "verification_code":verification_code,
        "verification_id":verification_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(password)
    print(json.loads(run.response))

if __name__ == "__main__":
    try:
        # console_out('F:\mohu-test\logs\logging.log')
        # verification_token = login_step1("15521057551","zjw971006")
        # print(verification_token)
        # verification_id = send_sms("2","15521057551")
        # print(verification_id)
        # token = login_step2(verification_token,verification_id,"15521057551")
        # print(token)
        # print(user_login("2","13826284310","111111"))
        # print(user_login("2", "15916750662", "123456")) #永健账号
        # print(user_login("2", "15521057551", "zjw971006"))
        validate_login_pwd(token=token_wen, password="zjw971006")
        modify_login_pwd(token=token_wen, password="zjw971006", account="15521057551")
    except Exception:
        print(traceback.print_exc(file=open(r'logs\err.log','w+')))