# -*- coding: utf-8 -*-
import time
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal


class Runthread(QtCore.QThread):
    newsignal = pyqtSignal(int)

    def __init__(self, progress_start=0, parent=None):
        super().__init__(parent)
        self.progress_value = progress_start

    def run(self):
        while True:
            if self.progress_value > 100:
                self.stop()                 # 结束线程
            else:
                time.sleep(0.1)
                self.progress_value += 1
                self.newsignal.emit(self.progress_value)

    def stop(self):
        self.terminate()

