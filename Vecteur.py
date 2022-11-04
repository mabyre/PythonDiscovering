import math


class Vecteur:

    __slots__ = ('x', 'y')

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def norme(self):
        return math.sqrt(self.x**2 + self.y**2)

    def calculer_produit_scalaire(self, v):
        return self.x * v.x + self.y * v.y

    def normaliser(self):
        norme = self.norme
        self.x /= norme
        self.y /= norme

    def __repr__(self):
        return f"Vecteur({self.x},{self.y})"

    def __call__(self):
        print(f"called")
