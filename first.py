import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    #创建QApplication实例
    app = QApplication(sys.argv)
    #创建窗口
    window = QWidget()
    window.resize(500,500)
    #移动窗口
    window.move(300,300)
    window.setWindowTitle('第一个pyqt5桌面应用程序')
    window.show()
    sys.exit(app.exec_())