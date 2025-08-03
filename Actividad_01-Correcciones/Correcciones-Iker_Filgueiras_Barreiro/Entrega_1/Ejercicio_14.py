import timeit

lista=list(range(0,1000005))
diccionario= {"d"+str(i):i for i in range (0,1000005)}

def prueba1(toDel):
    del lista[toDel]

def prueba2(dToDel):
    del diccionario[dToDel]

toDel = 1

dToDel = "d"+str(toDel)

print("Prueba para indice: ",toDel)

tiempo1 = timeit.Timer("prueba1(toDel)", "from __main__ import prueba1, toDel")

print("Prueba listas: ",tiempo1.timeit(1)," segundos")

tiempo2 = timeit.Timer("prueba2(dToDel)", "from __main__ import prueba2, dToDel")

print("Prueba diccionario: ",tiempo2.timeit(1)," segundos")