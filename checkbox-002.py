import numpy
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

fig, (ax1, ax2) = plt.subplots( 2, 1 ) 

# Graphiques
x = numpy.linspace(0, 10, 100)
y1 = numpy.sin(x)
y2 = numpy.cos(2*x)

ax1.set_title('Fenêtre de Graphiques')
ax1.plot(x, y1)
ax2.plot(x, y2)

# Créer une nouvelle figure et des axes pour les cases à cocher
fig_checkbox, ax_checkbox = plt.subplots()
ax_checkbox.set_title('Fenêtre de Cases à cocher')

# Créer les cases à cocher
checkbox_labels = ['Graphique 1', 'Graphique 2']
checkbox = CheckButtons(ax_checkbox, checkbox_labels)

# Tracer les graphiques initiaux
lines = []
lines.append( ax1.plot(x, y1) )
lines.append( ax2.plot(x, y2) )

def update_visibility(label):
    index = checkbox_labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()   

# Associer la fonction update_visibility à chaque case à cocher
checkbox.on_clicked(update_visibility)

plt.show()
