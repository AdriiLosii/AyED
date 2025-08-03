# Tema4_14
def ordenamientoPorInsercion(unaLista):
    for indice in range(1, len(unaLista)):

        valorActual = unaLista[indice]
        posicion = indice

        while posicion > 0 and unaLista[posicion-1] > valorActual:
            unaLista[posicion] = unaLista[posicion-1]
            posicion = posicion-1

        unaLista[posicion] = valorActual
        print(unaLista)


unaLista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
ordenamientoPorInsercion(unaLista)
print(unaLista)
