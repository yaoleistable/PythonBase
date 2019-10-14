# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@file: P02_Python_QIcon.py
@time: 2019/10/14 12:25
"""
# 这里我们提供必要的引用。基本控件位于PyQt5.QtWidgets模块中。
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('QIcon')
        icon_path = 'Lei.ico'
        self.setWindowIcon(QIcon(icon_path))
        self.show()


def main():
    # 每一PyQt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    ex = App()
    # QWidget部件是PyQt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
