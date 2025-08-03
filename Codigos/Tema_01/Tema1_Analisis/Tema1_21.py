import time


def sumaDeN3(n):
    inicio = time.time()

    laSuma = (n*(n+1))/2

    final = time.time()

    return laSuma, final-inicio


for i in range(5):
    print("La suma es %d y requirió %10.7f segundos" % sumaDeN3(10000000))
