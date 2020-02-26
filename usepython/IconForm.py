
import sys
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtGui import QIcon #添加图标的

"""
课时28：窗口的setWindowIcon用于设置窗口图标，只在windows linux下可用
QApplication中的setWindowIcon用于设置窗口和应用程序图标，对窗口的图标设置优先级落后于窗口的setWindowIcon方法
"""
class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm,self).__init__()
        self.init_UI()
    def init_UI(self):
        # 设置窗口位置和尺寸
        self.setGeometry(800, 600,500,500)
        #设置主窗口标题
        self.setWindowTitle("设置窗口图标")
        self.setWindowIcon(QIcon('./images/Dragon.ico'))

        #获得状态栏
        #self.status = self.statusBar()
        #self.status.showMessage("只存在五秒的消息",5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon('./images/.ico'))
    main = IconForm()
    main.show()
    sys.exit(app.exec_())



