# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DDd.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 342)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 30, 121, 251))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 1)
        self.qtable = QtWidgets.QTableView(self.centralwidget)
        self.qtable.setGeometry(QtCore.QRect(210, 40, 550, 240))
        self.dblabel = QtWidgets.QLabel(self.centralwidget)
        self.dblabel.setGeometry(QtCore.QRect(30, 300, 500, 35))
        self.dblabel.setText('未连接数据库')
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "数据库"))
        self.pushButton_1.setText(_translate("MainWindow", "连接"))
        self.pushButton_2.setText(_translate("MainWindow", "查询"))
        self.pushButton_3.setText(_translate("MainWindow", "添加"))
        self.pushButton_4.setText(_translate("MainWindow", "删除"))
        self.pushButton_5.setText(_translate("MainWindow", "断开"))

