#
# import module.Vector as vect no no no !
# v1 = vect.Vector(2, 3)
#
from module.Vector import *

v1 = Vector(2, 3)
print(v1)
print(v1.norme)

v1.normalize()
print(v1)
print('v1.x: ', v1.x, 'v1.y: ', v1.y)

v1 = Vector(2, 3)
v2 = Vector(2, 3)
v3 = v2.scalar_product(v1)
print(v3)

# Error: Vector object is not iterable !
# v4 = v2 + v3
# print(v4)

# Vecteur(2, 3)
# 3.605551275463989
# Vecteur(0.5547001962252291, 0.8320502943378437)
# v1.x:  0.5547001962252291 v1.y:  0.8320502943378437
# 13
