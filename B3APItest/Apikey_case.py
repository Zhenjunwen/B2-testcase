# coding=utf-8
import json
from B3APItest.API_test import RunMain
from B3APItest.DB_config import DB
from log import out_log
from B3APItest.login_register import send_email_sms,send_sms
from B3APItest.signature import get_signture
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
host = cf.get("Mysql_DataBase","host")
port = int(cf.get("Mysql_DataBase","port"))
user = cf.get("Mysql_DataBase","user")
password = cf.get("Mysql_DataBase","password")
database = cf.get("Mysql_DataBase","db")

def apikey_create(account,token,permission,bind_ip,remark,dialing_code=""):
    #申请ApiKey
    url = "%s/api/v1/merchant/apikey/create" % B3_url
    db = DB(host, port,user, password, database)  # B3devDB
    verification_id = send_email_sms(sms_type="8", account=account,token=token, language="zh")
    # verification_id = send_sms(sms_type="8", account=account, token=token, language="zh",dialing_code=dialing_code)
    verification_code = db.query("SELECT verification_code FROM `user_verification_code` WHERE user_account = '%s' ORDER BY code_over_time DESC LIMIT 1" % (dialing_code+account))[0][0]
    body={
        "token":token,
        "permission":permission,    #权限类型，取值范围：1=读取 2=交易 4=划转，可组合使用
        "verification_code":verification_code,
        "verification_id":verification_id,
        "bind_ip":bind_ip,
        "remark":remark
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def online_apikey_create(account,token,permission,bind_ip,remark):
    #申请ApiKey
    url = "%s/api/v1/merchant/apikey/create" % B3_url
    verification_id = send_email_sms(sms_type="8", account=account,token=token, language="zh")
    # verification_id = send_sms(sms_type="8",account=account,token=token,language="zh")
    verification_code = input("验证码：")
    body = {
        "token":token,
        "permission":permission,    #权限类型，取值范围：1=读取 2=交易 4=划转，可组合使用
        "verification_code":verification_code,
        "verification_id":verification_id,
        "bind_ip":bind_ip,
        "remark":remark
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def apikey_get_list(token):
    #获取ApiKey列表
    url = "%s/api/v1/merchant/apikey/get_list" % B3_url
    body={
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def apikey_modify(account,token,api_key,bind_ip,remark,permission,dialing_code="86"):
    #修改ApiKey信息
    url = "%s/api/v1/merchant/apikey/modify" % B3_url
    db = DB(host, port, user, password, database)  # B3devDB
    # verification_id = send_email_sms(sms_type="9", account=account,token=token, language="zh")
    verification_id = send_sms(sms_type="9", account=account,token=token, language="zh",dialing_code=dialing_code)
    verification_code = db.query("SELECT verification_code FROM `user_verification_code` WHERE user_account = '%s' ORDER BY code_over_time DESC LIMIT 1" % (dialing_code+account))[0][0]
    body={
        "token":token,
        "api_key":api_key,
        "verification_code":verification_code,
        "verification_id":verification_id,
        "bind_ip":bind_ip,
        "remark":remark,
        "permission":permission
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def online_apikey_modify(account,token,api_key,bind_ip,remark,permission,dialing_code="86"):
    #修改ApiKey信息
    url = "%s/api/v1/merchant/apikey/modify" % B3_url
    # verification_id = send_email_sms(sms_type="9", account=account,token=token, language="zh")
    verification_id = send_sms(sms_type="9", account=account,token=token, language="zh",dialing_code=dialing_code)
    verification_code = input("验证码：")
    body={
        "token":token,
        "api_key":api_key,
        "verification_code":verification_code,
        "verification_id":verification_id,
        "bind_ip":bind_ip,
        "remark":remark,
        "permission":permission
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    # apikey_create(account="zhenjunwen@mohukeji.com",token="a5a76dd69108b19fe5ef2d44b0bc79f9", permission="7",bind_ip="", remark='test')
    online_apikey_create(account="zhenjunwen123@163.com", token="90de857fdeea4be9c2883281d262543d", permission="7", bind_ip="192.168.0.40", remark="10000号ApiKey")
    # apikey_modify(account="15521057551", token=token_wen, api_key="", bind_ip="", remark="编辑APIKEY", permission="7", dialing_code="86")
    # online_apikey_modify(account="15521057551", token=token_wen, api_key="", bind_ip="", remark="编辑APIKEY", permission="7", dialing_code="86")
    # apikey_modify(verification_id="12",verification_code="021740",token="e30726c6e126048a65053a4d27150c8f", api_key="23b0939a-ae38-4394-bb92-aeca0a77daeb",bind_ip="47.91.199.73", remark="增加ip", permission="7")
