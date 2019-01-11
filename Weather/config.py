# -*- coding: utf-8 -*-
import os
import sys

DB = {
    "main": {"server": "11.22.33.44", "user": "developer1", "password": "123456"},
    "qa": {"server": "55.66.77.88", "user": "developer2", "password": "2345678"}
}

city_Info = {}
city_list = []

path_icon = os.path.split(os.path.realpath(sys.argv[0]))[0] + '\logo.png'
path_csv = os.path.split(os.path.realpath(sys.argv[0]))[0] + '\data.csv'
path_qss = os.path.split(os.path.realpath(sys.argv[0]))[0] + '\style.qss'


# # 随机电话号码
# phoneRandom = str(random.randint(10000000000, 10999999999))
#
# # 随机汉字
# def GB2312():
#     head = random.randint(0xb0, 0xf7)
#     body = random.randint(0xa1, 0xfe)
#     wenzi = bytes([head, body]).decode('gb2312')
#     return wenzi
