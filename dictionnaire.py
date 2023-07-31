def chercher_definition(dictionnaire, mot):
    """
    Cherche la définition d'un mot dans le dictionnaire.

    Args:
        dictionnaire (dict): Un dictionnaire contenant les mots et leurs définitions.
        mot (str): Le mot à rechercher dans le dictionnaire.

    Returns:
        str: La définition du mot si trouvé, ou "Nous ne connaissons pas ce mot" sinon.
    """
    if mot in dictionnaire:
        return dictionnaire[mot]
    else:
        return "Nous ne connaissons pas ce mot"

# Dictionnaire contenant les mots et leurs définitions
mon_dictionnaire = {
    "Python": "Un langage de programmation interprété, orienté objet et de haut niveau.",
    "Intelligence artificielle": "La simulation de processus intelligents par des machines.",
    "Science des données": "L'extraction de connaissances à partir de données brutes."
}

try:
    mot_recherche = input("Entrez un mot : ")
    definition = chercher_definition(mon_dictionnaire, mot_recherche)
    print(definition)
except Exception as e:
    print("Erreur :", e)
