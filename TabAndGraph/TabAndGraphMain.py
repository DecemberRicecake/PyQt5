# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from TabAndGraphUI import Ui_MainWindow
import pyqtgraph as pg


class MyWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('选项卡和绘图')              # 界面标题
        pw = pg.PlotWidget(name='Plot1')
        pw.showGrid(x=True, y=True)
        self.tab.addTab(pw, "折线图")
        p1 = pw.plot()
        p1.setPen((200, 200, 100))
        xd, yd = [1, 2, 3], [4, 1, 6]
        p1.setData(y=yd, x=xd)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_show = MyWindow()
    my_show.show()
    sys.exit(app.exec_())
