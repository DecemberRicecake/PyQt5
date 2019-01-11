# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtSql
from PyQt5 import QtWidgets
from DbLinkUI import Ui_MainWindow


class MyWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('数据库操作')              # 界面标题
        self.pushButton_1.clicked.connect(self.db_link)
        self.pushButton_2.clicked.connect(self.db_query)
        self.pushButton_3.clicked.connect(self.db_add)
        self.pushButton_4.clicked.connect(self.db_del)
        self.pushButton_5.clicked.connect(self.db_quit)
        self.db_status = False

    def db_link(self):
        if not self.db_status:
            try:
                self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
                self.db.setHostName('127.0.0.1')
                self.db.setPort(3306)
                self.db.setDatabaseName('TestPlatform')
                self.db.setUserName('root')
                self.db.setPassword('123456')
                if self.db.open():
                    self.db_status = True
                    self.dblabel.setText('数据库已连接')
                    self.model = QtSql.QSqlTableModel()
                    self.qtable.setModel(self.model)
                    self.model.setTable('api_project')  # 填查询的表名
                    self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
                else:
                    self.dblabel.setText(self.db.lastError().text())
            except Exception as e:
                self.dblabel.setText(e)

    def db_query(self):
        if self.db_status:
            self.model.select()
            # self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
            # self.model.setHeaderData(1, QtCore.Qt.Horizontal, '标题1')

    def db_add(self):               # 添加一条数据
        if self.db_status:
            self.db_query()         # 刷新页面
            self.model.insertRow(self.model.rowCount())

    def db_del(self):
        if self.db_status:          # 删除一条数据
            self.model.removeRow(self.qtable.currentIndex().row())
            self.db_query()         # 刷新页面

    def db_quit(self):              # 关闭数据库连接
        if self.db_status:
            self.db.close()
            self.db_status = False
            self.dblabel.setText('数据库已关闭')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_show = MyWindow()
    my_show.show()
    sys.exit(app.exec_())
