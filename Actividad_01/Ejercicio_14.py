"""
Programa: Ejercicio_14.py
Propósito:
    Diseña un experimento que compare el desempeño del operador del en listas y en diccionarios.
Fecha:26/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


import timeit


####    Borrando el último elemento del vector  ####
ejecuciones = 0
seg_tot_list = 0
seg_tot_dicc = 0
print("Si el elemento que borramos es el último de la lista:")
print("    Tamaño         T. lista      T. diccionario")
for i in range(10000, 1000000 + 1, 30000):

    lista = list(range(i)) #Creamos la lista
    diccionario = {j:None for j in range(i)} #Creamos el diccionario
    
    tiempo_lista = timeit.Timer("del lista[i-1]", "from __main__ import lista,i").timeit(number=1) #Guardamos el tiempo en una variable
    tiempo_diccionario = timeit.Timer("del diccionario[i-1]", "from __main__ import diccionario,i").timeit(number=1) #Guardamos el tiempo en una variable
    ejecuciones += 1
    seg_tot_list += tiempo_lista
    seg_tot_dicc += tiempo_diccionario

    print("%10d       %10.7f        %10.7f" % (i, tiempo_lista, tiempo_diccionario)) #Mostramos el resultado.

print("\nPromedio lista: %1.7f"%(seg_tot_list/ejecuciones))
print("Promedio diccionario: %1.7f"%(seg_tot_dicc/ejecuciones))

#Conclusión.
print("\nEl tiempo que tardan ambos es constante O(1).\n")


####    Borrando el primer elemento del vector  ####
ejecuciones = 0
seg_tot_list = 0
seg_tot_dicc = 0
print("Sin embargo si el elemento que se borra es el primero:")
print("    Tamaño         T. lista      T. diccionario")
for i in range(10000, 1000000 + 1, 30000):

    lista = list(range(i)) #Creamos la lista
    diccionario = {j:None for j in range(i)} #Creamos el diccionario
    
    tiempo_lista = timeit.Timer("del lista[0]", "from __main__ import lista").timeit(number=1) #Guardamos el tiempo en una variable
    tiempo_diccionario = timeit.Timer("del diccionario[0]", "from __main__ import diccionario").timeit(number=1) #Guardamos el tiempo en una variable
    ejecuciones += 1
    seg_tot_list += tiempo_lista
    seg_tot_dicc += tiempo_diccionario

    print("%10d       %10.7f        %10.7f" % (i, tiempo_lista, tiempo_diccionario)) #Mostramos el resultado.

print("\nPromedio lista: %1.7f"%(seg_tot_list/ejecuciones))
print("Promedio diccionario: %1.7f"%(seg_tot_dicc/ejecuciones))

#Conclusión.
print("\nEl tiempo que tarda el operador del en listas va aumentando (O(n)), mientras que el tiempo del operador del en diccionarios es constante (O(1))\n")

input("Pulse ENTER para finalizar.")