spisok = [2,2,2,3,4,5,6,6,6,6,6,6,6,6,4,3,6,6,4]
dct = {}
for i in spisok:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
print(dct)