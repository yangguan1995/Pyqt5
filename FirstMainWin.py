"""
课时24
"""
import sys
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtGui import QIcon #添加图标的

"""
创建类
"""
class FirstMainWin(QMainWindow):
    def __index__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)
        #设置主窗口标题
        self.setWindowTitle("第一个主窗口应用")
        #设置窗口尺寸


