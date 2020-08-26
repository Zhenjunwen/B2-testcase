from dingtalkchatbot.chatbot import DingtalkChatbot
import time
import hmac
import hashlib
import base64
import urllib.parse
import requests

# 加签机器人
class DingDingRobot:

    def __init__(self, webhook_url, secret):
        timestamp = str(round(time.time() * 1000))
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        url = webhook_url + '&timestamp=%s&sign=%s' % (str(timestamp), sign)
        self.robot = DingtalkChatbot(url)

    def send_custom_info(self, msg):
        self.robot.send_text(msg)

    def get_index(self,symbol):
        url = "https://api.socoin.cc/v2/futures/market/last60min_avg_index_price"
        params = {
            "symbol": symbol
        }
        res = requests.get(url=url, params=params).json()
        print(res)
        return res

if __name__ == '__main__':
    try:
        robot = DingDingRobot('https://oapi.dingtalk.com/robot/send?access_token=fb4340cd5960964cce9d4f894d5a21c40509c303cc9905480658f337b5a8a9c0',"SEC79c6bee6b4a367d1cb7de154b100dc33464e25d05683ef8e132d51ad62646490")
        while True:
            res = robot.get_index('BTC')
            if res['code'] == 1000:
                pass
                # robot.send_custom_info("时间：%s\n"%time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"指数价：%s\n"%res["data"]["avg_index_price"]+"币种：%s\n"%res["data"]["symbol"])
            else:
                robot.send_custom_info("指数价出错")
            res = robot.get_index('ETH')
            if res['code'] == 1000:
                pass
                # robot.send_custom_info("时间：%s\n" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "指数价：%s\n" % res["data"]["avg_index_price"] + "币种：%s\n" % res["data"]["symbol"])
            else:
                robot.send_custom_info("指数价出错")
            time.sleep(60)
    except Exception as err:
        print(err)
        robot.send_custom_info("指数价文件出错:"+err)
