# -*- coding: utf-8 -*-


import os, sys
from qgis.core import *
from qgis.gui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QFileDialog
from ui.mapView import Ui_MainWindow
from ui.resultView2 import Ui_MainWindow as resultView
import numpy as np
from osgeo import gdal, gdal_array
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
import matplotlib.image as mpimg
import cv2


class ResultWindow(QMainWindow,resultView):
    def __init__(self,pt):
        super(ResultWindow, self).__init__()
        self.setupUi(self)
        self.init_mapcanvas()
        my_path = os.path.dirname(__file__)
        print(my_path)
        print(pt)
        self.fullpath=pt.strip('./')
        full=os.path.join(my_path,self.fullpath)
        self.fullpath=full
        print(self.fullpath)
        if os.path.exists(self.fullpath):
            self.loadMap()
        else: print("error reading file")
        self.slot_connect()

    def init_mapcanvas(self):
        #实例化地图画布
        self.mapCanvas = QgsMapCanvas()
        self.mapCanvas.xyCoordinates.connect(self.show_lonlat)
        self.mapCanvas.setCanvasColor(Qt.white)
        # self.mapCanvas.show()
        layout = QVBoxLayout(self.mapWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.mapCanvas)

    def loadMap(self):
        print(self.fullpath)
        info = QFileInfo(self.fullpath)
        basename = info.baseName()
        suffix = info.suffix()
        print(basename)
        print(suffix)
        if suffix == 'shp':
            print('vector')
            # 打开矢量图层
            self.layer = QgsVectorLayer(self.fullpath, basename, "ogr")
            if not self.layer:
                print("failed")
            # 添加下拉框
        else:
            print('raster')
            # 打开栅格图层
            self.layer = QgsRasterLayer(self.fullpath, basename, "gdal")
            if not self.layer:
                print("failed")
            # 添加下拉框
        # 注册图层
        QgsProject.instance().addMapLayer(self.layer)
        layers = QgsProject.instance().mapLayers()
        layerList = []
        for layer in layers.values():
            print(layer)
            layerList.append(layer)
        print(self.layer)
        print(layerList)
        self.mapCanvas.setLayers(layerList)
        # 设置图层范围
        self.mapCanvas.setExtent(self.layer.extent())
        self.mapCanvas.refresh()
        #self.mmqgis_fill_combo_box_with_layers(self.input_vector_layer, self.input_raster_layer)

    def slot_connect(self):
        self.actionzoom_in.clicked.connect(self.action_zoomin_triggered)
        self.actionzoom_out.clicked.connect(self.action_zoomout_triggered)
        self.actionpan.clicked.connect(self.action_pan_triggered)
        self.actionfull_extent.clicked.connect(self.action_fullextent_triggered)

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
        self.statusbar.showMessage('经度:{x},纬度:{y}')


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
        self.pushButton_3.clicked.connect(self.build_kmeans)

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

    def build_kmeans(self):
        # 没有什么循环，所以做了个假的进度条
        print("当前值为：", self.spinBox.value())
        if self.input_raster_layer.count() == 0:
            print("无矢量图层数据")
            sys.exit(-1)
        self.img = gdal.Open(self.layer.dataProvider().dataSourceUri())
        if self.img is None:
            print("数据加载失败")
            sys.exit(-1)
        self.status.setValue(0)
        print(self.img.RasterYSize)
        self.status.setMaximum(100)

        print(self.comboBox.currentText())
        if self.comboBox.currentText() == "全波段":
            self.tmpimg = np.zeros((self.img.RasterYSize, self.img.RasterXSize, self.img.RasterCount),
                                   gdal_array.GDALTypeCodeToNumericTypeCode(self.img.GetRasterBand(1).DataType))
            j = 0
            for b in range(self.tmpimg.shape[2]):
                self.tmpimg[:, :, b] = self.img.GetRasterBand(b+1).ReadAsArray()
                self.status.setValue(b)
                j = b
            self.new_shape = (self.tmpimg.shape[0] * self.tmpimg.shape[1], self.tmpimg.shape[2])
            x = self.tmpimg[:, :, :13].reshape(self.new_shape)
            print("1")
            if self.spinBox.value() == 0:
                print("聚类数不可为0")
                sys.exit(-1)
            k_means = KMeans(n_clusters=self.spinBox.value())
            k_means.fit(x)
            self.status.setValue(99)
            # for j in range(30, 78):
            #     self.progressBar.setValue(j)
            #     j = j + 1
            x_cluster = k_means.labels_
            x_cluster = x_cluster.reshape(self.tmpimg[:, :, 0].shape)
        elif self.comboBox.currentText() == "波段1":
            band = self.img.GetRasterBand(1)
            self.tmpimg = band.ReadAsArray()
            x = self.tmpimg.reshape((-1, 1))
            if self.spinBox.value() == 0:
                print("聚类数不可为0")
                sys.exit(-1)
            self.status.setValue(84)
            k_means = KMeans(n_clusters=self.spinBox.value())
            k_means.fit(x)
            # for j in range(30, 78):
            #     self.progressBar.setValue(j)
            #     j = j + 1
            x_cluster = k_means.labels_
            self.status.setValue(96)
            x_cluster = x_cluster.reshape(self.tmpimg.shape)
        elif self.comboBox.currentText() == "波段2":
            band = self.img.GetRasterBand(2)
            self.tmpimg = band.ReadAsArray()
            self.status.setValue(77)
            x = self.tmpimg.reshape((-1, 1))
            if self.spinBox.value() == 0:
                print("聚类数不可为0")
                sys.exit(-1)
            k_means = KMeans(n_clusters=self.spinBox.value())
            k_means.fit(x)
            # for j in range(30, 78):
            #     self.progressBar.setValue(j)
            #     j = j + 1
            x_cluster = k_means.labels_
            self.status.setValue(93)
            x_cluster = x_cluster.reshape(self.tmpimg.shape)
        else:
            band = self.img.GetRasterBand(3)
            self.tmpimg = band.ReadAsArray()
            x = self.tmpimg.reshape((-1, 1))
            if self.spinBox.value() == 0:
                print("聚类数不可为0")
                sys.exit(-1)
            k_means = KMeans(n_clusters=self.spinBox.value())
            k_means.fit(x)
            # for j in range(30, 78):
            #     self.progressBar.setValue(j)
            #     j = j + 1
            x_cluster = k_means.labels_
            x_cluster = x_cluster.reshape(self.tmpimg.shape)

        cv2.imwrite('generated.tif', x_cluster)
        # self.progressBar.setValue(99)
        self.resultwindow = ResultWindow('generated.tif')
        self.status.setValue(100)
        # resultwindow.fullpath=outFilePath
        self.resultwindow.show()


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
    main()