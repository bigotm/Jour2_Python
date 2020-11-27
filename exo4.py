# class Vecteur:
#   def __init__(self, x, y):
#      self.x = x
#     self.y = y

# def __str__(self):
#   return "(" + str(self.x) + ", "+str(self.y) + ")"

# vec = Vecteur(-4, 2)
# print(vec)

class Domino:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def affiche_points(self):
        return "Face A: " + str(self.a) + ", Face B: " + str(self.b)

    def total(self):
        return self.a + self.b


def exo():
    d = Domino(4,6)
    print(d.affiche_points())
    x = d.total()
    print(x)

print(exo())
