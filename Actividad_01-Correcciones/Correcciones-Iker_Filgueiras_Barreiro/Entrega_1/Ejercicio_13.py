"""13. Diseña un experimento para verificar que las operaciones de obtención y asignación de
ítems para diccionarios son 𝑶(𝟏).
"""

import timeit
import random

print("%s\t%s\t%s"%("N","list time","dict time"))
for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i, # comprueba si i esta en x
                     "from __main__ import random,x") # debe importar todos los símbolos de main necesarios
   
    x = list(range(i)) # crear una lista de tamaño i de 0 a i-1
    lst_time = t.timeit(number=1000) # obtener la hora de la lista para la lista de tamaño i
    x = {j:None for j in range(i)} # crear entradas de i dict donde la clave es de 0 a i-1 y el valor es None
    d_time = t.timeit(number=1000) # obtener tiempo de tamaño i
    print("%d\t%.5f\t%.5f" % (i, lst_time, d_time)) # imprimir resultados