# coding=utf-8
import traceback
import json
from API_test import RunMain
import time
from log import out_log
from B3APItest.signature import get_signture
import configparser
from TruncateDecimal import truncateDecimal

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


def get_tradePairs():
    # 获取交易对
    url = '%s/api/v1/common/get_tradePairs' % B3_url
    run = RunMain(url=url, params=None, data=None, headers=get_signture(H5_apikey,H5_apisecret), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))

def user_payway_get_list(token):
    # 获取收付款列表
    url = "%s/api/v1/payway/get_list" % B3_url
    body = {
        "token": token
    }
    run = RunMain(url=url, params=None, data=body, headers=get_signture(H5_apikey, H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        pay_detail = json.loads(run.response)["data"]
        # print(pay_detail)
        return pay_detail
    else:
        print(json.loads(run.response))

def busines_payway_get_list(token_wen):
    # 获取收付款列表
    url = "%s/api/v1/payway/get_list" % B3_url
    body = {
        "token": token_wen
    }
    run = RunMain(url=url, params=None, data=body, headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        pay_detail = json.loads(run.response)["data"]
        print(pay_detail)
        return pay_detail
    else:
        print(json.loads(run.response))

# 商户下买单的pay_detail
def buy_payway_detail(token_wen):
    # 获取收付款列表
    url = "%s/api/v1/payway/get_list"%B3_url
    body = {
        "token": token_wen
    }
    run = RunMain(url=url, params=None, data= body, headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        # print(json.loads(run.response))
        # 发布广告的收付款详情
        pay = json.loads(run.response)["data"]
        payway= 0
        buy_pay_detail=[]
        for i in pay:
            p = payway
            payway = (payway | i['pay_way'])
            if p != payway:
                buy_pay_detail.append({
                    "pay_way":i['pay_way']
                })
        print(buy_pay_detail)
        # print("获取发布买广告需要的payway_detail")
        return buy_pay_detail
    else:
        print(json.loads(run.response))

# 商户下卖单的pay_detail
def sell_payway_detail(token_wen):
    # 获取收付款列表
    url = "%s/api/v1/payway/get_list" % B3_url
    body = {
        "token": token_wen
    }
    run = RunMain(url=url, params=None, data=body, headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        # 发布广告的收付款详情
        pay = json.loads(run.response)["data"]
        sell_pay_detail = []
        for i in pay:
            a = i["pay_detail"]
            sell_pay_detail.append(a)
        # print(sell_pay_detail)
        # print("获取发布卖广告需要的payway_detail")
        return sell_pay_detail
    else:
        print(json.loads(run.response))


def add_order(token,price,quantity,side,min_trx_cash,pay_way,symbol):
    # 商户发布广告
    url = '%s/api/v1/otc/add_order'%B3_url
    payway_detail = []
    if side == "1":
        payway_detail = json.dumps(buy_payway_detail(token))
    elif side == "0":
        payway_detail = json.dumps(sell_payway_detail(token),ensure_ascii=False)
    else:
        return print("side参数不合法")
    # print((buy_pay_detail))
    print(payway_detail)
    # 发布广告的收付款详情
    body ={
        "token": token,# 文，商户
        "price": str(price),  #发布广告价格
        "quantity":  truncateDecimal(num=quantity,digits=8),  #发布广告数量
        "side": side,  #买卖方向 0=卖出，1=买入
        "source": "app",  #来源，取值web/app
        "min_trx_cash": min_trx_cash, #最低交易金额，最多支持两位小数
        "max_trx_cash":  truncateDecimal(num=int(price*quantity),digits=2), #最高交易金额，最多支持两位小数
        "symbol": symbol, #交易对
        "pay_way": pay_way, 	#支持的收付款方式，1=银行卡，2=微信，4=支付宝，可组合使用(数字相加)
        "pay_detail": payway_detail,#银行卡收付款信息详情（JSON数组格式字符串），具体格式定义见 备注
        "nationality": "156" #所属国家或地区（三位数字代码）, 默认值：156
    }
    run = RunMain(url= url, params=None, data=body, headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        order_id = json.loads(run.response)["data"]["order_id"] #将返回值转换成字典
        # print(parmas_add_order['pay_detail'])
        print("广告ID：%s"%order_id)
        if side == '0':
            way = "卖"
        else:
            way = "买"
        print("发布%s币广告成功"%way)
        return order_id
    else:
        print(json.loads(run.response))

def cancel_order(token,order_id):
    #商户下架广告
    url = "%s/api/v1/otc/cancel_order"%B3_url
    body = {
        "token":token,
        "order_id":order_id
    }
    run = RunMain(url= url, params=None, data=body, headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print("order_id:%s 下架广告成功" % order_id)
    else:
        print(json.loads(run.response))


def get_orders(token_wen,state="7",pay_way="0",nationality="0",base_currency="",quote_currency=""):
    #获取商户发布的广告
    url = "%s/api/v1/otc/get_orders"%B3_url
    body = {
        "token":token_wen,
        "page_number":"2",
        "page_size":"10",
        "state":state, #广告状态，取值：1=可交易；2=完全成交；4=已下架 可组合使用
        "pay_way":pay_way, #【2020.1.13新增】支持的收付款方式，1=银行卡，2=微信，4=支付宝，可组合使用，0=全部，默认值：0
        "nationality":nationality, #【2020.1.13新增】所属国家或地区（3位数字代码），0=全部，默认值：0
        "base_currency":base_currency, #【2020.1.13新增】基础币种，""=全部，默认值：""
        "quote_currency":quote_currency #【2020.1.13新增】报价币种，""=全部，默认值：""
    }
    run = RunMain(url=  url, params=None, data=body, headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print("获取商户发布的广告")
    else:
        print(json.loads(run.response))


def user_sell_transaction(token_junxin,order_id,amount,price):
    # 客户下卖单
    url = "%s/api/v1/otc/add_transaction"%B3_url
    user_sell_pay_detail = json.dumps(sell_payway_detail(token_wen)[0])
    body = {
        "token": token_junxin,
        "order_id": order_id,
        "amount":str(format(amount,".8f")),
        "pay_way": sell_payway_detail(token_wen)[0]["pay_way"],
        "pay_detail": user_sell_pay_detail,
        "trx_cash":str(format(price*amount,".2f"))
    }
    # print(parmas_sell_transaction)
    run = RunMain(url= url, params=None, data= body, headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, send_msg=body,response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        trx_id = json.loads(run.response)["data"]["trx_id"]
        print("客户下卖单trx_id:%s"%trx_id)
        return trx_id
    else:
        print(json.loads(run.response))


def user_buy_transaction(token_junxin,order_id,amount,price):
    #客户下买单
    url = "%s/api/v1/otc/add_transaction"%B3_url
    body = {
        "token": token_junxin,
        "order_id": order_id,
        "amount":str(format(amount,".8f")),
        # "pay_way": user_pay_way, #客户买币不需要pay_way
        # "pay_detail": {'account_no': '4646464545454788787', 'bank_branch': '中国银行天河支行', 'bank_name': '中国银行', 'pay_way': '1', 'realname': '甄俊文'}, #买币不需要pay_detail
        "trx_cash":str(format(price*amount,".2f"))
    }
    # print(parmas_add_transaction)
    run = RunMain(url= url, params=None, data= body, headers= get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        trx_id = json.loads(run.response)["data"]["trx_id"]
        print("客户下买单trx_id:%s"%trx_id)
        return trx_id
    else:
        print(json.loads(run.response))

def usersell_business_confirm(token_wen,trx_id):
    # 买币广告-商户确认付款
    url = "%s/api/v1/otc/usersell_business_confirm" % B3_url
    body = {
        "token": token_wen,
        "trx_id": trx_id
    }
    # print(parmas_usersell_business_confirm)
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print("买币广告-商户确认付款")
        return run.response
    else:
        print(json.loads(run.response))

def usersell_customer_confirm(token_wen,trx_id):
    # 买币广告-客户确认收款
    url = "%s/api/v1/otc/usersell_customer_confirm" % B3_url
    body = {
        "token": token_wen,
        "trx_id": trx_id
    }
    # print(parmas_usersell_customer_confirm)
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print("买币广告-客户确认收款")
        return run.response
    else:
        print(json.loads(run.response))


def usersell_business_cancel(token_wen,trx_id):
    # 买币广告-商户取消交易
    url = "%s/api/v1/otc/usersell_business_cancel" % B3_url
    body = {
        "token": token_wen,
        "trx_id": trx_id
    }
    # print(parmas_usersell_business_cancel)
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print("买币广告-商户取消交易")
        return run.response
    else:
        print(json.loads(run.response))


def user_customer_confirm_transaction(token_junxin,trx_id):
    # 客户下买单确认付款
    url = "%s/api/v1/otc/customer_confirm_transaction"%B3_url
    user_sell_pay_detail = json.dumps(sell_payway_detail(token_wen)[0])
    body = {
        "token": token_junxin,
        "trx_id": trx_id,
        "pay_way": sell_payway_detail(token_wen)[0]["pay_way"],
        "pay_detail": user_sell_pay_detail
    }
    # print(parmas_customer_confirm_transaction)
    run = RunMain(url= url, params=None, data= body, headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print("客户下买单确认付款")
        return run.response
    else:
        print(json.loads(run.response))


def business_confirm_transaction(token_wen,trx_id):
    # 卖币广告-商户确认收款
    url = "%s/api/v1/otc/business_confirm_transaction" % B3_url
    body = {
        "token": token_wen,
        "trx_id": trx_id
    }
    # print(parmas_business_confirm_transaction)
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print("卖币广告-商户确认收款")
        return run.response
    else:
        print(json.loads(run.response))


def cancel_transaction(token_junxin,trx_id):
    # 卖币广告-客户取消交易
    url = "%s/api/v1/otc/cancel_transaction" % B3_url
    body = {
        "token": token_junxin,
        "trx_id": trx_id
    }
    # print(parmas_cancel_transaction)
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print("卖币广告-客户取消交易")
        return run.response
    else:
        print(json.loads(run.response))


def admin_cancel_usersell_transaction(sys_token,trx_id):
    # C2C交易-买币广告-订单仲裁取消（卖币客户胜诉）
    url = "%s/api/v1/admin/otc/cancel_usersell_transaction" % B3_url
    body = {
        "token": sys_token,
        "trx_id": trx_id
    }
    # print(parmas_admin_cancel_usersell_transaction)
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(sys_apikey,sys_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print("C2C交易-买币广告-订单仲裁取消（卖币客户胜诉）")
        return run.response
    else:
        print(json.loads(run.response))


def admin_confirm_usersell_transaction(sys_token,trx_id):
    # C2C交易-买币广告-订单仲裁完成（买币商户胜诉）
    url = "%s/api/v1/admin/otc/confirm_usersell_transaction" % B3_url
    body = {
        "token": sys_token,
        "trx_id": trx_id
    }
    # print(parmas_admin_confirm_usersell_transaction)
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(sys_apikey,sys_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print("C2C交易-买币广告-订单仲裁完成（买币商户胜诉）")
        return run.response
    else:
        print(json.loads(run.response))


def admin_cancel_arbitrated_transaction(sys_token,trx_id):
    # C2C交易-卖币广告-订单仲裁取消（卖币商户胜诉）
    url= "%s/api/v1/admin/otc/cancel_arbitrated_transaction" % B3_url
    body = {
        "token": sys_token,
        "trx_id": trx_id
    }
    # print(parmas_admin_cancel_arbitrated_transaction)
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(sys_apikey,sys_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print("C2C交易-卖币广告-订单仲裁取消（卖币商户胜诉）")
        return run.response
    else:
        print(json.loads(run.response))


def admin_confirm_arbitrated_transaction(sys_token,trx_id):
    # C2C交易-卖币广告-订单仲裁完成（买币客户胜诉）
    url = "%s/api/v1/admin/otc/confirm_arbitrated_transaction" % B3_url
    body = {
        "token": sys_token,
        "trx_id": trx_id
    }
    # print(parmas_admin_confirm_arbitrated_transaction)
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(sys_apikey,sys_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print("C2C交易-卖币广告-订单仲裁完成（买币客户胜诉）")
        return run.response
    else:
        print(json.loads(run.response))


def get_transaction_detail(token_junxin,trx_id):
    # 获取订单详情
    url = "%s/api/v1/otc/get_transaction_detail" % B3_url
    body = {
        "token": token_junxin,
        "trx_id": trx_id
    }
    # print(parmas_get_transaction_detail)
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        side = json.loads(run.response)["data"]["side"]
        # print(type(side))
        # print(side)
        return side
    else:
        print(json.loads(run.response))


def arbitrate_transaction(token,trx_id):
    # 卖家申诉
    url = "%s/api/v1/otc/arbitrate_transaction" % B3_url
    body = {
        "token": token,
        "trx_id": trx_id
    }
    # print(parmas_arbitrate_transaction)
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def cancel_all_orders(token):
    # 下架商户所有广告
    url = "%s/api/v1/otc/get_orders" % B3_url
    body = {
        "token": token,
        "page_number": "1",
        "page_size": "20",
        "state":"1"
    }
    # print(parmas_cancel_all_orders)
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        data = json.loads(run.response)["data"]
        # print(data)
        if data != []:
            for i in data:
                order_id = i["order_id"]
                cancel_order(token, order_id)
        else:
            print("没有可下架广告")
        return run.response
    else:
        print(json.loads(run.response))


def get_transaction_state(token_wen,trx_id):
    # 订单详情
    url = "%s/api/v1/otc/get_transaction_detail" % B3_url
    body = {
        "token": token_wen,
        "trx_id": trx_id
    }
    # print(parmas_get_transaction_detail)
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        state = json.loads(run.response)['data']['state']  # 获取状态
        # print(type(state))
        print("state=", state)
        return state
    else:
        print(json.loads(run.response))


def get_assets_c2c(token):
    # 订单详情
    url = "%s/api/v1/wallet/get_assets_c2c" % B3_url
    body = {
        "token": token,
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    print(json.loads(run.response))


def query_invitation_get_stats(token):
    #我的邀请信息
    url = "%s/api/v1/partner/query_invitation_get_stats" % B3_url
    body = {
        "token":token
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print(json.loads(run.response))
    else:
        print(json.loads(run.response))


def query_identity_byToken(token):
    #查询用户是否是荣誉合伙人
    url = "%s/api/v1/partner/query_identity_byToken" % B3_url
    body = {
        "token":token
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey,H5_apisecret,body), method='POST')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print(json.loads(run.response))
    else:
        print(json.loads(run.response))

def get_otc_config():
    # 获取C2C交易配置参数
    url = "%s/api/v1/parameter/get_otc_config" % B3_url
    run = RunMain(url=url, params=None, data=None,
                  headers=get_signture(H5_apikey, H5_apisecret), method='GET')
    out_log(url, response_msg=json.loads(run.response))
    if json.loads(run.response)["code"] == 1000:
        print(json.loads(run.response))
    else:
        print(json.loads(run.response))

def otc_add_deposit(token,symbol,amount):
    #1192-商户追加保证金
    url = "%s/api/v1/otc/add_deposit" % B3_url
    body={
        "token":token,
        "symbol":symbol,
        "amount":amount
    }
    run = RunMain(url=url, params=None, data=body,
                  headers=get_signture(H5_apikey, H5_apisecret, body), method='POST')
    out_log(url,send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))


def c2c_all(token_wen,token_junxin,sys_token,symbol,amount,price,quantity):
    # 发布买币广告
    order_id = add_order(price=price, quantity=quantity, side="1", min_trx_cash="10",pay_way=7,symbol=symbol)

    # 客户下买单交易完成
    trx_id = user_sell_transaction(token_junxin,order_id,amount,price)  # 客户下卖单
    state = get_transaction_state(token_wen,trx_id)
    if state == 1:
        usersell_business_confirm(token_wen,trx_id)  # 商户确认付款
        state = get_transaction_state(token_wen,trx_id)
        if state == 8192:
            usersell_customer_confirm(token_wen,trx_id)  # 客户确认收款
            state = get_transaction_state(token_wen,trx_id)
            if state == 16:
                print("交易完成")
            else:
                print("状态有误")
                exit(1)
        else:
            print("状态有误")
            exit(1)
    else:
        print("状态有误")
        exit(1)
    time.sleep(3)

    # 客户下卖单交易手动取消
    trx_id = user_sell_transaction(token_junxin,order_id,amount,price)
    state = get_transaction_state(token_wen,trx_id)
    if state == 1:
        usersell_business_cancel(token_wen,trx_id)  # 商户手动取消交易
        state = get_transaction_state(token_wen,trx_id)
        if state == 2048:
            print("交易取消")
    else:
        print("状态有误")
        exit(1)
    time.sleep(3)

    # 客户下卖单交易仲裁取消
    trx_id = user_sell_transaction(token_junxin,order_id,amount,price) # 客户下卖单
    state = get_transaction_state(token_wen,trx_id)
    if state == 1:
        usersell_business_confirm(token_wen,trx_id)  # 商户确认付款
        state = get_transaction_state(token_wen,trx_id)
        print(state)
        if state == 8192:
            get_transaction_detail(token_junxin,trx_id)  # 获取订单详情
            token = ""  # 判断卖家token
            if get_transaction_detail(token_junxin,trx_id) == 0:
                token = token_junxin
            else:
                token = token_wen
            # print(token)
            arbitrate_transaction(token,trx_id)  # 卖家申诉
            state = get_transaction_state(token_wen,trx_id)
            if state == 16384:
                admin_cancel_usersell_transaction(sys_token,trx_id)  # 买币广告仲裁取消
                state = get_transaction_state(token_wen,trx_id)
                if state == 128:
                    pass
                else:
                    print("状态有误")
                    exit(1)
            else:
                print("状态有误")
                exit(1)
        else:
            print("状态有误")
            exit(1)
    else:
        print("状态有误")
        exit(1)
    time.sleep(3)

    # 客户下卖单交易仲裁完成
    trx_id = user_sell_transaction(token_junxin,order_id,amount,price) # 客户下卖单
    state = get_transaction_state(token_wen,trx_id)
    if state == 1:
        usersell_business_confirm(token_wen,trx_id)  # 商户确认付款
        state = get_transaction_state(token_wen,trx_id)
        if state == 8192:
            get_transaction_detail(token_junxin,trx_id)  # 获取订单详情
            token = ""  # 判断卖家token
            if get_transaction_detail(token_junxin,trx_id) == 0:
                token = token_junxin
            else:
                token = token_wen
            # print(token)
            arbitrate_transaction(token,trx_id)  # 卖家申诉
            state = get_transaction_state(token_wen,trx_id)
            if state == 16384:
                admin_confirm_usersell_transaction(sys_token,trx_id)  # 买币广告仲裁完成
                state = get_transaction_state(token_wen,trx_id)
                if state == 256:
                    pass
                else:
                    print("状态有误")
                    exit(1)
            else:
                print("状态有误")
                exit(1)
        else:
            print("状态有误")
            exit(1)
    else:
        print("状态有误")
        exit(1)
    time.sleep(3)

    # 发布卖币广告
    order_id = add_order(price=price, quantity=quantity, side="0", min_trx_cash="10", pay_way=7,symbol=symbol)

    # 客户下买单交易完成
    trx_id = user_buy_transaction(token_junxin,order_id,amount,price)  # 客户下买单
    state = get_transaction_state(token_wen,trx_id)
    if state == 2:
        user_customer_confirm_transaction(token_junxin,trx_id)  # 客户确认付款
        state = get_transaction_state(token_wen,trx_id)
        if state == 4:
            business_confirm_transaction(token_wen,trx_id)  # 商户确认收款
            state = get_transaction_state(token_wen,trx_id)
            if state == 16:
                print("交易完成")
            else:
                print("状态有误")
                exit(1)
        else:
            print("状态有误")
            exit(1)
    else:
        print("状态有误")
        exit(1)
    time.sleep(3)

    # 客户下买单交易手动取消
    trx_id = user_buy_transaction(token_junxin,order_id,amount,price)  # 客户下买单
    state = get_transaction_state(token_wen,trx_id)
    if state == 2:
        cancel_transaction(token_junxin,trx_id)  # 客户取消交易
        state = get_transaction_state(token_wen,trx_id)
        if state == 32:
            pass
        else:
            print("状态有误")
            exit(1)
    else:
        print("状态有误")
        exit(1)

    # 客户下买单仲裁完成
    trx_id = user_buy_transaction(token_junxin,order_id,amount,price)  # 客户下买单
    state = get_transaction_state(token_wen,trx_id)
    if state == 2:
        user_customer_confirm_transaction(token_junxin,trx_id)  # 客户确认付款
        state = get_transaction_state(token_wen,trx_id)
        if state == 4:
            get_transaction_detail(token_junxin,trx_id)  # 获取订单详情
            token = ""  # 判断卖家token
            if get_transaction_detail(token_junxin,trx_id) == 0:
                token = token_junxin
            else:
                token = token_wen
            arbitrate_transaction(token,trx_id)  # 卖家申诉
            state = get_transaction_state(token_wen,trx_id)
            if state == 8:
                admin_confirm_arbitrated_transaction(sys_token,trx_id)  # C2C交易-卖币广告-订单仲裁取消（买币客户胜诉）
                state = get_transaction_state(token_wen,trx_id)
                if state == 256:
                    pass
                else:
                    print("状态有误")
                    exit(1)
            else:
                print("状态有误")
                exit(1)
        else:
            print("状态有误")
            exit(1)
    else:
        print("状态有误")
        exit(1)

    # 客户下买单仲裁取消
    trx_id = user_buy_transaction(token_junxin,order_id,amount,price)  # 客户下买单
    state = get_transaction_state(token_wen,trx_id)
    if state == 2:
        user_customer_confirm_transaction(token_junxin,trx_id)  # 客户确认付款
        state = get_transaction_state(token_wen,trx_id)
        if state == 4:
            get_transaction_detail(token_junxin,trx_id)  # 获取订单详情
            token = ""  # 判断卖家token
            if get_transaction_detail(token_junxin,trx_id) == 0:
                token = token_junxin
            else:
                token = token_wen
            arbitrate_transaction(token,trx_id)  # 卖家申诉
            state = get_transaction_state(token_wen,trx_id)
            if state == 8:
                admin_cancel_arbitrated_transaction(sys_token,trx_id)  # C2C交易-卖币广告-订单仲裁取消（卖币商户胜诉）
                state = get_transaction_state(token_wen,trx_id)
                if state == 128:
                    pass
                else:
                    print("状态有误")
                    exit(1)
            else:
                print("状态有误")
                exit(1)
        else:
            print("状态有误")
            exit(1)
    else:
        print("状态有误")
        exit(1)
    time.sleep(3)

def oneclick_add_transaction(token,side,base_currency,amount,trx_cash,pay_way,quote_currency="CNY",nationality=""):
    # 客户一键下单
    url = "%s/api/v1/otc/oneclick/add_transaction" % B3_url
    if side == "0":
        pay_detail = ''
    elif side == "1":
        payway_list = user_payway_get_list(token)
        if 0 >= int(pay_way) > 7 :
            return print("pay_way参数不合法")
        for pay in payway_list:
            if pay["pay_way"] == int(pay_way):
                pay_detail=json.dumps(pay["pay_detail"],ensure_ascii=False)
                print(pay_detail)
                break
            else:
                print("pay_detail参数空缺")
    else:
        return print("参数错误")
    body = {
        "token": token,
        "side":side,
        "base_currency":base_currency,
        "amount":amount,
        "trx_cash":trx_cash,
        "pay_way":pay_way,
        "pay_detail":pay_detail,
        "quote_currency":quote_currency,
        "nationality":nationality,
    }
    run = RunMain(url=url, params=None, data=body, headers=get_signture(H5_apikey, H5_apisecret,body), method='POST')
    out_log(url, send_msg=body,response_msg=json.loads(run.response))
    print(json.loads(run.response))

if __name__ == "__main__":

    # buy_payway_detail = buy_payway_detail(token_junxin)
    # sell_payway_detail = sell_payway_detail(token_wen)
    # c2c_all(token_wen, token_junxin, sys_token,symbol="BTC-CNY",amount=0.05,price=49000.12,quantity=0.5)
    # c2c_all(token_wen, token_junxin, sys_token, symbol="USDT-CNY", amount=10.12, price=7.12, quantity=10000)
    # get_orders(token_wen,state="0",pay_way="7",nationality="0",base_currency="USDT",quote_currency="CNY")
    # busines_payway_get_list(token_wen)
    # add_order(token=token_junxin,price=7.2, quantity=100, side="1", min_trx_cash="10", pay_way=7, symbol="USDT-CNY")
    # otc_add_deposit(token=token_wen, symbol="USDT", amount="100")
    # get_assets_c2c(token=token_wen)
    # user_payway_get_list(token_wen)
    # arbitrate_transaction(token=token_junxin, trx_id="100")
    # oneclick_add_transaction(token=token_wen, side="1", base_currency="USDT", amount="0", trx_cash="500", pay_way=2,quote_currency="CNY", nationality="")

    # cancel_all_orders(token_junxin) # 下架所有广告
    pass
