import random, time


def busquedaBinaria_1(unaLista, item):
    inicio1 = time.time()
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

    fin1 = time.time()
    dif = fin1 - inicio1

    print(dif)

    return encontrado


def busquedaBinaria_2(unaLista,primero,ultimo,item):
    inicio2 = time.time()
    if primero == ultimo:
        fin2 = time.time()
        print(fin2 - inicio2)
        return False
    else:
        puntoMedio = (primero+ultimo)//2
        if unaLista[puntoMedio]==item:
            fin2 = time.time()
            print(fin2 - inicio2)
            return True
        else:
            if item<unaLista[puntoMedio]:
                return busquedaBinaria_2 (unaLista,primero,puntoMedio,item)
            else:
                return busquedaBinaria_2 (unaLista,puntoMedio+1,ultimo,item)


def busquedaBinaria_3(unaLista, item):
    inicio2 = time.time()
    if len(unaLista) == 0:
        fin2 = time.time()
        print(fin2 - inicio2)
        return False
    else:
        puntoMedio = len(unaLista)//2
        if unaLista[puntoMedio] == item:
            fin2 = time.time()
            print(fin2 - inicio2)
            return True
        else:
            if item < unaLista[puntoMedio]:
                return busquedaBinaria_3(unaLista[:puntoMedio], item)
            else:
                return busquedaBinaria_3(unaLista[puntoMedio+1:], item)


listainicio = []
for i in range (10000):
    elem = random.randrange(5000)
    listainicio.append(elem)

listaPrueba = sorted(listainicio)
x = random.randint(1,5000)
y = random.randint(1,5000)
print("x =",x)
print("y =",y)

#print(listaPrueba)

print("x = ",busquedaBinaria_1(listaPrueba, x))
print("y = ",busquedaBinaria_1(listaPrueba, y))


print("x = ",busquedaBinaria_2(listaPrueba,0,len(listaPrueba)-1, x))
print("y = ",busquedaBinaria_2(listaPrueba,0,len(listaPrueba)-1, y))

print("x = ",busquedaBinaria_3(listaPrueba, x))
print("y = ",busquedaBinaria_3(listaPrueba, y))