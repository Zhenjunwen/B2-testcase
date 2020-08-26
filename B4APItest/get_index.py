#-*- coding=utf-8 -*-
#-*- encoding:utf-8 -*-
import requests
import smtplib
def sendMail(body):
    smtp_server = 'smtp.qq.com'
    from_mail = '444130378@qq.com'
    mail_pass = 'tivutkrbcztwcaeh'
    to_mail = ['zhenjunwen123@163.com','zhenjunwen@mohukeji.com',"wsad322@163.com"]
    cc_mail = ['']
    from_name = 'zhenjunwen'
    subject = 'This is a get_index report'   # 以gbk编码发送，一般邮件客户端都能识别
    #     msg = '''\
    # From: %s <%s>
    # To: %s
    # Subject: %sl
    # %s''' %(from_name, from_mail, to_mail_str, subject, body)  # 这种方式必须将邮件头信息靠左，也就是每行开头不能用空格，否则报SMTP 554
    mail = [
         "From: %s <%s>" % (from_name, from_mail),
         "To: %s" % ','.join(to_mail),   # 转成字符串，以逗号分隔元素
         "Subject: %s" % subject,
         "Cc: %s" % ','.join(cc_mail),
         "",
         body
         ]
    msg = '\n'.join(mail)  # 这种方式先将头信息放到列表中，然后用join拼接，并以换行符分隔元素，结果就是和上面注释一样了
    s = smtplib.SMTP()
    s.connect(smtp_server, '25')
    s.login(from_mail, mail_pass)
    s.sendmail(from_mail, to_mail+cc_mail, msg)
    s.quit()

def get_index(symbol):
    url = "https://api.socoin.cc/v2/futures/market/last60min_avg_index_price"
    params = {
        "symbol":symbol
    }
    res = requests.get(url=url, params=params).json()
    print(res)

if __name__ == "__main__":
    # get_index(symbol="btc")
    sendMail("this a  text")