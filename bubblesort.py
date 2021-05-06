a = [25,32,2,15,98,31,77,56,32,1,6]

#Array não ordenado
print(a)

#Bubblesort
for j in range(1, len(a)):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            temp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = temp

#Array ordenado pelo Bubblesort
print(a)