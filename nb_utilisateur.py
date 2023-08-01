def detecter_pair_impair(nombre):
    """
    Détermine si un nombre est pair ou impair et affiche le résultat.

    Args:
        nombre (int): Le nombre entier à vérifier.

    Returns:
        None: La fonction n'a pas de valeur de retour explicite, elle affiche le résultat directement.
    """
    if nombre % 2 == 0:
        print("Le nombre est pair")
    else:
        print("Le nombre est impair")

try:
    nb_utilisateur = int(input("Entrez un nombre entier : "))
    detecter_pair_impair(nb_utilisateur)
except ValueError:
    print("Vous devez entrer un nombre entier valide.")
