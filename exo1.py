
def chiffrePortebonheur(nb):
    s=0
    for i in nb:
        s += int(i)*int(i)
        if s > 10:
            s += int(i) * int(i)
    if s == 1:
        print("Votre chiffre est porte bonheur")
    elif(s < 10 & s>1) :
        print("Votre chiffre n'est pas porte bonheur")
    return s



nombre = input("Rentrer un nombre: ")



print(chiffrePortebonheur(nombre))