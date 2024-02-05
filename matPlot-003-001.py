#
# https://pythonprogramming.net/fill-pruning-matplotlib-tutorial/
#
# Aim is to show how to use date in horizontal axe of graph
#
# demonstrate moving average exponential
#
# At boursorama in the stock price graph, there is a download button which allows you 
# to export the values in text format with \t as a separator
#
#
import matplotlib.pyplot as plt
from matplotlib import style
import digitsignalprocessing.func as dsp

import numpy
import pandas

style.use('fivethirtyeight')
print(plt.style.available)
print(plt.__file__)

TITLE = 'ENGIE'

#FILE_NAME = r'.\datas\VALNEVA_2022-11-24.txt'
FILE_NAME = r'.\datas\CARMAT_2022-12-12.txt'
#FILE_NAME = r'.\datas\ENGIE_2024-01-25.txt'

SLIDING_WINDOW_WIDTH = 5

def graph_data(stock):
    """
    Display graph for stock
    Args:
        stock (_type_): _description_
    """
    plt.title(stock)

    # Read data in DataFrame df
    #
    df = pandas.read_csv( FILE_NAME, sep='\t', parse_dates=['date'] )

    date = df['date']
    y_data = df['clot']

    # Sanity check
    assert len( date ) == len( y_data ), "Error in reading file"
    
    print( f'signal\'s lenght: {len( date )}' )
    
    ma1 = dsp.moving_average( y_data, SLIDING_WINDOW_WIDTH )
    mae1 = dsp.moving_average_exp( y_data, SLIDING_WINDOW_WIDTH )
    
    # Reshape
    for x in range( 0, len(date) - len(ma1) ):
        ma1 = numpy.append(ma1, ma1[len(ma1)-1] )
        
    # Reshape
    for x in range( 0, len(date) - len(mae1) ):
        mae1 = numpy.append(mae1, mae1[len(mae1)-1] )        
    
    # Plot Graphs
    #
    plt.plot( date, y_data, color='k', label=f"price" )
    plt.plot( date, ma1, linewidth=2, color='darkorange', label=f"mov avg" )
    plt.plot( date, mae1, linewidth=2, color='green', label=f"mov avg exp" )
    plt.xticks( rotation = 45 )
    # Otherwise dates are ploted out of graph
    plt.subplots_adjust( 
        left=0.11, 
        bottom=0.24, 
        right=0.90, 
        top=0.90, 
        wspace=0.2, 
        hspace=0 
    )
    plt.legend()
    plt.show()

graph_data(TITLE)

print('Program ending...')
