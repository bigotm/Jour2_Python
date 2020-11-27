def generateur():
    liste="abcdef"
    return liste
    i = 0
    while i < len(liste):
        print(liste[i] +","+ liste[i]+",",end="")
        i += 1

gen = generateur()

print(gen)

