"""
Programa: Ej18.py
Propósito:
    Dado el grafo de la figura, encuentra un árbol de expansión de coste mínimo describiendo el proceso paso a
    paso mediante el algoritmo de Prim
Fecha: 10/05/2022
"""


#Incluimos las clases.
from Class_Vertices_18 import *
from Class_Grafos_18 import *


def buscar_minD(G,lista):

    nodo=0             #damos valores iniciales
    mind=sys.maxsize

    for i in lista:   #recorremos cada vertice utilizado

        vertice=G.listaVertices[i]      #sacamos el objeto correcpondiente al vertice
        #print(vertice)

        conexiones=vertice.obtenerConexiones()   #obtenemos las conexiones delvertice
        #print(conexiones)

        for j in conexiones:   #recorremos las conexiones

            distancia=vertice.conectadoA[j]   #sacamos la distancia de la arista
            #print(distancia)

            if j.id in lista:  #si el vertice al que nos conectariamos ya esta en la lista nos lo saltamos

                continue

            elif(distancia<mind):    #si la distancia es menor a la almacenada se cambia por esta

                mind=distancia
                nodo=j.id         #conseguimos el vertice con el que se conecta
                previo=i          #devolvemos tambien el vertice que se esta conectando

            #print(nodo)

    return previo,nodo,mind    #devolvemos el vertice y la distancia


def prim(G,inicio):

    Vutilizados=[inicio]    #inicializamos dos listas, una con los vertices utilizads donde metemos el inicio y otra con
    Conexiones=[inicio]     #las conexiones donde tambien metemos el inicio
    N=Grafo()                   #creamos un nuevo grafo para al final mostrarlo con prim
    N.agregarVertice(inicio)    #incluimos el primer vertice

    while(len(Vutilizados)!=G.numVertices):   #un bucle mientras los vertices utilizados no sean igual al total de vertices

        previo,nodo,mind=buscar_minD(G,Vutilizados)   #buscamos la conexion con la minima distancia

        print("Se conecta el vertice {0} con el vertice {1} teniendo un coste de {2}".format(previo,nodo,mind))
        route.append((previo,nodo))
        N.agregarArista(previo,nodo,mind)      #vamos colocando las aristas que se vayan formando
        N.agregarArista(nodo,previo,mind)

        Vutilizados.append(nodo)               #añadimos el vertice siguiente a los utilizados
        Conexiones.append([previo,nodo,mind])  #añadimos el vertice conectado, con quien se conecta y la distancia
 
    return Conexiones,N     #al final de todo devolvemos las conexiones hechas (en una lista) y el nuevo grafo


def main(): #definimos el programa principal

    G = Grafo() #creamos un grafo vacio

    G.agregarVertice("H")  #agregamos los vertices
    G.agregarVertice("J")
    G.agregarVertice("Z")
    G.agregarVertice("W")
    G.agregarVertice("R")
    G.agregarVertice("K")
    G.agregarVertice("Y")
    G.agregarVertice("L")
    G.agregarVertice("T")

    G.agregarArista("H", "J", 3) #agregamos las aristas
    G.agregarArista("H", "Z", 2)
    G.agregarArista("J", "R", 1)
    G.agregarArista("R", "J", 1)
    G.agregarArista("Z", "J", 4)
    G.agregarArista("J", "Z", 4)
    G.agregarArista("Z", "W", 4)
    G.agregarArista("W", "Z", 4)
    G.agregarArista("W", "R", 1)
    G.agregarArista("R", "W", 1)
    G.agregarArista("R", "K", 1)
    G.agregarArista("K", "R", 1)
    G.agregarArista("R", "Y", 1)
    G.agregarArista("Y", "R", 1)
    G.agregarArista("K", "Y", 2)
    G.agregarArista("Y", "K", 2)
    G.agregarArista("K", "L", 5)
    G.agregarArista("L", "K", 5)
    G.agregarArista("K", "T", 6)
    G.agregarArista("T", "K", 6)
    G.agregarArista("Y", "T", 5)
    G.agregarArista("T", "Y", 5)
    G.agregarArista("L", "T", 2)
    G.agregarArista("T", "L", 2)

    vertices_posibles = ["H","J","K","L","R","Z","W","Y","T"]
    try:
        vertice = str(input("\nIntroduzca el vértice para aplicar el algoritmo de Prim: "))
        if (vertice not in vertices_posibles):
            print("\nError, el vértice introducido no pertenece al grafo.")
            print("Vértices del grafo: H, J, K, L, R, Z, W, Y, T.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

        else:
            Conexiones,N=prim(G,"H") #llamamos a la funcion prim y le pasamos el grafo y el vertice inicial

            G.draw(name= "Grafo inicial", mapon= True) #dibujamos el grafo inicial
            G.draw(name="Recorrido", edge_route = route) #dibujamos el grafo con su recorrido
            N.draw(name= "Aristas") #dibujamos el grafo con las aristas

            print(Conexiones) #imprimimos las conexiones

    except ValueError:
        print("\nError, ha ocurrido algo inesperado.")
        input("Pulse ENTER para finalizar.")
        quit() #Salimos del programa

if __name__ == "__main__":
    route = [] #creamos una lista para almacenar las conexiones
    main() #llamamos al programa principal

#FIN.
input("\nPulse ENTER para finalizar.")