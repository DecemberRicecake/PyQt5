# -*- coding: utf-8 -*-
import time
import sxtwl
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal


class Runthread_t(QtCore.QThread):
    timesignal = pyqtSignal(str)
    nonglisignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        lunar = sxtwl.Lunar()   # 实例化日历库
        ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
        rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
               "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十",
               "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]
        year = int(time.strftime("%Y"))
        month = int(time.strftime("%m"))
        day = int(time.strftime("%d"))
        days = lunar.getDayBySolar(year, month, day)
        print("公历:", days.y, "年", days.m, "月", days.d, "日")

        if days.Lleap:
            nongli_info = "农历：  润" + ymc[days.Lmc] + "月" + rmc[days.Ldi]
        else:
            nongli_info = "农历：  " + ymc[days.Lmc] + "月" + rmc[days.Ldi]
        self.nonglisignal.emit(nongli_info)

        while True:
            self.timesignal.emit(str(time.strftime("%Y-%m-%d %H:%M:%S")))
            time.sleep(1)

