import os, sys,struct
from qgis.core import *
from qgis.gui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog

# from RasterPlugin_library import MapExplorer
from ui.DEM_information import InformationDialog

class DEMInformation(QDialog, InformationDialog):
    def __init__(self):
        super(DEMInformation, self).__init__()
        self.setupUi(self)