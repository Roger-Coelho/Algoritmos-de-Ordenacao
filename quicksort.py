a = [25,32,2,15,98,31,77,56,32,1,6]

#Array não ordenado
print(a)

#Partition
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

#Função de chamada do Quicksort
def quicksort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quicksort(array, start, p-1)
    quicksort(array, p+1, end)


quicksort(a, 0, len(a) - 1)

#Array ordenado pelo Quicksort
print(a)