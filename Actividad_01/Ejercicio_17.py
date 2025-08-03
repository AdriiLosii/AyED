"""
Programa: Ejercicio_17.py
Propósito:
    Escribir en lenguaje Python una función que calcule la suma de los elementos de un vector. Calcular 
    la complejidad temporal de dicha función y expresarla en notación asintótica.
Fecha:23/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


import timeit

def sumatorio(vector): #Función que suma número a número todos los elementos del vector.

    suma = 0.0
    for i in vector:
        suma += i

    return suma

def operador_sum(vector): #Función sum() para calcular el sumatorio de un vector.
    return float(sum(vector))

def formula_suma_seguido(n): #Fórmula para hallar el sumatorio de un vector de números en orden.
    return float((n * (n + 1))/2)

ejecuciones = 0
seg_tot1 = 0
seg_tot2 = 0
seg_tot3 = 0
print("          Tamaño      Elemento a elemento         Sum()              Fórmula")
for i in range(5000, 100000 + 1, 5000):

    x = list(range(i)) #Creamos la lista de longitud i.

    #Guardamos los tiempos de ejecución de variables distintas.
    t1 = timeit.Timer("sumatorio(x)","from __main__ import sumatorio,x").timeit(number=1000)
    t2 = timeit.Timer("operador_sum(x)","from __main__ import operador_sum,x").timeit(number=1000)
    t3 = timeit.Timer("formula_suma_seguido(i)","from __main__ import formula_suma_seguido,i").timeit(number=1000)
    ejecuciones += 1
    seg_tot1 += t1
    seg_tot2 += t2
    seg_tot3 += t3

    print("%15d       %15.5f    %15.5f     %15.5f" %(i,t1,t2,t3)) #Mostramos los resultados.

print("\nPromedio de tiempo elemento a elemento: %1.5f"%(seg_tot1/ejecuciones))
print("Promedio de tiempo función sum(): %1.5f"%(seg_tot2/ejecuciones))
print("Promedio de tiempo fórmula: %1.5f"%(seg_tot3/ejecuciones))

#Conclusión.
print("\nObservando la tabla se pueden obtener las siguientes conclusiones:")
print("1- El orden del sumatorio sumando elemento a elemento es O(n)")
print("2- El orden del sumatorio usando la función sum() es O(n)")
print("3- El orden del sumatorio usando la fórmula es O(1)")
print("\nPor lo tanto, la función más óptima es la 3º")

input("\nPulse ENTER para finalizar.")