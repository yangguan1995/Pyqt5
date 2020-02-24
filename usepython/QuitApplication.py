"""
课时26：用代码实现布局和退出应用程序
"""

import sys
from PyQt5.QtWidgets import QMainWindow , QApplication,QDesktopWidget, QVBoxLayout,QWidget,QPushButton

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(800,700)
        self.setWindowTitle("退出应用程序")
        #添加Button
        self.button1 = QPushButton("退出应用程序") #相当于信号
        self.button2 = QPushButton("点击无效")
        #将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)
        layout = QVBoxLayout() #把button放在layout上
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        #创建一个主框架
        mainFrame = QWidget()
        mainFrame.setLayout(layout) #把layout放在主框架上

        self.setCentralWidget(mainFrame)#把主框架充满整个屏幕
    """按钮单击事件的方法,相当于槽(事件得方法)"""
    def onClick_Button(self):
        sender = self.sender() #sender 获取发送信号的对象，也就是button
        print(sender.text() + '按钮被按下')  #sender.text获取发送信号的button对象的文本描述
        app = QApplication.instance()
        #退出应用程序
        app.quit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication ()
    main.show()
    sys.exit(app.exec_())