#Tema4_05
import math

def SaltoSearch(vector, val):  
    longitud = len(vector)
    salto = int(math.sqrt(longitud))
    izda,dcha = 0,0
    encontrado= (vector[izda] <= val and vector[dcha] >= val) #True
    while izda < longitud and  vector[izda] <= val and not encontrado:
        dcha = min(longitud-1,izda+salto)
        if vector[izda] <= val and vector[dcha] >= val:
            encontrado=True
        if not encontrado:
            izda += salto
    if izda >= longitud or vector[izda] > val:
        return False
    dcha = min(longitud-1,dcha)
    i = izda
    while i <= dcha and vector[i] <= val:
        if vector[i] == val:
            return i
        i += 1
    return False

listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(SaltoSearch(listaPrueba, 3))
print(SaltoSearch(listaPrueba, 32))

"""
    originalmente: 
    dcha = min(longitud - 1, izda + salto)
    if vector[izda] <= val and vector[dcha] >= val:
        break
    izda += salto;
"""