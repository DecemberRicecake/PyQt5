# -*- coding: utf-8 -*-
import csv
import os
import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QSystemTrayIcon
from PyQt5.QtWidgets import QTableWidgetItem
from weatherThread import Runthread

import config
from BaseUI import Ui_MainWindow
from QssLoader import QssLoader
from timeThread import Runthread_t


class MyWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('天气小工具')    # 界面标题
        self.setWindowOpacity(0.9)              # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        ''' 给无边框移动用的三个变量 '''
        self._startPos = None
        self._endPos = None
        self._isTracking = False
        self.init_info()                  # 读取csv文件，初始化城市数据
        self.cityComboBox.addItems(["{0}".format(x) for x in config.city_list])     # 初始化界面下拉框
        # self.pushButton_refresh.clicked.connect(lambda: self.start_create("customer", 1))  # 可以传多个参数入线程
        self.pushButton_refresh.clicked.connect(lambda: self.start_create())    # 界面的按钮事件需要提前注册
        self.closeButton.clicked.connect(self.close)         # 界面退出程序
        self.miniButton.clicked.connect(self.init_tuopan)  # 界面最小化
        # self.miniButton.clicked.connect(self.showMinimized)  # 界面最小化
        self.trayIcon = QSystemTrayIcon(self)           # 托盘
        self.trayIcon.setIcon(QIcon(config.path_icon))  # 托盘图标
        self.time_thread = Runthread_t(self)
        self.time_thread.nonglisignal.connect(self.displaynongli)   # 刷新界面农历
        self.time_thread.timesignal.connect(self.displaytime)       # 刷新界面公历
        self.time_thread.start()

    def init_tuopan(self):
        self.hide()
        restoreAction = QAction("&显示主窗口", self, triggered=self.showNormal)
        quitAction = QAction("&退出", self, triggered=self.close)
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(restoreAction)
        # self.trayIconMenu.addSeparator()   # 分割线
        self.trayIconMenu.addAction(quitAction)

        self.setWindowIcon(QIcon(config.path_icon))
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.show()


    def init_info(self):
        File = open(config.path_csv, 'r')
        cityReader = csv.reader(File)
        cityData = list(cityReader)
        for i in cityData:
            if i[0] != '城市':
                config.city_Info[i[0]] = i[1]
                config.city_list.append(i[0])
        print(config.city_list, config.city_Info)
        File.close()

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):  # 重写鼠标事件
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):  # 重写鼠标事件
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def displaytime(self, s):       # 界面刷新当前时间
        self.timeLabel.setText(s)

    def displaynongli(self, s):     # 界面刷新农历
        self.yinliLabel.setText(s)

    # 可以建多个线程
    # def start_create(self, type, Nums):               # 可以传多个参数入线程
    def start_create(self):
        self.pushButton_refresh.setDisabled(True)
        # self.thread = Runthread(self, type, Nums)     # 可以传多个参数入线程
        self.thread = Runthread(self)
        self.thread.cmysignal.connect(self.add_info)    # 通过槽输出信号到前台界面
        self.thread.weasignal.connect(self.refreshweather)  # 刷新界面表格
        self.thread.start()

    def refreshweather(self, weather):
        for i in range(2):
            for j in range(5):
                self.weaTable.setItem(j + 1, i + 1, QTableWidgetItem(weather[i][j]))

    def add_info(self, message):                        # 界面打印信息
        if message == "结束！":
            self.pushButton_refresh.setDisabled(False)
        # else:
        #     str_date = +": "+message
        #     self.textBrowser.append(str_date)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_show = MyWindow()
    style = QssLoader.readQss(config.path_qss)
    app.setStyleSheet(style)
    my_show.show()
    sys.exit(app.exec_())
