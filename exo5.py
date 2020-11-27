#EXO2 TP5

class CompteBancaire:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde

    def affiche(self):
        return "Le solde du compte de "+str(self.nom)+" est de "+str(self.solde)

    def depot(self, somme):
        self.solde += somme
        return self.solde

    def retrait(self, somme):
        self.solde -= somme
        return self.solde



def exo():
    compte1 = CompteBancaire("Jean",100)
    compte1.depot(1000)
    print(compte1.affiche())
    compte1.retrait(1000)
    print(compte1.affiche())

print(exo())
