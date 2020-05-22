# coding=utf-8
import traceback
import json
from API_test import RunMain
from DB_config import DB
from log import out_log
from login_register import send_email_sms
from signature import get_signture
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

def apikey_create(token,permission,account,bind_ip,remark=None):
    #申请ApiKey
    url = "%s/api/v1/merchant/apikey/create" % B3_url
    db = DB('mysql.b3dev.xyz', 3306, 'b3_api', 'fGFcqRkHC5D2z^b^', 'b3')  # B3devDB
    verification_id = send_email_sms(sms_type="8", account=account,token=token, language="zh")
    verification_code = db.query("SELECT verification_code FROM `user_verification_code` WHERE user_account = '%s' ORDER BY code_over_time DESC LIMIT 1" % account)[0][0]
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

if __name__ == "__main__":
    apikey_create(token="a47b9a20655f8db5cdf8472b39212b54", permission="7", verification_code="896753",verification_id="60", bind_ip="192.168.0.134", remark='平仓号')


