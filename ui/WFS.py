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
        WFS_Dialog.resize(321, 261)
        self.verticalLayoutWidget = QtWidgets.QWidget(WFS_Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 241, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 0, 5, 10)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(10)
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
        self.service = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.service.setObjectName("service")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.service)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.version = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.version.setObjectName("version")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.version)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.request = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.request.setObjectName("request")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.request)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.typename_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.typename_2.setObjectName("typename_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.typename_2)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.srsname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.srsname.setObjectName("srsname")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.srsname)
        self.addWFSLayer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addWFSLayer.setObjectName("addWFSLayer")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.addWFSLayer)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(WFS_Dialog)
        QtCore.QMetaObject.connectSlotsByName(WFS_Dialog)

    def retranslateUi(self, WFS_Dialog):
        _translate = QtCore.QCoreApplication.translate
        WFS_Dialog.setWindowTitle(_translate("WFS_Dialog", "Dialog"))
        self.label.setText(_translate("WFS_Dialog", "URI:"))
        self.URI.setText(_translate("WFS_Dialog", "http://localhost:8080/geoserver/nyc_roads/ows?"))
        self.label_3.setText(_translate("WFS_Dialog", "service:"))
        self.service.setText(_translate("WFS_Dialog", "WFS"))
        self.label_4.setText(_translate("WFS_Dialog", "version:"))
        self.version.setText(_translate("WFS_Dialog", "1.0.0"))
        self.label_5.setText(_translate("WFS_Dialog", "request:"))
        self.request.setText(_translate("WFS_Dialog", "GetFeature"))
        self.label_6.setText(_translate("WFS_Dialog", "typename:"))
        self.typename_2.setText(_translate("WFS_Dialog", "nyc_roads:nyc_roads"))
        self.label_7.setText(_translate("WFS_Dialog", "srsname:"))
        self.srsname.setText(_translate("WFS_Dialog", "EPSG:2908"))
        self.addWFSLayer.setText(_translate("WFS_Dialog", "添加图层"))
