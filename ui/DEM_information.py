# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DEM_information.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class InformationDialog(object):
    def setupUi(self, InformationDialog):
        InformationDialog.setObjectName("InformationDialog")
        InformationDialog.resize(492, 398)
        self.label = QtWidgets.QLabel(InformationDialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 9))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(InformationDialog)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(InformationDialog)
        self.label_4.setGeometry(QtCore.QRect(240, 90, 41, 9))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(InformationDialog)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 41, 9))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(InformationDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 41, 9))
        self.label_2.setObjectName("label_2")
        self.textName = QtWidgets.QTextBrowser(InformationDialog)
        self.textName.setGeometry(QtCore.QRect(80, 10, 331, 21))
        self.textName.setObjectName("textName")
        self.textExtent = QtWidgets.QTextBrowser(InformationDialog)
        self.textExtent.setGeometry(QtCore.QRect(80, 50, 331, 21))
        self.textExtent.setObjectName("textExtent")
        self.textWidth = QtWidgets.QTextBrowser(InformationDialog)
        self.textWidth.setGeometry(QtCore.QRect(80, 80, 101, 21))
        self.textWidth.setObjectName("textWidth")
        self.textHeight = QtWidgets.QTextBrowser(InformationDialog)
        self.textHeight.setGeometry(QtCore.QRect(310, 80, 101, 21))
        self.textHeight.setObjectName("textHeight")
        self.widget = QtWidgets.QWidget(InformationDialog)
        self.widget.setGeometry(QtCore.QRect(30, 150, 421, 221))
        self.widget.setObjectName("widget")

        self.retranslateUi(InformationDialog)
        QtCore.QMetaObject.connectSlotsByName(InformationDialog)

    def retranslateUi(self, InformationDialog):
        _translate = QtCore.QCoreApplication.translate
        InformationDialog.setWindowTitle(_translate("InformationDialog", "DEM 基本信息"))
        self.label.setText(_translate("InformationDialog", "名称"))
        self.label_5.setText(_translate("InformationDialog", "高程直方图"))
        self.label_4.setText(_translate("InformationDialog", "高度"))
        self.label_3.setText(_translate("InformationDialog", "宽度"))
        self.label_2.setText(_translate("InformationDialog", "范围"))
