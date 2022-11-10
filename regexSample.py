# import du module des expressions régulières
import re

# --------------------------------------------------------------------------


def compare(modèle, chaine):
    # compare la chaîne [chaîne] au modèle [modèle]
    # affichage résultats
    print(f"\nRésultats({chaine},{modèle})")
    match = re.match(modèle, chaine)
    if match:
        print(match.groups())
    else:
        print(f"La chaîne [{chaine}] ne correspond pas au modèle [{modèle}]")


# expression régulières en python
# récupérer les différents champs d'une chaîne
# le modèle : une suite de chiffres entourée de caractères quelconques
# on ne veut récupérer que la suite de chiffres
modèle = r"^.*?(\d+).*?$"

# on confronte la chaîne au modèle
compare(modèle, "xyz1234abcd")
compare(modèle, "12 34")
compare(modèle, "abcd")

# le modèle : une suite de chiffres entourée de caractères quelconques
# on veut la suite de chiffres ainsi que les champs qui suivent et précèdent
modèle = r"^(.*?)(\d+)(.*?)$"

# on confronte la chaîne au modèle
compare(modèle, "xyz1234abcd")
compare(modèle, "12 34")
compare(modèle, "abcd")

# le modèle - une date au format jj/mm/aa
modèle = r"^\s*(\d\d)\/(\d\d)\/(\d\d)\s*$"
compare(modèle, "10/05/97")
compare(modèle, " 04/04/01 ")
compare(modèle, "5/1/01")

# le modèle - un nombre décimal
modèle = r"^\s*([+-]?)\s*(\d+\.\d*|\.\d+|\d+)\s*$"
compare(modèle, "187.8")
compare(modèle, "-0.6")
compare(modèle, "4")
compare(modèle, ".6")
compare(modèle, "4.")
compare(modèle, " + 4")
# fin

# Résultats(xyz1234abcd, ^ .*?(\d+).*?$)
# ('1234',)

# Résultats(12 34, ^ .*?(\d+).*?$)
# ('12',)

# Résultats(abcd, ^ .*?(\d+).*?$)
# La chaîne [abcd] ne correspond pas au modèle [ ^ .*?(\d+).*?$]

# Résultats(xyz1234abcd, ^ (.*?)(\d+)(.*?)$)
# ('xyz', '1234', 'abcd')

# Résultats(12 34, ^ (.*?)(\d+)(.*?)$)
# ('', '12', ' 34')

# Résultats(abcd, ^ (.*?)(\d+)(.*?)$)
# La chaîne [abcd] ne correspond pas au modèle [ ^ (.*?)(\d+)(.*?)$]

# Résultats(10/05/97, ^\s*(\d\d)\/ (\d\d)\/ (\d\d)\s *$)
# ('10', '05', '97')

# Résultats(04/04/01, ^\s*(\d\d)\/ (\d\d)\/ (\d\d)\s *$)
# ('04', '04', '01')

# Résultats(5/1/01, ^\s*(\d\d)\/ (\d\d)\/ (\d\d)\s *$)
# La chaîne [5/1/01] ne correspond pas au modèle [ ^\s*(\d\d)\/ (\d\d)\/ (\d\d)\s *$]

# Résultats(187.8, ^\s*([+-]?)\s*(\d +\.\d*|\.\d+|\d+)\s *$)
# ('', '187.8')

# Résultats(-0.6, ^\s*([+-]?)\s*(\d +\.\d*|\.\d+|\d+)\s *$)
# ('-', '0.6')

# Résultats(4, ^\s*([+-]?)\s*(\d +\.\d*|\.\d+|\d+)\s *$)
# ('', '4')

# Résultats(.6, ^\s*([+-]?)\s*(\d +\.\d*|\.\d+|\d+)\s *$)
# ('', '.6')

# Résultats(4., ^\s*([+-]?)\s*(\d +\.\d*|\.\d+|\d+)\s *$)
# ('', '4.')

# Résultats(+ 4, ^\s*([+-]?)\s*(\d +\.\d*|\.\d+|\d+)\s *$)
# ('+', '4')
