""" Use of TensorFlow and Keras

    Here I try to make my own signal y_data
"""
import numpy as np
import matplotlib.pyplot as plt

from keras import Sequential
from keras.layers import Dense

# ------------
# Prepare data
# ------------
# my own data signal
#
y_data = [2.0, 4.0, 3.0, 5.0, 5.0, 5.0, 5.0, 6.0, 4.0, 
          4.0,]

x_train = np.arange(0,len(y_data))
y_train = np.array(y_data, dtype=np.float32)

# ---------------
# Construct model
# ---------------
model = Sequential([
    Dense(units=1, input_shape=[1],) # Dense layer with 1 neurone
])

# Compile model before training or prediction
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(x_train, y_train, epochs=25, batch_size=16, verbose=0)

# -------------------
# Make the prediction
# -------------------
predictions = model.predict(y_train)

# ---------------
# Display results
# ---------------
print("Predictions:\n", predictions)

# Plot the Predictions
plt.plot(y_train, color='black', label=f"y_train")
plt.plot(predictions, color='green', label=f"predictions")
plt.title(f"Title")
plt.xlabel('x', color='b')
plt.ylabel('y', color='green')
plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
plt.legend
plt.show()
