import turtle

# Fonction pour dessiner un carré de 100px sur 100px
def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

# Fonction pour dessiner un pentagone de 10px de côté
def draw_pentagon():
    for _ in range(5):
        turtle.forward(90)
        turtle.left(72)

def draw_boat():
    for _ in range(6):
        turtle.forward(100) #Ici une instruction permettant d'avancer de 100px
        turtle.left(30) #Ici une instruction permettant de tourné a gauche de 30px
        turtle.forward(50)
        turtle.left(150)
        turtle.forward(187)
        turtle.left(150)
        turtle.forward(50)

     #voile
        turtle.penup()
        turtle.goto(230, 30)  # Positionnez la tortue à une position appropriée pour la première voile
        turtle.pendown()
        turtle.left(120)
        turtle.forward(100)
        turtle.right(137)
        turtle.forward(140)
        turtle.right(133)
        turtle.forward(188)
        turtle.right(132)
        turtle.forward(147)
        turtle.end_fill() # permet d'indiquer à la tortue que nous n'avons plus besoin de remplir les nouvelles formes
        turtle.done() # permet d'indiquer à la tortue que nous avons fini le dessin

# Réglages de la tortue
turtle.speed(8)

turtle.penup()
turtle.goto(-180, 0)
turtle.pendown()
# Dessiner le carré
draw_square()

# Déplacer la tortue pour dessiner le pentagone
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Dessiner le pentagone
draw_pentagon()

# Déplacer la tortue pour dessiner le bateau
turtle.penup()
turtle.goto(180, 0)
turtle.pendown()

# Dessiner le bateau
draw_boat()

# Afficher le dessin et attendre que l'utilisateur ferme la fenêtre
turtle.done()
