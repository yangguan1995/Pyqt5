"""课时29：显示控件信息"""
import sys
from PyQt5.QtWidgets import QPushButton,QHBoxLayout,QWidget,QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon,QFont #添加图标,字体
class ToolTipForm(QMainWindow):
    def __init__(self):
        super(ToolTipForm,self).__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(800,800,600,600)
        self.setWindowTitle('设置控件提示信息')
        self.button1 = QPushButton('wo')
        self.button1.setToolTip('这是一个按钮')
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        main = QWidget()
        main.setLayout(layout)
        self.setCentralWidget(main)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon('./images/.ico'))
    main = ToolTipForm()
    main.show()
    sys.exit(app.exec_())