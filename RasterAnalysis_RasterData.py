from collections import defaultdict
from qgis.core import *
from main import *
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

r1_path = r"C:\Users\zyb71\Desktop\qgis\pics\B1.tif"


def load_raster_layer(file_path):
    return QgsRasterLayer(file_path, '')


def raster_stat_unique_count(raster_layer,wave):
    """
    :param QgsRasterLayer raster_layer:
    :return:
    """
    dp = raster_layer.dataProvider()
    x_width, y_height = raster_layer.width(), raster_layer.height()
    box = dp.extent()

    block = dp.block(wave, box, x_width, y_height, None)  # type:QgsRasterBlock

    print(x_width, y_height, box)

    if block.hasNoData():
        no_data = int(block.noDataValue())
    else:
        no_data = 0

    ret = defaultdict(int)
    for x in range(block.width()):
        for y in range(block.height()):
            value = int(block.value(x, y))
            if value == no_data:
                continue

            ret[value] = ret[value] + 1
    a=0
    return ret

def histogram_draw(value,count):
    sum1=0
    sum2=0
    for i in range(len(value)):
        sum1=sum1+value[i]*count[i]
        sum2=sum2+count[i]

    ave = sum1/sum2
    maxcount=max(count)
    maxvalue=max(value)*3/4
    text1 = "mean=" + str(round(ave, 2))
    text4 = "sum=" + str(sum1)
    text2 = "min=" + str(value[0])
    text3 = "max=" + str(value[-1])
    plt.text(maxvalue, maxcount/10*9, text4)
    plt.text(maxvalue, maxcount/10*8, text1)
    plt.text(maxvalue, maxcount/10*7, text2)
    plt.text(maxvalue, maxcount / 10 * 6, text3)
    plt.bar(value, count, label="frequency")
    plt.legend()
    plt.show()
    plt.xlabel('Value')
    plt.ylabel('frequency')
    plt.title(u'Raster-Histogram')

# layer = load_raster_layer(r1_path)


def Rasterdata(layer,wave):
    out = raster_stat_unique_count(layer,wave)
    print()
    value=[]
    count=[]
    for k in sorted(out.keys()):
        print("value = ", k, '\t, count = ', out[k])
        if(k>0):
            value.append(k)
            count.append(out[k])
    histogram_draw(value, count)
    return









