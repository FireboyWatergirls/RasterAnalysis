# -*- coding: utf-8 -*-


import os, sys
from qgis.core import *
from qgis.gui import *
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QFileDialog, QGridLayout, QWidget, QLabel,QDialog
from ui.mapView import Ui_MainWindow

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class PlotLinear(QMainWindow):
    def __init__(self):
        super(PlotLinear, self).__init__()
        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.ax1 = self.figure1.add_subplot(111)

        self.xishu_label = QLabel('相关系数：')

        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.statusBar().showMessage(' ')
        self._main_layout = QGridLayout()
        self.widget.setLayout(self._main_layout)
        self._main_layout.addWidget(self.canvas1, 0, 0)
        self._main_layout.addWidget(self.xishu_label, 1, 0, 1, -1)

        self.setFixedSize(self.sizeHint())
        self.show()

    def plot(self, x, y, X, Y):
        self.ax1.plot(x, y, 'k.')
        self.ax1.plot(X, Y)
        self.canvas1.draw()
        x_temp = pd.DataFrame()
        x_temp['x'] = [i[0] for i in x]
        x_temp['y'] = [i[0] for i in y]
        self.xishu_label.setText('相关系数：'+str(x_temp[u'x'].corr(x_temp[u'y'])))


class MapExplorer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MapExplorer, self).__init__()
        self.setupUi(self)

        self.init_mapcanvas()
        self.slot_connect()
    #信号和槽的连接
    def slot_connect(self):
        self.actionopen_file.triggered.connect(self.action_open_triggered)
        self.actionzoom_in.triggered.connect(self.action_zoomin_triggered)
        self.actionzoom_out.triggered.connect(self.action_zoomout_triggered)
        self.actionpan.triggered.connect(self.action_pan_triggered)
        self.actionfull_extent.triggered.connect(self.action_fullextent_triggered)
        self.actionsave.triggered.connect(self.action_save_triggered)
        self.openXcsv.clicked.connect(self.open_gdp)
        self.openYcsv.clicked.connect(self.open_light)
        self.correlation.clicked.connect(self.linear_regression)

    def open_gdp(self):
        fullpath, format = QFileDialog.getOpenFileNames(self, '打开数据', '',
                                                       '*.csv')
        gdp_data_temp = pd.read_csv(fullpath[0], encoding='gbk').to_dict(orient='index')
        years = None
        for i in gdp_data_temp[0].keys():
            if i != '地区' and 'Unnamed' not in i:
                years = i
                break
        if years is None:
            print('数据有问题！')
        else:
            self.gdp_dict = {}
            for i in range(31):
                self.gdp_dict[gdp_data_temp[i]['地区']] = gdp_data_temp[i][years]

    def open_light(self):
        fullpath, format = QFileDialog.getOpenFileNames(self, '打开数据', '',
                                                        '*.csv')
        light_data_temp = pd.read_csv(fullpath[0], encoding='gbk').to_dict(orient='index')
        self.light_dict = {}
        for i in range(31):
            self.light_dict[light_data_temp[i]['地区']] = light_data_temp[i]['亮度']

    def linear_regression(self):
        # self.light_dict和self.gdp_dict都是{城市名:值}
        data = []
        for k, v in self.gdp_dict.items():
            data.append([v, self.light_dict[k]])
        # data.sort()
        x = []
        y = []
        for i in data:
            x.append([i[0]])
            y.append([i[1]])
        reg = LinearRegression()
        reg.fit(x, y)
        X = list(range(int(min([i[0] for i in x])), int(max([i[0] for i in x]))))
        Y = reg.predict(np.reshape(X, (-1, 1)))
        self.plot_widget = PlotLinear()
        self.plot_widget.plot(x, y, X, Y)

    def init_mapcanvas(self):
        #实例化地图画布
        self.mapCanvas = QgsMapCanvas()
        self.mapCanvas.xyCoordinates.connect(self.show_lonlat)
        self.mapCanvas.setCanvasColor(Qt.white)
        # self.mapCanvas.show()
        layout = QVBoxLayout(self.mapWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.mapCanvas)

    def loadMap(self, fullpath):
        print(fullpath)
        info=QFileInfo(fullpath)
        basename=info.baseName()
        suffix=info.suffix()
        print(basename)
        print(suffix)
        if suffix == 'shp':
            print('vector')
            # 打开矢量图层
            self.layer = QgsVectorLayer(fullpath, basename, "ogr")
            if not self.layer:
                print("failed")
            # 添加下拉框
        else:
            print('raster')
            #打开栅格图层
            self.layer = QgsRasterLayer(fullpath, basename,"gdal")
            if not self.layer:
                print("failed")
            # 添加下拉框
        # 注册图层
        QgsProject.instance().addMapLayer(self.layer)
        layers=QgsProject.instance().mapLayers()
        layerList=[]
        for layer in layers.values():
            print(layer)
            layerList.append(layer)
        print(self.layer)
        print(layerList)
        self.mapCanvas.setLayers(layerList)
        #设置图层范围
        self.mapCanvas.setExtent(self.layer.extent())
        self.mapCanvas.refresh()
        self.mmqgis_fill_combo_box_with_layers(self.input_vector_layer,self.input_raster_layer)

    def action_open_triggered(self):
        fullpath, format = QFileDialog.getOpenFileName(self, '打开数据', '', '*.shp;;remote sensing image(*.tif *.tiff);;image(*.jpg *.jpeg *.png *.bmp)')
        if os.path.exists(fullpath):
            self.loadMap(fullpath)

    def action_save_triggered(self):
        fullpath,format = QFileDialog.getSaveFileName(self,'保存数据','','*.tif')
        self.mapCanvas.saveAsImage(fullpath)

    def action_zoomin_triggered(self):
        self.maptool = QgsMapToolZoom(self.mapCanvas, False)
        self.mapCanvas.setMapTool(self.maptool)

    def action_zoomout_triggered(self):
        self.maptool = QgsMapToolZoom(self.mapCanvas, True)
        self.mapCanvas.setMapTool(self.maptool)

    def action_pan_triggered(self):
        self.maptool = QgsMapToolPan(self.mapCanvas)
        self.mapCanvas.setMapTool(self.maptool)

    def action_fullextent_triggered(self):
        self.mapCanvas.setExtent(self.layer.extent())
        self.mapCanvas.refresh()
    #显示鼠标点的经纬度信息
    def show_lonlat(self, point):
        x = point.x()
        y = point.y()
        self.statusbar.showMessage(f'经度:{x},纬度:{y}')

    def mmqgis_fill_combo_box_with_layers(self,combo_box_vector, combo_box_raster):
        # Add layers not in the combo box
        for layer in self.mapCanvas.layers():
            if layer.type() == QgsMapLayer.VectorLayer:
                if combo_box_vector.findText(layer.name()) < 0:
                    combo_box_vector.addItem(layer.name())
                    #if layer in QgsLayerTreeView().selectedLayers():
                        #combo_box.setCurrentIndex(combo_box.count() - 1)

        # Remove layers no longer on the map
        removed = []
        for index in range(combo_box_vector.count()):
            print("2")
            found = False
            for layer in self.mapCanvas.layers():
                if layer.name() == combo_box_vector.itemText(index):
                    found = True
                    break
            if not found:
                removed.append(index)

        removed.reverse()
        for index in removed:
            combo_box_vector.removeItem(index)

        # Add layers not in the combo box
        for layer in self.mapCanvas.layers():
            if layer.type() == QgsMapLayer.RasterLayer:
                if combo_box_raster.findText(layer.name()) < 0:
                    combo_box_raster.addItem(layer.name())
                    # if layer in QgsLayerTreeView().selectedLayers():
                    # combo_box.setCurrentIndex(combo_box.count() - 1)

        # Remove layers no longer on the map
        removed = []
        for index in range(combo_box_raster.count()):
            print("2")
            found = False
            for layer in self.mapCanvas.layers():
                if layer.name() == combo_box_raster.itemText(index):
                    found = True
                    break
            if not found:
                removed.append(index)

        removed.reverse()
        for index in removed:
            combo_box_raster.removeItem(index)



def main():
    qgs = QgsApplication([], True)
    qgs.setPrefixPath('qgis', True)
    #启动QGIS
    qgs.initQgis()

    window = MapExplorer()
    window.show()

    exit_code = qgs.exec_()
    #退出QGIS
    qgs.exitQgis()
    sys.exit(exit_code)


if __name__ == '__main__':
    import cgitb
    cgitb.enable(format='text')
    main()