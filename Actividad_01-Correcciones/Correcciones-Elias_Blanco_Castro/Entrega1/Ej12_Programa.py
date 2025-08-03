import timeit
import random

print("%10s %10s" % ("tamaño", "lista"))
for i in range(10000, 1000001, 20000):
    prueba = 0
    t1 = timeit.Timer("x[random.randrange(%d)]" %
                     i, "from __main__ import random,x")

    x = list(range(i))
    tiempo_lista = t1.timeit(number=1000)


    print("%10d %10.3f" % (i, tiempo_lista))