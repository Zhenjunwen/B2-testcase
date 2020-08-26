import datetime

from appium import webdriver
import time,traceback
from B3APItest.DB_config import DB

# 所使用的平台
desired_caps = {}
# 所使用的手机的名字   可以通过 adb devices 获得
desired_caps['platformName'] = 'Android'
# Android 的版本
desired_caps['platformVersion'] = '5.1.1'
# 测试名字
desired_caps['deviceName'] = 'test'
# app 的路径
# desired_caps['app'] = r'C:\Users\qiu\Desktop\btcso_dev.apk'
# app的包名
desired_caps['appPackage'] = 'com.mohu.btcso.debug'
# app 加载页面
desired_caps['appActivity'] = 'com.mohu.btcso.ui.splash.SplashActivity'
# 是否使用unicode键盘输入，在输入中文字符和unicode字符时设置为true
desired_caps['unicodeKeyboard'] = True
# 是否将键盘重置为初始状态，设置了unicodeKeyboard时，在测试完成后，设置为true，将键盘重置
desired_caps['resetKeyboard'] = True
desired_caps['newCommandTimeout'] = 6000

# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

# 获取屏幕大小
def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    print('width:',x,'height:',y)
    return x, y
# 屏幕向上滑动
def swipeUp(t):
    l=get_size()
    x1=int(l[0]*0.5)# x坐标
    y1=int(l[1]*0.75)# 起始y坐标
    y2=int(l[1]*0.25)# 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


# 屏幕向下滑动
def swipeDown(t):
    l=get_size()
    x1=int(l[0]*0.5)# x坐标
    y1=int(l[1]*0.25)# 起始y坐标
    y2=int(l[1]*0.75)# 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


# 屏幕向左滑动
def swipLeft(t):
    l = get_size()
    x1 = int(l[0] * 0.9)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.1)
    driver.swipe(x1, y1, x2, y1, t)

# 屏幕向右滑动
def swipRight(t):
    l = get_size()
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    driver.swipe(x1, y1, x2, y1, t)

def login_password():
    driver.tap([(975, 1235)], 2) #切换字母
    time.sleep(1)
    driver.tap([(231, 1688)], 2) #z
    time.sleep(1)
    driver.tap([(727, 1521)], 2) #j
    time.sleep(1)
    driver.tap([(158, 1366)], 2) #w
    time.sleep(1)
    driver.tap([(567, 1231)], 2) #切换数字
    time.sleep(1)
    driver.tap([(198, 1807)], 2) #9
    time.sleep(1)
    driver.tap([(206, 1664)], 2) #7
    time.sleep(1)
    driver.tap([(202, 1362)], 2) #1
    time.sleep(1)
    driver.tap([(534, 1803)], 2) #0
    time.sleep(1)
    driver.tap([(534, 1803)], 2) #0
    time.sleep(1)
    driver.tap([(874, 1517)], 2) #6
    time.sleep(1)
    driver.tap([(874, 1807)], 2) #点击完成
    time.sleep(1)
    return print("密码输入成功")

def login():
    db = DB('192.168.0.120',3306,'tars2','#k6tYIA4KrYfFU0y','biso')
    #获取验证码
    msm_code = db.query(sqlString="SELECT verification_code FROM `user_verification_code` WHERE user_account = 8615521057551 ORDER BY code_over_time DESC LIMIT 1")[0][0]
    print(msm_code)
    # 输入验证码
    ele_Verification_Code = driver.find_element_by_id('com.mohu.btcso.debug:id/verify_code_et').send_keys(msm_code)
    # 登录
    ele_login = driver.find_element_by_id("com.mohu.btcso.debug:id/sign_in_btn").click()
    return ele_Verification_Code,ele_login

try:
    driver.implicitly_wait(100)


#导航栏向左滑动两次
    for i in range(2):
        time.sleep(2)
        swipLeft(500)


    #点击导航栏立即体验
    ele_start = driver.find_element_by_id('com.mohu.btcso.debug:id/action_go_btn').click()
    time.sleep(1)
    #点击关闭海报
    ele_close_poster = driver.find_element_by_id('com.mohu.btcso.debug:id/close_iv')
    if ele_close_poster:
        ele_close_poster.click()
        #点击我的去登录页面
        ele_my_info = driver.find_element_by_id('com.mohu.btcso.debug:id/i_mine').click()
    else:
        ele_my_info = driver.find_element_by_id('com.mohu.btcso.debug:id/i_mine').click()

    # 点击输入手机号
    ele_phone = driver.find_element_by_id("com.mohu.btcso.debug:id/phone_num_et").send_keys('15521057551')
    time.sleep(1)

    #点击输入密码
    ele_password = driver.find_element_by_id('com.mohu.btcso.debug:id/password_et').click()
    #输入密码
    login_password()
    time.sleep(3)
    #点击下一步
    ele_next = driver.find_element_by_id('com.mohu.btcso.debug:id/action_btn').click()
    time.sleep(1)
    # 登录
    login()
    #计时
    now_time = datetime.datetime.now()
    print(now_time)
    end_time = now_time + datetime.timedelta(seconds=8)
    print(end_time)

    if now_time > end_time:
        login()
        print('登录超时，重新登录')
    else:
        pass


except:
    print(traceback.format_exc())