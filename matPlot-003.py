#
# https://pythonprogramming.net/fill-pruning-matplotlib-tutorial/
#
# Aim is to show how to use date in horizontal axe of graph
#
# At boursorama in the stock price graph, there is a download button which allows you 
# to export the values in text format with \t as a separator
#
#
import matplotlib.pyplot as plt
from matplotlib import style

import numpy
import pandas

style.use('fivethirtyeight')
print(plt.style.available)
print(plt.__file__)

TITLE = 'CARMAT_2022'
#FILE_NAME = r'.\datas\VALNEVA_2022-11-24.txt'
FILE_NAME = r'.\datas\CARMAT_2022-12-12.txt'

def graph_data(stock):
    """
    Display graph for stock
    Args:
        stock (_type_): _description_
    """
    plt.title(stock)

    # Read data in DataFrame df
    #
    df = pandas.read_csv(FILE_NAME, sep='\t', parse_dates=['date'])

    date = df['date']
    y_data = df['clot']

    # Sanity check
    assert len(date) == len(y_data), "Error in reading file"

    plt.plot( date, y_data, label=f"price" ) # color='midnightblue',
    plt.xticks( rotation = 45 )

    # Otherwise dates are ploted out of graph
    plt.subplots_adjust(left=0.11, bottom=0.24, right=0.90,
                        top=0.90, wspace=0.2, hspace=0)
    plt.show()

graph_data(TITLE)

print('Program ending...')
