def produit_de_valeurs_absolues(a, b):
    """
    Calcule le produit des valeurs absolues de deux nombres a et b.

    Cette fonction prend deux nombres a et b en argument, calcule le produit de leurs valeurs absolues,
    et renvoie le résultat.

    Args:
        a (int or float): Le premier nombre.
        b (int or float): Le deuxième nombre.

    Returns:
        int or float: Le produit des valeurs absolues de a et b.
    """
    # Prend la valeur absolue de a si elle est négative
    if a < 0:
        a = -a

    # Prend la valeur absolue de b si elle est négative
    if b < 0:
        b = -b

    # Renvoie le produit des valeurs absolues de a et b
    return a * b


try:
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))

    resultat = produit_de_valeurs_absolues(nombre1, nombre2)
    print(f"Le produit des valeurs absolues est : {resultat}")
except ValueError:
    print("Vous devez entrer des nombres valides.")
