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
        MainWindow.resize(700, 697)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mapWidget = QtWidgets.QWidget(self.centralwidget)
        self.mapWidget.setObjectName("mapWidget")
        self.verticalLayout_2.addWidget(self.mapWidget)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(20)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_4.addWidget(self.line_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_4.addWidget(self.line_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 8, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 2, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_6.addWidget(self.line_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_6.addWidget(self.line_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 3, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEditY = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditY.setObjectName("lineEditY")
        self.horizontalLayout_2.addWidget(self.lineEditY)
        self.openYcsv = QtWidgets.QToolButton(self.centralwidget)
        self.openYcsv.setObjectName("openYcsv")
        self.horizontalLayout_2.addWidget(self.openYcsv)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 6)
        self.horizontalLayout_2.setStretch(2, 2)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 5, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEditX = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditX.setObjectName("lineEditX")
        self.horizontalLayout.addWidget(self.lineEditX)
        self.openXcsv = QtWidgets.QToolButton(self.centralwidget)
        self.openXcsv.setObjectName("openXcsv")
        self.horizontalLayout.addWidget(self.openXcsv)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_7.addWidget(self.line_8)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_7.addWidget(self.line_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 10, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.k_means = QtWidgets.QPushButton(self.centralwidget)
        self.k_means.setObjectName("k_means")
        self.gridLayout.addWidget(self.k_means, 1, 2, 1, 1)
        self.comboBox_NIR = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_NIR.setObjectName("comboBox_NIR")
        self.gridLayout.addWidget(self.comboBox_NIR, 2, 1, 1, 1)
        self.action_countndvi = QtWidgets.QPushButton(self.centralwidget)
        self.action_countndvi.setObjectName("action_countndvi")
        self.gridLayout.addWidget(self.action_countndvi, 2, 2, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.comboBox_R = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_R.setObjectName("comboBox_R")
        self.gridLayout.addWidget(self.comboBox_R, 2, 0, 1, 1)
        self.selectClusterBand = QtWidgets.QComboBox(self.centralwidget)
        self.selectClusterBand.setObjectName("selectClusterBand")
        self.selectClusterBand.addItem("")
        self.selectClusterBand.addItem("")
        self.selectClusterBand.addItem("")
        self.selectClusterBand.addItem("")
        self.gridLayout.addWidget(self.selectClusterBand, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.clusterNumber = QtWidgets.QSpinBox(self.centralwidget)
        self.clusterNumber.setObjectName("clusterNumber")
        self.gridLayout.addWidget(self.clusterNumber, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 9, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 7, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_8.addWidget(self.line_9)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_8.addWidget(self.line_5)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 12, 0, 1, 2)
        self.input_vector_layer = QtWidgets.QComboBox(self.centralwidget)
        self.input_vector_layer.setObjectName("input_vector_layer")
        self.gridLayout_3.addWidget(self.input_vector_layer, 1, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonRender = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRender.setObjectName("pushButtonRender")
        self.gridLayout_2.addWidget(self.pushButtonRender, 1, 2, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.centralwidget)
        self.label_61.setObjectName("label_61")
        self.gridLayout_2.addWidget(self.label_61, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setObjectName("label_42")
        self.gridLayout_2.addWidget(self.label_42, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButtonHis = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHis.setObjectName("pushButtonHis")
        self.gridLayout_2.addWidget(self.pushButtonHis, 0, 2, 1, 1)
        self.demRenderType = QtWidgets.QComboBox(self.centralwidget)
        self.demRenderType.setObjectName("demRenderType")
        self.gridLayout_2.addWidget(self.demRenderType, 1, 1, 1, 1)
        self.pushButtonInfor = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInfor.setObjectName("pushButtonInfor")
        self.gridLayout_2.addWidget(self.pushButtonInfor, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 11, 0, 1, 2)
        self.input_raster_layer = QtWidgets.QComboBox(self.centralwidget)
        self.input_raster_layer.setObjectName("input_raster_layer")
        self.gridLayout_3.addWidget(self.input_raster_layer, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.correlation = QtWidgets.QPushButton(self.centralwidget)
        self.correlation.setObjectName("correlation")
        self.horizontalLayout_3.addWidget(self.correlation)
        self.ImageData = QtWidgets.QPushButton(self.centralwidget)
        self.ImageData.setObjectName("ImageData")
        self.horizontalLayout_3.addWidget(self.ImageData)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 6, 0, 1, 2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(6, -1, 6, -1)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.WFS = QtWidgets.QPushButton(self.centralwidget)
        self.WFS.setObjectName("WFS")
        self.horizontalLayout_9.addWidget(self.WFS)
        self.WMS = QtWidgets.QPushButton(self.centralwidget)
        self.WMS.setObjectName("WMS")
        self.horizontalLayout_9.addWidget(self.WMS)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 13, 0, 1, 2)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 3)
        self.horizontalLayout_11.addLayout(self.gridLayout_3)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 23))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.view = QtWidgets.QMenu(self.menubar)
        self.view.setObjectName("view")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
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
        self.actionAMOLED = QtWidgets.QAction(MainWindow)
        self.actionAMOLED.setObjectName("actionAMOLED")
        self.actionAqua = QtWidgets.QAction(MainWindow)
        self.actionAqua.setObjectName("actionAqua")
        self.actionConsoleStyle = QtWidgets.QAction(MainWindow)
        self.actionConsoleStyle.setObjectName("actionConsoleStyle")
        self.actionElegantDark = QtWidgets.QAction(MainWindow)
        self.actionElegantDark.setObjectName("actionElegantDark")
        self.actionManjaroMix = QtWidgets.QAction(MainWindow)
        self.actionManjaroMix.setObjectName("actionManjaroMix")
        self.actionMaterialDark = QtWidgets.QAction(MainWindow)
        self.actionMaterialDark.setObjectName("actionMaterialDark")
        self.actionUbuntu = QtWidgets.QAction(MainWindow)
        self.actionUbuntu.setObjectName("actionUbuntu")
        self.file.addAction(self.actionopen_file)
        self.file.addAction(self.actionsave)
        self.file.addAction(self.actionsave_as)
        self.view.addAction(self.actionzoom_in)
        self.view.addAction(self.actionzoom_out)
        self.view.addAction(self.actionfull_extent)
        self.view.addAction(self.actionpan)
        self.view.addAction(self.actiondisplay_layers)
        self.menu.addAction(self.actionAMOLED)
        self.menu.addAction(self.actionAqua)
        self.menu.addAction(self.actionConsoleStyle)
        self.menu.addAction(self.actionElegantDark)
        self.menu.addAction(self.actionManjaroMix)
        self.menu.addAction(self.actionMaterialDark)
        self.menu.addAction(self.actionUbuntu)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.view.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MyPYQGIS"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">多光谱影像分析</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">夜光遥感分析</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "矢量图层"))
        self.label_4.setText(_translate("MainWindow", "亮度数据Y"))
        self.openYcsv.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "影像图层"))
        self.label_3.setText(_translate("MainWindow", "GDP数据X"))
        self.openXcsv.setText(_translate("MainWindow", "..."))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">DEM数据分析</span></p></body></html>"))
        self.k_means.setText(_translate("MainWindow", "K均值分类"))
        self.action_countndvi.setText(_translate("MainWindow", "计算植被指数"))
        self.label_41.setText(_translate("MainWindow", "红波段"))
        self.selectClusterBand.setItemText(0, _translate("MainWindow", "全波段"))
        self.selectClusterBand.setItemText(1, _translate("MainWindow", "Red"))
        self.selectClusterBand.setItemText(2, _translate("MainWindow", "Blue"))
        self.selectClusterBand.setItemText(3, _translate("MainWindow", "Green"))
        self.label_5.setText(_translate("MainWindow", "聚类个数："))
        self.label_11.setText(_translate("MainWindow", "近红外波段"))
        self.label_6.setText(_translate("MainWindow", "选择聚类波段："))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">在线地图</span></p></body></html>"))
        self.pushButtonRender.setText(_translate("MainWindow", "渲染"))
        self.label_61.setText(_translate("MainWindow", "数据预览"))
        self.label_42.setText(_translate("MainWindow", "DEM 渲染"))
        self.pushButtonHis.setText(_translate("MainWindow", "高程直方图"))
        self.pushButtonInfor.setText(_translate("MainWindow", "基本信息"))
        self.correlation.setText(_translate("MainWindow", "计算相关系数"))
        self.ImageData.setText(_translate("MainWindow", "影像数据"))
        self.WFS.setText(_translate("MainWindow", "WFS"))
        self.WMS.setText(_translate("MainWindow", "WMS"))
        self.file.setTitle(_translate("MainWindow", "文件"))
        self.view.setTitle(_translate("MainWindow", "视图"))
        self.menu.setTitle(_translate("MainWindow", "主题"))
        self.actionopen_file.setText(_translate("MainWindow", "打开"))
        self.actionsave.setText(_translate("MainWindow", "保存"))
        self.actionsave_as.setText(_translate("MainWindow", "另存为"))
        self.actionzoom_in.setText(_translate("MainWindow", "放大"))
        self.actionzoom_out.setText(_translate("MainWindow", "缩小"))
        self.actionfull_extent.setText(_translate("MainWindow", "全图"))
        self.actionpan.setText(_translate("MainWindow", "平移"))
        self.actionj.setText(_translate("MainWindow", "j"))
        self.action.setText(_translate("MainWindow", "display all"))
        self.actiondisplay_layers.setText(_translate("MainWindow", "全部图层"))
        self.actionAMOLED.setText(_translate("MainWindow", "AMOLED"))
        self.actionAqua.setText(_translate("MainWindow", "Aqua"))
        self.actionConsoleStyle.setText(_translate("MainWindow", "ConsoleStyle"))
        self.actionElegantDark.setText(_translate("MainWindow", "ElegantDark"))
        self.actionManjaroMix.setText(_translate("MainWindow", "ManjaroMix"))
        self.actionMaterialDark.setText(_translate("MainWindow", "MaterialDark"))
        self.actionUbuntu.setText(_translate("MainWindow", "Ubuntu"))
