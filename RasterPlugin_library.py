# -*- coding: utf-8 -*-


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
from RasterPlugin_showNDVI import *
from RasterPlugin_RasterData import *

#w问题：如果有多个图层，是只显示选项框里的图层还是全部显示？
##扩展部分
##1 栅格运算：添加计算器
##2 弹出窗口显示结果

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
        self.actiondisplay_layers.triggered.connect(self.action_display_layers)
        self.actionsave.triggered.connect(self.action_save_triggered)
        self.action_countndvi.clicked.connect(self.action_count_ndvi_triggered)
        self.input_vector_layer.activated.connect(lambda :self.action_change_layer(1))
        self.input_raster_layer.activated.connect(lambda :self.action_change_layer(0))
        self.WFS.clicked.connect(self.open_WFS_dialog)
        self.WMS.clicked.connect(self.open_WMS_dialog)
        self.pushButton.clicked.connect(self.RasterData)

    def onCountChanged(self, value):
        self.progressBar.setValue(value)

    def createOutputImage(self, outFilename, inDataset):
        # Define the image driver to be used
        # This defines the output file format (e.g., GeoTiff)
        driver = gdal.GetDriverByName("GTiff")
        # Check that this driver can create a new file.
        metadata = driver.GetMetadata()

        # Get the spatial information from the input file
        geoTransform = inDataset.GetGeoTransform()
        geoProjection = inDataset.GetProjection()
        # Create an output file of the same size as the inputted
        # image, but with only 1 output image band.
        newDataset = driver.Create(outFilename, inDataset.RasterXSize, inDataset.RasterYSize, 1, gdal.GDT_Float32)
        # Define the spatial information for the new image.
        newDataset.SetGeoTransform(geoTransform)
        newDataset.SetProjection(geoProjection)
        return newDataset

    def action_count_ndvi_triggered(self):
        #the function runs a counter thread ( a separate thread)
        print("ndvi")
        self.progressBar.setValue(0)
        #countChanged = pyqtSignal(int)
        #countChanged.connect(self.onCountChanged)
        #combox_R
        #combox_NIR
        print("action_ndvi triggered")
        if self.input_raster_layer.count() == 0:
            print("input_raster = 0")
            msg = QMessageBox()
            print("set msgbox")
            #msg.setIcon(QMessageBox.critical)
            msg.setText("cannot calculate NDVI")
           # msg.setInformativeText("This is additional information")
            msg.setWindowTitle("Error")
            msg.setDetailedText("Please import at least one raster layer")
            msg.setStandardButtons(QMessageBox.Ok)
            returnValue = msg.exec()
            if returnValue == QMessageBox.Ok:
                print('OK clicked')
            return


        outFilePath="./ndvi.tif"
        #可以改的一个地方
        #curLayer= self.input_raster_layer.currentText()
        #layer= QgsProject.instance().mapLayersByName(curLayer)[0]
        #dataset = gdal.Open(layer.dataProvider().dataSourceUri()) 
        #添加可选择波段
        #for i in range(self.rasterDataset.RasterCount):
        #   self.comboBox_R.addItem(str(i))
        #   self.comboBox_NIR.addItem(str(i))
        #self.comboBox_R.addItems(["1","2","3","4"])
        #self.comboBox_NIR.addItems(["1","2","3","4"])

        if self.rasterDataset is None:
            print("The dataset could not opened")
            sys.exit(-1)

            # Create the output dataset
        outDataset = self.createOutputImage(outFilePath, self.rasterDataset)
        # Check the datasets was successfully created.
        if outDataset is None:
            print('Could not create output image')
            sys.exit(-1)

        # Get hold of the RED and NIR image bands from the image
        # Note that the image bands have been hard coded
        # in this case for the Landsat sensor. RED = 3
        # and NIR = 4 this might need to be changed if
        # data from another sensor was used.

        red_band_ind = int(self.comboBox_R.currentText())
        nir_band_ind = int(self.comboBox_NIR.currentText())
        red_band = self.rasterDataset.GetRasterBand(red_band_ind )  # RED BAND
        nir_band = self.rasterDataset.GetRasterBand(nir_band_ind)  # NIR BAND
        # Retrieve the number of lines within the image
        numLines = red_band.YSize
        # Loop through each line in turn.

        self.progressBar.setMaximum(numLines)
        j=0
        for line in range(numLines):
            self.progressBar.setValue(j)
            # Define variable for output line.
            outputLine = bytearray()
            # outputLine=struct.pack('s',outputLines)
            # Read in data for the current line from the
            # image band representing the red wavelength
            red_scanline = red_band.ReadRaster(0, line, red_band.XSize, 1, \
                                               red_band.XSize, 1, gdal.GDT_Float32)
            # Unpack the line of data to be read as floating point data
            red_tuple = struct.unpack('f' * red_band.XSize, red_scanline)

            # Read in data for the current line from the
            # image band representing the NIR wavelength
            nir_scanline = nir_band.ReadRaster(0, line, nir_band.XSize, 1, \
                                               nir_band.XSize, 1, gdal.GDT_Float32)
            # Unpack the line of data to be read as floating point data
            nir_tuple = struct.unpack('f' * nir_band.XSize, nir_scanline)

            # Loop through the columns within the image
            #self.progressBar.setValue(0)

            for i in range(len(red_tuple)):
                # Calculate the NDVI for the current pixel.
                ndvi_lower = (nir_tuple[i] + red_tuple[i])
                ndvi_upper = (nir_tuple[i] - red_tuple[i])
                ndvi = 0
                # Be careful of zero divide
                if ndvi_lower == 0:
                    ndvi = 0
                else:
                    ndvi = ndvi_upper / ndvi_lower
                    # Add the current pixel to the output line
                # outputLine = outputLine + struct.pack('f', ndvi)
                outputLine.extend(struct.pack('f', ndvi))
                # Write the completed line to the output image
            outDataset.GetRasterBand(1).WriteRaster(0, line, red_band.XSize, 1, \
                                                    bytes(outputLine), buf_xsize=red_band.XSize,
                                                    buf_ysize=1, buf_type=gdal.GDT_Float32)
            j=j+1

            # Delete the output line following write
        del outputLine
        self.progressBar.setValue(j)
        print('NDVI Calculated and Outputted to File')
        del outDataset

        self.resultwindow = ResultWindow(outFilePath)
        #resultwindow.fullpath=outFilePath
        self.resultwindow.show()


        #t弹出新的窗口 显示图层！

    def init_mapcanvas(self):
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
        if suffix == 'shp':
            # 打开矢量图层
            self.layer = QgsVectorLayer(fullpath, basename, "ogr")
            if not self.layer:
                print("failed")
            # 添加下拉框
        else:
            #打开栅格图层
            self.layer = QgsRasterLayer(fullpath, basename,"gdal")
            if not self.layer:
                print("failed")
            # 添加下拉框
            self.fill_combo_box_band()
        # 注册图层
        QgsProject.instance().addMapLayer(self.layer)
        layers=QgsProject.instance().mapLayers()
        layerList=[]
        for layer in layers.values():
            layerList.append(layer)
        self.mapCanvas.setLayers(layerList)
        #设置图层范围
        self.mapCanvas.setExtent(self.layer.extent())
        self.mapCanvas.refresh()
        self.fill_combo_box_with_layers(self.input_vector_layer,self.input_raster_layer)
        #curLayer = self.input_raster_layer.currentText()
        #layer = QgsProject.instance().mapLayersByName(curLayer)[0]


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

    def action_display_layers(self):
        layers = QgsProject.instance().mapLayers()
        layerList = []
        for layer in layers.values():
            layerList.append(layer)
        self.mapCanvas.setLayers(layerList)
        # 设置图层范围
        self.mapCanvas.setExtent(self.layer.extent())
        self.mapCanvas.refresh()

    #显示鼠标点的经纬度信息
    def show_lonlat(self, point):
        x = point.x()
        y = point.y()
        self.statusbar.showMessage(f'经度:{x},纬度:{y}')

    def fill_combo_box_with_layers(self,combo_box_vector, combo_box_raster):
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

        if self.layer.type() == QgsMapLayer.RasterLayer:
            combo_box_raster.setCurrentText(self.layer.name())
        else:
            combo_box_vector.setCurrentText(self.layer.name())

    def fill_combo_box_band(self):
        self.rasterDataset = gdal.Open(self.layer.dataProvider().dataSourceUri())
        # 添加可选择波段
        self.comboBox_R.clear()
        self.comboBox_NIR.clear()
        for i in range(self.rasterDataset.RasterCount):
            self.comboBox_R.addItem(str(i + 1))
            self.comboBox_NIR.addItem(str(i + 1))

    def action_change_layer(self,flag):
        vector_layer=self.find_layer(self.input_vector_layer.currentText())
        raster_layer = self.find_layer(self.input_raster_layer.currentText())
        if flag == 1:
            self.layer=vector_layer
        else:
            self.layer=raster_layer
            #更新NDVI下拉框
            self.fill_combo_box_band()
        self.mapCanvas.setLayers([vector_layer,raster_layer])
        self.mapCanvas.setExtent(self.layer.extent())
        self.mapCanvas.refresh()

    def find_layer(self, layer_name):
        if not layer_name:
            return None

        layers = QgsProject.instance().mapLayersByName(layer_name)
        print(layers)
        if (len(layers) >= 1):
            return layers[0]

        return None

    def open_WFS_dialog(self):
        self.WFSdialog = wfsLayer()
        self.WFSdialog.show()
        self.WFSdialog.wfsLayerSignal.connect(self.add_WFS_layer)

    def add_WFS_layer(self,wfsLayer):
        self.layer=wfsLayer
        QgsProject.instance().addMapLayer(self.layer)
        layers = QgsProject.instance().mapLayers()
        layerList = []
        for layer in layers.values():
            layerList.append(layer)
        self.mapCanvas.setLayers(layerList)
        # 设置图层范围
        self.mapCanvas.setExtent(self.layer.extent())
        self.mapCanvas.refresh()
        self.fill_combo_box_with_layers(self.input_vector_layer, self.input_raster_layer)

    def open_WMS_dialog(self):
        self.WMSdialog = xyzTileLayer()
        self.WMSdialog.show()
        self.WMSdialog.xyzLayerSignal.connect(self.add_WMS_layer)

    def add_WMS_layer(self,wmsLayer):
        self.layer=wmsLayer
        QgsProject.instance().addMapLayer(self.layer)
        layers = QgsProject.instance().mapLayers()
        layerList = []
        for layer in layers.values():
            layerList.append(layer)
        self.mapCanvas.setLayers(layerList)
        # 设置图层范围
        self.mapCanvas.setExtent(self.layer.extent())
        self.mapCanvas.refresh()
        self.fill_combo_box_with_layers(self.input_vector_layer, self.input_raster_layer)

    def RasterData(self):
        self.progressBar.setValue(0)
        layer = self.find_layer(self.input_raster_layer.currentText())
        wave=int(self.comboBox_R.currentText())
        out = raster_stat_unique_count(layer,wave)
        print()
        value = []
        count = []
        for i in range(1, 20):
            self.progressBar.setValue(i)
        for k in sorted(out.keys()):
            # print("value = ", k, '\t, count = ', out[k])
            if (k<1000):
                value.append(k)
                count.append(out[k])
        for i in range(21, 60):
            self.progressBar.setValue(i)
        histogram_draw(value, count)
        for i in range(61,101):
            self.progressBar.setValue(i)

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