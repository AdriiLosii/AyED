import numpy as np
#Enontrar el numero más pequeño de una lista con una funcion o(n*2) y con otra función O(n)

#Random array 1D.
def random_array():
    return np.random.randint(0,10,10)

#O(n*2)

#O(n)
def menor(lista):
    menor = None
    for numero in lista:
        if menor==None:
            menor=numero
        else:
            if numero<menor:
                menor=numero
    return menor

vector =random_array()
print(f"Este es el vector -- {vector}")
menor=menor(vector)

#Este es con O(n^2)
print(f"El numero menor es {menor}")

#Ej lineal.  O(n)
print(f"El menor numero es {min(vector)}")