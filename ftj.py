# -*- coding:utf-8 -*-
"""封天记API接口"""

import time
import urllib
import urllib2
import json
import hashlib
import requests
import base64
from md5 import md5
from decimal import Decimal
from flask import current_app

class ftj(object):
    # 3D引擎
    is_3d = 1
    def __init__(self, server_id=None):

        self.sid = server_id
        # 防沉迷。1：不防沉迷，0：开启防沉迷，2：未填写fcm信息
        self.fcm = 1
        # 附加参数
        self.exts = ''
        # 平台标示
        self.platform = '2217'
        # 登陆类型 web:网页登陆   pc：微端登陆
        self.type = 'web'
        # 登录密钥
        self.lkey = ''
        # 充值密钥
        self.pkey = ''
        # 登录url
        self.login_url = 'http://ftjg.com/login.html?'
        # 查询url
        self.role_url = 'http://ftj.com/role.html?'
        # 充值url
        self.charge_url = 'http://xiyou-g.com/pay.html?'
        # 游戏兑换比例
        self.exchange_ratio = Decimal('10')
        self.pay_rt = 0
        # 渠道标示
        self.channel = ''


    @property
    def access_time(self):
        return int(time.time())


    def make_login_sign(self,login_name=None,user_id=None,client=None):
        """生成sign"""
        date = "sid=%s&uid=%s&fcm=%s&exts=%s&time=%s&platform=%s%s"
        date = date % (self.sid, user_id, self.fcm, self.exts, self.access_time, self.platform, self.lkey)
 #       print date
 #       date = base64.b64encode(date)
        return md5(date).hexdigest()

    def login(self,client=None,login_name=None, source=None, back_url=None, user_id=None):
        """登录接口"""
        if client == 'hz' or client>0:
            self.type='pc'
            self.channel = 'hz'
        elif client !='hz' or client<=0:
            self.type='web'
        sign = self.make_login_sign(login_name=login_name,user_id=user_id,client=self.type)
        params = [('sid',self.sid),('uid',user_id),('fcm',self.fcm),('exts',base64.b64encode(self.exts)),
                  ('time',self.access_time),('platform',self.platform),('sign',sign),
                  ('type',self.type),('channel',self.channel)]
        login_url = ''.join([self.login_url, urllib.urlencode(params)])
        return login_url


    def make_role_sign(self, login_name=None, t=None,user_id=None):
        """生成角色查询签名"""
        data = "sid=%s&uid=%s&time=%s&platform=%s%s"
        data = data % (self.sid,user_id,t,self.platform,self.lkey)
        sign = md5(data).hexdigest()
        return sign

    def user_roles(self,  user_id=None, login_name=None, get_code=False):
        """用户角色
        pid=1&sid=55&uid=1222&time=1254924732&sign= bc636f85d4bd7b703a2a1df943db812e
        """
        from urllib import unquote
        t = self.access_time
        sign = self.make_role_sign(login_name,t,user_id)
        params = [('sid',self.sid),('uid',user_id),('time',t),
                  ('platform',self.platform),('sign',sign)]
        role_url = ''.join([self.role_url,urllib.urlencode(params)])
 #       print role_url
        response_data = urllib2.urlopen(role_url, timeout=2).read()
        response_data = json.loads(unquote(response_data))

        if get_code:
            return response_data

        status = response_data.get('status', '')

        if int(status) !=200:
            return []
        else:
            response_data = response_data.get('data')

   #     response_data = response_data[0]

        role_name = response_data.get('name')
        role_level = response_data.get('level')
        fightpower = response_data.get('fight')

        return [dict(role_name=role_name, role_level=role_level, fightpower=fightpower)]
    #    return [dict(role_name=role_name, role_level=role_level)]


    def user_role(self, user_id=None, login_name=None):
        """查询用户角色信息, 只查询一个"""

        roles = self.user_roles(user_id=user_id, login_name=login_name)

        if roles:
            return roles[0]
        return {}


    def verify_payment_money(self, game_money=None, u_money=None):
        """校验游戏货币数量和人民币是否移植
        * game_money: 游戏货币数量
        * u_money: 人民币(分为单位)
        """
        if not game_money or not u_money or not self.exchange_ratio:
            return False

        rmb_money = Decimal(str(u_money)) / Decimal('100')
        if rmb_money == (Decimal(str(game_money)) / self.exchange_ratio):
            return True
        return False

    def make_payment_sign(self, login_name=None, game_money=None, money=None, order_id=None, t=None, user_id=None):
        """签名验证方法
        """
        date = "sid=%s&uid=%s&oid=%s&money=%s&gold=%s&time=%s&platform=%s%s"
        date = date % (self.sid,user_id,order_id,money,game_money,t,self.platform,self.pkey)
   #     print date
        return md5(date).hexdigest()

    def get_charge_url(self, user_id=None, login_name=None, order_id=None, game_money=None, u_money=None):
        """得到充值链接
        """
        if not self.verify_payment_money(game_money=game_money, u_money=u_money):
            return False

        t = self.access_time
 #       order_money = Decimal(str(u_money/100.0))
        order_money = Decimal(str(u_money / 1))
        sign = self.make_payment_sign(login_name=login_name, game_money=game_money, money=order_money, order_id=order_id, t=t, user_id=user_id)
        params = [('sid',self.sid),('uid',user_id),('oid',order_id),('money',order_money),('gold',game_money),('time',t),
                  ('platform',self.platform),('sign',sign)]
        charge_url = ''.join([self.charge_url,urllib.urlencode(params)])
        return charge_url


    def payment(self, user_id=None, login_name=None, order_id=None, game_money=None, u_money=None, get_code=False):
        """充值"""
        charge_url = self.get_charge_url(user_id=user_id, login_name=login_name,
            order_id=order_id, game_money=game_money, u_money=u_money)
        response_data = self.__http_request(charge_url)
        if get_code:
            return response_data

        if not response_data:
            return False
    #    rs_code = str(response_data.get('status'))
        rs_code = response_data

        #记录返回信息
        data = [user_id, login_name, order_id, game_money, u_money, rs_code]
        data = [str(i) for i in data]
        key = '/'.join(data)
        try:
            current_app.logger.error(key)
        except Exception, e:
            pass

        if int(rs_code)==1:
            return True
        elif int(rs_code)==-12:
            self.pay_rt = -1
            return True

        return False

    def __http_request(self, url):
        response_data = None
        try:
            response_data = urllib2.urlopen(url, timeout=2).read()
            response_data = json.loads(response_data)
        except Exception, e:
            response_data = []

        return response_data

if __name__=='__main__':
    ftj = ftj(1)
#    print ftj.login(client='hz',login_name='good_8', source=None, back_url=None, user_id='100001')
   # print wd.get_charge_url(login_name='good_8', user_id=10000001, order_id='1000023', game_money=10, u_money=100)
 #   print ftj.user_role(login_name='good_8',user_id='100001')
    # print wd.make_login_sign(login_name='good_8')
 #   print ftj.payment(user_id='100001',login_name='good_8', order_id='1000000001', game_money=10, u_money=100)

