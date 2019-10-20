"""
学习PyQt5消息对话框的使用
学习资料来源于：https://blog.csdn.net/qq_40006058/article/details/80074944
"""

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel
from PyQt5.QtGui import QPixmap
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 330, 300)
        self.setWindowTitle('早点毕业吧--消息对话框')

        self.la = QLabel('这里将会显示我们选择的按钮信息',self)
        self.la.move(20,20)
        self.bt1 = QPushButton('提示',self)
        self.bt1.move(20,70)
        self.bt2 = QPushButton('询问',self)
        self.bt2.move(120,70)
        self.bt3 = QPushButton('警告',self)
        self.bt3.move(220,70)
        self.bt4 = QPushButton('错误',self)
        self.bt4.move(20,140)
        self.bt5 = QPushButton('关于',self)
        self.bt5.move(120,140)
        self.bt6 = QPushButton('关于Qt',self)
        self.bt6.move(220,140)

        self.bt1.clicked.connect(self.info)
        self.bt2.clicked.connect(self.question)
        self.bt3.clicked.connect(self.warning)
        self.bt4.clicked.connect(self.critical)
        self.bt5.clicked.connect(self.about)
        self.bt6.clicked.connect(self.aboutqt)

        self.show()
        
    def info(self):
        """
        这里我们描述了一个信息提示的对话框。
        这个函数中我们显示的按钮分别是Ok、Close，默认按钮是Close。
        标签上的信息会根据我们选择的按钮信息相应的变化，判断是选择了OK还是Close。
        """
        reply = QMessageBox.information(self,'提示','这是一个消息提示对话框!', 
        QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.la.setText("你选择了Ok")
        else:
            self.la.setText("你选择了Close")
    
    def critical(self):
        #QMessageBox.critical(self,'错误','这是一个错误消息对话框', 
        #QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore , QMessageBox.Retry)
        msgBox = QMessageBox()
        msgBox.setWindowTitle('错误')
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("这是一个错误消息对话框")
        msgBox.setStandardButtons(QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore)
        msgBox.setDefaultButton(QMessageBox.Retry)
        msgBox.setDetailedText('这是详细的信息：学点编程吧，我爱你！')#该属性保存要在详细信息区域中显示的文本。文本将被解释为纯文本。默认情况下，此属性包含一个空字符串
        reply = msgBox.exec() 

        if reply == QMessageBox.Retry:
            self.la.setText('你选择了Retry！')
        elif reply == QMessageBox.Abort:
            self.la.setText('你选择了Abort！')
        else:
            self.la.setText('你选择了Ignore！')
    
    def warning(self):
         QMessageBox.warning(self,'警告','这是一个警告消息对话框', 
         QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Save)
    
    def question(self):
        reply = QMessageBox.question(self,'询问','这是一个询问消息对话框，默认是No', 
        QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.la.setText('你选择了Yes！')
        elif reply == QMessageBox.No:
            self.la.setText('你选择了No！')
        else:
            self.la.setText('你选择了Cancel！')
    
    def about(self):
        #QMessageBox.about(self,'关于','这是一个关于消息对话框!')
        msgBox = QMessageBox(QMessageBox.NoIcon, '关于','不要意淫了，早点洗洗睡吧!')
        msgBox.setIconPixmap(QPixmap("Lei.ico"))
        msgBox.exec()
        
    def aboutqt(self):
        QMessageBox.aboutQt(self,'关于Qt')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
