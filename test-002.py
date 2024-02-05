import matplotlib.pyplot as plt
import numpy as np

# Données exemple (peut être remplacé par vos données réelles)
x = np.linspace(0, 10, 100)
signal1 = np.sin(x)
signal2 = 0.5 * np.cos(x)

# Créer la figure et le sous-plot
fig, ax = plt.subplots(figsize=(8, 6))

# Tracer les deux signaux
ax.plot(x, signal1, label='Signal 1', color='blue')
ax.plot(x, signal2, label='Signal 2', color='green')

# Colorier la surface en vert (signal1 > signal2)
ax.fill_between(x, signal1, signal2, where=(signal1 > signal2), interpolate=True, color='green', alpha=0.3, label='Surface verte')

# Colorier la surface en rouge (signal1 < signal2)
ax.fill_between(x, signal1, signal2, where=(signal1 < signal2), interpolate=True, color='red', alpha=0.3, label='Surface rouge')

# Ajouter une légende
ax.legend()

# Ajouter des titres et des étiquettes d'axe
ax.set_title('Surface entre deux signaux')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Afficher la fenêtre
plt.show()
