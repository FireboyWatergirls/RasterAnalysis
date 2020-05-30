# -*- coding: utf-8 -*-


import os, sys
from qgis.core import QgsProject, QgsApplication, QgsVectorLayer, QgsRasterLayer,QgsMapLayer
from qgis.gui import QgsMapCanvas, QgsMapToolPan, QgsMapToolZoom, QgsMapToolIdentify
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QFileDialog
from ui.mapView import Ui_MainWindow


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
        else:
            print('raster')
            #打开栅格图层
            self.layer = QgsRasterLayer(fullpath, basename,"gdal")
            if not self.layer:
                print("failed")
        # 注册图层
        QgsProject.instance().addMapLayer(self.layer)
        self.mapCanvas.setLayers([self.layer])
        #设置图层范围
        self.mapCanvas.setExtent(self.layer.extent())
        self.mapCanvas.refresh()

        #layers = QgsProject.instance().mapLayers()
        #print(layers)
        #for layer in layers:
            #print(layer.name())
        #self.mmqgis_fill_combo_box_with_vector_layers(self.input_vector_layer)

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

    def mmqgis_fill_combo_box_with_vector_layers(self, combo_box):
        # Add layers not in the combo box
        print('0')
        for layer in self.iface.mapCanvas().layers():
            print('1')
            if layer.type() == QgsMapLayer.VectorLayer:
                print('2')
                if combo_box.findText(layer.name()) < 0:
                    print('3')
                    combo_box.addItem(layer.name())
                    if layer in self.iface.layerTreeView().selectedLayers():
                        combo_box.setCurrentIndex(combo_box.count() - 1)

        # Remove layers no longer on the map
        removed = []
        for index in range(combo_box.count()):
            found = False
            for layer in self.iface.mapCanvas().layers():
                if layer.name() == combo_box.itemText(index):
                    found = True
                    break
            if not found:
                removed.append(index)

        removed.reverse()
        for index in removed:
            combo_box.removeItem(index)

    def mmqgis_fill_combo_box_with_raster_layers(self, combo_box):
        # Add layers not in the combo box
        for layer in self.iface.mapCanvas().layers():
            if layer.type() == QgsMapLayer.RasterLayer:
                if combo_box.findText(layer.name()) < 0:
                    combo_box.addItem(layer.name())
                    if layer in self.iface.layerTreeView().selectedLayers():
                        print('4')
                        combo_box.setCurrentIndex(combo_box.count() - 1)

        # Remove layers no longer on the map
        removed = []
        for index in range(combo_box.count()):
            found = False
            for layer in self.iface.mapCanvas().layers():
                if layer.name() == combo_box.itemText(index):
                    found = True
                    break
            if not found:
                removed.append(index)

        removed.reverse()
        for index in removed:
            combo_box.removeItem(index)



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