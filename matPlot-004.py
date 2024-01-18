#
# https://pythonprogramming.net/fill-pruning-matplotlib-tutorial/
#
# Very tuff sample to updated, many problems to solve in compare to the original
# After had solved many problems it works
#
# Install
# -------
# >pip install matplotlib
# >pip install mplfinance
#
# Aim is to use candlestick_ohlc to plot a candle stick graph
#
# At boursorama in the stock price graph, there is a download button, 
# this is where I retrieve the data files
#
#
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib import style

import numpy
import datetime as dt

style.use('fivethirtyeight')
print(plt.style.available)
print(plt.__file__)

# Should be choosen inside signal, means less than over the end
# MA1 = 10
# MA2 = 30
# filename = r'.\datas\VALNEVA_2022-11-24.txt'

MA1 = 5
MA2 = 15
filename = r'.\datas\CARMAT_2024-01-16.txt'


def moving_average(values, window):
    weights = numpy.repeat(1.0, window)/window
    asa_values = numpy.asarray(values, dtype=float)
    smas = numpy.convolve(asa_values, weights, 'valid')
    return smas


def high_minus_low(highs, lows):
    return highs-lows


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
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
    plt.title(stock)
    plt.ylabel('H-L')
    ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1)
    plt.ylabel('Price')
    ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1)
    plt.ylabel('MAvgs')

    # Unfortunately, Yahoo's API is no longer available
    # stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + \
    #     stock + '/chartdata;type=quote;range=1y/csv'
    # source_code = urllib.request.urlopen(stock_price_url).read().decode()

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
    y1 = len(openp)

    assert y == y1, "Error in reading file"

    # Let's create OHLC
    ohlc = []
    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x += 1

    ma1 = moving_average(closep, MA1)
    ma2 = moving_average(closep, MA2)
    start = len(date[MA2-1:])

    h_l = list(map(high_minus_low, highp, lowp))

    ax1.plot_date(date, h_l, '-')
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='lower'))

    candlestick_ohlc(ax2, ohlc, width=0.4,
                     colorup='#77d879', colordown='#db3f3f')

    ax2.grid(True)

    bbox_props = dict(boxstyle='round', fc='w', ec='k', lw=1)

    ax2.annotate(str(closep[-1]), (date[-1], closep[-1]),
                 xytext=(date[-1]+4, closep[-1]), bbox=bbox_props)


# Annotation example with arrow
# ax2.annotate('Bad News!',(date[11],highp[11]),
# xytext=(0.8, 0.9), textcoords='axes fraction',
# arrowprops = dict(facecolor='grey',color='grey'))
##
##
# Font dict example
# font_dict = {'family':'serif',
# 'color':'darkred',
# 'size':15}
# Hard coded text
##    ax2.text(date[10], closep[1],'Text Example', fontdict=font_dict)

    ax3.plot(date[-start:], ma1[-start:], linewidth=1)
    ax3.plot(date[-start:], ma2[-start:], linewidth=1)

    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                     where=(ma1[-start:] < ma2[-start:]),
                     facecolor='r', edgecolor='r', alpha=0.5)

    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                     where=(ma1[-start:] > ma2[-start:]),
                     facecolor='g', edgecolor='g', alpha=0.5)

    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))

    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.subplots_adjust(left=0.11, bottom=0.24, right=0.90,
                        top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('VALNEVA')

print('Program ending...')
