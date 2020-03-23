import pymysql


# 这里的connect,也可以写为Connection和Connect
def get_Verification_Code(sql):
    database = pymysql.connect(
        charset="utf8",
        host='192.168.0.120', # 如果是服务器，则输公网ip
        user='tars2', # 当时设置的数据超级管理员账户
        passwd='#k6tYIA4KrYfFU0y', # 当时设置的管理员密码
        port=3306, #MySQL数据的端口为3306，注意:切记这里不要写引号''
        database='biso' # 当时在MySQL中创建的数据库名字
        )

    # 获取一个游标 — 也就是开辟一个缓冲区，用于存放sql语句执行的结果
    cursor = database.cursor()
    cursor.execute(sql) #执行sql
    Verification_Code = cursor.fetchall() #绑定变量
    cursor.close() #关闭游标
    database.close() #关闭数据库
    return Verification_Code

if __name__ == "__main__":
    data = get_Verification_Code('SELECT verification_code FROM `user_verification_code` WHERE user_account = 8613533166909 ORDER BY code_over_time DESC LIMIT 1')
    print(data)
    sms_code = data[0][0]
    print(sms_code)


