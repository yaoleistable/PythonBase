# -*- coding: utf-8 -*-

"""Module implementing MainWindow."""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

from Ui_P01_TextEdit import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor.

        @param parent reference to the parent widget
        @type QWidget

        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot(str)
    def on_lineEdit_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # str_me = "我爱我的祖国"
        # self.lineEdit.setText(str_me) # 设置单行文本内容
        input_text = self.lineEdit.text()
        self.textEdit.setPlainText(input_text)
        # self.textEdit.setHtml(input_text)  # 显示Html，如 <font color='red' size='20'>HELLO!</font>
        a = self.textEdit.toPlainText()
        print(a)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        """:type:PyQt5.QtWidgets.QMainWindow"""

        # self.textEdit.clear()  # 清空文本内容
        # 关闭窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
