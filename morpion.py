def afficher_plateau(plateau):
    """
    Affiche le plateau de jeu.

    Args:
        plateau (list): Une liste 2D représentant le plateau de jeu.

    Returns:
        None
    """
    for ligne in plateau:
        print("|".join(ligne))
        print("-----")


def verifier_victoire(plateau, symbole):
    """
    Vérifie s'il y a une victoire pour le symbole donné sur le plateau.

    Args:
        plateau (list): Une liste 2D représentant le plateau de jeu.
        symbole (str): Le symbole (X ou O) à vérifier pour la victoire.

    Returns:
        bool: True si le symbole a gagné, False sinon.
    """
    # Vérifier les lignes
    for ligne in plateau:
        if ligne.count(symbole) == 3:
            return True

    # Vérifier les colonnes
    for col in range(3):
        if all(plateau[i][col] == symbole for i in range(3)):
            return True

    # Vérifier les diagonales
    if all(plateau[i][i] == symbole for i in range(3)) or all(plateau[i][2 - i] == symbole for i in range(3)):
        return True

    return False


def morpion():
    """
    Fonction principale pour jouer au morpion.

    Returns:
        None
    """
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    symboles = ["X", "O"]
    tour = 0

    while True:
        afficher_plateau(plateau)

        joueur = symboles[tour % 2]
        print(f"C'est au tour du joueur {joueur}")

        while True:
            try:
                ligne = int(input("Entrez le numéro de ligne (0, 1 ou 2) : "))
                colonne = int(input("Entrez le numéro de colonne (0, 1 ou 2) : "))

                if plateau[ligne][colonne] == " ":
                    plateau[ligne][colonne] = joueur
                    break
                else:
                    print("Cette case est déjà prise. Essayez à nouveau.")
            except (ValueError, IndexError):
                print("Veuillez entrer un numéro de ligne/colonne valide (0, 1 ou 2).")

        if verifier_victoire(plateau, joueur):
            afficher_plateau(plateau)
            print(f"Le joueur {joueur} a gagné !")
            break

        if all(all(case != " " for case in ligne) for ligne in plateau):
            afficher_plateau(plateau)
            print("Match nul !")
            break

        tour += 1


if __name__ == "__main__":
    morpion()
