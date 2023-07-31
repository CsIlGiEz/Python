import random

# Liste par compréhension avec 1000 nombres aléatoires entre 1 et 100
liste_nombres_aleatoires = [random.randint(1, 100) for _ in range(1000)]

# Méthode 1 : Avec une boucle
jets_inferieurs_a_10 = []
for jet in liste_nombres_aleatoires:
    if jet < 10:
        jets_inferieurs_a_10.append(jet)

# Affichage du nombre de jets inférieurs à 10
print(f"Nombre de jets inférieurs à 10 : {len(jets_inferieurs_a_10)}")

import random

# Liste par compréhension avec 1000 nombres aléatoires entre 1 et 100
liste_nombres_aleatoires = [random.randint(1, 100) for _ in range(1000)]

# Méthode 2 : Avec une compréhension de liste
jets_inferieurs_a_10 = [jet for jet in liste_nombres_aleatoires if jet < 10]

# Affichage du nombre de jets inférieurs à 10
print(f"Nombre de jets inférieurs à 10 : {len(jets_inferieurs_a_10)}")
