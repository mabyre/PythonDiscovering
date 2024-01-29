""" Play with NumPy

    numpy.convolve is used through moving_average
    
    calculation of moving_average for the tree modes: valid, same, full

    https://numpy.org/doc/stable/user/quickstart.html
    https://www.labri.fr/perso/rgiot/cours/anavis/Exercices/
"""
import numpy
import pandas
import matplotlib.pyplot as plt
import digitsingnalprocessing.func as dsp

# ------------
# User choices
# ------------

#FILE_NAME = r'.\datas\CARMAT_2024-01-16.txt'
FILE_NAME = r'.\datas\ATOS_2024-01-24.txt'

SLIDING_AVERAGE_WINDOW_WIDTH = 15

# -------------------------
# Read data in DataFrame df
# -------------------------
df = pandas.read_csv(FILE_NAME, sep='\t', parse_dates=['date'])
date = df['date']
y_data = df['clot']

lg_date = len(date)
print( f'len(date): {lg_date}')

# Calculate tree types of moving average
mov_avg_valid = dsp.moving_average( y_data, SLIDING_AVERAGE_WINDOW_WIDTH ) # 'valid' by default
mov_avg_same = dsp.moving_average( y_data, SLIDING_AVERAGE_WINDOW_WIDTH, 'same' )
mov_avg_full = dsp.moving_average( y_data, SLIDING_AVERAGE_WINDOW_WIDTH, 'full' )

# What the signal's length
lg_mov_avg_valid = len( mov_avg_valid )
print( f'valid: {lg_mov_avg_valid}')

lg_mov_avg_same = len( mov_avg_same )
print( f' same: {lg_mov_avg_same}' )

lg_mov_avg_full = len( mov_avg_full )
print( f' full: {lg_mov_avg_full}' )

# len(date): 256
# valid: 242
#  same: 256
#  full: 270
 
# Tried with 'reshape' did not succeed
for x in range(0, lg_date - lg_mov_avg_valid):
    mov_avg_valid = numpy.append(mov_avg_valid, [0])

# Plot valid
#
plt.figure()
plt.plot( date, y_data, color='midnightblue', label=f"price" ) 
plt.plot( date, mov_avg_valid, color='g', label=f"valid" )
plt.xticks( rotation = 45 )
plt.title( f"Moving Average = {SLIDING_AVERAGE_WINDOW_WIDTH}" )
plt.xlabel( f'Days' )
plt.ylabel( f'Price' )
# Otherwise dates are ploted out of graph
plt.subplots_adjust( bottom = 0.2 )
plt.legend() # diplay label for plot
# plt.show()

# Plot same
#
plt.figure()
plt.plot( date, y_data, color='midnightblue', label=f"price" ) 
plt.plot( date, mov_avg_same, color='g', label=f"same" )
plt.xticks( rotation = 45 )
plt.title( f"Moving Average = {SLIDING_AVERAGE_WINDOW_WIDTH}" )
plt.xlabel( f'Days' )
plt.ylabel( f'Price' )
# Otherwise dates are ploted out of graph
plt.subplots_adjust( bottom = 0.2 )
plt.legend() # diplay label for plot
# plt.show()

# Plot full
#
plt.figure()
plt.plot( y_data, color='midnightblue', label=f"price" ) 
plt.plot( mov_avg_full, color='g', label=f"full" )
plt.xticks( rotation = 45 )
plt.title( f"Moving Average = {SLIDING_AVERAGE_WINDOW_WIDTH}" )
plt.xlabel( f'Days' )
plt.ylabel( f'Price' )
# Otherwise dates are ploted out of graph
plt.subplots_adjust( bottom = 0.2 )
plt.legend() # diplay label for plot
# plt.show()

# Plot histogram for fun
#
plt.figure()
plt.hist(y_data, 20)

plt.show()


