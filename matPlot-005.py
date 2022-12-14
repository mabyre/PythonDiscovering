#
# matPlot-0xx series will lead us to predictive of linear series
#
# Chez boursorama dans le grapqhique du cours de l'action, il y a un bouton télécharger
# pour exporter les données au format .txt séparées par un \t
#
# https://www.geeksforgeeks.org/convert-a-numpy-array-to-a-pandas-series/
# Convert a NumPy array to a Pandas series
#
# https://geekyhumans.com/how-to-predict-us-stock-price-using-python/
# https://geekyhumans.com/fr/prediction-boursiere-avec-python/
# Prédiction boursière avec Python
#
# https://clemovernet.wordpress.com/2020/01/01/tensorflow-2-prediction-dun-cours-de-bourse-version-simple/
# Some other example of using keras.models.Sequential
#
# https://github.com/JosueAfouda/Analyse-quantitative/blob/master/Prediction%20du%20prix%20des%20actions.ipynb
#
# https://matplotlib.org/stable/gallery/color/named_colors.html#css-colors
# Get nice colors for graph
#
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import numpy
import pandas

from matplotlib import style

from sklearn.preprocessing import MinMaxScaler
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

COMPAGNY = 'CARMAT'


def bytespdate2num(fmt, encoding='utf-8'):
    def bytesconverter(b):
        s = b.decode(encoding)
        s1 = mdates.datestr2num(datetime.strptime(
            s, fmt).strftime('%m/%d/%Y %H%M'))
        return (s1)
    return bytesconverter


# Colums you'll find in file
#
date, openp, highp, lowp, closep, volume = numpy.loadtxt(filename,
                                                         delimiter='\t',
                                                         skiprows=1,  # first line is column's names
                                                         unpack=True,
                                                         usecols=(
                                                             0, 1, 2, 3, 4, 5),
                                                         converters={0: bytespdate2num('%d/%m/%Y %H:%M')})

y = len(openp)
print(f'signal weight: {y}')

assert len(date) == y, "Error in reading file"

# Prepare data
# ------------
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(numpy.reshape(closep, (-1, 1)))

# how many days we want to look at the past to predict
prediction_days = 10

# defining two empty lists for preparing the training data
x_train = []
y_train = []

# we are counting from the prediction_days'th index to the last index
for x in range(prediction_days, len(scaled_data)):
    x_train.append(scaled_data[x-prediction_days:x, 0])
    y_train.append(scaled_data[x, 0])

x_train, y_train = numpy.array(x_train), numpy.array(y_train)
x_train = numpy.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Construct model
# ---------------
model = Sequential()
# specify the layer
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
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
# ----------
test_closep = pandas.Series(closep)
actual_prices = test_closep
total_dataset = pandas.concat((test_closep, test_closep), axis=0)

model_input = total_dataset[len(total_dataset) - len(test_closep) - prediction_days:].values
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
plt.plot(actual_prices, color='midnightblue', label=f"Actual {COMPAGNY} price")
plt.plot(predicted_price, color='green', label=f"Predicted {COMPAGNY} Price")
plt.title(f"{COMPAGNY} share price")
plt.xlabel('Time')
plt.ylabel(f'{COMPAGNY} share price')
plt.legend
plt.show()

# Predict data for tomorrow using real data
#
all_days = len(closep)
real_data = []
for x in range(0, all_days):
    real_data.append(closep[x])

real_data = numpy.array(real_data)
real_data = numpy.reshape(real_data, (all_days, 0, 1))

prediction = model.predict(real_data)
prediction = scaler.inverse_transform(prediction)

# Plot the Predictions
plt.plot(actual_prices, color='midnightblue', label=f"Actual {COMPAGNY} price")
plt.plot(prediction, color='green', label=f"Predicted {COMPAGNY} Price")
plt.title(f"{COMPAGNY} share price")
plt.xlabel('Time')
plt.ylabel(f'{COMPAGNY} share price')
plt.legend
plt.show()
