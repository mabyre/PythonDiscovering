#
# Objects concepts in Python
#
# Polymorphism, same function different behavior
#

class Animals:
    def __init__(self, name):
        self.name = name

    def Moving(self):
        pass  # should be written by subclass


class Lyon(Animals):

    def Moving(self):
        print('Lyon Running')


class Aigle(Animals):

    def Moving(self):
        print('Aigle Flying')


myLyon = Lyon("Dactary")
myAigle = Aigle("Pygargue")

myLyon.Moving()
myAigle.Moving()
