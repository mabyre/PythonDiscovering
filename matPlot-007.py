""" matPlot-0xx series will lead us to predictive of linear series

    Pandas is better than NumPy to read csv file, bytespdate2num no more needed

    See matPlot-006 for details on implementation
    
    Here is tried to make few days prediction

    https://matplotlib.org/stable/gallery/color/named_colors.html#css-colors
    Get nice colors for graph
    
    Thanks to chatgpt ;)
"""
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import numpy as np
import pandas

from matplotlib import style

from sklearn.preprocessing import MinMaxScaler
from keras import Sequential
from keras.layers import Dense, Dropout, LSTM

style.use('fivethirtyeight')
print(plt.style.available)

print(plt.__file__)

# ------------
# User choices
# ------------
# variables the user can choice
# 
#FILE_NAME = r'.\datas\CARMAT_2024-01-19 (1).txt'
FILE_NAME = r'.\datas\ENGIE_2024-01-25.txt'

COMPAGNY_NAME = 'ENGIE_2024'

# How many days we want to look at the past to predict
DAYS_IN_PAST = 60

# Algorithme parameters
EPOCHS = 100

# ---------
# Read file
# ---------

# Read data in DataFrame df
df = pandas.read_csv(FILE_NAME, sep='\t', parse_dates=['date'])

date = df['date']
y_data = df['clot']

# Sanity check
y = len(df['ouv'])
print(f'signal weight: {y}')
assert len(date) == y, "Error in reading file"

# ------------
# Prepare data
# ------------
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(np.reshape(y_data, (-1, 1)))

# defining two empty lists for preparing the training data
x_train = []
y_train = []

# we are counting from the prediction_days'th index to the last index
for x in range(DAYS_IN_PAST, len(scaled_data)):
    x_train.append(scaled_data[x-DAYS_IN_PAST:x, 0])
    y_train.append(scaled_data[x, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# ---------------
# Construct model
# ---------------
DROP_OUT_RATE = 0.3
model = Sequential()
# specify the layers LSTM (Long Short-Term Memory)
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(DROP_OUT_RATE))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(DROP_OUT_RATE))
model.add(LSTM(units=50))
model.add(Dropout(DROP_OUT_RATE))
# this is going to be a prediction of the next closing value
model.add(Dense(units=1))

print(model.summary())

# Compile model before training or prediction
model.compile(optimizer='adam', loss='mean_squared_error')

# Fit the model in the training data
model.fit(x_train, y_train, epochs=EPOCHS, batch_size=32)

# Evaluate the trained model should be done with x_test
score = model.evaluate(x_train, y_train, verbose=0)
print(f'Test loss: {score}')

# ----------
# Test model
# ----------
y_data_test = pandas.Series(y_data)
actual_prices = y_data_test
total_dataset = pandas.concat((y_data_test, y_data_test), axis=0)

model_input = total_dataset[len(total_dataset) - len(y_data_test) - DAYS_IN_PAST:].values
# reshaping the model
model_input = model_input.reshape(-1, 1)
# scaling down the model
model_input = scaler.transform(model_input)

# -------------------------
# Predict data for tomorrow
# -------------------------
# split data into windows
#
x_test = []
for x in range(DAYS_IN_PAST, len(model_input)):
    x_test.append(model_input[x-DAYS_IN_PAST:x, 0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

predicted_price = model.predict(x_test)
predicted_price = scaler.inverse_transform(predicted_price)

# ------------------------------------------
# Make the predictions for days in the futur
# ------------------------------------------
#
DAYS_IN_FUTUR = 5
all_days = len( scaled_data )

real_data = np.array( scaled_data[-DAYS_IN_PAST:] )
real_data = np.reshape( real_data, (1, DAYS_IN_PAST, 1) )

predictions = []

for _ in range(DAYS_IN_FUTUR):

    prediction = model(real_data, training=False )
    predictions.append(prediction[0, 0])

    # Update the input sequence to include the new prediction
    real_data = np.append(real_data[:, 1:, :], [[[prediction[0, 0]]]], axis=1)

predictions = scaler.inverse_transform([predictions])
predictions = np.reshape(predictions, (DAYS_IN_FUTUR,1))

# Create an X axis
#
x_axe =  np.arange(0, all_days)
x_axep = np.arange(all_days , all_days + DAYS_IN_FUTUR)

# Plot the test Predictions
#
plt.plot(x_axe, actual_prices, color='midnightblue', linewidth=3, label=f"Actual price")
plt.plot(x_axe, predicted_price, color='green', linewidth=2, label=f"Predicted Price")
plt.plot(x_axep, predictions, linewidth=2, label='Predicted Data', marker='o', color='red') # linestyle='--'
plt.title(f"{COMPAGNY_NAME} days in past: {DAYS_IN_PAST} EPOCHS: {EPOCHS}")
plt.xlabel('Days')
plt.ylabel(f'{COMPAGNY_NAME} share price')
plt.legend()
plt.show()
