#coding=utf-8
import  sys
import json
from API_test import RunMain
import time
from B2_C2C_api import get_signture
import hashlib
from log import out_log
from errlog import Logger


# B2_url = "http://192.168.0.22:12024" #孙骞
# B2_url = "https://api.btc.so"  # B2外网
B2_url = "http://api.b2dev.xyz" #B2dev
token_junxin = "6a1ad8eba28ec8c8107f25482c02ce2a"  # 俊鑫token
token_wen = "0b88d5881bc7f12dcf76d734a6246b59"  # 俊文token
# sys_token = "2da373f6d5ffc1f6a42120eb5a893adb" #B2后台token
H5_apikey = "sUY7qsoHudTrw2Ct"
H5_apisecret = "gEq76SZv"
sys_apikey = "5S7NukaMpMVW8U4Z"
sys_apisecret = "p0fbgZI0"
Android_apikey = "qbmkIS55ptjBhZFp"
Android_apisecret = "7M1H4mXA"
IOS_apikey = "oStkKLmJ5Q8S4n3b"
IOS_apisecret = "gKByU6HC"
sys_token = "48edd9862203d1e7e1e26eb510967846"#后台

def miner_basic(token):
    #获取指定用户的基础矿工信息
    url = "%s/api/v1/mining/miner/basic" % B2_url
    body={
        "token":token
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))

def miner_detail(token):
    #获取指定用户的矿工状态信息
    url = "%s/api/v1/mining/miner/detail" % B2_url
    body={
        "token":token
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))

def miner_levels():
    #获取所有矿工等级及对应升级条件
    url = "%s/api/v1/mining/parameter/miner_levels" % B2_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    print(json.loads(run.response))
    """{
        'code': 1000,
        'data': [{
            'id': 1,
            'invitations_required': 0,
            'is_open': 1,
            'level_description_en': 'Bronze',
            'level_description_zh': '倔强青铜',
            'level_icon': 'https://btcso-static.oss-cn-hongkong.aliyuncs.com/Manage/MiningImages/Bronze.png',
            'miner_level': 1,
            'usdt_amount_required': 1
        }, {
            'id': 2,
            'invitations_required': 0,
            'is_open': 1,
            'level_description_en': 'Silver',
            'level_description_zh': '秩序白银',
            'level_icon': 'https://btcso-static.oss-cn-hongkong.aliyuncs.com/Manage/MiningImages/Silver.png',
            'miner_level': 2,
            'usdt_amount_required': 10
        }, {
            'id': 3,
            'invitations_required': 0,
            'is_open': 1,
            'level_description_en': 'Gold',
            'level_description_zh': '荣耀黄金',
            'level_icon': 'https://btcso-static.oss-cn-hongkong.aliyuncs.com/Manage/MiningImages/Gold.png',
            'miner_level': 3,
            'usdt_amount_required': 100
        }, {
            'id': 4,
            'invitations_required': 0,
            'is_open': 1,
            'level_description_en': 'Platinum',
            'level_description_zh': '尊贵铂金',
            'level_icon': 'https://btcso-static.oss-cn-hongkong.aliyuncs.com/Manage/MiningImages/Platinum.png',
            'miner_level': 4,
            'usdt_amount_required': 1000
        }, {
            'id': 5,
            'invitations_required': 0,
            'is_open': 1,
            'level_description_en': 'Diamond',
            'level_description_zh': '永恒钻石',
            'level_icon': 'https://btcso-static.oss-cn-hongkong.aliyuncs.com/Manage/MiningImages/Diamond.png',
            'miner_level': 5,
            'usdt_amount_required': 5000
        }, {
            'id': 6,
            'invitations_required': 100,
            'is_open': 0,
            'level_description_en': 'Master',
            'level_description_zh': '至尊星耀',
            'level_icon': 'https://btcso-static.oss-cn-hongkong.aliyuncs.com/Manage/MiningImages/Master.png',
            'miner_level': 6,
            'usdt_amount_required': 10000
        }, {
            'id': 7,
            'invitations_required': 1000,
            'is_open': 0,
            'level_description_en': 'Challenger',
            'level_description_zh': '最强王者',
            'level_icon': 'https://btcso-static.oss-cn-hongkong.aliyuncs.com/Manage/MiningImages/Challenger.png',
            'miner_level': 7,
            'usdt_amount_required': 50000
        }]
    }"""    #矿工等级

