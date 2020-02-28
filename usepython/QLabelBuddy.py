"""
课时31：设置伙伴关系
        mainlayout.addWidget(控件对象,行索引,列索引,占用行,占用列)
"""

from  PyQt5.QtWidgets import *
import sys

class QLabelBuddy(QDialog): #对话框
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLabel与伙伴控件")
        nameLabel = QLabel('&Name',self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password',self)
        passwordLineEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)

        benOK = QPushButton('&OK')
        benCancel = QPushButton('&Cancel')

        mainlayout = QGridLayout(self)
        mainlayout.addWidget(nameLabel,0,0)
        mainlayout.addWidget(nameLineEdit,0,1,1,2)

        mainlayout.addWidget(passwordLabel,1,0)
        mainlayout.addWidget(passwordLineEdit,1,1,1,2)

        mainlayout.addWidget(benOK,2,1)
        mainlayout.addWidget(benCancel,2,2)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=QLabelBuddy()
    main.show()
    sys.exit(app.exec_())