# coding=utf-8
import json
from API_test import RunMain
from log import out_log
from B1APItest.signature import get_signture
import configparser
import requests

cf = configparser.ConfigParser()
#配置文件路径
cf.read("F:\mohu-test\configfile\B1config.cfg")

B1_url = cf.get("url", "url")
token_wen = cf.get('token', 'token_wen')
token_junxin = cf.get('token', 'token_junxin')
H5_apikey = cf.get("Apikey", "H5_apikey")
H5_apisecret = cf.get("Apikey", "H5_apisecret")
PC_apikey = cf.get("Apikey", "PC_apikey")
PC_apisecret = cf.get("Apikey", "PC_apisecret")


def authentication_kyc(token,name,certificate_type,certificate_no,face_photo="",nationality="156"):
    #提交KYC实名认证
    url = "%s/api/v1/authentication/kyc"% B1_url
    body = {
        "token":token,
        "name":name,
        "certificate_type":certificate_type,    #证件类型，0=其他 1=护照 2=身份证
        "certificate_front":"ff4e9cac40a2d5e8e4538e36df2b5b35.png",
        "certificate_back":"ff4e9cac40a2d5e8e4538e36df2b5b35.png",
        "certificate_handheld":"ff4e9cac40a2d5e8e4538e36df2b5b35.png",
        "certificate_no":certificate_no,    #证件号码
        "nationality":nationality,
        "face_photo":face_photo           #人脸识别照片
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(PC_apikey, PC_apisecret, body), method='POST')
    out_log(url,send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def upload(action):
    url = "https://admin.b3dev.xyz/api/upload"
    params = {
        "action":action
    }
    with open(r"C:\Users\qiu\Desktop\币种图标\bitcoin_200_200.png","rb") as upload_files:
        print(upload_files)
        body = {
            "file":upload_files
        }
        res = requests.post(url=url,params=params, files=body).json()
        print(res["data"]["serverPath"])
        return res["data"]["serverPath"]

def authentication_get_kyc_info(token):
    #获取提交的实名认证信息
    url = "%s/api/v1/authentication/get_kyc_info"% B1_url
    body = {
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(PC_apikey, PC_apisecret, body), method='POST')
    out_log(url,send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))
    return json.loads(run.response)

if __name__ == "__main__":
    # authentication_kyc(token="b8b8fa7db194b3fdd66c3aacf209ce9b" , name="孙骞", certificate_type="2", certificate_no="430281199007091313", face_photo="",nationality="156")
    # upload(action="kyc")
    # authentication_get_kyc_info(token=token_wen)
    pass