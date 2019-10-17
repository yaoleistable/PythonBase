# -*- coding: utf-8 -*-

"""
Module implementing helloMac.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QApplication

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
        # TODO: not implemented yet
        self.label.setText("你好")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = helloMac()
    # ui.setupUi(MainWindow)
    ui.show()
    sys.exit(app.exec_())
