# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(10, 10, 431, 321))
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab.addTab(self.tab1, "Tab 1")
        self.tab.addTab(self.tab2, "Tab 2")
        self.tab.setCurrentIndex(0)
        self.tab1UI()
        self.retranslateUi(MainWindow)

    def tab1UI(self):
        self.label = QtWidgets.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(10, 20, 150, 50))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))

