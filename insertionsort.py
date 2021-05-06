a = [25,32,2,15,98,31,77,56,32,1,6]

#Array não ordenado
print(a)

#Insertionsort
for j in range(1,len(a)):
    chave = a[j]
    i = j - 1
    while i >= 0 and a[i] > chave:
        a[i + 1] = a[i]
        i = i -1
    a[i + 1] = chave

#Array ordenado pelo Insertionsort
print(a)