# -*-coding:utf-8 -*-
from websocket import create_connection
from sys import argv
import json
import threading


# 合约深度行情(带精度)
def precisionDepth():
    data_type = 10
    contract = ['BTC_20200501']
    symbol = []
    precision = -2  # 价格聚合精度，-2=2位小数，-1=1位小数，0=1位整数，1=2位整数... 以此类推
    m = {
        'Action': 1,
        'DataType': data_type,
        'Symbol': symbol,
        'Precision': precision,
        "Period": 0,  # K 线周期 （0：一分钟；1：五分钟；2：十五分钟；3：三十分钟；4：六十分钟；5：一天）
        "Contract": contract,
    }
    return json.dumps(m)


# 合约最新成交跌涨
def LastTrade():
    data_type = 9
    contract = ['BTC_202006012', 'BTC_202006019', 'BTC_20200626']
    symbol = []
    m = {
        'Action': 1,
        'DataType': data_type,
        'Symbol': symbol,
        'Precision': -2,  # 价格聚合精度，-2=2位小数，-1=1位小数，0=1位整数，1=2位整数... 以此类推
        "Period": 0,  # K 线周期 （0：一分钟；1：五分钟；2：十五分钟；3：三十分钟；4：六十分钟；5：一天）
        "Contract": contract,
    }
    return m


# 合约K线图
def KLine():
    data_type = 8
    contract = ['BTC_20200501']
    symbol = []
    period = 1
    m = {
        'Action': 1,
        'DataType': data_type,
        'Symbol': symbol,
        'Precision': -2,  # 价格聚合精度，-2=2位小数，-1=1位小数，0=1位整数，1=2位整数... 以此类推
        "Period": period,  # K 线周期 （0：一分钟；1：五分钟；2：十五分钟；3：三十分钟；4：六十分钟；5：一天）
        "Contract": contract,
    }
    return m


# 合约成交明细
def Trade():
    data_type = 7
    contract = ['BTC_20200501']
    symbol = []
    m = {
        'Action': 1,
        'DataType': data_type,
        'Symbol': symbol,
        'Precision': -2,  # 价格聚合精度，-2=2位小数，-1=1位小数，0=1位整数，1=2位整数... 以此类推
        "Period": 0,  # K 线周期 （0：一分钟；1：五分钟；2：十五分钟；3：三十分钟；4：六十分钟；5：一天）
        "Contract": contract,
    }
    return m


# 合约深度行情
def Depth():
    data_type = 6
    contract = ['BTC_20200501']
    symbol = []
    m = {
        'Action': 1,
        'DataType': data_type,
        'Symbol': symbol,
        'Precision': -2,  # 价格聚合精度，-2=2位小数，-1=1位小数，0=1位整数，1=2位整数... 以此类推
        "Period": 0,  # K 线周期 （0：一分钟；1：五分钟；2：十五分钟；3：三十分钟；4：六十分钟；5：一天）
        "Contract": contract,
    }
    return m


def connect_test(thread_name):
    ws = create_connection("wss://ws.b4dev.xyz/ws")

    data_type = 9
    contract = ['BTC_20200925']
    symbol = []
    precision = -2  # 价格聚合精度，-2=2位小数，-1=1位小数，0=1位整数，1=2位整数... 以此类推
    m = {
        'Action': 1,
        'DataType': data_type,
        'Symbol': symbol,
        'Precision': precision,
        "Period": 2,  # K 线周期 （0：一分钟；1：五分钟；2：十五分钟；3：三十分钟；4：六十分钟；5：一天）
        "Contract": contract,
    }

    trade_str = json.dumps(m)

    ws.send(trade_str)
    print("request: {}".format(trade_str))

    while True:
        try:
            result = ws.recv()
            print("{}: {}".format(thread_name, result))
            if result.find("ping") != -1:
                pong_time = result[9:len(result) - 1]
                pong = '{' + '"pong":   {0}'.format(pong_time) + '}'
                ws.send(pong.encode())
        except:
            return

def exchange_rate_test(thread_name):
    ws = create_connection("ws://192.168.0.149:2100/ws/price")
    m = {
        'Action':1,
        'Symbol':['ETH'],
    }
    trade_str = json.dumps(m)
    ws.send(trade_str)
    print("request: {}".format(trade_str))
    while True:
        try:
            result = ws.recv()
            print("{}: {}".format(thread_name, result))
            if result.find("ping") != -1:
                pong_time = result[9:len(result) - 1]
                pong = '{' + '"pong":   {0}'.format(pong_time) + '}'
                ws.send(pong.encode())
        except:
            return


def run(number_of_threads):
    n = number_of_threads
    ts = []
    for i in range(n):
        name = 'thread{}'.format(i)
        t1 = threading.Thread(target=connect_test, args=(name,))
        t1.start()
        ts.append(t1)

    for t in ts:
        t.join()


def main():
    if len(argv) >= 2:
        n = int(argv[5])
    else:
        n = 1

    run(n)


if __name__ == '__main__':
    main()