"""
课时38：单选框按钮
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QRadioButtonDemo')
        layout = QHBoxLayout()

        self.button1 = QRadioButton('单选按钮1')
        self.button1.setChecked(True)
        self.button1.toggled.connect(self.buttonstate)

        self.button2 = QRadioButton('单选按钮2')
        self.button2.setChecked(True)
        self.button2.toggled.connect(self.buttonstate)


        layout.addWidget(self.button1)
        layout.addWidget(self.button2)


        self.setLayout(layout)


    def buttonstate(self):
        radio = self.sender()
        if radio.isChecked() ==True:
            print('<'+radio.text()+ '>被选中')
        else:
            print('<'+radio.text()+'>未被选中')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())