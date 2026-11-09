def moyenne(L):
    if len(L) == 0:
        return 0
    somme = 0
    for x in L:
        somme += x
    return somme / len(L)
notes = [12, 15, 10, 18, 5]
print("Moyenne :", moyenne(notes))