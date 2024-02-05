import numpy
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import LSTM, Dense

# Création d'un modèle séquentiel LSTM à des fins d'illustration
model = Sequential([
    LSTM(10, input_shape=(5, 1), activation='relu'),
    Dense(1)
])

# Compilez le modèle
model.compile(optimizer='adam', loss='mean_squared_error')

# Générez des données d'entrée fictives pour l'illustration
input_data = numpy.random.random((10, 5, 1))

# Utilisez la méthode predict pour faire des prédictions
predictions = model.predict(input_data)

# La variable 'input_data' représente votre séquence actuelle.
# Utilisez-la pour prédire la valeur du prochain coup.
next_input = numpy.random.random((1, 5, 1))  # Exemple de séquence pour le prochain coup
next_prediction = model.predict(next_input)

# Affichez les prédictions
print("Predictions sur la séquence actuelle :\n", predictions)
print("Prédiction pour le prochain coup :\n", next_prediction)
