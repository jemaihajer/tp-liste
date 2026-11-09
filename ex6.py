def maximum(L):
    maxi = L[0]
    ind_max = 0
    for i in range(1, len(L)):
        if L[i] > maxi:
            maxi = L[i]
            ind_max = i
    return maxi, ind_max

ma_liste = [14, 8, 25, 19, 3]
val, pos = maximum(ma_liste)
print("Valeur max :", val, "indice :", pos)
