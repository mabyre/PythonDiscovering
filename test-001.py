""" Plusieurs graphique dans la même fenêtre
    avec des case à cocher pour afficher ou non les graphiques
"""
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
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

# Créer la figure et le sous-plot
fig, ax = plt.subplots(figsize=(10, 5))

plt.subplots_adjust(
    left=0.11, 
    bottom=0.24, 
    right=0.90,
    top=0.90, wspace=0.2, 
    hspace=0)

# Tracer les graphiques initiaux
lines = []
lines.append(ax.plot(df['Date'], df['Open'], label='Open')[0])
lines.append(ax.plot(df['Date'], df['High'], label='High')[0])
lines.append(ax.plot(df['Date'], df['Low'], label='Low')[0])
lines.append(ax.plot(df['Date'], df['Close'], label='Close')[0])

# Ajouter des cases à cocher
ax_checkbox = plt.axes([0.1, 0.02, 0.3, 0.15], facecolor='lightgoldenrodyellow') # (left, bottom, width, height)
checkbox = CheckButtons(ax_checkbox, ['Open', 'High', 'Low', 'Close'], (True, True, True, True))

# Fonction pour gérer la visibilité des lignes en fonction des cases à cocher
def update_visibility(label):
    index = ['Open', 'High', 'Low', 'Close'].index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()

# Lier la fonction de mise à jour à la fonction des cases à cocher
checkbox.on_clicked(update_visibility)

# Ajouter une légende
ax.legend()

# Afficher la fenêtre
plt.show()
