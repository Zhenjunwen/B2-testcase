#coding=utf-8

import json
from API_test import RunMain
import hashlib

from B1APItest.authentication_KYC import authentication_get_kyc_info
from B4APItest.login_register import send_sms
from DB_config import DB
from B4APItest.signature import get_signture
from log import out_log
import configparser

cf = configparser.ConfigParser()
CF = configparser.ConfigParser()
#配置文件路径
CF.read("F:\mohu-test\configfile\B1config.cfg")
B1token_wen = CF.get("token","token_wen")

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
host = cf.get("Mysql_DataBase","host")
port = int(cf.get("Mysql_DataBase","port"))
user = cf.get("Mysql_DataBase","user")
password = cf.get("Mysql_DataBase","password")
database = cf.get("Mysql_DataBase","db")


def register_kyc(account,password,dialing_code="86",invitation_code=""):
    # 实名认证注册
    url = "%s/api/v1/user/register_kyc" % B4_url
    kyc = authentication_get_kyc_info(token=B1token_wen)
    if kyc["code"] == 1000:
        if kyc["data"]["state"] == 3:
            certificates_name = kyc["data"]["certificates_name"]
            # print(certificates_name)
            certificates_no = kyc["data"]["certificates_no"]
            # print(certificates_no)
        else:
            print(kyc)
            certificates_name = input()
    # print(kyc)
    verification_id = send_sms(sms_type="1", account=account, dialing_code=dialing_code)
    db = DB('mysql.b4dev.xyz', 3306, 'b4_api', 'eYKRj3Vp@zM0SGWj', 'b4')  # B4devDB
    verification_code = db.query(
        "SELECT verification_code FROM user_verification_code WHERE user_account = '%s' ORDER BY code_over_time DESC LIMIT 1" % (
                    dialing_code + account))[0][0]
    password = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
    body = {
        "account":account,
        "password":password,
        "verification_id":verification_id,
        "verification_code":verification_code,
        "invitation_code":invitation_code,
        "name":str(certificates_name),
        "certificate_no":str(certificates_no)
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(Android_apikey, Android_apisecret, body), method='POST')
    out_log(url,body,json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    register_kyc(account="15521057551", password="zjw971006", dialing_code="86", invitation_code="", nationality="")
    pass