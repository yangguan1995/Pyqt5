"""
课时27:面向过程的
"""
import sys
from PyQt5.QtWidgets import QPushButton,QHBoxLayout,QWidget,QApplication,QMainWindow
def on_clicked():
    print("1")
    print("wiget x: {}".format(wiget.x())) #窗口左上角横坐标
    print("wiget y: {}".format(wiget.y()))#窗口左上角纵坐标
    print("wiget width: {}".format(wiget.width()))  #工作区宽度500
    print("wiget height: {}".format(wiget.height())) #工作区宽度500
    """
    窗口不含标志栏和四周边缘空白区域;工作区四周有12像素的空白地区
    geometry x :可用工作区到屏幕顶距离
    geometry y :可用工作区到屏幕左边距离
    """
    print("2")
    print("wiget geometry x: {}".format(wiget.geometry().x())) #工作区左上角横坐标
    print("wiget geometry y: {}".format(wiget.geometry().y())) #工作区左上角纵坐标
    print("wiget geometry width: {}".format(wiget.geometry().width())) #工作区宽度
    print("wiget geometry height: {}".format(wiget.geometry().height())) #工作区高度
    """
    frameGeometry().weight():工作区包含窗口四周边缘空白区域宽度
    frameGeometry().heigth():工作区包含标志栏高度
    """
    print("3")
    print("wiget FrameGeometry x: {}".format(wiget.frameGeometry().x())) #窗口左上角横坐标
    print("wiget FrameGeometry y: {}".format(wiget.frameGeometry().y()))  #窗口左上角纵坐标
    print("wiget FrameGeometry width: {}".format(wiget.frameGeometry().width())) #窗口宽度
    print("wiget FrameGeometry height: {}".format(wiget.frameGeometry().height()))#窗口高度
    #得到标志栏高度40
    #app.quit()

app = QApplication(sys.argv)
wiget = QWidget() #创建一个窗口
btn = QPushButton(wiget)
btn.setText("按他,告诉你窗口大小和位置")
btn.clicked.connect(on_clicked)
btn.move(20,30)
wiget.resize(500,500) #设置工作区的尺寸，不是整个窗口的
wiget.move(1000,600)  #设置窗口左上角位于屏幕的位置，不是工作区左上角位于屏幕的位置
wiget.setWindowTitle("ScreenGeometry")
#wiget.setCentralWidget()
wiget.show()
sys.exit(app.exec_())