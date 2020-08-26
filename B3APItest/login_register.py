#coding=utf-8

import json
from API_test import RunMain
import hashlib

from DB_config import DB
from B3APItest.signature import get_signture
from log import out_log
import configparser

cf = configparser.ConfigParser()
#配置文件路径
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

def send_email_sms(sms_type,account,token="",language="zh"):
    #发送邮箱验证码-验证码发送成功后服务器返回的验证码ID
    url = "%s/api/v1/send/mail" % B3_url
    body = {
        "type": sms_type,#验证码类型，1=注册 2=登录 3=重置登录密码 4=修改登录密码 5=重置交易密码 6=添加收款方式 7=钱包提现 8=申请ApiKey  9=编辑ApiKey 10=绑定谷歌验证器
        "account":account,
        "token":token, #用户令牌 type > 3时必填
        "language":language #语言，取值："zh"=简体中文, "en"=英文, 默认"zh"
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey,Android_apisecret,body), method='POST')
    out_log(url,body,json.loads(run.response))
    # print(json.loads(run.response))
    code = json.loads(run.response)["code"]
    # print(code)
    # print(json.loads(run.response))
    if code == 1000:
        verification_id = json.loads(run.response)["data"]["verification_id"]
        # print(verification_id)
        return verification_id
    elif code == 2994:
        wait_time = json.loads(run.response)["data"]["wait_time"]
        print("重新获取验证需等待%d秒"%wait_time)
    else:
        print(json.loads(run.response))

def register(account,password,verification_id,verification_code,type,dialing_code="",invitation_code="",platform="2"):
    #注册
    url = "%s/api/v1/user/register" % B3_url
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
    # print(password)
    code = json.loads(run.response)["code"]
    if code == 1000:
        token = json.loads(run.response)["data"]["token"]
        return token
    else:
        print(json.loads(run.response))

def login_step1(account,password,type,dialing_code=""):
    url = "%s/api/v1/user/login/step1" % B3_url
    password = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
    body = {
        "type":type, #账号类型，1=手机号码 2=邮箱地址
        "dialing_code":dialing_code, #国际电话区号，仅当type=1 时有效
        "account":account,
        "password":password #SHA256加密后的登录密码
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,body,json.loads(run.response))
    # print(password)
    code = json.loads(run.response)["code"]
    if code == 1000:
        verification_token = json.loads(run.response)["data"]["verification_token"]
        # print(verification_token)
        return verification_token
    else:
        print(json.loads(run.response))

def login_step2(verification_token,verification_id,verification_code,account,platform="2",dialing_code=""):
    url = "%s/api/v1/user/login/step2" % B3_url
    body = {
        "verification_token":verification_token, # 登录步骤1验证通过后返回的登录验证令牌
        "verification_code":verification_code, # 验证码
        "verification_id" : verification_id, # 验证码发送成功后服务器返回的验证码ID
        "account":dialing_code+account, #账号（国际电话区号+手机号码/邮箱地址）
        "platform":platform #终端类型，1=移动端 2=PC端
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,body,json.loads(run.response))
    code = json.loads(run.response)["code"]
    if code == 1000:
        token = json.loads(run.response)["data"]["token"]
        return token
    else:
        print(json.loads(run.response))

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

