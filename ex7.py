def trisel(L):
    n = len(L)
    for i in range(n - 1):
        ind_min = i
        for j in range(i + 1, n):
            if L[j] < L[ind_min]:
                ind_min = j
        L[i], L[ind_min] = L[ind_min], L[i]
    return L


ma_liste = [25, 10, 40, 5, 18]
print("Liste triée :", trisel(ma_liste))
