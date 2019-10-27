# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/yaolei/PycharmProjects/PythonBase/PyQt5Projects/PyQt5快速开发与实战/02_基本窗口控件.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/img/Lei.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(530, 300, 61, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pic/img/help_64px_1236243_easyicon.net.ico"))
        self.label.setObjectName("label")
        self.btn_close = QtWidgets.QPushButton(self.centralWidget)
        self.btn_close.setGeometry(QtCore.QRect(30, 10, 113, 32))
        self.btn_close.setObjectName("btn_close")
        self.btn_QWidget = QtWidgets.QPushButton(self.centralWidget)
        self.btn_QWidget.setGeometry(QtCore.QRect(30, 40, 121, 31))
        self.btn_QWidget.setObjectName("btn_QWidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(330, 40, 251, 151))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(330, 10, 60, 16))
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(30, 70, 221, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_QLable = QtWidgets.QPushButton(self.widget)
        self.btn_QLable.setObjectName("btn_QLable")
        self.horizontalLayout.addWidget(self.btn_QLable)
        self.label_learn = QtWidgets.QLabel(self.widget)
        self.label_learn.setObjectName("label_learn")
        self.horizontalLayout.addWidget(self.label_learn)
        self.widget1 = QtWidgets.QWidget(self.centralWidget)
        self.widget1.setGeometry(QtCore.QRect(30, 110, 267, 33))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_QLineEdit = QtWidgets.QPushButton(self.widget1)
        self.btn_QLineEdit.setObjectName("btn_QLineEdit")
        self.horizontalLayout_2.addWidget(self.btn_QLineEdit)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setMouseTracking(True)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_close.setText(_translate("MainWindow", "关闭窗口"))
        self.btn_QWidget.setText(_translate("MainWindow", "QWidget学习"))
        self.textEdit.setToolTip(_translate("MainWindow", "我是多行文本框"))
        self.label_2.setText(_translate("MainWindow", "输出结果："))
        self.btn_QLable.setToolTip(_translate("MainWindow", "这是个按钮"))
        self.btn_QLable.setText(_translate("MainWindow", "QLable学习"))
        self.label_learn.setStatusTip(_translate("MainWindow", "QLable学习"))
        self.label_learn.setText(_translate("MainWindow", "TextLabel"))
        self.btn_QLineEdit.setText(_translate("MainWindow", "QLineEdit学习"))
        self.lineEdit.setToolTip(_translate("MainWindow", "我是单行文本框"))
        self.lineEdit.setText(_translate("MainWindow", "我是单行文本框"))
        self.statusBar.setStatusTip(_translate("MainWindow", "状态栏"))


import apprcc_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
