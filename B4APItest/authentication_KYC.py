# coding=utf-8
import json
from API_test import RunMain
from log import out_log
from B4APItest.signature import get_signture
import configparser
import requests

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

def authentication_kyc(token,name,certificate_type,certificate_no,face_photo="",nationality="156"):
    #提交KYC实名认证
    url = "%s/api/v1/authentication/kyc"% B4_url
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
                  headers=get_signture(IOS_apikey, IOS_apisecret, body), method='POST')
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

if __name__ == "__main__":
    authentication_kyc(token="3160ad7abce58a0438b256d8db5ee99f", name="甄俊文1", certificate_type="0", certificate_no="440682199710064034", face_photo="",nationality="156")
    authentication_kyc(token="94b0cd2bd8270d7d13c9688a4eaa7df6", name="甄俊文2", certificate_type="0", certificate_no="440682199710064035", face_photo="",nationality="156")
    authentication_kyc(token="d3c1ffb67b73f2d9d2734128db4990f6", name="甄俊文3", certificate_type="0", certificate_no="440682199710064036", face_photo="",nationality="156")
    authentication_kyc(token="2244757a294c56724c82c4304eabdaa5", name="甄俊文4", certificate_type="0", certificate_no="440682199710064037", face_photo="",nationality="156")
    authentication_kyc(token="979a4206fecf04a4b23db2ef93f35ddd", name="甄俊文5", certificate_type="0", certificate_no="440682199710064038", face_photo="",nationality="156")
    authentication_kyc(token="3fdff761dc1e2e8c3c95fb22f30d112a", name="甄俊文6", certificate_type="0", certificate_no="440682199710064039", face_photo="",nationality="156")
    authentication_kyc(token="ae490e3ba8a0ff628c02213a9d22bc33", name="甄俊文7", certificate_type="0", certificate_no="440682199710064031", face_photo="",nationality="156")
    authentication_kyc(token="8f195c7bdfb47bfbd15321f4d7f5c694", name="甄俊文8", certificate_type="0", certificate_no="440682199710064032", face_photo="",nationality="156")
    authentication_kyc(token="ed37c795681f4c4a0b514926704a8714", name="甄俊文9", certificate_type="0", certificate_no="440682199710064033", face_photo="",nationality="156")
    authentication_kyc(token="8de32a463f9f6a6e6d55884a89deabca", name="甄俊文10", certificate_type="0", certificate_no="440682199710064030", face_photo="",nationality="156")

    # upload(action="kyc")