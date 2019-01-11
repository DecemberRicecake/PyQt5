# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
import config
import pymssql
import collectData
import uuid
import decimal
# import _mssql
# import pypyodbc
# decimal.__version__
# uuid.ctypes.__version__
# _mssql.__version__


class czThread(QtCore.QThread):
    czsignal = pyqtSignal(str)

    def __init__(self, MyWindow, typex, parent=None):
        super().__init__(parent)
        self.MyWindow = MyWindow
        self.recharge_type = typex

    def run(self):
        front_data = collectData.get_front_data(self.MyWindow)  # 获取界面数据
        db_data = config.DB[front_data["env"]]
        server = db_data["server"]
        user = db_data["user"]
        password = db_data["password"]
        database = "xxxxxdddd_com"
        conn = pymssql.connect(server, user, password, database)
        cursor = conn.cursor()
        if not cursor:
            raise Exception('数据库连接失败！')
        sSQL = "SELECT id FROM " + database + ".dbo.user where UserName = " + \
               front_data["phoneNum"]
        cursor.execute(sSQL)
        s_data = cursor.fetchall()
        conn.commit()
        conn.close()
        if not s_data:
            output_text = "异常：用户不存在，请检查手机号"
        else:
            database = "ggg_Pay"
            conn = pymssql.connect(server, user, password, database)
            cursor = conn.cursor()
            if not cursor:
                raise Exception('数据库连接失败！')
            if self.recharge_type == "coin":
                sSQL = "UPDATE " + database + ".dbo.pay_Account " \
                                              "SET Amount = " + front_data["coinNum"] + \
                       " WHERE UserID = " + str(s_data[0][0])
            else:
                sSQL = "UPDATE " + database + ".dbo.Score_Account " \
                                              "SET Score = " + front_data["scoreNum"] + \
                       " WHERE UserID = " + str(s_data[0][0])
            cursor.execute(sSQL)
            conn.commit()
            conn.close()
            output_text = "修改成功"

        self.czsignal.emit(output_text)
        self.czsignal.emit("结束！")
        self.quit()

