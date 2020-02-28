"""
课时33
限制QLineEdit控件的输入(校验器)
如限制只能输入数字，整数，浮点数或满足一定条件的字符串
"""
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
class QLineEditValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("校验器")
        formlayout = QFormLayout()
        INT = QLineEdit()
        DOUBLE = QLineEdit()
        REG = QLineEdit()

        formlayout.addRow("整数类型",INT)
        formlayout.addRow("浮点数",DOUBLE)
        formlayout.addRow("数字和字母",REG)

        INT.setPlaceholderText("整型")
        DOUBLE.setPlaceholderText("浮点型")
        REG.setPlaceholderText("字母和数字")

        intvalidator = QIntValidator(self)
        intvalidator.setRange(1,99)

        doublevalidator = QDoubleValidator(self)
        doublevalidator.setRange(-360,360)
        doublevalidator.setNotation(QDoubleValidator.StandardNotation) #标准显示法
        doublevalidator.setDecimals(2)#设置精度

        reg = QRegExp('[a-zA-Z0-9]+$')
        RegExpValidator = QRegExpValidator(self)
        RegExpValidator.setRegExp(reg)

        #设置校验器
        INT.setValidator(intvalidator)
        DOUBLE.setValidator(doublevalidator)
        REG.setValidator(RegExpValidator)

        self.setLayout(formlayout)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=QLineEditValidator()
    main.show()
    sys.exit(app.exec_())



