
import random

def busquedaSecuencial(unaLista, item):
    pos = 0
    encontrado = False

    while pos < len(unaLista) and not encontrado:
        if unaLista[pos] == item:
            encontrado = True
        else:
            pos = pos+1

    return encontrado


def busquedaSecuencialOrdenada(unaLista, item):
    pos = 0
    encontrado = False
    parar = False
    while pos < len(unaLista) and \
        not encontrado and not parar:
        if unaLista[pos] == item:
            encontrado = True
        else:
            if unaLista[pos] > item:
                parar = True
            else:
                pos = pos+1

    return encontrado


def busquedaBinaria_1(unaLista, item):
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


def busquedaBinaria_2(unaLista,primero,ultimo,item):
    if primero == ultimo:
        return False
    else:
        puntoMedio = (primero+ultimo)//2
        if unaLista[puntoMedio]==item:
          return True
        else:
          if item<unaLista[puntoMedio]:
            return busquedaBinaria_2 (unaLista,primero,puntoMedio,item)
          else:
            return busquedaBinaria_2 (unaLista,puntoMedio+1,ultimo,item)

def busquedaBinaria_3(unaLista, item):
    if len(unaLista) == 0:
        return False
    else:
        puntoMedio = len(unaLista)//2
        if unaLista[puntoMedio] == item:
            return True
        else:
            if item < unaLista[puntoMedio]:
                return busquedaBinaria_3(unaLista[:puntoMedio], item)
            else:
                return busquedaBinaria_3(unaLista[puntoMedio+1:], item)



listaPrueba = []
for i in range (200):
    elem = random.randrange(30)
    listaPrueba.append(elem)
x = random.randint(1,30)
y = random.randint(1,30)


print("x =",x)
print("y =",y)

listaPrueba.sort()

print(listaPrueba)


print("busquedaSecuencial: ",busquedaSecuencial(listaPrueba, x))
print("busquedaSecuencial: ",busquedaSecuencial(listaPrueba, y))

print("busquedaSecuencialOrdenada: ",busquedaSecuencialOrdenada(listaPrueba, x))
print("busquedaSecuencialOrdenada: ",busquedaSecuencialOrdenada(listaPrueba, y))

print("busquedaBinaria_1: ",busquedaBinaria_1(listaPrueba, x))
print("busquedaBinaria_1: ",busquedaBinaria_1(listaPrueba, y))

print("busquedaBinaria_2: ",busquedaBinaria_2(listaPrueba,0,len(listaPrueba)-1, x))
print("busquedaBinaria_2: ",busquedaBinaria_2(listaPrueba,0,len(listaPrueba)-1, y))

print("busquedaBinaria_3: ",busquedaBinaria_3(listaPrueba, x))
print("busquedaBinaria_3: ",busquedaBinaria_3(listaPrueba, y))
