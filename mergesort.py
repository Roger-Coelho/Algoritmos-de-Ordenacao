a = [25,32,2,15,98,31,77,56,32,1,6]

#Array não ordenado
print(a)

#Mergesort
def merge(A, aux, esquerda, meio, direita):
    
    #Combina dois vetores ordenados em único vetor
    for k in range(esquerda, direita + 1):
        aux[k] = A[k]
    i = esquerda
    j = meio + 1
    for k in range(esquerda, direita + 1):
        if i > meio:
            A[k] = aux[j]
            j += 1
        elif j > direita:
            A[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            A[k] = aux[j]
            j += 1
        else:
            A[k] = aux[i]
            i += 1

def mergesort(A, aux, esquerda, direita):
    if direita <= esquerda:
        return
    meio = (esquerda + direita) // 2

    # Ordena a primeira metade do arranjo.
    mergesort(A, aux, esquerda, meio)

    # Ordena a segunda metade do arranjo.
    mergesort(A, aux, meio + 1, direita)

    # Combina as duas metades ordenadas anteriormente.
    merge(A, aux, esquerda, meio, direita)


# Testa o algoritmo.
aux = [0] * len(a)
mergesort(a, aux, 0, len(a) - 1)

#Array ordenado pelo Mergesort
print(a)