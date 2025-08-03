# Tema4_07
def busquedaBinaria(unaLista, item):
    primero = 0
    ultimo = len(unaLista)-1
    encontrado = False

    while primero <= ultimo and not encontrado:
        puntoMedio = (primero + ultimo)//2
        if unaLista[puntoMedio] == item:
            encontrado = True
        else:
            if item < unaLista[puntoMedio]:
                ultimo = puntoMedio-1
            else:
                primero = puntoMedio+1

    return encontrado


def ExponencialSearch(vector, val):
    if vector[0] == val:
        return 0
    indice = 1
    while indice < len(vector) and vector[indice] <= val:
        indice = indice * 2
    return busquedaBinaria(vector[:min(indice, len(vector))], val)


listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(ExponencialSearch(listaPrueba, 3))
print(ExponencialSearch(listaPrueba, 32))
