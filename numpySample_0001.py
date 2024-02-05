""" ChatGpt is wrong
    you can't reshape
"""
import numpy as np

# Créer un tableau unidimensionnel de 252 éléments (exemple)
tableau_original = np.arange(252)

# Remodeler le tableau pour avoir 256 éléments
tableau_reshaped = np.array(tableau_original)
tableau_reshaped = np.reshape(tableau_original, (256,))

# Afficher le tableau après le remodelage
print(tableau_reshaped)
