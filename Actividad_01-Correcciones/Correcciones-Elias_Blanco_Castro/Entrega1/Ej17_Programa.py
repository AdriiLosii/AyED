import timeit
import numpy as np


def suma_vector(v):
    suma = sum(v)

    return suma
    
print("%10s %10s" %("tamaño","tiempo"))


for i in range(10000,1000001,50000):
    v=np.arange(1000)
    t = timeit.Timer("suma_vector(v)","from __main__ import suma_vector,v")
    tiempo_suma = t.timeit(number=1000)
    
    print("%10d %10.3f" % (i, tiempo_suma))


print("La suma de los elementos del vector es ",suma_vector(v))
print("La complejidad de este algoritmo expresado mediante el sistema Big-O es de tipo O(n)")