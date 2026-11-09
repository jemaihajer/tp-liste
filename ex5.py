def searchL(element, L):
    for k in range(len(L)):
        if L[k] == element:
            return k
    return False
ma_liste = [10, 20, 30, 40]
print("Indice de 20 :", searchL(20, ma_liste))  
print("Indice de 50 :", searchL(50, ma_liste)) 
