""" Using TensorFlow

    Time series forecasting
"""
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas
import numpy

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

print("TensorFlow version:", tf.__version__)

fft = tf.signal.rfft(y_data)
f_per_dataset = numpy.arange(0, len(fft))

# n_samples_h = len(y_data)
# hours_per_year = 24*365.2524
# years_per_dataset = n_samples_h/(hours_per_year)

# only one year in dataset
years_per_dataset = len(y_data)

f_per_year = f_per_dataset/years_per_dataset
plt.step(f_per_year, numpy.abs(fft))
plt.xscale('log')
plt.ylim(0, 50) # 400000
plt.xlim([0.1, max(plt.xlim())])
plt.xticks([1, 365.2524], labels=['1/Year', '1/day'])
_ = plt.xlabel('Frequency (log scale)')

plt.show()