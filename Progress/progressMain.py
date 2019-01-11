# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from progressThread import Runthread
from progressUI import Ui_MainWindow


class MyWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('控制进度条')              # 界面标题
        self.radioButton.clicked.connect(self.start_progress)
        self.radioButton_2.clicked.connect(self.stop_progress)
        self.radioButton_3.clicked.connect(self.reset_progress)

    def start_progress(self):
        self.thread = Runthread(self.progressBar.value())
        self.thread.newsignal.connect(self.update_progress)
        self.thread.start()

    def stop_progress(self):
        self.thread.stop()

    def reset_progress(self):
        self.thread.stop()
        self.progressBar.reset()

    def update_progress(self, value):
        self.progressBar.setValue(value)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_show = MyWindow()
    my_show.show()
    sys.exit(app.exec_())
