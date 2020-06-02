# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WFS.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WFS_Dialog(object):
    def setupUi(self, WFS_Dialog):
        WFS_Dialog.setObjectName("WFS_Dialog")
        WFS_Dialog.resize(375, 335)
        self.URI = QtWidgets.QLineEdit(WFS_Dialog)
        self.URI.setGeometry(QtCore.QRect(150, 20, 113, 20))
        self.URI.setObjectName("URI")
        self.label = QtWidgets.QLabel(WFS_Dialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 31, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(WFS_Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(WFS_Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 90, 51, 21))
        self.label_3.setObjectName("label_3")
        self.service = QtWidgets.QLineEdit(WFS_Dialog)
        self.service.setGeometry(QtCore.QRect(150, 90, 113, 20))
        self.service.setObjectName("service")
        self.version = QtWidgets.QLineEdit(WFS_Dialog)
        self.version.setGeometry(QtCore.QRect(150, 130, 113, 20))
        self.version.setObjectName("version")
        self.label_4 = QtWidgets.QLabel(WFS_Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 130, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(WFS_Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 170, 54, 12))
        self.label_5.setObjectName("label_5")
        self.request = QtWidgets.QLineEdit(WFS_Dialog)
        self.request.setGeometry(QtCore.QRect(150, 170, 113, 20))
        self.request.setObjectName("request")
        self.label_6 = QtWidgets.QLabel(WFS_Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 210, 54, 12))
        self.label_6.setObjectName("label_6")
        self.typename_2 = QtWidgets.QLineEdit(WFS_Dialog)
        self.typename_2.setGeometry(QtCore.QRect(150, 210, 113, 20))
        self.typename_2.setObjectName("typename_2")
        self.label_7 = QtWidgets.QLabel(WFS_Dialog)
        self.label_7.setGeometry(QtCore.QRect(80, 250, 54, 12))
        self.label_7.setObjectName("label_7")
        self.srsname = QtWidgets.QLineEdit(WFS_Dialog)
        self.srsname.setGeometry(QtCore.QRect(150, 250, 113, 20))
        self.srsname.setObjectName("srsname")
        self.addWFSLayer = QtWidgets.QPushButton(WFS_Dialog)
        self.addWFSLayer.setGeometry(QtCore.QRect(150, 290, 75, 23))
        self.addWFSLayer.setObjectName("addWFSLayer")

        self.retranslateUi(WFS_Dialog)
        QtCore.QMetaObject.connectSlotsByName(WFS_Dialog)

    def retranslateUi(self, WFS_Dialog):
        _translate = QtCore.QCoreApplication.translate
        WFS_Dialog.setWindowTitle(_translate("WFS_Dialog", "Dialog"))
        self.URI.setText(_translate("WFS_Dialog", "http://localhost:8080/geoserver/nyc_roads/ows?"))
        self.label.setText(_translate("WFS_Dialog", "URI:"))
        self.label_2.setText(_translate("WFS_Dialog", "参数：:"))
        self.label_3.setText(_translate("WFS_Dialog", "service:"))
        self.service.setText(_translate("WFS_Dialog", "WFS"))
        self.version.setText(_translate("WFS_Dialog", "1.0.0"))
        self.label_4.setText(_translate("WFS_Dialog", "version:"))
        self.label_5.setText(_translate("WFS_Dialog", "request:"))
        self.request.setText(_translate("WFS_Dialog", "GetFeature"))
        self.label_6.setText(_translate("WFS_Dialog", "typename:"))
        self.typename_2.setText(_translate("WFS_Dialog", "nyc_roads:nyc_roads"))
        self.label_7.setText(_translate("WFS_Dialog", "srsname:"))
        self.srsname.setText(_translate("WFS_Dialog", "EPSG:2908"))
        self.addWFSLayer.setText(_translate("WFS_Dialog", "添加图层"))
