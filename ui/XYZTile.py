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
        XYZ_Dialog.resize(236, 271)
        self.verticalLayoutWidget = QtWidgets.QWidget(XYZ_Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 160, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.URI = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.URI.setObjectName("URI")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.URI)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lyrs = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lyrs.setObjectName("lyrs")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lyrs)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Xvalue = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Xvalue.setObjectName("Xvalue")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Xvalue)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.Yvalue = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Yvalue.setObjectName("Yvalue")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Yvalue)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.Zvalue = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Zvalue.setObjectName("Zvalue")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Zvalue)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.zmin = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.zmin.setObjectName("zmin")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.zmin)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.zmax = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.zmax.setObjectName("zmax")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.zmax)
        self.addXYZTileLayer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addXYZTileLayer.setObjectName("addXYZTileLayer")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.addXYZTileLayer)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(XYZ_Dialog)
        QtCore.QMetaObject.connectSlotsByName(XYZ_Dialog)

    def retranslateUi(self, XYZ_Dialog):
        _translate = QtCore.QCoreApplication.translate
        XYZ_Dialog.setWindowTitle(_translate("XYZ_Dialog", "Dialog"))
        self.label.setText(_translate("XYZ_Dialog", "URI:"))
        self.URI.setText(_translate("XYZ_Dialog", "www.google.cn/maps/vt/"))
        self.label_3.setText(_translate("XYZ_Dialog", "lyrs:"))
        self.lyrs.setText(_translate("XYZ_Dialog", "s"))
        self.label_4.setText(_translate("XYZ_Dialog", "x:"))
        self.Xvalue.setText(_translate("XYZ_Dialog", "{x}"))
        self.label_5.setText(_translate("XYZ_Dialog", "y:"))
        self.Yvalue.setText(_translate("XYZ_Dialog", "{y}"))
        self.label_6.setText(_translate("XYZ_Dialog", "z:"))
        self.Zvalue.setText(_translate("XYZ_Dialog", "{z}"))
        self.label_8.setText(_translate("XYZ_Dialog", "zmin:"))
        self.zmin.setText(_translate("XYZ_Dialog", "0"))
        self.label_9.setText(_translate("XYZ_Dialog", "zmax:"))
        self.zmax.setText(_translate("XYZ_Dialog", "12"))
        self.addXYZTileLayer.setText(_translate("XYZ_Dialog", "添加图层"))
