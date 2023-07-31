def inverse_liste(liste):
    """
    Renverse l'ordre des éléments d'une liste.

    Args:
        liste (list): Une liste contenant les éléments à inverser.

    Returns:
        list: Une nouvelle liste avec les éléments dans l'ordre inverse.
    """
    return liste[::-1]
ma_liste = [1, "test", 0.9867, "Python, c'est génial !"]
nouvelle_liste = inverse_liste(ma_liste)
print(nouvelle_liste)
