
# Cette fonction retourne 2 valeurs : resultat, reste
t = [20, 4]
resultat, reste = divmod(*t)
print("Le résultat de la division est", resultat, "avec comme reste", reste)
# Affiche Le résultat de la division est 5 avec comme reste 0


def dire_bonjour_a(prenom, nom):
    print("Bonjour", prenom, nom)


d = {"nom": "Gayerie", "prenom": "David"}
dire_bonjour_a(**d)
# Affiche Bonjour David Gayerie
