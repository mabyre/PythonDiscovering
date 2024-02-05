"""
    Display moving average and exponential moving average
    
    Surface between curves are filled with colors
    
"""
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
#FILE_NAME = r'.\datas\CARMAT_2022-12-12.txt'
FILE_NAME = r'.\datas\ENGIE_2024-01-25.txt'

def graph_data(stock):
    """
    Display graph for stock
    Args:
        stock (_type_): _description_
    """
    # Read data in DataFrame df
    #
    df = pandas.read_csv( FILE_NAME, sep='\t', parse_dates=['date'] )

    date = df['date']
    y_data = df['clot']

    # Sanity check
    assert len( date ) == len( y_data ), "Error in reading file"
    
    print( f'signal\'s lenght: {len( date )}' )
    
    width_ma1 = 10
    width_ma2 = 15
    
    ma1 = dsp.moving_average( y_data, width_ma1 )
    ma2 = dsp.moving_average( y_data, width_ma2 )
    ma3 = dsp.moving_average_exp( y_data, 15 )
    
    ma1 = dsp.reshape( y_data, ma1 )
    ma2 = dsp.reshape( y_data, ma2 )
    ma3 = dsp.reshape( y_data, ma3 )
   
    # Plot Graphs
    #
    fig, axe = plt.subplots(figsize=(8, 6))

    axe.plot( date, y_data, linewidth=2, color='k', label=f"price" )
    axe.plot( date, ma1, linewidth=1, color='blue', label=f"avg 10" )
    axe.plot( date, ma2, linewidth=1, color='green', label=f"avg 15" )
    axe.plot( date, ma3, linewidth=1, color='darkorange', label=f"avg exp 15" )
    
    axe.fill_between(date, ma2, ma1, where=(ma1 > ma2), interpolate=True, color='r', alpha=0.3)
    axe.fill_between(date, ma2, ma1, where=(ma1 < ma2), interpolate=True, color='g', alpha=0.3)
    
    axe.legend()

    plt.title(stock)
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
    plt.show()

graph_data(TITLE)

print('Program ending...')
