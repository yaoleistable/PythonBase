# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox

from Ui_P05_单项选择 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        print("您选择了A")
    
    @pyqtSlot()
    def on_radioButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        print("您选择了B")
    
    @pyqtSlot()
    def on_radioButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        print("您选择了C")
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
#        if self.radioButton_3.isChecked():
#            print("恭喜你，答对了")
#        else:
#            print("错误，请再次尝试")

        msgBox = QMessageBox()
        msgBox.setWindowTitle(u'答案')
        msgBox.setText(u"\n正确答案为：\n C")
        #msgBox.setWindowIcon(QtGui.QIcon(r':/0102.png'))
        #隐藏ok按钮
        msgBox.addButton(QMessageBox.Ok)
        msgBox.button(QMessageBox.Ok).hide()
        #模态对话框
        msgBox.exec_()
        


if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

