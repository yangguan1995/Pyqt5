"""
QLabel控件
setAlignment():设置文本对齐方式
setIndent():设置文本缩进
text():获取文本内容
setBuddy():设置伙伴关系
setText():设置文本内容
selectedText()：返回所选择的字符
setWordWrap():设置是否允许换行
QLabel常用的信号(事件):
1.鼠标滑过QLabel控件时触发：linkHovered（槽）
2.鼠标单击QLabel控件时触发:linkActivated
"""
import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication,QHBoxLayout,QVBoxLayout,QPushButton,QMainWindow
from PyQt5.QtGui import QPalette,QPixmap,QIcon
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo,self).__init__()
        self.initUI()
    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        label1.setText("<font color = yellow>这是一个文本标签。</font>")
        palette = QPalette()
        label1.setAutoFillBackground(True)
        palette.setColor(QPalette.Window,Qt.blue) #设置背景色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./images/python.jpg"))
        label4.setOpenExternalLinks(True)#True：打开网页；False:调用槽函数
        label4.setText("<a href='https://item.jd.com'>我想买手机</a>")

        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')
        #label放入垂直布局
        Vbox = QVBoxLayout()
        Vbox.addWidget(label1)
        Vbox.addWidget(label2)
        Vbox.addWidget(label3)
        Vbox.addWidget(label4)
        label2.linkHovered.connect(self.linkHovered) #linkHovered，linkActivated： label内置的事件
        label4.linkActivated.connect(self.linkClicked) #链接槽是自定义的

        self.setLayout(Vbox)
        self.setWindowTitle('QLabel控件演示')
        self.setWindowIcon(QIcon('./images/Dragon.ico'))
    def linkHovered(self):
        print("当鼠标滑过label2标签时，触发")
    def linkClicked(self):
        print("鼠标点击label4标签时，触发事件")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())