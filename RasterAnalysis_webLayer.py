import os, sys
from qgis.core import *
from qgis.gui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog
from ui.WFS import Ui_WFS_Dialog
from ui.XYZTile import Ui_XYZ_Dialog
import urllib.parse

class wfsLayer(QDialog, Ui_WFS_Dialog):
    #定义信号
    wfsLayerSignal = pyqtSignal(QgsVectorLayer)
    def __init__(self):
        super(wfsLayer, self).__init__()
        self.setupUi(self)
        self.slot_connect()

    def slot_connect(self):
        self.addWFSLayer.clicked.connect(lambda :self.get_WFS_layer())

    def get_WFS_layer(self):
        URI=self.URI.text()
        service=self.service.text()
        version=self.version.text()
        request=self.request.text()
        typename=self.typename_2.text()
        srsname=self.srsname.text()
        params = {
            'service': service,
            'version': version,
            'request': request,
            'typename': typename,
            'srsname': srsname
        }
        url = URI + urllib.parse.unquote(urllib.parse.urlencode(params))
        layer = QgsVectorLayer(url,"wfs layer","WFS")
        self.wfsLayerSignal.emit(layer)
        self.close()

class xyzTileLayer(QDialog, Ui_XYZ_Dialog):
    #定义信号
    xyzLayerSignal = pyqtSignal(QgsVectorLayer)
    def __init__(self):
        super(xyzTileLayer, self).__init__()
        self.setupUi(self)
        self.slot_connect()

    def slot_connect(self):
        self.addXYZTileLayer.clicked.connect(lambda :self.get_XYZ_layer())

    def get_XYZ_layer(self):
        URI=self.URI.text()
        lyrs=self.lyrs.text()
        x=self.Xvalue.text()
        y=self.Yvalue.text()
        z=self.Zvalue.text()
        zmin=self.zmin.text()
        zmax=self.zmax.text()
        params = {
            'lyrs': lyrs,
            'x': x,
            'y': y,
            'z': z
        }
        params2 = {
            'zmin': zmin,
            'zmax': zmax
        }
        url = URI + urllib.parse.unquote(urllib.parse.urlencode(params))
        zparam = urllib.parse.unquote(urllib.parse.urlencode(params2))
        uri="type=xyz&"+zparam+"&url=https://"+urllib.parse.quote(url)
        print(uri)
        layer = QgsRasterLayer(uri,"wms layer","wms")
        if layer.isValid():
            self.xyzLayerSignal.emit(layer)
        self.close()