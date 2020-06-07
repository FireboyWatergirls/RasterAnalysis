# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DEM_information.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InformationDialog(object):
    def setupUi(self, InformationDialog):
        InformationDialog.setObjectName("InformationDialog")
        InformationDialog.resize(483, 321)
        self.label_6 = QtWidgets.QLabel(InformationDialog)
        self.label_6.setGeometry(QtCore.QRect(250, 170, 61, 21))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(InformationDialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 31, 21))
        self.label_3.setObjectName("label_3")
        self.textWidth = QtWidgets.QTextBrowser(InformationDialog)
        self.textWidth.setGeometry(QtCore.QRect(100, 120, 131, 31))
        self.textWidth.setObjectName("textWidth")
        self.label_4 = QtWidgets.QLabel(InformationDialog)
        self.label_4.setGeometry(QtCore.QRect(260, 120, 31, 21))
        self.label_4.setObjectName("label_4")
        self.textHeight = QtWidgets.QTextBrowser(InformationDialog)
        self.textHeight.setGeometry(QtCore.QRect(320, 120, 141, 31))
        self.textHeight.setObjectName("textHeight")
        self.label_8 = QtWidgets.QLabel(InformationDialog)
        self.label_8.setGeometry(QtCore.QRect(20, 220, 51, 20))
        self.label_8.setObjectName("label_8")
        self.textType = QtWidgets.QTextBrowser(InformationDialog)
        self.textType.setGeometry(QtCore.QRect(100, 220, 361, 30))
        self.textType.setObjectName("textType")
        self.label = QtWidgets.QLabel(InformationDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 31, 21))
        self.label.setObjectName("label")
        self.textName = QtWidgets.QTextBrowser(InformationDialog)
        self.textName.setGeometry(QtCore.QRect(100, 20, 361, 31))
        self.textName.setObjectName("textName")
        self.textMax = QtWidgets.QTextBrowser(InformationDialog)
        self.textMax.setGeometry(QtCore.QRect(100, 170, 131, 31))
        self.textMax.setObjectName("textMax")
        self.textMin = QtWidgets.QTextBrowser(InformationDialog)
        self.textMin.setGeometry(QtCore.QRect(320, 170, 141, 31))
        self.textMin.setObjectName("textMin")
        self.label_5 = QtWidgets.QLabel(InformationDialog)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 61, 21))
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(InformationDialog)
        self.label_9.setGeometry(QtCore.QRect(20, 270, 51, 20))
        self.label_9.setObjectName("label_9")
        self.textBandNum = QtWidgets.QTextBrowser(InformationDialog)
        self.textBandNum.setGeometry(QtCore.QRect(100, 270, 361, 31))
        self.textBandNum.setObjectName("textBandNum")
        self.label_2 = QtWidgets.QLabel(InformationDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 31, 21))
        self.label_2.setObjectName("label_2")
        self.textExtent = QtWidgets.QTextBrowser(InformationDialog)
        self.textExtent.setGeometry(QtCore.QRect(100, 70, 361, 31))
        self.textExtent.setObjectName("textExtent")

        self.retranslateUi(InformationDialog)
        QtCore.QMetaObject.connectSlotsByName(InformationDialog)

    def retranslateUi(self, InformationDialog):
        _translate = QtCore.QCoreApplication.translate
        InformationDialog.setWindowTitle(_translate("InformationDialog", "Dialog"))
        self.label_6.setText(_translate("InformationDialog", "高程最小值"))
        self.label_3.setText(_translate("InformationDialog", "宽度"))
        self.label_4.setText(_translate("InformationDialog", "高度"))
        self.label_8.setText(_translate("InformationDialog", "栅格类型"))
        self.label.setText(_translate("InformationDialog", "<html><head/><body><p>名称</p></body></html>"))
        self.label_5.setText(_translate("InformationDialog", "高程最大值"))
        self.label_9.setText(_translate("InformationDialog", "波段个数"))
        self.label_2.setText(_translate("InformationDialog", "范围"))
