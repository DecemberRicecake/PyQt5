# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets

from Dialog.dialogUI import Ui_Dialog
from Dialog.dialogmainUI import Ui_MainWindow


class MyWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('处理对话框')              # 界面标题
        self.pushButton.clicked.connect(self.click_button)

    def click_button(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            self.label.setText("ok")
        if result == QtWidgets.QDialog.Rejected:
            self.label.setText("cancel")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_show = MyWindow()
    my_show.show()
    sys.exit(app.exec_())
