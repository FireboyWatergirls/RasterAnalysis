# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mapWidget = QtWidgets.QWidget(self.centralwidget)
        self.mapWidget.setGeometry(QtCore.QRect(80, 10, 321, 461))
        self.mapWidget.setObjectName("mapWidget")
        self.input_raster_layer = QtWidgets.QComboBox(self.centralwidget)
        self.input_raster_layer.setGeometry(QtCore.QRect(502, 30, 161, 22))
        self.input_raster_layer.setObjectName("input_raster_layer")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(432, 30, 51, 21))
        self.label.setObjectName("label")
        self.input_vector_layer = QtWidgets.QComboBox(self.centralwidget)
        self.input_vector_layer.setGeometry(QtCore.QRect(502, 60, 161, 22))
        self.input_vector_layer.setObjectName("input_vector_layer")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(432, 60, 51, 20))
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(432, 100, 61, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(562, 230, 101, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(432, 200, 51, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(432, 300, 61, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.action_countndvi = QtWidgets.QPushButton(self.centralwidget)
        self.action_countndvi.setGeometry(QtCore.QRect(562, 260, 101, 23))
        self.action_countndvi.setObjectName("action_countndvi")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(432, 370, 61, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(492, 330, 101, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.WFS = QtWidgets.QPushButton(self.centralwidget)
        self.WFS.setGeometry(QtCore.QRect(432, 400, 101, 23))
        self.WFS.setObjectName("WFS")
        self.WMS = QtWidgets.QPushButton(self.centralwidget)
        self.WMS.setGeometry(QtCore.QRect(552, 400, 101, 23))
        self.WMS.setObjectName("WMS")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(-10, 480, 462, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(492, 100, 101, 21))
        self.label_7.setObjectName("label_7")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(592, 100, 71, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(432, 230, 51, 21))
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(492, 230, 51, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(492, 200, 101, 20))
        self.label_8.setObjectName("label_8")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(602, 200, 61, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(432, 130, 51, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(492, 130, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(622, 130, 41, 21))
        self.toolButton.setObjectName("toolButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(432, 160, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.ImageData = QtWidgets.QPushButton(self.centralwidget)
        self.ImageData.setGeometry(QtCore.QRect(562, 160, 101, 23))
        self.ImageData.setObjectName("ImageData")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(492, 300, 101, 20))
        self.label_9.setObjectName("label_9")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(592, 300, 71, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(492, 370, 101, 20))
        self.label_10.setObjectName("label_10")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(592, 370, 71, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.comboBox_R = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_R.setGeometry(QtCore.QRect(422, 261, 60, 22))
        self.comboBox_R.setObjectName("comboBox_R")
        self.comboBox_NIR = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_NIR.setGeometry(QtCore.QRect(492, 261, 60, 22))
        self.comboBox_NIR.setObjectName("comboBox_NIR")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(439, 280, 31, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 280, 51, 20))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 23))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.view = QtWidgets.QMenu(self.menubar)
        self.view.setObjectName("view")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen_file = QtWidgets.QAction(MainWindow)
        self.actionopen_file.setObjectName("actionopen_file")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionsave_as = QtWidgets.QAction(MainWindow)
        self.actionsave_as.setObjectName("actionsave_as")
        self.actionzoom_in = QtWidgets.QAction(MainWindow)
        self.actionzoom_in.setObjectName("actionzoom_in")
        self.actionzoom_out = QtWidgets.QAction(MainWindow)
        self.actionzoom_out.setObjectName("actionzoom_out")
        self.actionfull_extent = QtWidgets.QAction(MainWindow)
        self.actionfull_extent.setObjectName("actionfull_extent")
        self.actionpan = QtWidgets.QAction(MainWindow)
        self.actionpan.setObjectName("actionpan")
        self.actionj = QtWidgets.QAction(MainWindow)
        self.actionj.setObjectName("actionj")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actiondisplay_layers = QtWidgets.QAction(MainWindow)
        self.actiondisplay_layers.setObjectName("actiondisplay_layers")
        self.file.addAction(self.actionopen_file)
        self.file.addAction(self.actionsave)
        self.file.addAction(self.actionsave_as)
        self.view.addAction(self.actionzoom_in)
        self.view.addAction(self.actionzoom_out)
        self.view.addAction(self.actionfull_extent)
        self.view.addAction(self.actionpan)
        self.view.addAction(self.actiondisplay_layers)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.view.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MyPYQGIS"))
        self.label.setText(_translate("MainWindow", "影像图层"))
        self.label_2.setText(_translate("MainWindow", "矢量图层"))
        self.pushButton_3.setText(_translate("MainWindow", "K均值分类"))
        self.action_countndvi.setText(_translate("MainWindow", "计算植被指数"))
        self.pushButton_5.setText(_translate("MainWindow", "计算坡度"))
        self.WFS.setText(_translate("MainWindow", "WFS"))
        self.WMS.setText(_translate("MainWindow", "WMS"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">夜光遥感分析</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "聚类个数"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">多光谱影像分析</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "GDP数据"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.pushButton_2.setText(_translate("MainWindow", "计算相关系数"))
        self.ImageData.setText(_translate("MainWindow", "影像数据"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">DEM数据分析</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">前端显示</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "红波段"))
        self.label_6.setText(_translate("MainWindow", "近红外波段"))
        self.file.setTitle(_translate("MainWindow", "文件"))
        self.view.setTitle(_translate("MainWindow", "视图"))
        self.actionopen_file.setText(_translate("MainWindow", "open file"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave_as.setText(_translate("MainWindow", "save as"))
        self.actionzoom_in.setText(_translate("MainWindow", "zoom in"))
        self.actionzoom_out.setText(_translate("MainWindow", "zoom out"))
        self.actionfull_extent.setText(_translate("MainWindow", "full extent"))
        self.actionpan.setText(_translate("MainWindow", "pan"))
        self.actionj.setText(_translate("MainWindow", "j"))
        self.action.setText(_translate("MainWindow", "display all"))
        self.actiondisplay_layers.setText(_translate("MainWindow", "display layers"))
