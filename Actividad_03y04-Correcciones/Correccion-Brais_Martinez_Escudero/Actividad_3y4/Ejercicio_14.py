from time import time
import timeit
import random

def busquedaBinaria1(unaLista, item):
    primero = 0
    ultimo = len(unaLista)-1
    encontrado = False

    while primero<=ultimo and not encontrado:
        puntoMedio = (primero + ultimo)//2
        if unaLista[puntoMedio] == item:
            encontrado = True
        else:
            if item < unaLista[puntoMedio]:
                ultimo = puntoMedio-1
            else:
                primero = puntoMedio+1

    return encontrado

def busquedaBinaria2(unaLista,primero,ultimo,item):
    if primero == ultimo:
        return False
    else:
        puntoMedio = (primero+ultimo)//2
        if unaLista[puntoMedio]==item:
          return True
        else:
          if item<unaLista[puntoMedio]:
            return busquedaBinaria2 (unaLista,primero,puntoMedio,item)
          else:
            return busquedaBinaria2 (unaLista,puntoMedio+1,ultimo,item)

def busquedaBinaria3(unaLista, item):
    if len(unaLista) == 0:
        return False
    else:
        puntoMedio = len(unaLista)//2
        if unaLista[puntoMedio] == item:
            return True
        else:
            if item < unaLista[puntoMedio]:
                return busquedaBinaria3(unaLista[:puntoMedio], item)
            else:
                return busquedaBinaria3(unaLista[puntoMedio+1:], item)

v  = [random.randint(0, 300) for x in range(200)]
listaPrueba1 = sorted(v)

busquedabin1 = timeit.timeit("busquedaBinaria1(listaPrueba1, 198)", 
    setup="from __main__ import busquedaBinaria1,listaPrueba1", number=100)
busquedabin2 = timeit.timeit("busquedaBinaria2(listaPrueba1,0,len(listaPrueba1)-1, 198)", 
    setup="from __main__ import busquedaBinaria2,listaPrueba1", number=100)
busquedabin3 = timeit.timeit("busquedaBinaria3(listaPrueba1, 198)", 
    setup="from __main__ import busquedaBinaria3,listaPrueba1", number=100)

print("busquedaBinaria1: ",busquedabin1/100)
print("busquedaBinaria2: ",busquedabin2/100)
print("busquedaBinaria3: ",busquedabin3/100)
