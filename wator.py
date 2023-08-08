import os
from random import choice, randint
from typing import List
from time import sleep


class Monde:
    def __init__(self, largeur: int, hauteur: int) -> None:
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [[None for _ in range(largeur)] for _ in range(hauteur)]

    def afficher_monde(self):
        """Fonction qui permet d'afficher le monde dans le terminal
        """
        for ligne in self.grille:
            for case in ligne:
                if isinstance(case, Poisson):
                    print("🐠", end="")
                elif isinstance(case, Requin):
                    print("🦈", end="")
                else:
                    print("  ", end="")
            print("\n")

    def peupler(self, nb_poisson: int, nb_requin: int) -> None:
        """
        Méthode qui permet d'ajouter des poissons et des requins dans notre monde
        :param nb_poisson: Nombre de poisson à ajouter dans notre monde
        :param nb_requin: Nombre de requin à ajouter dans notre monde
        """
        for _ in range(nb_poisson):
            x_rand = randint(0, self.largeur - 1)
            y_rand = randint(0, self.hauteur - 1)

            while self.grille[y_rand][x_rand] is not None:
                x_rand = randint(0, self.largeur - 1)
                y_rand = randint(0, self.hauteur - 1)
            self.grille[y_rand][x_rand] = Poisson(x_rand, y_rand)

        for _ in range(nb_requin):
            x_rand = randint(0, self.largeur - 1)
            y_rand = randint(0, self.hauteur - 1)

            while self.grille[y_rand][x_rand] is not None:
                x_rand = randint(0, self.largeur - 1)
                y_rand = randint(0, self.hauteur - 1)
            self.grille[y_rand][x_rand] = Requin(x_rand, y_rand)

    def jouer_un_tour(self) -> None:
        for ligne in self.grille:
            for case in ligne:
                if isinstance(case, Poisson) or isinstance(case, Requin):
                    case.vivre_une_journee(self)


class Poisson:
    nb_poissons = 0

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.compteur_repro = 0
        Poisson.nb_poissons += 1

    def __del__(self):
        Poisson.nb_poissons -= 1

    def deplacement_possible(self, monde: Monde) -> list:
        coup_possibles = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_x, new_y = self.x + i, self.y + j
                if (
                        0 <= new_x < monde.largeur
                        and 0 <= new_y < monde.hauteur
                        and monde.grille[new_y][new_x] is None
                ):
                    coup_possibles.append((new_x, new_y))
        return coup_possibles

    def se_deplacer(self, monde: Monde) -> None:
        coups_possibles = self.deplacement_possible(monde)
        if len(coups_possibles) != 0:
            coup_a_jouer = choice(coups_possibles)
            x_coup, y_coup = coup_a_jouer
            x_preced, y_preced = self.x, self.y

            self.x, self.y = x_coup, y_coup
            monde.grille[y_coup][x_coup] = self

            if self.compteur_repro >= 5:
                monde.grille[y_preced][x_preced] = Poisson(x_preced, y_preced)
                self.compteur_repro = 0
            else:
                monde.grille[y_preced][x_preced] = None

    def vivre_une_journee(self, monde: Monde) -> None:
        self.compteur_repro += 1
        self.se_deplacer(monde)


class Requin:
    nb_requins = 5

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.compteur_repro = 0
        self.energie = 5  # Ajout de l'attribut énergie
        Requin.nb_requins += 1

    def __del__(self):
        Requin.nb_requins -= 1

    def deplacement_possible(self, monde: Monde) -> list:
        coup_possibles = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_x, new_y = self.x + i, self.y + j
                if (
                        0 <= new_x < monde.largeur
                        and 0 <= new_y < monde.hauteur
                        and monde.grille[new_y][new_x] is None
                ):
                    coup_possibles.append((new_x, new_y))
        return coup_possibles

    def trouver_proies(self, monde: Monde) -> List:
        proies_possibles = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_x, new_y = self.x + i, self.y + j
                if (
                        0 <= new_x < monde.largeur
                        and 0 <= new_y < monde.hauteur
                        and isinstance(monde.grille[new_y][new_x], Poisson)
                ):
                    proies_possibles.append((new_x, new_y))
        return proies_possibles

    def se_deplacer(self, monde: Monde) -> None:
        coups_possibles = self.deplacement_possible(monde)
        if len(coups_possibles) != 0:
            coup_a_jouer = choice(coups_possibles)
            x_coup, y_coup = coup_a_jouer
            x_preced, y_preced = self.x, self.y

            self.x, self.y = x_coup, y_coup
            monde.grille[y_coup][x_coup] = self
            monde.grille[y_preced][x_preced] = None

    def manger(self, monde: Monde) -> None:
        proies_possibles = self.trouver_proies(monde)
        if len(proies_possibles) != 0:
            proie_a_manger = choice(proies_possibles)
            x_proie, y_proie = proie_a_manger

            self.energie += 2
            monde.grille[y_proie][x_proie] = None

    def vivre_une_journee(self, monde: Monde) -> None:
        self.compteur_repro += 1
        self.energie -= 1

        if self.energie <= 0:
            monde.grille[self.y][self.x] = None
            return

        if len(self.trouver_proies(monde)) != 0:
            self.manger(monde)
        else:
            self.se_deplacer(monde)


world = Monde(60, 15)
world.peupler(100, 18)  # Mettez 10 poissons et 3 requins au départ

tour = 0  # Initialisation du compteur de tours

while True:

    if tour % 1 == 0: 
        for _ in range(10):  # Ajouter 10 poissons à chaque fois
            x_rand = randint(0, world.largeur - 1)
            y_rand = randint(0, world.hauteur - 1)

            while world.grille[y_rand][x_rand] is not None:
                x_rand = randint(0, world.largeur - 1)
                y_rand = randint(0, world.hauteur - 1)
            world.grille[y_rand][x_rand] = Poisson(x_rand, y_rand)

        for _ in range(3):  # Ajouter 3 requins à chaque fois
            x_rand = randint(0, world.largeur - 1)
            y_rand = randint(0, world.hauteur - 1)

            while world.grille[y_rand][x_rand] is not None:
                x_rand = randint(0, world.largeur - 1)
                y_rand = randint(0, world.hauteur - 1)
            world.grille[y_rand][x_rand] = Requin(x_rand, y_rand)

    world.jouer_un_tour()  # Exécute un tour de la simulation
    world.afficher_monde()
    print("Nombre de poissons:", Poisson.nb_poissons)
    print("Nombre de requins:", Requin.nb_requins)
    sleep(0.03)  # Attendre 0.03 secondes entre chaque tour
    os.system("cls")

    tour += 1  # Incrémenter le compteur de tours
