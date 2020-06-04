# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XYZTile.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_XYZ_Dialog(object):
    def setupUi(self, XYZ_Dialog):
        XYZ_Dialog.setObjectName("XYZ_Dialog")
        XYZ_Dialog.resize(338, 404)
        self.URI = QtWidgets.QLineEdit(XYZ_Dialog)
        self.URI.setGeometry(QtCore.QRect(150, 20, 113, 20))
        self.URI.setObjectName("URI")
        self.label = QtWidgets.QLabel(XYZ_Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 31, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(XYZ_Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(XYZ_Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 90, 51, 21))
        self.label_3.setObjectName("label_3")
        self.lyrs = QtWidgets.QLineEdit(XYZ_Dialog)
        self.lyrs.setGeometry(QtCore.QRect(150, 90, 113, 20))
        self.lyrs.setObjectName("lyrs")
        self.Xvalue = QtWidgets.QLineEdit(XYZ_Dialog)
        self.Xvalue.setGeometry(QtCore.QRect(150, 130, 113, 20))
        self.Xvalue.setObjectName("Xvalue")
        self.label_4 = QtWidgets.QLabel(XYZ_Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 130, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(XYZ_Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 170, 54, 12))
        self.label_5.setObjectName("label_5")
        self.Yvalue = QtWidgets.QLineEdit(XYZ_Dialog)
        self.Yvalue.setGeometry(QtCore.QRect(150, 170, 113, 20))
        self.Yvalue.setObjectName("Yvalue")
        self.label_6 = QtWidgets.QLabel(XYZ_Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 210, 54, 12))
        self.label_6.setObjectName("label_6")
        self.Zvalue = QtWidgets.QLineEdit(XYZ_Dialog)
        self.Zvalue.setGeometry(QtCore.QRect(150, 210, 113, 20))
        self.Zvalue.setObjectName("Zvalue")
        self.addXYZTileLayer = QtWidgets.QPushButton(XYZ_Dialog)
        self.addXYZTileLayer.setGeometry(QtCore.QRect(130, 340, 75, 23))
        self.addXYZTileLayer.setObjectName("addXYZTileLayer")
        self.label_7 = QtWidgets.QLabel(XYZ_Dialog)
        self.label_7.setGeometry(QtCore.QRect(100, 20, 51, 20))
        self.label_7.setObjectName("label_7")
        self.zmin = QtWidgets.QLineEdit(XYZ_Dialog)
        self.zmin.setGeometry(QtCore.QRect(150, 250, 113, 20))
        self.zmin.setObjectName("zmin")
        self.label_8 = QtWidgets.QLabel(XYZ_Dialog)
        self.label_8.setGeometry(QtCore.QRect(80, 250, 54, 12))
        self.label_8.setObjectName("label_8")
        self.zmax = QtWidgets.QLineEdit(XYZ_Dialog)
        self.zmax.setGeometry(QtCore.QRect(150, 290, 113, 20))
        self.zmax.setObjectName("zmax")
        self.label_9 = QtWidgets.QLabel(XYZ_Dialog)
        self.label_9.setGeometry(QtCore.QRect(80, 290, 54, 12))
        self.label_9.setObjectName("label_9")

        self.retranslateUi(XYZ_Dialog)
        QtCore.QMetaObject.connectSlotsByName(XYZ_Dialog)

    def retranslateUi(self, XYZ_Dialog):
        _translate = QtCore.QCoreApplication.translate
        XYZ_Dialog.setWindowTitle(_translate("XYZ_Dialog", "Dialog"))
        self.URI.setText(_translate("XYZ_Dialog", "www.google.cn/maps/vt/"))
        self.label.setText(_translate("XYZ_Dialog", "URI:"))
        self.label_2.setText(_translate("XYZ_Dialog", "参数：:"))
        self.label_3.setText(_translate("XYZ_Dialog", "lyrs:"))
        self.lyrs.setText(_translate("XYZ_Dialog", "s"))
        self.Xvalue.setText(_translate("XYZ_Dialog", "{x}"))
        self.label_4.setText(_translate("XYZ_Dialog", "x:"))
        self.label_5.setText(_translate("XYZ_Dialog", "y:"))
        self.Yvalue.setText(_translate("XYZ_Dialog", "{y}"))
        self.label_6.setText(_translate("XYZ_Dialog", "z:"))
        self.Zvalue.setText(_translate("XYZ_Dialog", "{z}"))
        self.addXYZTileLayer.setText(_translate("XYZ_Dialog", "添加图层"))
        self.label_7.setText(_translate("XYZ_Dialog", "https://"))
        self.zmin.setText(_translate("XYZ_Dialog", "0"))
        self.label_8.setText(_translate("XYZ_Dialog", "zmin:"))
        self.zmax.setText(_translate("XYZ_Dialog", "12"))
        self.label_9.setText(_translate("XYZ_Dialog", "zmax:"))
