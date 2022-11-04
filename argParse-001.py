"""
    argparse – Parseur d’arguments, d’options, et de sous-commandes de ligne de commande

    "store_true" signifie que si l’option est précisée la valeur True est assignée à args.verbose. 
    Ne rien préciser implique la valeur False.

    En debug, si les paramètres passés au programme ne correspondent pas à la description 
    crée dans "parser" une exception est levée. Inutile de chercher à faire un try: except, 
    l'exception levée est un "SystemExit" et le message indique alors clairement ce que 
    l'utilisateur doit faire.
"""
import argparse

parser = argparse.ArgumentParser(description="Calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")

args = parser.parse_args()

answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))

print("Suite du programme !")


# ------------------------
# > argParse-001.py --help
# ------------------------
# usage: argParse-001.py[-h][-v | -q] x y
#
# Calculate X to the power of Y
#
# positional arguments:
#   x              the base
#   y              the exponent
#
# optional arguments:
#   -h, --help     show this help message and exit
#   -v, --verbose
#   -q, --quiet
