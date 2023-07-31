def afficher_fizz_fuzz():
    """
    Affiche les nombres de 1 à 100 avec deux exceptions :
    les nombres divisibles par 3 sont remplacés par "Fizz" et
    les nombres divisibles par 5 sont remplacés par "Fuzz".
    """
    for nombre in range(1, 101):
        if nombre % 3 == 0 and nombre % 5 == 0:
            print("FizzFuzz")
        elif nombre % 3 == 0:
            print("Fizz")
        elif nombre % 5 == 0:
            print("Fuzz")
        else:
            print(nombre)

afficher_fizz_fuzz()
