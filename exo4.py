#EXO 1 du TP5

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
