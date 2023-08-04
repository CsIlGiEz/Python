import random

# Dimensions de la grille
GRID_WIDTH = 30
GRID_HEIGHT = 15

# Durée de vie maximale des poissons et des requins
FISH_BREED_AGE = 2
FISH_MAX_AGE = 5
SHARK_BREED_AGE = 10
SHARK_MAX_AGE = 20

# Paramètres du modèle
FISH_INITIAL_POPULATION = 50
SHARK_INITIAL_POPULATION = 20

# Les directions de mouvement possibles
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0

    def move(self):
        dx, dy = random.choice(DIRECTIONS)
        self.x = (self.x + dx) % GRID_WIDTH
        self.y = (self.y + dy) % GRID_HEIGHT
        self.age += 1

    def breed(self):
        return Fish(self.x, self.y)

class Shark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0
        self.hunger = 0

    def move(self):
        dx, dy = random.choice(DIRECTIONS)
        self.x = (self.x + dx) % GRID_WIDTH
        self.y = (self.y + dy) % GRID_HEIGHT
        self.age += 1
        self.hunger += 1

    def breed(self):
        return Shark(self.x, self.y)

def initialize():
    fish_population = [Fish(random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
                       for _ in range(FISH_INITIAL_POPULATION)]
    shark_population = [Shark(random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
                        for _ in range(SHARK_INITIAL_POPULATION)]
    return fish_population, shark_population

def main():
    fish_population, shark_population = initialize()

    for step in range(100):  # Nombre d'étapes de la simulation
        # Déplacement des poissons
        for fish in fish_population:
            fish.move()

        # Déplacement des requins
        for shark in shark_population:
            shark.move()

        # Interaction poissons-requins
        for shark in shark_population:
            for fish in fish_population[:]:
                if shark.x == fish.x and shark.y == fish.y:
                    shark.hunger = 0
                    fish_population.remove(fish)

        # Reproduction des poissons et des requins
        new_fish_population = [fish.breed() for fish in fish_population if fish.age >= FISH_BREED_AGE and fish.age < FISH_MAX_AGE]
        new_shark_population = [shark.breed() for shark in shark_population if shark.age >= SHARK_BREED_AGE and shark.age < SHARK_MAX_AGE and shark.hunger < 3]

        fish_population.extend(new_fish_population)
        shark_population.extend(new_shark_population)

        # Supprimer les poissons et requins trop âgés
        fish_population = [fish for fish in fish_population if fish.age < FISH_MAX_AGE]
        shark_population = [shark for shark in shark_population if shark.age < SHARK_MAX_AGE]

        # Affichage
        print(f"Step: {step}, Fish: {len(fish_population)}, Sharks: {len(shark_population)}")

if __name__ == "__main__":
    main()
