""" Sample by ChatGpt on a sinus 
"""
import numpy as np
import matplotlib.pyplot as plt

from keras import Sequential
from keras.layers import Dense, LSTM

# Générer des données d'entraînement
time = np.arange(0, 100, 0.1)
sin_wave = np.sin(time) + 0.1 * np.random.normal(size=len(time))

# Préparer les données pour une séquence temporelle
seq_length = 10
X_train, y_train = [], []
for i in range(len(time) - seq_length):
    X_train.append(sin_wave[i:i+seq_length])
    y_train.append(sin_wave[i+seq_length])

X_train = np.array(X_train)
y_train = np.array(y_train)

# Réorganiser les données pour les entrées LSTM [batch, time steps, features]
X_train = np.reshape(X_train, (X_train.shape[0], seq_length, 1))

# Créer le modèle LSTM
model = Sequential([
    LSTM(units=50, return_sequences=True, input_shape=(seq_length, 1)),
    LSTM(units=50),
    Dense(units=1)
])

# Compiler le modèle
model.compile(optimizer='adam', loss='mean_squared_error')

# Entraîner le modèle
model.fit(X_train, y_train, epochs=10, batch_size=16)

# Préparer une nouvelle séquence pour la prédiction
X_new = sin_wave[-seq_length:]
X_new = np.reshape(X_new, (1, seq_length, 1))

# Faire des prédictions avec le modèle entraîné
predicted_y = model.predict(X_new)

# Afficher les prédictions
plt.plot(time[-len(X_new[0]):], sin_wave[-len(X_new[0]):], label='Actual Data')
plt.plot(time[-1] + 0.1, predicted_y[0, 0], marker='o', markersize=8, color='red', label='Predicted Value')
plt.legend()
plt.show()
