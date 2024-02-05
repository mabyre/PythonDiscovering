""" Given by ChatGpt
    add an amplitude
"""
import numpy as np
import matplotlib.pyplot as plt

from keras import Sequential
from keras.layers import LSTM, Dense # Long Short-Term Memory layer

# Générer des données d'entraînement (ex : signal sinusoïdal)
amplitude = 1.237
time = np.arange(0, 100, 0.1)
sin_wave = amplitude * np.sin(time) + 0.1 * np.random.normal(size=len(time))

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
model.fit(X_train, y_train, epochs=10, batch_size=16) # epochs=100

# Préparer les données pour la prédiction
X_new = sin_wave[-seq_length:]
X_new = np.reshape(X_new, (1, seq_length, 1))

# Faire des prédictions pour les n prochaines valeurs
n_predictions = 45
predictions = []

for x in range(n_predictions):
    # Faire une prédiction avec le modèle
    #predicted_value = model.predict(X_new)
    predicted_value = model(X_new, training=False)

    # Ajouter la prédiction à la liste des prédictions
    predictions.append(predicted_value[0, 0])

    # Mettre à jour la séquence d'entrée pour inclure la nouvelle prédiction
    X_new = np.append(X_new[:, 1:, :], [[[predicted_value[0, 0]]]], axis=1)


# Afficher les résultats
plt.plot(time, sin_wave, label='Actual Data')
plt.plot(time[-1] + 0.1 * np.arange(1, n_predictions + 1), predictions, label='Predicted Data', linestyle='--', color='red')
plt.legend()
plt.show()
