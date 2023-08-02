def afficher_triangle(taille):
    """
    Affiche un triangle de la taille spécifiée en utilisant le caractère "#".

    Args:
        taille (int): La taille du triangle.

    Returns:
        None: La fonction affiche le triangle dans la console.
    """
    for i in range(1, taille + 1):
        print("#" * i)

try:
    taille_triangle = int(input("Entrez la taille du triangle : "))
    if taille_triangle <= 0:
        print("La taille du triangle doit être un nombre positif.")
    else:
        afficher_triangle(taille_triangle)
except ValueError:
    print("Vous devez entrer un nombre entier.")
