# -*- coding: utf-8 -*-

"""
Module implementing helloMac.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from Ui_helloMac import Ui_MainWindow


class helloMac(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(helloMac, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        user_name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if user_name == "admin" and password == "123456":
            print("登录成功")
        else:
            print("用户名密码不匹配")

    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("你好，我是退出")
        lineEdit_text2 = self.lineEdit_2.text()
        print(lineEdit_text2)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = helloMac()
    ui.show()
    sys.exit(app.exec_())
