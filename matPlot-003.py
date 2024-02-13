""" matPlot-00x series will lead us to predictive of linear series
    
    - candlestick_ohlc
    - on_scroll_zoom
    - on_click_mouse_annotation

    https://matplotlib.org/stable/gallery/color/named_colors.html#css-colors
    Get nice colors for graph
"""
import matplotlib.pyplot as plt
import pandas
import figure.helper as fighelper

from matplotlib import style
from matplotlib.dates import date2num
import matplotlib.dates as mdates
from matplotlib.ticker import StrMethodFormatter
from mplfinance.original_flavor import candlestick_ohlc

style.use('fivethirtyeight')
print(plt.style.available)

print(plt.__file__)

# ------------
# User choices
# ------------
# variables the user can choice
# 

#FILE_NAME = r'.\datas\CARMAT_2024-01-19 (1).txt'
FILE_NAME = r'.\datas\CARMAT_2024-02-07.txt'

COMPAGNY_NAME = 'CARMAT'

# ---------
# Read file
# ---------

# Read data in DataFrame df
df = pandas.read_csv(FILE_NAME, sep='\t', parse_dates=['date'],  date_format='%d/%m/%Y %H:%M')
dates = df['date']
volume = df['vol']
y_data = df['clot']

# Sanity check
all_days = len( y_data )
print( f'signal weight: {all_days}' )
assert len( dates ) == all_days, "ERROR: Reading file with read_csv"
assert df['date'].dtypes == 'datetime64[ns]', "ERROR: df['date'] bad type"

# Prepare figure
#
fig = plt.figure( figsize = (9, 7) )
fig.canvas.mpl_connect('scroll_event', lambda event: fighelper.on_scroll_zoom(event, fig))
fig.canvas.mpl_connect('button_press_event', lambda event: fighelper.click_annotate_h(event, ax1, line))

# ax1
#
ax1 = fig.add_subplot( facecolor='#FAFAFA' )
ax1.set_title( f"{COMPAGNY_NAME}")

# convert df['date'] into new column as a TimeStamp for ohlc graph
print(df['date'].dtypes)

df['date2num'] = pandas.to_datetime(df['date'])
df['date2num'] = df['date'].apply(date2num)

# Make ohlc graph
#
ohlc = df[['date2num', 'ouv', 'haut', 'bas', 'clot']].values.tolist()
candlestick_ohlc( ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f' )
        
# Format axis
ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:.2f}'))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y')) # %Y year on for digits - %y year on txo digits

line = ax1.axhline( y=y_data[0], color='red', linestyle='--', linewidth=1 )
line.set_visible(False)

# ax1.legend()

plt.gcf().autofmt_xdate() # auto format dates label
plt.tight_layout()
plt.subplots_adjust( right=0.91 )
plt.show()
