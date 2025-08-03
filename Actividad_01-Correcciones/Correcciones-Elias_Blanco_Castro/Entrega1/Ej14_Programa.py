import timeit
import random

print("%10s %10s   %10s" % ("tamaño", "lista", "diccionario"))
for i in range(10000, 1000001, 20000):
    t1 = timeit.Timer("del x[random.randrange(%d) in x]" %
                     i, "from __main__ import random,x")
    t2 = timeit.Timer("y.pop(random.randrange(%d) in y, 0)" %
                     i, "from __main__ import random,y")
    x = list(range(i))
    tiempo_lista = t1.timeit(number=1000)
    y = {j: None for j in range(i)}
    tiempo_diccionario = t2.timeit(number=1000)
    print("%10d %10.3f %10.3f" % (i, tiempo_lista, tiempo_diccionario))