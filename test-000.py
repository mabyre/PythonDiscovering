""" Display pulsieurs graphiques dans des fenêtres différentes
"""
import matplotlib.pyplot as plt
import pandas as pd

# Données exemple (peut être remplacé par vos données réelles)
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
    'Open': [100, 110, 95, 105],
    'High': [120, 115, 100, 110],
    'Low': [90, 100, 92, 98],
    'Close': [110, 105, 98, 102]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Premier graphique dans la première fenêtre
plt.figure()
plt.plot(df['Date'], df['Open'])
plt.title('Graphique 1')
plt.xlabel('Date')
plt.ylabel('Prix')

# Deuxième graphique dans une nouvelle fenêtre
plt.figure()
plt.plot(df['Date'], df['Close'], color='orange')
plt.title('Graphique 2')
plt.xlabel('Date')
plt.ylabel('Prix')

# Afficher les deux fenêtres de graphiques
plt.show()
