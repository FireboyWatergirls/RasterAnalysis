import os, sys,struct
from qgis.core import *
from qgis.gui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QFileDialog,QMessageBox
from ui.mapView import Ui_MainWindow
from ui.resultView2 import Ui_MainWindow as resultView
#from ui.resultView import Ui_Dialog
from osgeo import gdal
from RasterPlugin_webLayer import *

#w问题：如果有多个图层，是只显示选项框里的图层还是全部显示？
##扩展部分
##1 栅格运算：添加计算器
##2 弹出窗口显示结果

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
