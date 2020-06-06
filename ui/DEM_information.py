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
        self.label.setGeometry(QtCore.QRect(30, 50, 41, 9))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(InformationDialog)
        self.label_4.setGeometry(QtCore.QRect(240, 130, 41, 9))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(InformationDialog)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 41, 9))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(InformationDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 41, 9))
        self.label_2.setObjectName("label_2")
        self.textName = QtWidgets.QTextBrowser(InformationDialog)
        self.textName.setGeometry(QtCore.QRect(90, 40, 321, 21))
        self.textName.setObjectName("textName")
        self.textExtent = QtWidgets.QTextBrowser(InformationDialog)
        self.textExtent.setGeometry(QtCore.QRect(90, 80, 321, 21))
        self.textExtent.setObjectName("textExtent")
        self.textWidth = QtWidgets.QTextBrowser(InformationDialog)
        self.textWidth.setGeometry(QtCore.QRect(90, 120, 101, 21))
        self.textWidth.setObjectName("textWidth")
        self.textHeight = QtWidgets.QTextBrowser(InformationDialog)
        self.textHeight.setGeometry(QtCore.QRect(310, 120, 101, 21))
        self.textHeight.setObjectName("textHeight")
        self.label_5 = QtWidgets.QLabel(InformationDialog)
        self.label_5.setGeometry(QtCore.QRect(30, 170, 51, 16))
        self.label_5.setObjectName("label_5")
        self.textMax = QtWidgets.QTextBrowser(InformationDialog)
        self.textMax.setGeometry(QtCore.QRect(90, 170, 101, 21))
        self.textMax.setObjectName("textMax")
        self.textMin = QtWidgets.QTextBrowser(InformationDialog)
        self.textMin.setGeometry(QtCore.QRect(310, 170, 101, 21))
        self.textMin.setObjectName("textMin")
        self.label_6 = QtWidgets.QLabel(InformationDialog)
        self.label_6.setGeometry(QtCore.QRect(240, 170, 51, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(InformationDialog)
        self.label_7.setGeometry(QtCore.QRect(30, 220, 51, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(InformationDialog)
        self.label_8.setGeometry(QtCore.QRect(30, 270, 51, 21))
        self.label_8.setObjectName("label_8")
        self.textType = QtWidgets.QTextBrowser(InformationDialog)
        self.textType.setGeometry(QtCore.QRect(90, 220, 321, 21))
        self.textType.setObjectName("textType")
        self.textBandNum = QtWidgets.QTextBrowser(InformationDialog)
        self.textBandNum.setGeometry(QtCore.QRect(90, 270, 321, 21))
        self.textBandNum.setObjectName("textBandNum")

        self.retranslateUi(InformationDialog)
        QtCore.QMetaObject.connectSlotsByName(InformationDialog)

    def retranslateUi(self, InformationDialog):
        _translate = QtCore.QCoreApplication.translate
        InformationDialog.setWindowTitle(_translate("InformationDialog", "DEM 基本信息"))
        self.label.setText(_translate("InformationDialog", "名称"))
        self.label_4.setText(_translate("InformationDialog", "高度"))
        self.label_3.setText(_translate("InformationDialog", "宽度"))
        self.label_2.setText(_translate("InformationDialog", "范围"))
        self.label_5.setText(_translate("InformationDialog", "高程最大值"))
        self.label_6.setText(_translate("InformationDialog", "高程最大值"))
        self.label_7.setText(_translate("InformationDialog", "栅格类型"))
        self.label_8.setText(_translate("InformationDialog", "波段个数"))
