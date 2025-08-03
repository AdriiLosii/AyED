import random
import timeit

def primero(v, izq, der):
    # inicializacion
    i = izq
    j = der
    pivote = v[i]

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

    # llamadas recursivas
    if izq < j:
        primero(v, izq, j)
    if i < der:
        primero(v, i, der)
    return(v)

def ultimo(v, izq, der):
    # inicializacion
    i = izq
    j = der
    pivote = v[j]
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

    # llamadas recursivas
    if izq < j:
        ultimo(v, izq, j)
    if i < der:
        ultimo(v, i, der)
    return(v)

def aleatorio(v, izq, der):
    # inicializacion
    i = izq
    j = der
    pivote = v[random.randint(izq, der)]
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
    # llamadas recursivas
    if izq < j:
        aleatorio(v, izq, j)
    if i < der:
        aleatorio(v, i, der)
    return(v)

v = [random.randint(0, 100) for x in range(10)]

tprimero = timeit.timeit("primero(v, 0, len(v)-1)", 
    setup="from __main__ import primero,v", number=10000)
tultimo = timeit.timeit("ultimo(v, 0, len(v)-1)", 
    setup="from __main__ import ultimo,v", number=10000)
taleatorio = timeit.timeit("aleatorio(v, 0, len(v)-1)", 
    setup="from __main__ import aleatorio,v", number=10000)

print("Pivote primer elemento: ",tprimero/10000)
print("Pivote ultimo elemento: ",tultimo/10000)
print("Pivote elemento aleatorio: ",taleatorio/10000)
