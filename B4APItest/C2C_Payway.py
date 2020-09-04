# coding=utf-8
import traceback
import json
from API_test import RunMain
from B4APItest.login_register import send_sms,send_email_sms
from DB_config import DB
from log import out_log
from B4APItest.signature import get_signture
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


def payway_add(token,pay_way,pay_detail,account,dialing_code=""):
    #添加收付款方式
    url = "%s/api/v1/payway/add"%B4_url
    # verification_id = send_sms(sms_type="6", account=account, dialing_code=dialing_code, token=token, language="zh")
    verification_id= send_email_sms(sms_type="6",account=account,token=token)
    db = DB('mysql.b4dev.xyz', 3306, 'b4_api', 'eYKRj3Vp@zM0SGWj', 'b4')  # B4devDB
    verification_code = db.query(
        "SELECT verification_code FROM `user_verification_code` WHERE user_account = '%s' ORDER BY code_over_time DESC LIMIT 1" % (
                    dialing_code + account))[0][0]
    pay_detail=json.dumps(pay_detail, ensure_ascii=False)
    body = {
        "token":token,
        "pay_way":pay_way,
        "pay_detail":pay_detail,
        "verification_id":verification_id,
        "verification_code":verification_code
    }
    run = RunMain(url= url, params=None, data=body, headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def payway_get_list(token):
    #添加收付款方式
    url = "%s/api/v1/payway/get_list"%B4_url
    body = {
        "token":token,
    }
    run = RunMain(url= url, params=None, data=body, headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def payway_remove(token,record_id):
    #删除收付款方式
    url = "%s/api/v1/payway/remove"%B4_url
    body = {
        "token":token,
        "record_id":record_id
    }
    run = RunMain(url= url, params=None, data=body, headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    payway_add(token="3160ad7abce58a0438b256d8db5ee99f", pay_way="2", pay_detail={ "pay_way": 2, "account_no": "微信账号", "qr_code_url": "支付二维码图片路径", "realname": "真实姓名" }, account="00000001@mohukeji.com", dialing_code="")
    payway_add(token="94b0cd2bd8270d7d13c9688a4eaa7df6", pay_way="2", pay_detail={ "pay_way": 2, "account_no": "微信账号", "qr_code_url": "支付二维码图片路径", "realname": "真实姓名" }, account="00000002@mohukeji.com", dialing_code="")
    payway_add(token="d3c1ffb67b73f2d9d2734128db4990f6", pay_way="2", pay_detail={ "pay_way": 2, "account_no": "微信账号", "qr_code_url": "支付二维码图片路径", "realname": "真实姓名" }, account="00000003@mohukeji.com", dialing_code="")
    payway_add(token="2244757a294c56724c82c4304eabdaa5", pay_way="2", pay_detail={ "pay_way": 2, "account_no": "微信账号", "qr_code_url": "支付二维码图片路径", "realname": "真实姓名" }, account="00000004@mohukeji.com", dialing_code="")
    payway_add(token="979a4206fecf04a4b23db2ef93f35ddd", pay_way="2", pay_detail={ "pay_way": 2, "account_no": "微信账号", "qr_code_url": "支付二维码图片路径", "realname": "真实姓名" }, account="00000005@mohukeji.com", dialing_code="")
    payway_add(token="3fdff761dc1e2e8c3c95fb22f30d112a", pay_way="2", pay_detail={ "pay_way": 2, "account_no": "微信账号", "qr_code_url": "支付二维码图片路径", "realname": "真实姓名" }, account="00000006@mohukeji.com", dialing_code="")
    payway_add(token="ae490e3ba8a0ff628c02213a9d22bc33", pay_way="2", pay_detail={ "pay_way": 2, "account_no": "微信账号", "qr_code_url": "支付二维码图片路径", "realname": "真实姓名" }, account="00000007@mohukeji.com", dialing_code="")
    payway_add(token="8f195c7bdfb47bfbd15321f4d7f5c694", pay_way="2", pay_detail={ "pay_way": 2, "account_no": "微信账号", "qr_code_url": "支付二维码图片路径", "realname": "真实姓名" }, account="00000008@mohukeji.com", dialing_code="")
    payway_add(token="ed37c795681f4c4a0b514926704a8714", pay_way="2", pay_detail={ "pay_way": 2, "account_no": "微信账号", "qr_code_url": "支付二维码图片路径", "realname": "真实姓名" }, account="00000009@mohukeji.com", dialing_code="")
    payway_add(token="8de32a463f9f6a6e6d55884a89deabca", pay_way="2", pay_detail={ "pay_way": 2, "account_no": "微信账号", "qr_code_url": "支付二维码图片路径", "realname": "真实姓名" }, account="00000010@mohukeji.com", dialing_code="")

    # payway_get_list(token=token_wen)
    # payway_remove(token=token_wen, record_id="1")
    pass
