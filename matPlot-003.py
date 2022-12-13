#
# https://pythonprogramming.net/fill-pruning-matplotlib-tutorial/
#
# Aim is to show how to use date in horizontal axe of graph
#
# Chez boursorama dans le grapqhique du cours de l'action, il y a un bouton télécharger
# qui permet d'exporter les valeurs au format texte avec \t comme séparateur
#
#
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import style

import numpy
import urllib
import datetime as dt

style.use('fivethirtyeight')
print(plt.style.available)
print(plt.__file__)

TITLE = 'CARMAT_2022'
#filename = r'.\datas\VALNEVA_2022-11-24.txt'
filename = r'.\datas\CARMAT_2022-12-12.txt'


def bytespdate2num(fmt, encoding='utf-8'):
    def bytesconverter(b):
        s = b.decode(encoding)
        s1 = mdates.datestr2num(datetime.strptime(
            s, fmt).strftime('%m/%d/%Y %H%M'))
        return (s1)
    return bytesconverter


def graph_data(stock):
    """
    Display graph for stock
    Args:
        stock (_type_): _description_
    """
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0), rowspan=1, colspan=1)
    plt.title(stock)

    # Colums you'll find in file
    #
    date, openp, highp, lowp, closep, volume = numpy.loadtxt(filename,
                                                             delimiter='\t',
                                                             skiprows=1,  # first line is column's names
                                                             unpack=True,
                                                             usecols=(
                                                                 0, 1, 2, 3, 4, 5),
                                                             converters={0: bytespdate2num('%d/%m/%Y %H:%M')})

    x = 0
    y = len(date)
    y1 = len(closep)

    assert y == y1, "Error in reading file"

    ax1.plot_date(date, closep, r'-')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.setp(ax1.get_xticklabels(), visible=True)

    # Otherwise dates are ploted out of graph
    plt.subplots_adjust(left=0.11, bottom=0.24, right=0.90,
                        top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data(TITLE)

print('Program ending...')
