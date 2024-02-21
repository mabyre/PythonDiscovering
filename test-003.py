""" ChatGpt 
    synchroniser deux signaux sur un zoom
    et dit moi chatgpt, faire un zoom avec la molette de la souris c'est posible ?
"""
import matplotlib.pyplot as plt
import numpy as np

# Activer le zoom avec la molette de la souris
def on_scroll(event):
    if event.name == 'scroll_event':
        factor = 1.2  # Facteur de zoom
        if event.button == 'up':
            factor = 1 / factor  # Zoom arrière pour la molette vers le haut
        ax1.set_xlim(ax1.get_xlim()[0], ax1.get_xlim()[1] * factor)
        ax2.set_xlim(ax2.get_xlim()[0], ax2.get_xlim()[1] * factor)
        fig.canvas.draw_idle()

# Données à tracer
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Créer la grille de sous-tracés
fig = plt.figure()

ax1 = plt.subplot2grid((2, 1), (0, 0))
ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)  # Partage de l'axe x <--- ###

# Tracé du premier graphique
ax1.plot(x, y1, label='Sin(x)')
ax1.set_ylabel('Amplitude')

# Tracé du deuxième graphique
ax2.plot(x, y2, label='Cos(x)')
ax2.set_xlabel('X')
ax2.set_ylabel('Amplitude')

# Afficher la légende
ax1.legend()
ax2.legend()

fig.canvas.mpl_connect('scroll_event', on_scroll)

# Afficher les tracés
plt.show()
