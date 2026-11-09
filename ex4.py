L = [10, 4, 7, 12, 5, 20, 30, 4]

maxi = L[0]
mini = L[0]

for x in L:
    if x > maxi:
        maxi = x
    if x < mini:
        mini = x

etendue = maxi - mini
print("Maximum :", maxi)
print("Minimum :", mini)
print("Étendue :", etendue)
