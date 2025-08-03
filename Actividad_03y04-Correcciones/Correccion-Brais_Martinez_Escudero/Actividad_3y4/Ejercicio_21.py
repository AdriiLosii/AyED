import timeit
def ordenamientoDeShell(unaLista,x,y):
    contadorSublistas = len(unaLista)//x

    while contadorSublistas > 0:

        for posicionInicio in range(contadorSublistas):
            brechaOrdenamientoPorInsercion(
                unaLista, posicionInicio, contadorSublistas)

        #print("Después de los incrementos de tamaño",
              #contadorSublistas, "La lista es", unaLista)

        contadorSublistas = contadorSublistas // y


def brechaOrdenamientoPorInsercion(unaLista, inicio, brecha):
    for i in range(inicio+brecha, len(unaLista), brecha):

        valorActual = unaLista[i]
        posicion = i

        while posicion >= brecha and unaLista[posicion-brecha] > valorActual:
            unaLista[posicion] = unaLista[posicion-brecha]
            posicion = posicion-brecha

        unaLista[posicion] = valorActual


unaLista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(unaLista)

Shell22 = timeit.timeit("ordenamientoDeShell(unaLista,2,2)", 
    setup="from __main__ import ordenamientoDeShell,unaLista", number=100)
print(unaLista)

unaLista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
Shell12 = timeit.timeit("ordenamientoDeShell(unaLista,1,2)", 
    setup="from __main__ import ordenamientoDeShell,unaLista", number=100)
print(unaLista)

unaLista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
Shell42 = timeit.timeit("ordenamientoDeShell(unaLista,4,2)", 
    setup="from __main__ import ordenamientoDeShell,unaLista", number=100)
print(unaLista)

unaLista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
Shell13 = timeit.timeit("ordenamientoDeShell(unaLista,6,3)", 
    setup="from __main__ import ordenamientoDeShell,unaLista", number=100)
print(unaLista)

print("busquedaBinaria 2 y 2: ",Shell22/100)
print("busquedaBinaria 1 y 2: ",Shell12/100)
print("busquedaBinaria 4 y 2: ",Shell42/100)
print("busquedaBinaria 6 y 3: ",Shell13/100)