"""
Programa: Ej15.py
Propósito:
    Dado el grafo dirigido y valorado de la figura, encuentra el camino más corto desde el vértice A a todos los
    demás vértices usando el algoritmo de Dijkstra. Describe el proceso paso a paso.
Fecha: 12/05/2022
"""

'''
Resultado teórico
D=[0,11,6,20,14,18,11]
P=[0,2,1,2,3,2,1]
'''


#Importamos lo necesario para la ejecución del ejercicio
from Class_cola_prioridad_con_tuplas_15 import ColaPrioridad
import sys
import os

os.system('clear') #Borramos la términal para una mejor estética


#Buscamos cual es el tamaño de la grafo
def maximo(grafo):
    nums=[]
    
    for item in grafo:
        nums.append(item[1])

    return max(nums)

#Realizamos el algorítmo de dijkstra
def dijkstra(unGrafo,inicio,j,tamanho):
    #Llamamos a la clase colaprioridad modificada
    cp = ColaPrioridad(tamanho) 
    #Construímos un montículo con el grafo mandado
    cp.construirMonticulo(unGrafo)
    y=0
    #Nos iniciamos en el punto llamado inicio por el usuario
    inicio2=[0,inicio,0]
    siguientes=[inicio2]
    siguientes2=[]
    #Lo repetimos tantas veces como grafos haya
    for i in range(len(unGrafo)):
        k=0
        siguientesayuda=siguientes.copy()
        #Buscamos entre los nuevos grafos añadidos en la lista, que serán los siguientes a donde podemos ir
        for h in range(len(siguientes2),len(siguientes)):
            #Subimos veces por donde tenemos que pasar por otras paradas
            if k==0:
                j += 1
                k += 1

            #Obtenemos las conexiones a los siguientes vértices
            verticeActual = cp.obtenerConexiones(siguientes[h][1])
            for verticeSiguiente in verticeActual:
                #Añadimos el siguiente vértice a la lista 
                siguientes.append(verticeSiguiente)
                a,b,y=cp.decrementarClave(verticeSiguiente,inicio,j,y)

        siguientes2=siguientesayuda.copy()
    
    return a,b

#Programa principal:
def main():
    j=0
    #Le ponemos el grafo
    grafo=[
        [1,3,6],
        [1,7,11],
        [2,5,3],
        [3,2,5],
        [3,6,12],
        [4,1,8],
        [4,2,10],
        [4,3,4],
        [4,6,6],
        [5,6,6],
        [7,5,5],
        [7,4,9]
    ]
    inicio=1
    #Buscamos el tamaño
    tamanho=maximo(grafo)
    #Sacamos la distancia al punto y las vueltas necesarias para ella
    Distancia_al_punto_a,vueltas=dijkstra(grafo,inicio,j,tamanho)
    Puntos=['A','B','C','D','E','F','H']

    #Pintamos el resultado final
    print('\n\n\t***ENTONCES QUEDARÍA:***\n')

    for distancia in range(0,tamanho):
        if distancia+1!=inicio:
            if Distancia_al_punto_a[distancia][1] == sys.maxsize or Distancia_al_punto_a[distancia][1]==0:
                print('\tDel Punto {} al Punto {} no se puede llegar debido a que el grafo no está dirigido para que así se haga.'.format(Puntos[inicio-1],Puntos[distancia]))
            else:
                print('\tLa distancia del Punto {} al Punto {} es: {}, pasando por {} recorridos'.format(Puntos[inicio-1],Puntos[distancia],Distancia_al_punto_a[distancia][1],vueltas[distancia]))


#Llamamos al programa principal.
main()

#FIN.
input("\nPulse ENTER para finalizar.")