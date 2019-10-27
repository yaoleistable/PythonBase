# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QDesktopWidget

from Ui_02_基本窗口控件 import Ui_MainWindow


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
        self.statusBar_Learn()  # 调用函数
        self.connect_Fun()

    def connect_Fun(self):
        """
        连接槽函数 
        """
        self.btn_close.clicked.connect(self.btn_closeWindow)  # 连接槽函数
        self.btn_QWidget.clicked.connect(self.btn_QWidget_Clicked)
        self.btn_QLable.clicked.connect(self.btn_QLable_Clicked)
        self.btn_QLineEdit.clicked.connect(self.btn_QLineEdit_Clicked)

    def print_Message(self, message):
        """
        多行文本框显示消息
        """
        self.textEdit.append(str(message))

    def btn_QWidget_Clicked(self):
        """
        QWidget类学习
        """
        screen = QDesktopWidget().screenGeometry()
        # self.move(300, 300) # 设置窗口显示位置
        size = self.geometry()
        self.move((screen.width() - size.width()) / 4, (screen.height() - size.height()) / 2)  # 设置窗口显示位置
        self.setWindowTitle("QWidget学习")  # 设置窗口标题
        # self.setWindowIcon(QIcon("./img/pig_32px.ico"))  # 设置窗口图标

        self.setToolTip("这是个气泡提示")  # 设置气泡提示

        self.print_Message("获取客户区的宽度和高度:{0}".format(self.size()))
        self.print_Message("窗体左上角坐标:x={0}，坐标y={1}".format(self.x(), self.y()))  # 打印窗体左上角x，y坐标
        self.print_Message("窗体宽度:{0}、高度:{1}".format(self.width(), self.height()))  # 打印窗体宽度、高度
        self.setFixedHeight(500)  # 设置窗口高度
        self.setGeometry(30, 30, 600, 400)  # 设置窗口位置和大小
        self.print_Message("获得窗口的大小和位置:{0}".format(self.frameGeometry()))
        self.print_Message("窗口左上角坐标:{0}".format(self.pos()))
        self.print_Message("窗口左上角坐标:{0},{1}".format(self.geometry().x(), self.geometry().y()))
        msg = self.textEdit.toPlainText()  # 获取多行文本框内容
        print(msg)

    def btn_QLable_Clicked(self):
        self.label_learn.setText("label学习")
        self.label_learn.setAutoFillBackground(True)
        self.print_Message(self.label_learn.text())
        self.label_learn.setToolTip("这是一个标签")

    def statusBar_Learn(self):
        """
        状态栏学习
        """
        self.statusBar.showMessage("我是状态栏", 5000)  # 状态栏设置函数 showMessage()

    def btn_closeWindow(self):
        """
        自定义关闭窗口
        """
        sender = self.sender()
        print(sender.text() + "被按下了")
        qApp = QApplication.instance()
        qApp.quit()

    def btn_QLineEdit_Clicked(self):
        self.lineEdit.clear()  # 清空单行文本框内容
        self.lineEdit.setText("我爱你，我的祖国")
        self.print_Message(self.lineEdit.text())
        QApplication.processEvents()  # 刷新页面


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
