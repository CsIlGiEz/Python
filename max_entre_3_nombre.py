def trouver_nombre_le_plus_grand(nombre1, nombre2, nombre3):
    return max(nombre1, nombre2, nombre3)

try:
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    nombre3 = float(input("Entrez le troisième nombre : "))

    plus_grand = trouver_nombre_le_plus_grand(nombre1, nombre2, nombre3)

    print(f"Le nombre le plus grand est : {plus_grand}")
except ValueError:
    print("Vous devez entrer des nombres valides.")
