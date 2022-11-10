# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====
#!/usr/bin/env python3
#
# Ajouter au path systeme - Ne fonctionne pas ... oui cela ajoute au path mais
# uniquement pour le programme en cours d'exécution
# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====

""" 
 Example - 2021
"""
import os
import sys

print('Python sys.path:')
print(sys.path)

wait = input("Press <ENTER> to continue.")

# os.system("pause")

sys.path.append(
    'C:\\Users\\Mabyre\\AppData\\Local\\Programs\\Python\\Python38\\Scripts')

print('Python sys.path:')
print(sys.path)

wait = input("Press <ENTER> to continue.")
