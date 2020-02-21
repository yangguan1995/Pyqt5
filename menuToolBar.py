# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuToolBar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 34))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionnew_file = QtWidgets.QAction(MainWindow)
        self.actionnew_file.setObjectName("actionnew_file")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionnew_file)
        self.menuFile.addAction(self.actionsave)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addAction(self.actionnew_file)
        self.toolBar.addAction(self.actionsave)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionnew_file.setText(_translate("MainWindow", "new file"))
        self.actionsave.setText(_translate("MainWindow", "save"))

