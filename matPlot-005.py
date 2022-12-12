#
# https://pythonprogramming.net/fill-pruning-matplotlib-tutorial/
# https://geekyhumans.com/fr/prediction-boursiere-avec-python/
# https://www.geeksforgeeks.org/convert-a-numpy-array-to-a-pandas-series/
#
# matPlot series will lead us to preditive of linear series
#
# Chez boursorama dans le grapqhique du cours de l'action, il y a un bouton télécharger.
#
#
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import numpy
import urllib
import datetime as dt
import pandas

from mplfinance.original_flavor import candlestick_ohlc
from matplotlib import style

from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.model_selection import PredefinedSplit

from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense, Dropout, LSTM


style.use('fivethirtyeight')
print(plt.style.available)

print(plt.__file__)

# MA1 = 10
# MA2 = 30
#filename = r'.\datas\VALNEVA_2022-11-24.txt'

# Should be choosen inside signal, means less than over the end
MA1 = 5
MA2 = 15
filename = r'.\datas\CARMAT_2022-12-12.txt'

COMPAGNY = 'Name of the compagny'


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


"""
Display graph for stock
Args:
    stock (_type_): _description_
"""
fig = plt.figure()
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
plt.title('stock')
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

# Prepare data
# ------------
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(numpy.reshape(closep, (-1, 1)))

# how many days we want to look at the past to predict
prediction_days = 10

# defining two empty lists for preparing the training data
x_train = []
y_train = []

# we are counting from the prediction_days_th index to the last index
for x in range(prediction_days, len(scaled_data)):
    x_train.append(scaled_data[x-prediction_days:x, 0])
    y_train.append(scaled_data[x, 0])

x_train, y_train = numpy.array(x_train), numpy.array(y_train)
x_train = numpy.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Construct model
# ---------------
model = Sequential()
# specify the layer
model.add(LSTM(units=50, return_sequences=True,
          input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
# this is going to be a prediction of the next closing value
model.add(Dense(units=1))

# Complete model
model.compile(optimizer='adam', loss='mean_squared_error')
# fit the model in the training data
model.fit(x_train, y_train, epochs=25, batch_size=32)

# Test model
#
test_closep = pandas.Series(closep)
actual_prices = test_closep
total_dataset = pandas.concat((test_closep, test_closep), axis=0)

model_input = total_dataset[len(
    total_dataset) - len(test_closep) - prediction_days:].values
# reshaping the model
model_input = model_input.reshape(-1, 1)
# scaling down the model
model_input = scaler.transform(model_input)

# Predict data for tomorrow
# -------------------------
x_test = []
for x in range(prediction_days, len(model_input)):
    x_test.append(model_input[x-prediction_days:x, 0])

x_test = numpy.array(x_test)
x_test = numpy.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

predicted_price = model.predict(x_test)
predicted_price = scaler.inverse_transform(predicted_price)

# plot the test Predictions
plt.plot(actual_prices, color="black", label=f"Actual{COMPAGNY} price")
plt.plot(predicted_price, color='green', label="Predicted {COMPAGNY} Price")
plt.title(f"{COMPAGNY} Share price")
plt.xlabel('Time')
plt.ylabel(f'{COMPAGNY} share price')
plt.legend
plt.show()

# Print prediction
#
# real_data = pandas.Series(closep)
# prediction = model.predict(real_data)
# prediction = scaler.inverse_transform(prediction)
# print(f"Prediction: {prediction}")
