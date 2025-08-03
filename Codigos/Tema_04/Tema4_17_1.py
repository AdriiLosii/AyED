# Tema4_17_1 Ordenacion quickSort
import random


def quicksort(v, izq, der):
    # inicializacion
    i = izq
    j = der
    pivote = v[random.randint(izq, der)]
    print(pivote)
    # ciclo principal(particion)
    while i <= j:
        while v[i] < pivote:
            i = i+1
        while v[j] > pivote:
            j = j - 1
        if i <= j:
            tmp = v[i]
            v[i] = v[j]
            v[j] = tmp
            i = i+1
            j = j-1
    # fin ciclo principal
    print(v)
    # llamadas recursivas
    if izq < j:
        quicksort(v, izq, j)
    if i < der:
        quicksort(v, i, der)
    return(v)


v = [3, 1, 7, -1, 0, 5]
print(v, '\n')
v = quicksort(v, 0, len(v)-1)
