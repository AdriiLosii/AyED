import timeit
import random

print("%10s %10s   %10s" % ("tamaño", "lista", "diccionario"))

for i in range(10000, 1000001, 20000):

    t = timeit.Timer("random.randrange(%d) in x" %i, "from __main__ import random,x")

    x = list(range(i))
    tiempo_lista = t.timeit(number=1000)

    x = {j: None for j in range(i)}
    tiempo_diccionario = t.timeit(number=1000)
    
    print("%10d %10.3f %10.3f" % (i, tiempo_lista, tiempo_diccionario))
