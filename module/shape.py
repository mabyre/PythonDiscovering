# Module shapes de dessin de formes avancées
# à l'aide d'une tortue
# Auteur : Sébastien Combéfis
# Version : 25 aout 2015

from turtle import *

def polygon(nbsides, side, col='black'):
    color(col)
    angle = 360 / nbsides
    i = 0
    while i < nbsides:
        forward(side)
        left(angle)
        i += 1

def square(side, col='black'):
    polygon(4, side, col)