# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@file: P02_UI_Mac_main.py
@time: 2019/10/14 9:38 下午
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQT.P02_UI_Mac import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
