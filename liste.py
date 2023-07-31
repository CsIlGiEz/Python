def somme_liste_nombres(liste):
    """
    Calcule la somme de tous les éléments d'une liste de nombres.

    Args:
        liste (list): Une liste de nombres.

    Returns:
        int or float: La somme de tous les éléments de la liste.
    """
    somme = 0
    for nombre in liste:
        somme += nombre
    return somme

try:
    taille_liste = int(input("Entrez le nombre d'éléments dans la liste : "))
    if taille_liste <= 0:
        print("La taille de la liste doit être un nombre positif.")
    else:
        liste_nombres = []
        for i in range(taille_liste):
            nombre = float(input(f"Entrez l'élément {i + 1} : "))
            liste_nombres.append(nombre)

        resultat = somme_liste_nombres(liste_nombres)
        print(f"La somme des éléments de la liste est : {resultat}")
except ValueError:
    print("Vous devez entrer un nombre entier pour la taille de la liste et des nombres valides pour les éléments.")

