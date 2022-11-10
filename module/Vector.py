#
# Very intresting vector class :
# https://gist.github.com/mcleonard/5351452
#
import math


class Vector(object):

    __slots__ = ('x', 'y')

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def norme(self):
        return math.sqrt(self.x**2 + self.y**2)

    def scalar_product(self, v):
        return self.x * v.x + self.y * v.y

    def normalize(self):
        norme = self.norme
        self.x /= norme
        self.y /= norme

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        if isinstance(other, Vector):
            added = tuple(a + b for a, b in zip(self, other))
        elif isinstance(other, (int, float)):
            added = tuple(a + other for a in self)
        else:
            raise ValueError(
                "Addition with type {} not supported".format(type(other)))

        return self.__class__(*added)

    def __repr__(self):
        return f"Vecteur({self.x},{self.y})"

    def __call__(self):
        print(f"called")
