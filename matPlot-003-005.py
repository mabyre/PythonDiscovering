""" matPlot_used - Graph candlestick_ohlc line_h line_v + BarGraph

    Use Bar rather than Stem + limegreen and tomato colors

	Add Volume displayed in ax2
    
    - candlestick_ohlc
    - yfinance.download
    - on_scroll_zoom
    - click_annotation
    - remove_annotation
    
    using yfinance
    Graph Volume Display
"""
import pandas
import yfinance
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import figure.helper as fighelper
import debug.func as dbg

from matplotlib import style
from matplotlib.dates import date2num
from matplotlib.ticker import StrMethodFormatter
from matplotlib.ticker import ScalarFormatter
from mplfinance.original_flavor import candlestick_ohlc

style.use('fivethirtyeight')
print(plt.style.available)

print(plt.__file__)

# ------------
# User choices
# ------------
# variables the user can choice
#

GRAPH_VOLUME_DISPLAY = True

READ_BY_YAHOO_FINANCE = True

START_DATE = "2023-03-01"

if READ_BY_YAHOO_FINANCE == False:
    #FILE_NAME = r'.\datas\CARMAT_2024-01-19 (1).txt'
    FILE_NAME = r'.\datas\CARMAT_2024-02-07.txt'

#COMPAGNY_NAME = "AAPL"  # Symbole boursier d'Apple, mais vous pouvez le changer
#COMPAGNY_NAME = ["ENGI.PA", "ENGIE"]
#COMPAGNY_NAME = ["VLA.PA", "VALNEVA"]
#COMPAGNY_NAME = ["ENGI.PA", "ENGIE"]
#COMPAGNY_NAME = ["DSY.PA", "DASSAULT SYSTEMES"]
COMPAGNY_NAME = ["ALCAR.PA", "CARMAT"]
#COMPAGNY_NAME = ["MAAT.PA", "MAT PHARMA"]

# ---------
# Read file
# ---------

# Read data with pandas DataFrame df
# ----------------------------------
if READ_BY_YAHOO_FINANCE == False:
    # Read data in DataFrame df
    df = pandas.read_csv(FILE_NAME, sep='\t', parse_dates=['date'],  date_format='%d/%m/%Y %H:%M')


# Read data with yfinance.download
# --------------------------------
if READ_BY_YAHOO_FINANCE == True:
	# Open    High     Low   Close  Adj Close   Volume  Daily_Return
	# Date
	data = yfinance.download( COMPAGNY_NAME[0], start = START_DATE ) # end_date = "2024-02-04"
	data = data.reset_index() # make date as a 'straight' column
	df = pandas.DataFrame(data)

	dbg.print(df.head())

	# rename column's name
	new_name = {
	    'Date': 'date',
	    'Open': 'ouv',
	    'High': 'haut',
	    'Low': 'bas', 
	    'Close': 'clot',
	    'Volume': 'vol'
	}
	df = df.rename( columns=new_name )
 
	dates =  df['date']
	volume = df['vol']

y_data = df['clot']

# Sanity check
# ------------
all_days = len( y_data )
dbg.print( f'signal weight: {all_days}' )
dbg.print( df['date'].dtypes )

assert len( df['date'] ) == all_days, "ERROR: Reading file with read_csv"
assert df['date'].dtypes == 'datetime64[ns]', "ERROR: df['date'] bad type"

# --------------
# Prepare figure
# --------------
# 
fig = plt.figure( figsize = (9, 7) )
fig.canvas.mpl_connect('scroll_event', lambda event: fighelper.on_scroll_zoom(event, fig))
fig.canvas.mpl_connect('button_press_event', lambda event: fighelper.remove_annotation(event, ax1))
fig.canvas.mpl_connect('button_press_event', lambda event: fighelper.click_annotation(event, ax1, line_h, line_v))

# ax1
#
if GRAPH_VOLUME_DISPLAY == True:
    ax1 = plt.subplot2grid( (8, 1), (0, 0), rowspan = 6, colspan = 1, facecolor='#FAFAFA' )
else:
    ax1 = fig.add_subplot( facecolor='#FAFAFA' )
    
ax1.set_title( f"{COMPAGNY_NAME[1]}")

# convert df['date'] into new column as a TimeStamp for ohlc graph
df['date2num'] = pandas.to_datetime(df['date'])
df['date2num'] = df['date'].apply(date2num)

# Make ohlc graph
#
ohlc = df[['date2num', 'ouv', 'haut', 'bas', 'clot']].values.tolist()
candlestick_ohlc( ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f' )
        
# Format axis
ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:.2f}'))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y')) # %Y year on for digits - %y year on txo digits

line_h = ax1.axhline( y=y_data[0], color='tomato', linestyle='--', linewidth=1 )
line_h.set_visible(False)

line_v = ax1.axvline( x=df['date'][0], color='lightseagreen', linestyle='--', linewidth=1 )
line_v.set_visible(False)

# ax1.legend()

# ax2
#
if GRAPH_VOLUME_DISPLAY == True:

    ax2 = plt.subplot2grid( (8, 1), (6, 0), rowspan = 2, colspan = 1, sharex = ax1 )
    ax2.set_ylabel( f'Volume' )

    # Calculate stock price change between each consecutive values
    y_data_changes = y_data.diff().fillna(0)

    bars = ax2.bar( dates, volume, color='g')
    
    # Set bar color based on stock price change
    for i, change in enumerate( y_data_changes ):
        if change > 0:
            bars[i].set_color('g') # going up 
        elif change < 0:
            bars[i].set_color('r') # going down    

    ax2.yaxis.set_major_formatter( ScalarFormatter(useMathText=True) )
    ax2.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    
plt.gcf().autofmt_xdate() # auto format dates label
plt.tight_layout()
plt.subplots_adjust( right=0.91 ) # place for annotation
plt.show()
