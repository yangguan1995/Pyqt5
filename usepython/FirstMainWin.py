"""
课时24:创建一个主窗口
课时25：主窗口居中，需要手工计算窗口左上角坐标，通过QDesktopWidget获得整个屏幕尺寸，类另外建立为 Centerform.py
"""
import sys
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtGui import QIcon #添加图标的

"""
创建类
"""
class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)
        #设置主窗口标题
        self.setWindowTitle("第一个主窗口应用")
        #设置窗口尺寸
        self.resize(800,600)
        #获得状态栏
        self.status = self.statusBar()
        self.status.showMessage("只存在五秒的消息",5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())



