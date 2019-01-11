# -*- coding: utf-8 -*-
import json
import HttpAction


def qweather(cityid):
    allurl = 'https://www.tianqiapi.com/api/'
    data = {'version': 'v1', 'cityid': cityid}
    weather = []
    try:
        resp = HttpAction.newget(allurl, data)
        if resp.status_code == 200:
            res = resp.content.decode('utf-8', 'replace')   # 用？取代非法字符
            tmp = json.loads(res, encoding='utf-8')
            weather.append(do_wea(tmp['data'][0], 0))
            weather.append(do_wea(tmp['data'][1], 1))
        return weather
    except Exception as e:
        print(e)
        return weather


def do_wea(weather, day):
    if day:
        air = '暂无'
    else:
        air = str(weather['air'])+weather['air_level']
    wea = [weather['wea'], weather['tem1']+'~'+weather['tem2'],
           air, weather['win'][0], weather['win_speed']]
    return wea
