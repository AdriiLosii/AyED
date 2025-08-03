"""
Programa: Ej14.py
Propósito:
    Utilizando el ejercicio 8, implementar el método decrementarClave en la clase MonticuloBinario para
    que funcione el algoritmo de Dijkstra. Muestra cada paso al aplicar el algoritmo de Dijkstra al grafo
    resultante del problema 11.
Fecha: 11/05/2022
"""


#Importamos lo necesario para la ejecución del ejercicio
from Class_cola_prioridad_con_tuplas_14 import ColaPrioridad
import sys
import os
#Borramos la términal para una mejor estética
os.system('clear')


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
    #Pedimos al usuario el punto de inicio
    try:
        inicio=int(input('Por que punto quieres iniciar(Debes poner un punto entre el 1 y el 6, desde los puntos A al F):\n'))
        while inicio!=1 and inicio!=2 and inicio!=3 and inicio!=4 and inicio!=5 and inicio!=6:
            inicio=int(input('Por que punto quieres iniciar(Debes poner un punto entre el 1 y el 6, desde los puntos A al F):\n'))
    except:
        print('Has cometido un error, inténtalo de nuevo')
        main()

    print('-'*100)
    j=0
    #Ponemos el grafo del ejercicio
    grafo=[
        [1,2,10],
        [1,3,15],
        [1,6,5],
        [2,3,7],
        [3,4,7],
        [3,6,10],
        [4,5,7],
        [6,4,5],
        [5,6,13],
    ]
    #Buscamos el punto máximo en el grado
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