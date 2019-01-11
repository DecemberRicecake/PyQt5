# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BaseUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
import config


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(250, 250)
        MainWindow.setWindowIcon(QtGui.QIcon(config.path_icon))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.box_city = QtWidgets.QGroupBox(self.centralwidget)         # 分组--城市选择
        self.box_city.setGeometry(QtCore.QRect(5, 5, 235, 100))
        self.box_weather = QtWidgets.QGroupBox(self.centralwidget)      # 分组--天气
        self.box_weather.setGeometry(QtCore.QRect(5, 105, 235, 140))
        self.UI_city()
        self.UI_weather()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def UI_city(self):
        self.timeLabel = QtWidgets.QLabel(self.box_city)
        self.timeLabel.setGeometry(QtCore.QRect(10, 10, 130, 25))
        self.closeButton = QtWidgets.QPushButton(self.box_city)
        self.closeButton.setGeometry(QtCore.QRect(150, 10, 70, 25))
        self.closeButton.setObjectName('closeButton')               # 一定要加名字，QSS会使用，不同的按钮可以取一样的名字
        self.yinliLabel = QtWidgets.QLabel(self.box_city)
        self.yinliLabel.setGeometry(QtCore.QRect(10, 40, 130, 25))
        self.miniButton = QtWidgets.QPushButton(self.box_city)
        self.miniButton.setGeometry(QtCore.QRect(150, 40, 70, 25))
        self.miniButton.setObjectName('miniButton')
        self.cityLabel = QtWidgets.QLabel(self.box_city)
        self.cityLabel.setGeometry(QtCore.QRect(10, 70, 60, 25))
        self.cityComboBox = QtWidgets.QComboBox(self.box_city)
        self.cityComboBox.setGeometry(QtCore.QRect(55, 70, 70, 25))
        self.pushButton_refresh = QtWidgets.QPushButton(self.box_city)
        self.pushButton_refresh.setGeometry(QtCore.QRect(150, 70, 70, 25))
        self.pushButton_refresh.setObjectName('pushButton_refresh')

    def UI_weather(self):
        self.weaTable = QtWidgets.QTableWidget(self.box_weather)
        self.weaTable.setGeometry(QtCore.QRect(10, 10, 212, 122))
        self.weaTable.setColumnCount(3)
        self.weaTable.setRowCount(6)
        self.weaTable.setShowGrid(False)
        self.weaTable.setFrameShape(QFrame.NoFrame)
        self.weaTable.setSelectionBehavior(QTableWidget.SelectRows)  # 设置选择行为时每次选择一行
        self.weaTable.setEditTriggers(QTableWidget.NoEditTriggers)   # 设置不可编辑
        self.weaTable.verticalHeader().setVisible(False)  # 表头不可见
        self.weaTable.horizontalHeader().setVisible(False)  # 表头不可见
        self.weaTable.verticalHeader().setDefaultSectionSize(20)
        self.weaTable.setColumnWidth(0, 40)
        self.weaTable.setColumnWidth(1, 85)
        self.weaTable.setColumnWidth(2, 85)
        self.weaTable.setItem(0, 1, QTableWidgetItem("今天"))
        self.weaTable.setItem(0, 2, QTableWidgetItem("明天"))
        self.weaTable.item(0, 1).setTextAlignment(Qt.AlignCenter)
        self.weaTable.item(0, 2).setTextAlignment(Qt.AlignCenter)
        self.weaTable.setItem(1, 0, QTableWidgetItem("天气:"))
        self.weaTable.setItem(2, 0, QTableWidgetItem("气温:"))
        self.weaTable.setItem(3, 0, QTableWidgetItem("空气:"))
        self.weaTable.setItem(4, 0, QTableWidgetItem("风向:"))
        self.weaTable.setItem(5, 0, QTableWidgetItem("风力:"))

    def retranslateUi(self):
        self.timeLabel.setText("时间")
        self.cityLabel.setText("城市：")
        self.closeButton.setText("关闭")
        self.miniButton.setText("最小化")
        self.pushButton_refresh.setText("查询")








