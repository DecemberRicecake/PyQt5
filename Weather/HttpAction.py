# -*- coding: utf-8 -*-
import requests
import json


def newpost(posturl, postdata, token):
    headers = {'content-type': 'charset=utf8',
               'content-type': 'application/json',
               'Token': token,
               'Accept': 'application/json'
               }
    datas = json.dumps(postdata)
    proxies = {
        "http": "http://10.22.333.222:4444",
    }
    if posturl == "http://xxx/api/yyy/zzz":
        r = requests.post(posturl, data=datas, headers=headers, proxies=proxies)
    else:
        r = requests.post(posturl, data=datas, headers=headers)
    result = r.json()
    # tmpstr = json.dumps(result, ensure_ascii=False)
    return result


def newget(geturl, getdata):
    # proxies = {
    #     "http": "http://10.22.333.222:4444",
    # }
    proxies = {}
    headers = {
        # "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:36.0) Gecko/20100101 Firefox/36.0",
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        # "Accept-Encoding": "gzip, deflate",
        # # "Connection":"keep-alive",
        "Content-Type": "application/x-www-form-urlencoded"
        }
    r = requests.get(geturl, headers=headers, params=getdata, proxies=proxies)
    return r
