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
B2_url = "http://api.b2dev.xyz" #B2dev
# B2_url = "http://api.b2sit.xyz" #B2sit
# B2_url = "http://api.b2sim.xyz" #B2sim
token_junxin = "17d740ce53869ceb3dce06e943e88488"  # 俊鑫token
token_wen = "942e0f834af162d12b63d3f3dde97326"  # 俊文token
sys_token = "2da373f6d5ffc1f6a42120eb5a893adb" #B2后台token
H5_apikey = "alLzET7dFLYN5ONg"
H5_apisecret = "rpoEwZeM"
sys_apikey = "4NHMhvsQ15TFNyVO"
sys_apisecret = "h8eiT26J"
Android_apikey = "ctyD04PtGMIsJtNZ"
Android_apisecret = "41DwD4ST"

def send_sms(sms_type,account,dialing_code="86",token="",language="zh"):
    #发送短信验证码-验证码发送成功后服务器返回的验证码ID
    url = "%s/api/v1/send/sms" % B2_url
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
    if code == 1000:
        verification_id = json.loads(run.response)["data"]["verification_id"]
        # print(verification_id)
        return verification_id
    elif code == 2994:
        wait_time = json.loads(run.response)["data"]["wait_time"]
        print("重新获取验证需等待%d秒"%wait_time)
    else:
        print(json.loads(run.response))

def register(account,password,verification_id,type="1",dialing_code="86",invitation_code="",platform="2"):
    #注册
    url = "%s/api/v1/user/register" % B2_url
    # db = DB('192.168.0.120', 3306, 'tars2', '#k6tYIA4KrYfFU0y', 'biso') #内网DB
    db = DB('mysql.b2dev.xyz', 3306, 'b2_cc', 'EV0Yom7L5l4r', 'biso') #devDB
    # db = DB('mysql.b2sit.xyz', 3306, 'b2_cc', '7iD5uXtW84tG', 'biso') #sitDB
    # db = DB('mysql.b2sim.xyz', 3306, 'b2_cc', '30iAc2sF8UZa', 'biso') #simDB
    verification_code = db.query("SELECT verification_code FROM `user_verification_code` WHERE user_account = 86%s ORDER BY code_over_time DESC LIMIT 1"%account)[0][0]
    # print(verification_code)
    password = str(hashlib.sha256((password+"BSOEXSS").encode('utf-8')).hexdigest()).upper()
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
    code = json.loads(run.response)["code"]
    if code == 1000:
        token = json.loads(run.response)["data"]["token"]
        return token
    else:
        print(json.loads(run.response))

def login_step1(account,password,type="1",dialing_code="86"):
    url = "%s/api/v1/user/login/step1" % B2_url

    password = str(hashlib.sha256((password+"BSOEXSS").encode('utf-8')).hexdigest()).upper()
    body = {
        "type":type, #账号类型，1=手机号码 2=邮箱地址
        "dialing_code":dialing_code, #国际电话区号，仅当type=1 时有效
        "account":account,
        "password":password #SHA256加密后的登录密码
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url,body,json.loads(run.response))
    code = json.loads(run.response)["code"]
    if code == 1000:
        verification_token = json.loads(run.response)["data"]["verification_token"]
        return verification_token
    else:
        print(run.response)

def login_step2(verification_token,verification_id,account,platform="2",dialing_code="86"):
    url = "%s/api/v1/user/login/step2" % B2_url
    # db = DB('192.168.0.120', 3306, 'tars2', '#k6tYIA4KrYfFU0y', 'biso') #内网DB
    db = DB('mysql.b2dev.xyz', 3306, 'b2_cc', 'EV0Yom7L5l4r', 'biso')  # devDB
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


if __name__ == "__main__":
    # console_out('F:\B2_Androidtest\logs\logging.log')
    # verification_token = login_step1("15521057551","zjw971006")
    # print(verification_token)
    # verification_id = send_sms("2","15521057551")
    # print(verification_id)
    # token = login_step2(verification_token,verification_id,"15521057551")
    # print(token)
    try:
        print(user_login("2","15521057551","zjw971006"))
        # print(user_login("2","13826284310","111111"))
    except Exception:
        print(traceback.print_exc(file=open(r'logs\err.log','w+')))
    # print(user_login("2","13870843611","Qq000000"))