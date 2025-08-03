import timeit

lista1=list(range(0,100))
lista2=list(range(0,500000))

def prueba1():
    i=lista1[0]

def prueba2():
    i=lista2[400000]


tiempo1=timeit.Timer("prueba1()","from __main__ import prueba1")
print("Prueba1: ", tiempo1.timeit(10000),"segundos")

tiempo2=timeit.Timer("prueba2()","from __main__ import prueba2")
print("Prueba2: ", tiempo2.timeit(10000),"segundos")
