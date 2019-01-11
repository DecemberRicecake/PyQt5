# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
import collectData
import config
import queryWeather


class Runthread(QtCore.QThread):
    cmysignal = pyqtSignal(str)
    weasignal = pyqtSignal(list)

    ''' 如果有入参，需要初始化入参 '''
    # def __init__(self, MyWindow, type, Nums, parent=None):
    #     super().__init__(parent)
    #     self.MyWindow = MyWindow
    #     self.type = type
    #     self.nums = Nums

    def __init__(self, MyWindow, parent=None):
        super().__init__(parent)
        self.MyWindow = MyWindow

    def run(self):
        front_data = collectData.get_front_data(self.MyWindow)   # 获取界面数据
        cityid = config.city_Info[front_data['city']]            # 转换成cityid
        weather = queryWeather.qweather(cityid)                  # 从第三方API查询天气
        if weather:
            self.weasignal.emit(weather)
        self.cmysignal.emit("结束！")
        self.quit()

        # self.MyWindow.weatherValue.setText(weather['weather'])
        # self.MyWindow.temp1Value.setText(weather['temp1'])
        # self.MyWindow.temp2Value.setText(weather['temp2'])

