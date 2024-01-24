""" matPlot-0xx series will lead us to predictive of linear series

    Using Pandas to read csv file, bytespdate2num no more needed

    # install python 3.11.1
    C:\\Users\\userxxx\\AppData\\Local\\Programs\\Python\\Python311

    # install
    >pip install scikit-learn
    NO: >pip install keras tensorFlow will uninstall this version to resintall his own
    >pip install tensorflow
    
    Version de Python :3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)]
    numpy: 1.26.3
    pandas: 2.1.4
    sklearn: 1.3.2

    Keras: 2.15.0
    Tensorflow: 2.15.0
    
    Difficulties to install keras and tensorflow somedays keras is integrated to tensorflow somedays installing keras crashed due to tensorflow chatgpt says there is no version of tensorflow copatible with pyhton 3.12 grrrr
    
    https://stackoverflow.com/questions/77236398/issue-installing-tensorflow-on-windows-11-with-python-3-12-0
    TensorFlow currently support python 3.11 so try downgrading your python edition 
    
    https://keras.io/guides/
    LSTM: Long Short-Term Memory

    Chez boursorama dans le grapqhique du cours de l'action, il y a un bouton télécharger
    pour exporter les données au format .txt séparées par un \t

    https://www.geeksforgeeks.org/convert-a-numpy-array-to-a-pandas-series/
    Convert a NumPy array to a Pandas series

    https://geekyhumans.com/how-to-predict-us-stock-price-using-python/
    How to predict US Stock Price using Python?
    https://geekyhumans.com/fr/prediction-boursiere-avec-python/
    French: Prédiction boursière avec Python

    https://clemovernet.wordpress.com/2020/01/01/tensorflow-2-prediction-dun-cours-de-bourse-version-simple/
    Some other example of using keras.models.Sequential
    Explain the split data into windows

    https://github.com/JosueAfouda/Analyse-quantitative/blob/master/Prediction%20du%20prix%20des%20actions.ipynb

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
FILE_NAME = r'.\datas\CARMAT_2024-01-19 (1).txt'

COMPAGNY_NAME = 'CARMAT_2024'

# how many days we want to look at the past to predict
PREDICTION_DAYS = 60

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
for x in range(PREDICTION_DAYS, len(scaled_data)):
    x_train.append(scaled_data[x-PREDICTION_DAYS:x, 0])
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
model.fit(x_train, y_train, epochs=25, batch_size=32)

# Evaluate the trained model should be done with x_test
score = model.evaluate(x_train, y_train, verbose=0)
print(f'Test loss: {score}')

# ----------
# Test model
# ----------
y_data_test = pandas.Series(y_data)
actual_prices = y_data_test
total_dataset = pandas.concat((y_data_test, y_data_test), axis=0)

model_input = total_dataset[len(total_dataset) - len(y_data_test) - PREDICTION_DAYS:].values
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
for x in range(PREDICTION_DAYS, len(model_input)):
    x_test.append(model_input[x-PREDICTION_DAYS:x, 0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

predicted_price = model.predict(x_test)
predicted_price = scaler.inverse_transform(predicted_price)

# --------------------------
# make the prediction
#
all_days = len(y_data)

real_data = np.array(y_data)
real_data = np.reshape(real_data, (all_days, 1 , 1))

prediction = model.predict(real_data)
prediction = scaler.inverse_transform(prediction)

# print(f"Prediction: {prediction}")

# take last point as prediction
prediction2 = prediction[all_days - 1]

print(f"Prediction: {prediction2}")

# plot the test Predictions
plt.plot(actual_prices, color='midnightblue', label=f"Actual {COMPAGNY_NAME} price")
plt.plot(predicted_price, color='green', label=f"Predicted {COMPAGNY_NAME} Price")
plt.scatter(all_days, prediction2, color='red', label=f"Prediction2", marker='s')
plt.plot(prediction, color='orangered', label=f"Prediction")
plt.title(f"{COMPAGNY_NAME} predic days {PREDICTION_DAYS}")
plt.xlabel('Days')
plt.ylabel(f'{COMPAGNY_NAME} share price')
plt.legend
plt.show()
