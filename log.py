#coding=utf-8
import os
import time

def out_log(url,send_msg="None",response_msg="None"):
    # 获得当前时间时间戳
    now = int(time.time())
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    logfiletime = time.strftime("%Y-%m-%d", timeArray)
    pathd = os.getcwd() + '\logs'
    if os.path.exists(pathd):  # 判断logs文件夹是否存在
        pass
    else:
        os.mkdir(pathd)  # 创建logs文件夹
    file_path = pathd + "\%s-log.log"%logfiletime
    with open(file_path,"a") as file:
        file.write(str(otherStyleTime)+"  "+" url "+url+" send_msg: "+str(send_msg)+" response_msg: "+str(response_msg))
        file.write("\r")
        file.close()
if __name__ == "__main__":
    out_log(url="aaa")