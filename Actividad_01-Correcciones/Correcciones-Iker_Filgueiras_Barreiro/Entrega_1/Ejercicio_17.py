from timeit import default_timer
import numpy as np

#Random array 1D.
def random_array():
    return np.random.randint(10, size=100)
    

#Funcion para sumar los elementos de un array.
def suma_array():
    arr = random_array()
    print(arr)
    return print("\nSum of arr : ", np.sum(arr))  
    


#Inicio del timer.
inicio = default_timer()
#Realiza la función.
suma_array()
#Pongo timer para que cuente cuando acabó.
final = default_timer()

print("El tiempo tardado en realizar la operación es de -> %10.7f" %(final-inicio))

# Experimento para cada n en el cual el tiempo que tarda no varía por tanto la función en una O(1)

