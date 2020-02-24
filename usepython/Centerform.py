#通过QDesktopWidget获得整个屏幕尺寸
"""
课时25：主窗口居中，需要手工计算窗口左上角坐标，通过QDesktopWidget获得整个屏幕尺寸，类另外建立为 Centerform.py
"""
import sys
from PyQt5.QtWidgets import QMainWindow , QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon #添加图标的

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm,self).__init__()
        #设置主窗口标题
        self.setWindowTitle("令窗口居中")
        #设置窗口尺寸
        self.resize(800,600)
    def center(self):
        #获取屏幕坐标系
        screen = QDesktopWidget.screenGeometry()
        #获取窗口坐标系
        size = self.geometry()
        #获取新坐标点
        newleft = (screen.width()-size.width())/2
        newtop = (screen.height()-size.height())/2
        self.move(newleft,newtop)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main = CenterForm   ()
    main.show()
    sys.exit(app.exec_())