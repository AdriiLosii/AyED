from random import randint
from time import time


print("%10s %10s   %10s" % ("tamaño", "lista", "diccionario"))
for i in range(0,1000001,10000):
    lista = list(range(i))
    startlista=time()
    numiguales=randint(0,i)
    lista.count(numiguales)
    endlista=time()

    diccionario = {}
    startdic=time()
    clave=list(diccionario.keys())
    clave.count(numiguales)
    valor=list(diccionario.values())
    valor.count(numiguales)
    enddic=time()

    print("%10d %10.7f %10.7f" % (i, endlista-startlista, enddic-startdic))
    
print("\n La eficiencia es de O(n logn) y como podemos ver el diccionario es mucho más rápido")
