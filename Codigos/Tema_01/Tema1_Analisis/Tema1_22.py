from numpy import arange
import time
MAXN = 10000000


def busca(v, MAXN, x):  # busca x en v[0...n-1]
    for i in range(MAXN+1):
        if v[i] == x:
            return i
    return -1


v = arange(MAXN+1)

#x=int(input("Dato a buscar: "))

print("MEJOR CASO")
inicio = time.time()
i = busca(v, MAXN, 0)
final = time.time()
print("Posición de %d: %d\n" % (0, i))
print("Este algoritmo requirió %10.7f segundos\n\n" % (final-inicio))

print("CASO MEDIO")
inicio = time.time()
i = busca(v, MAXN, MAXN//2)
final = time.time()
print("Posición de %d: %d\n" % (MAXN//2, i))
print("Este algoritmo requirió %10.7f segundos\n\n" % (final-inicio))

print("PEOR CASO")
inicio = time.time()
i = busca(v, MAXN, MAXN)
final = time.time()
print("Posición de %d: %d\n" % (MAXN, i))
print("Este algoritmo requirió %10.7f segundos\n\n" % (final-inicio))
