import random
import time



def ordenamientoDeShell(unaLista_1):


    inicio = time.time()

    contadorSublistas = len(unaLista_1)//2
    while contadorSublistas > 0:

        for posicionInicio in range(contadorSublistas):
            brechaOrdenamientoPorInsercion(
                unaLista_1, posicionInicio, contadorSublistas)

        print("Después de los incrementos de tamaño",
              contadorSublistas, "La lista es", unaLista_1, "\n")

        contadorSublistas = contadorSublistas // 2
    
    fin = time.time()
    print("tiempo: ",fin-inicio)


def brechaOrdenamientoPorInsercion(unaLista_1, inicio, brecha):
    for i in range(inicio+brecha, len(unaLista_1), brecha):

        valorActual = unaLista_1[i]
        posicion = i

        while posicion >= brecha and unaLista_1[posicion-brecha] > valorActual:
            unaLista_1[posicion] = unaLista_1[posicion-brecha]
            posicion = posicion-brecha

        unaLista_1[posicion] = valorActual

####

def ordenamientoRapido(unaLista_2):
    inicio = time.time()
    ordenamientoRapidoAuxiliar(unaLista_2, 0, len(unaLista_2)-1)
    fin = time.time()

    print("tiempo: ",fin-inicio)


def ordenamientoRapidoAuxiliar(unaLista_2, primero, ultimo):
    if primero < ultimo:

        puntoDivision = particion(unaLista_2, primero, ultimo)

        ordenamientoRapidoAuxiliar(unaLista_2, primero, puntoDivision-1)
        ordenamientoRapidoAuxiliar(unaLista_2, puntoDivision+1, ultimo)


def particion(unaLista_2, primero, ultimo):
    valorPivote = unaLista_2[primero]

    marcaIzq = primero+1
    marcaDer = ultimo

    hecho = False
    while not hecho:

        while marcaIzq <= marcaDer and unaLista_2[marcaIzq] <= valorPivote:
            marcaIzq = marcaIzq + 1

        while unaLista_2[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
            marcaDer = marcaDer - 1

        if marcaDer < marcaIzq:
            hecho = True
        else:
            unaLista_2[marcaIzq],unaLista_2[marcaDer] = unaLista_2[marcaDer],unaLista_2[marcaIzq]

    unaLista_2[primero],unaLista_2[marcaDer] = unaLista_2[marcaDer],unaLista_2[primero]

    return marcaDer

####

def ordenamientoBurbuja(unaLista_3):
    inicio = time.time()
    for numPasada in range(len(unaLista_3)-1,0,-1):
        for i in range(numPasada):
            if unaLista_3[i]>unaLista_3[i+1]:
                temp = unaLista_3[i]
                unaLista_3[i] = unaLista_3[i+1]
                unaLista_3[i+1] = temp
    fin = time.time()
    print("tiempo: ",fin-inicio)

####

unaLista = []
for i in range (1000):
    x = random.randrange(500)
    unaLista.append(x)

unaLista_1 = unaLista[:]
unaLista_2 = unaLista[:]
unaLista_3 = unaLista[:]

print("Lista 1")
ordenamientoBurbuja(unaLista_1)
print(unaLista_1)
print("\n")
print("\n")
print("\n")

print("Lista 2")
ordenamientoDeShell(unaLista_2)
print(unaLista_2)
print("\n")
print("\n")
print("\n")

print("Lista 3")
ordenamientoRapido(unaLista_3)
print(unaLista_3)
print("\n")
print("\n")
print("\n")

print("Lista original")
print(unaLista)

'''

Observando los resultados de los tiempos de ejecución para una lista de 1000 elementos, los datos que obtenemos de forma general
son los siguientes:

Ordenamiento Burbuja:
0.05 seg
Ordenamiento Shell:
0.02 seg
Ordenamiento Rápido:
0.00099 seg

Una vez analizados los resultados sacamos la conclusión de que el Ordenamiento Rápido es dos veces mas veloz que el
Ordenamiento Shell y 5 veces mas rapido que el Ordenamiento Burbuja.

Esto es debido a que el Big-O promedio de estos tres metodos son O(n^2), O(n(log(n))^2) y O(n log(n)) respectivamente.

'''