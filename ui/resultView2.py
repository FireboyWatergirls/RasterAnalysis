# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultView2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mapWidget = QtWidgets.QWidget(self.centralwidget)
        self.mapWidget.setObjectName("mapWidget")
        self.widget = QtWidgets.QWidget(self.mapWidget)
        self.widget.setGeometry(QtCore.QRect(740, 10, 34, 116))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.actionzoom_in = QtWidgets.QPushButton(self.widget)
        self.actionzoom_in.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionzoom_in.setIcon(icon)
        self.actionzoom_in.setObjectName("actionzoom_in")
        self.verticalLayout.addWidget(self.actionzoom_in)
        self.actionzoom_out = QtWidgets.QPushButton(self.widget)
        self.actionzoom_out.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionzoom_out.setIcon(icon1)
        self.actionzoom_out.setObjectName("actionzoom_out")
        self.verticalLayout.addWidget(self.actionzoom_out)
        self.actionpan = QtWidgets.QPushButton(self.widget)
        self.actionpan.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icon/pan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionpan.setIcon(icon2)
        self.actionpan.setObjectName("actionpan")
        self.verticalLayout.addWidget(self.actionpan)
        self.actionfull_extent = QtWidgets.QPushButton(self.widget)
        self.actionfull_extent.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icon/full_extend.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfull_extent.setIcon(icon3)
        self.actionfull_extent.setObjectName("actionfull_extent")
        self.verticalLayout.addWidget(self.actionfull_extent)
        self.horizontalLayout.addWidget(self.mapWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 23))
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
