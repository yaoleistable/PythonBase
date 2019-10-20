# -*- coding: utf-8 -*-
 
"""
学习消息框的使用
"""
 
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
 
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('消息框学习')    
        self.show()
        
        
    def closeEvent(self, event):
        """
        关闭窗口时，显示的消息框
        """
        reply = QMessageBox.question(self, 'Message',
            "你确定退出么?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
