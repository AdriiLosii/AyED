"""
Programa: Ejercicio_13.py
Propósito:
    Diseña un experimento para verificar que las operaciones de obtención y asignación de ítems para 
    diccionarios son O(1).
Fecha:27/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


import timeit


ejecuciones = 0
seg_tot_obt = 0
seg_tot_asig = 0
print("    Tamaño       T. obtención     T. asignación")
for i in range(10000, 1000000 + 1, 30000):

    diccionario = {j: 0 for j in range(i)}
    tiempo_obtencion = timeit.Timer("elemento = diccionario[i-1]", "from __main__ import diccionario,i").timeit(number=1000)
    tiempo_asignacion = timeit.Timer("diccionario[i-1] = 1", "from __main__ import diccionario,i").timeit(number=1000)
    ejecuciones += 1
    seg_tot_obt += tiempo_obtencion
    seg_tot_asig += tiempo_asignacion

    print("%10d       %10.5f        %10.5f" % (i, tiempo_obtencion, tiempo_asignacion))

print("\nPromedio de tiempo obtención: %1.5f"%(seg_tot_obt/ejecuciones))
print("Promedio de tiempo asignación: %1.5f"%(seg_tot_asig/ejecuciones))

print("\nComo se puede observar tanto la obtención como la asignación de ítems para diccionarios es O(1), es decir, tiempo constante.")

input("\nPulse ENTER para finalizar.")