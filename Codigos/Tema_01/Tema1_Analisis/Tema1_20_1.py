import time


def sumaDeN(n):
    inicio = time.time()

    laSuma = 0
    for i in range(1, n+1):
        laSuma = laSuma + i

    final = time.time()

    return laSuma, final-inicio

totales=0.0
# Programa principal
for i in range(5):
    Lasuma,segundos=sumaDeN(10000000)
    print("La suma es %d y requirió %10.7f segundos" % (Lasuma,segundos))
    totales+=segundos
print("Tiempo promedio",totales/5)