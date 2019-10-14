# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@file: P01_UI_maini.py.py
@time: 2019/10/14 17:11
"""
import sys
import P01_Ui
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = P01_Ui.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
