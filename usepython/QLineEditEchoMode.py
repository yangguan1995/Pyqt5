
"""
课时32：
QlineEdit控件与回显模式
基本功能：输入单行文本
EchoMode 回显模式：
输入文本时，怎样将其显示出来
1.Normal : 正常对话框一样，输入=输出
2.NoEcho：不回显，不显示输入
3.password：隐式显示*
4.PasswordEchoOnEdit:输入前一两秒显示，之后用*隐藏
"""
from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("文本输入框的回显模式")
        self.resize(500,500)
        formLayout = QFormLayout()
        Normal = QLineEdit()
        noEcho = QLineEdit()
        password = QLineEdit()
        passwordEcho = QLineEdit()

        formLayout.addRow("Normal",Normal)  #addRow添加表单项：增加一个Normal的标签，与Normal这个文本框对齐
        formLayout.addRow("noEcho",noEcho)
        formLayout.addRow("password",password)
        formLayout.addRow("passwordEcho",passwordEcho)

        #placeholdertext:灰色字体显示文本框提示，输入后消失
        Normal.setPlaceholderText("Normal")
        noEcho.setPlaceholderText("noEcho")
        password.setPlaceholderText("password")
        passwordEcho.setPlaceholderText("passwordEcho")

        Normal.setEchoMode(QLineEdit.Normal)
        noEcho.setEchoMode(QLineEdit.NoEcho)
        password.setEchoMode(QLineEdit.Password)
        passwordEcho.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())