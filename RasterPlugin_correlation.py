# -*- coding: utf-8 -*-

import os, sys
from qgis.core import *
from qgis.gui import *
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QFileDialog, QGridLayout, QWidget, QLabel
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