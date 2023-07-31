def est_pair(nombre):
    return nombre % 2 == 0

try:
    nombre = int(input("Entrez un nombre : "))
    if est_pair(nombre):
        print(f"Le nombre {nombre} est pair.")
    else:
        print(f"Le nombre {nombre} est impair.")
except ValueError:
    print("Vous devez entrer un nombre entier.")
