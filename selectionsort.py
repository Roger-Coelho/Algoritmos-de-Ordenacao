a = [25,32,2,15,98,31,77,56,32,1,6]

#Array não ordenado
print(a)

#Selectionsort
for j in range(0,len(a)):
    min = j
    for i in range(j + 1, len(a)):
        if a[i] < a[min]:
            min = i
    a[j], a[min] = a[min], a[j]

#Array ordenado pelo Selectionsort
print(a)