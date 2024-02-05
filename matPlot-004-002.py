""" Display CandleStick like graph

    Pandas is better then NumPy to read data file
    
    Here I use mpf to Plot
"""
import pandas
import mplfinance as mpf

# ------------
# User choices
# ------------

FILE_NAME = r'.\datas\OHLC-toupie.txt'
#FILE_NAME = r'.\datas\VALNEVA_2022-11-24.txt'
#FILE_NAME = r'.\datas\ENGIE_2024-01-25.txt'

# Read data in DataFrame columns are : date	ouv	haut	bas	clot	vol	devise	
df = pandas.read_csv(FILE_NAME, sep='\t', parse_dates=['date'])

print(df)

# Rename columns
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Unnamed', 'Unnamed', 'Unnamed']

# data = {
#     'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
#     'Open': [100, 110, 95, 105],
#     'High': [120, 115, 100, 110],
#     'Low': [90, 100, 92, 98],
#     'Close': [110, 105, 98, 102]
# }

print(df)

df['Date'] = pandas.to_datetime(df['Date'], format='%Y-%m-%d')
df = df.set_index('Date')

print(df)

mpf.plot(df, type='candle', style='yahoo', title='Graphique Candlestick',
         ylabel='Prix', ylabel_lower='Volume', show_nontrading=True)

# Show graphic
mpf.show()
