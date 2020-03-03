"""
课时36 QTextEdit控件
"""
from PyQt5.QtWidgets import *
import sys

class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QTextEdit控件演示')
        self.resize(500,500)
        self.textEdit = QTextEdit()
        self.buttonText = QPushButton('显示文本')
        self.buttonHTML = QPushButton('显示HTML')
        self.tobuttonText = QPushButton('获取文本')
        self.tobuttonHTML = QPushButton('获取HTML')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.tobuttonText)
        layout.addWidget(self.tobuttonHTML)

        self.setLayout(layout)
        self.buttonText.clicked.connect(self.onClickButtonText)
        self.buttonHTML.clicked.connect(self.onclickButtonHTML)
        self.tobuttonText.clicked.connect(self.onClicktoButtonText)
        self.tobuttonHTML.clicked.connect(self.onclicktoButtonHTML)
    def onClickButtonText(self):
        self.textEdit.setPlainText('Hello World,世界你好吗？\nhaha')
    def onClicktoButtonText(self):
        print(self.textEdit.toPlainText())
    def onclickButtonHTML(self):
        self.textEdit.setHtml('<font color = "blue" size = "5">Hello world </font>')
    def onclicktoButtonHTML(self):
        print(self.textEdit.toHtml())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())