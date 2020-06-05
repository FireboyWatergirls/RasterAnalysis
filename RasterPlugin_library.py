# -*- coding: utf-8 -*-


import os, sys

from PyQt5.QtGui import QColor
from qgis.core import *
from qgis.gui import *
from PyQt5.QtCore import Qt, QFileInfo, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QFileDialog

from DEM_Information import DEMInformation
from ui.mapView import Ui_MainWindow

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy


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
        self.pushButton_8.clicked.connect(self.action_show_information)
        self.pushButton_9.clicked.connect(self.action_render_dem)
        self.pushButton_5.clicked.connect(self.action_cal_slope)

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
        self.basename=info.baseName()
        suffix=info.suffix()
        print(suffix)
        if suffix == 'shp':
            print('vector')
            # 打开矢量图层
            self.layer = QgsVectorLayer(fullpath, self.basename, "ogr")
            if not self.layer:
                print("failed")
            # 添加下拉框
        else:
            print('raster')
            #打开栅格图层
            self.layer = QgsRasterLayer(fullpath, self.basename,"gdal")
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
        print('layerList', layerList)
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

    def action_show_information(self):
        self.dem_dialog = DEMInformation()
        self.dem_dialog.textName.setText(self.basename)
        self.dem_dialog.textWidth.setText(str(self.layer.width()))
        self.dem_dialog.textHeight.setText(str(self.layer.height()))
        self.dem_dialog.textExtent.setText(self.layer.extent().toString())
        self.dem_dialog.show()

        p = self.layer.dataProvider()
        p.initHistogram(QgsRasterHistogram(), 1, 100)
        h = p.histogram(1)
        print('最大值，最小值', h.maximum, h.minimum)
        array = h.histogramVector
        print(len(array))
        index = numpy.arange(h.minimum, h.maximum + 1, 1)
        print(len(index))
        plt.bar(index, array)
        plt.show()

    def action_render_dem(self):
        p = self.layer.dataProvider()
        p.initHistogram(QgsRasterHistogram(), 1, 100)
        h = p.histogram(1)
        maxh = h.maximum
        minh = h.minimum

        input_layer = self.layer
        fcn = QgsColorRampShader()
        fcn.setColorRampType(QgsColorRampShader.Interpolated)
        lst = [QgsColorRampShader.ColorRampItem(minh, QColor(0, 255, 0)),
               QgsColorRampShader.ColorRampItem(maxh, QColor(255, 255, 0))]
        fcn.setColorRampItemList(lst)
        shader = QgsRasterShader()
        shader.setRasterShaderFunction(fcn)
        renderer = QgsSingleBandPseudoColorRenderer(input_layer.dataProvider(), 1, shader)
        input_layer.setRenderer(renderer)
        input_layer.triggerRepaint()

        self.single_band_pseudo_color_renderer_widget = QgsSingleBandPseudoColorRendererWidget(
            input_layer
        )
        self.single_band_pseudo_color_renderer_widget.show()

    def action_cal_slope(self):
        print("cal_slope")
def main():
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
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