def miner_join(token,level):
    #成为矿工/矿工升级
    url = "%s/api/v1/mining/miner/join" % B2_url
    body={
        "token":token,
        "level":level #矿工目标等级
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))

def miner_quit(token):
    #退出挖矿
    url = "%s/api/v1/mining/miner/quit" % B2_url
    body={
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))

def miner_level_records(token,page_number,page_size):
    #获取我的存取记录
    url = "%s/api/v1/mining/miner/level_records" % B2_url
    body={
        "token":token,
        "page_number":page_number,
        "page_size":page_size
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    print(json.loads(run.response))

def miner_balance(token):
    #获取我的挖矿收益钱包余额
    url = "%s/api/v1/mining/wallet/balance" % B2_url
    body={
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_withdraw(token,amount):
    #提币申请
    url = "%s/api/v1/mining/wallet/withdraw" % B2_url
    body={
        "token":token,
        "amount":str(format(amount,".8f"))
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_withdrawal_records(token,page_number,page_size):
    #获取我的提币记录
    url = "%s/api/v1/mining/wallet/withdrawal_records" % B2_url
    body={
        "token":token,
        "page_number":page_number,
        "page_size":page_size
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_earning_records(token,page_number,page_size):
    #获取我的挖矿记录
    url = "%s/api/v1/mining/earnings/earning_records" % B2_url
    body={
        "token":token,
        "page_number":page_number,
        "page_size":page_size
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_earning_stat(token):
    #获取我的累计收益
    url = "%s/api/v1/mining/earnings/stats" % B2_url
    body={
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_today_stats(token):
    #获取我的今日任务完成情况
    url = "%s/api/v1/mining/quest/today_stats" % B2_url
    body={
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_tradePairs():
    #获取所有支持挖矿的交易对
    url = "%s/api/v1/mining/tradePairs" % B2_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_pool_stats():
    #获取矿池总数量及剩余数量
    url = "%s/api/v1/mining/pool/stats" % B2_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_pool_records(page_number,page_size):
    #获取矿池消耗流水记录（最大100条）
    url = "%s/api/v1/mining/pool/records" % B2_url
    query = {
        "page_number":page_number,
        "page_size":page_size
    }
    run = RunMain(url=url, params=query, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret,query), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_parameter_withdrawal():
    #获取提币参数
    url = "%s/api/v1/mining/parameter/withdrawal" % B2_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_parameter_quest_periods():
    #获取所有任务周期及对应收益加成
    url = "%s/api/v1/mining/parameter/quest_periods" % B2_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_pool_records_latest():
    #获取最新10条矿池挖矿流水记录
    url = "%s/api/v1/mining/pool/records/latest" % B2_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_cancel_join(token):
    #获取我的今日任务完成情况
    url = "%s/api/v1/mining/miner/cancel_join" % B2_url
    body={
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url, send_msg=body, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_latest_price(token):
    #用户获取当前最新有效价格
    url = "%s/api/v1/mining/miner/latest_price" % B2_url
    body={
        "token":token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def miner_invitation_earnings():
    #获取所有邀请人数及对应收益加成
    url = "%s/api/v1/mining/parameter/invitation_earnings" % B2_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url,response_msg=json.loads(run.response))
    print(json.loads(run.response))

def cancel_all_orders(token,symbol):
    #用户获取当前最新有效价格
    url = "%s/api/v1/admin/transaction/cancel_all_orders" % B2_url
    body={
        "token":token,
        "symbol":symbol
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(sys_apikey, sys_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":
    try:
        miner_latest_price(token_wen)
        # miner_pool_records("10", "7")
    except Exception as e:
        sys.stdout = Logger('a.txt', sys.stdout)  # 控制台输出日志
        print(e)