def modify_login_pwd(token, password, account, dialing_code=""):
    # 修改登录密码
    url = "%s/api/v1/user/modify_login_pwd" % B3_url
    db = DB('mysql.b3dev.xyz', 3306, 'b3_api', 'fGFcqRkHC5D2z^b^', 'b3')  # B3devDB
    verification_id = send_email_sms(sms_type="4", account=account, token=token, language="zh")
    # verification_id = send_sms(sms_type="4",account=account,dialing_code=dialing_code,token=token,language="zh")
    verification_code = db.query(
        "SELECT verification_code FROM `user_verification_code` WHERE user_account = '%s' ORDER BY code_over_time DESC LIMIT 1" % (dialing_code + account))[0][0]
    print(verification_code)
    password = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
    body = {
        "token": token,
        "password": password,
        "verification_code": verification_code,
        "verification_id": verification_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    # print(password)
    print(json.loads(run.response))

def online_modify_login_pwd(token,password,account,dialing_code=""):
    #线上修改登录密码
    url = "%s/api/v1/user/modify_login_pwd" % B3_url
    # verification_id = send_email_sms(sms_type="4", account=account, token=token, language="zh")
    verification_id = send_sms(sms_type="4", account=account, dialing_code=dialing_code, token=token, language="zh")
    verification_code = input("验证码：")
    password = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
    body={
        "token":token,
        "password":password,
        "verification_code":verification_code,
        "verification_id":verification_id
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    # print(password)
    print(json.loads(run.response))


def user_email_login(sms_type,account,password,type="2"):
    #dev邮箱登录
    verification_token = login_step1(account=account,password=password,type=type)
    verification_id = send_email_sms(sms_type=sms_type,account=account)
    db = DB('mysql.b3dev.xyz', 3306, 'b3_api', 'fGFcqRkHC5D2z^b^', 'b3')  # B3devDB
    verification_code = db.query(
        "SELECT verification_code FROM user_verification_code WHERE user_account = '%s' ORDER BY code_over_time DESC LIMIT 1" % account)[0][0]
    token = login_step2(verification_code=verification_code,verification_token=verification_token,verification_id=verification_id,account=account)
    print(token)
    return token

def user_phone_login(sms_type,account,password,type="1",dialing_code="86"):
    #dev手机登录
    verification_token = login_step1(account=account,password=password,type=type,dialing_code=dialing_code)
    verification_id = send_sms(sms_type=sms_type,account=account,dialing_code=dialing_code)
    db = DB('mysql.b3dev.xyz', 3306, 'b3_api', 'fGFcqRkHC5D2z^b^', 'b3')  # B3devDB
    verification_code = db.query("SELECT verification_code FROM user_verification_code WHERE user_account = '%s' ORDER BY code_over_time DESC LIMIT 1" % (dialing_code+account))[0][0]
    token = login_step2(verification_code=verification_code,verification_token=verification_token,verification_id=verification_id,account=account,dialing_code=dialing_code)
    print(token)
    return token

def user_email_register(sms_type,account,password,invitation_code=""):
    #dev邮箱注册
    verification_id = send_email_sms(sms_type,account)
    db = DB('mysql.b3dev.xyz', 3306, 'b3_api', 'fGFcqRkHC5D2z^b^', 'b3')  # B3devDB
    verification_code = db.query("SELECT verification_code FROM user_verification_code WHERE user_account = '%s' ORDER BY code_over_time DESC LIMIT 1" % account)[0][0]
    token = register(account=account, password=password, verification_id=verification_id,verification_code=verification_code, type="2",invitation_code=invitation_code, platform="2")
    print(token)
    return token

def user_phone_register(sms_type,account,password,dialing_code,invitation_code=""):
    #dev手机注册
    verification_id = send_sms(sms_type, account,dialing_code=dialing_code)
    db = DB('mysql.b3dev.xyz', 3306, 'b3_api', 'fGFcqRkHC5D2z^b^', 'b3')  # B3devDB
    verification_code = db.query(
        "SELECT verification_code FROM user_verification_code WHERE user_account = '%s' ORDER BY code_over_time DESC LIMIT 1" % (dialing_code+account))[0][0]
    token = register(account=account, password=password, verification_id=verification_id,verification_code=verification_code,dialing_code=dialing_code, type="1",invitation_code=invitation_code, platform="2")
    print(token)
    return token

def online_user_phone_login(sms_type,account,password,type="1",dialing_code="86"):
    #线上手机登录
    verification_token = login_step1(account=account,password=password,type=type,dialing_code=dialing_code)
    verification_id = send_sms(sms_type=sms_type,account=account)
    verification_code = input("验证码：")
    token = login_step2(verification_code=verification_code,verification_token=verification_token,verification_id=verification_id,account=account,dialing_code=dialing_code)
    print(token)
    return token

def online_user_email_login(sms_type,account,password,type="2"):
    #线上邮箱登录
    verification_token = login_step1(account=account,password=password,type=type)
    verification_id = send_email_sms(sms_type=sms_type,account=account)
    verification_code = input("验证码：")
    token = login_step2(verification_code=verification_code,verification_token=verification_token,verification_id=verification_id,account=account)
    print(token)
    return token


def online_user_phone_register(sms_type,account,password,dialing_code,invitation_code=""):
    #线上手机注册
    verification_id = send_sms(sms_type, account)
    verification_code = input("验证码：")
    token = register(account=account, password=password, verification_id=verification_id,verification_code=verification_code,dialing_code=dialing_code, type="1",invitation_code=invitation_code, platform="2")
    print(token)
    return token

def online_user_email_register(sms_type,account,password,invitation_code=""):
    #线上邮箱注册
    verification_id = send_email_sms(sms_type,account)
    verification_code = input("验证码：")
    token = register(account=account, password=password, verification_id=verification_id,verification_code=verification_code, type="2",invitation_code=invitation_code, platform="2")
    print(token)
    return token

def modify_nickname(token,nickname):
    url = "%s/api/v1/user/modify_nickname" % B3_url
    body = {
        "token":token,
        "nickname":nickname
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url,body,json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # send_sms(sms_type="2", account="15521057551", dialing_code="86", token="", language="zh")
    # send_email_sms(sms_type="2", account="zhenjunwen123@163.com", token="f80dfb7a06668d567282da239609c73d", language="zh")
    # verification_token = login_step1(account="zhenjunwen123@163.com",password="10000123456",type="2")
    # verification_id = send_email_sms(sms_type="2",account="zhenjunwen123@163.com",token="e30726c6e126048a65053a4d27150c8f",language="zh")
    # token = login_step2(verification_token="a14178b55e2ffa1478c60d19d0f17f04",verification_id="6",verification_code="971071",account="zhenjunwen123@163.com")
    # print(token)
    # user_phone_login(sms_type="2",account="15521057551",password="zjw971006")
    # print(user_phone_login(sms_type="2",account="13826284310",password="111111",dialing_code="86"))
    # print(user_login("2", "15916750662", "123456")) #永健账号
    # print(user_email_login(sms_type="2",type="2",account="1085751421@qq.com",password="10000123456"))
    # validate_login_pwd(token=token_wen, password="zjw971006")
    # modify_login_pwd(token="f80dfb7a06668d567282da239609c73d", password="10000123456", account="1085751421@qq.com")
    # user_phone_login(sms_type="2", account="16538854915", password="qq111111", type="1", dialing_code="86")
    # user_email_login(sms_type="2", account="00000011@mohukeji.com", password="Qq000000", type="2")
    # user_email_register(sms_type="1", account="00000012@mohukeji.com", password="Qq000000",invitation_code="")
    user_phone_register(sms_type="1", account="16538854913", password="qq111111",dialing_code="86")
    # online_user_phone_login(sms_type="2", account="15521057551", password="zjw971006", type="1", dialing_code="86")
    # online_user_email_login(sms_type="2", account="zhenjunwen123@163.com", password="10000123456", type="2")
    # online_user_phone_register(sms_type="1", account="15521057551", password="zjw971006", dialing_code="86")
    # online_user_email_register(sms_type="1", account="zhenjunwen123@163.com", password="zjw971006")
    # modify_nickname(token=token_wen,nickname="宇宙大帅哥")
    pass