# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultView2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileInfo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mapWidget = QtWidgets.QWidget(self.centralwidget)
        self.mapWidget.setGeometry(QtCore.QRect(0, 0, 731, 391))
        self.mapWidget.setObjectName("mapWidget")
        self.actionzoom_in = QtWidgets.QPushButton(self.centralwidget)
        self.actionzoom_in.setGeometry(QtCore.QRect(750, 10, 21, 20))
        self.actionzoom_in.setText("")
        r = QFileInfo(__file__).absolutePath()
        root = r.replace('/ui', '')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(root+"/icon/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionzoom_in.setIcon(icon)
        self.actionzoom_in.setObjectName("actionzoom_in")
        self.actionzoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.actionzoom_out.setGeometry(QtCore.QRect(750, 30, 21, 21))
        self.actionzoom_out.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(root+"/icon/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionzoom_out.setIcon(icon1)
        self.actionzoom_out.setObjectName("actionzoom_out")
        self.actionpan = QtWidgets.QPushButton(self.centralwidget)
        self.actionpan.setGeometry(QtCore.QRect(750, 50, 21, 21))
        self.actionpan.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(root+"/icon/pan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionpan.setIcon(icon2)
        self.actionpan.setObjectName("actionpan")
        self.actionfull_extent = QtWidgets.QPushButton(self.centralwidget)
        self.actionfull_extent.setGeometry(QtCore.QRect(750, 70, 21, 21))
        self.actionfull_extent.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(root+"/icon/full_extend.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfull_extent.setIcon(icon3)
        self.actionfull_extent.setObjectName("actionfull_extent")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

