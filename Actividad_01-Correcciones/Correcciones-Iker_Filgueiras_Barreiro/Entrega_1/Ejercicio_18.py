#Escribir una función que devuelva el número de valores que aparecen dos o más veces
#en un vector. Calcular la complejidad temporal de dicha función y expresarla en
#notación asintótica.

#importamos counter que registra cuantas veces se agregan valores equivalentes.
from collections import Counter

#importamos la libreria numpy y default_timer que cuenta el tiempo transcurrido
from timeit import default_timer
import numpy as np

#Funcion que genera un vector aleatorio
def vector_aleatorio():
    return np.random.randint(0,10,15)

#funcion que busca las repeticiones que hay en el vector y muestra cuales se repiten 2 veces o mas
def repeticiones(vector):
    repeticiones=Counter(vector)
    for i in repeticiones:
        if repeticiones[i]>=2:
            print("El numero ", i, "se repite: ", repeticiones[i], " veces")
            
#funcion principal que llama a las otras
def main():
    vector=vector_aleatorio()
    print("Las repeticiones que hay en el vector: ",vector,"son:")
    repeticiones(vector)

#contador que cronometra el tiempo de ejecucion de la funcion principal
comienzo=default_timer()

main()

final=default_timer()

#mostramos en pantalla el tiempo empleado
print("El tiempo empleado en ejecutarse ha sido: %10.7f" %(final-comienzo))