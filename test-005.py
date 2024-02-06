""" annotate on a graph
"""
import matplotlib.pyplot as plt

x= [0, 1, 2, 3]
y = [3.412, 4, 3, 6]

max_x = x[3]
max_y = y[3]

max_xy = ( max_x, max_y )

xytext_position = (x[1] + 0.5, y[1] + 0.5)

# Créer le graphique
fig, ax = plt.subplots()
ax.plot(x, y)

decale_x = x[3] + 0.2 # petit décalage par rapport au point

# Ajouter une annotation simple
ax.annotate('Point important',
            xy=(x[2], y[2]), 
            xytext=( xytext_position ), 
            arrowprops=dict(facecolor='black', arrowstyle='->'))

ax.annotate('Fin de la tendance', 
            xy=(x[1], y[1]), 
            xytext=(0.5, 5.1),
            arrowprops=dict(facecolor='red', arrowstyle='wedge,tail_width=0.7', lw=2))

ax.annotate('Point culminant', 
            xy=max_xy, 
            xytext=(2, 5),   
            arrowprops=dict(facecolor='green', arrowstyle='fancy', lw=1), 
            fontsize=12, 
            fontweight='bold', 
            color='purple')

bbox_props = dict(boxstyle='round', fc='w', ec='k', lw=1)

index = 0

ax.annotate(str(y[index]), (x[index], y[index]), xytext=(x[index] + decale_x, y[index]), bbox=bbox_props)

plt.show()
