"""
Programa: Ej16.py
Propósito:
    Usando el algoritmo de Prim, encuentra el árbol de expansión de ponderación mínima
Fecha: 10/05/2022
"""


#Importamos las clases.
from Class_Vertices_16 import *
from Class_Grafos_16 import *

def buscar_mind(G,lista):
    nodo=0             #damos valores iniciales
    mind=sys.maxsize
    try:
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

    except UnboundLocalError:
        print("\nError, no se puede visitar todos los vértices con el vértice indicado.")
        input("Pulse ENTER para finalizar.")
        quit() #Salimos del programa


def prim(G,inicio):

    Vutilizados=[inicio]    #inicializamos dos listas, una con los vertices utilizads donde metemos el inicio y otra con
    Conexiones=[inicio]     #las conexiones donde tambien metemos el inicio
    N=Grafo()                   #creamos un nuevo grafo para al final mostrarlo con prim
    N.agregarVertice(inicio)    #incluimos el primer vertice

    while(len(Vutilizados)!=G.numVertices):   #un bucle mientras los vertices utilizados no sean igual al total de vertices

        previo,nodo,mind=buscar_mind(G,Vutilizados)   #buscamos la conexion con la minima distancia

        print("Se conecta el vertice {0} con el vertice {1} teniendo un coste de {2}".format(previo,nodo,mind))
        route.append((previo,nodo))
        N.agregarArista(previo,nodo,mind)      #vamos colocando las aristas que se vayan formando
        N.agregarArista(nodo,previo,mind)

        Vutilizados.append(nodo)               #añadimos el vertice siguiente a los utilizados
        Conexiones.append([previo,nodo,mind])  #añadimos el vertice conectado, con quien se conecta y la distancia
 
    return Conexiones,N     #al final de todo devolvemos las conexiones hechas (en una lista) y el nuevo grafo

def main(): #definimos el programa principal
    G = Grafo() #creamos un grafo
    #agregamos los vertices
    G.agregarVertice("D")
    G.agregarVertice("C")
    G.agregarVertice("F")
    G.agregarVertice("B")
    G.agregarVertice("E")
    G.agregarVertice("H")
    G.agregarVertice("A")

    #agregamos las aristas
    G.agregarArista("D", "C", 4)
    G.agregarArista("D", "F", 6)
    G.agregarArista("C", "F", 12)
    G.agregarArista("D", "A", 8)
    G.agregarArista("D", "B", 10)
    G.agregarArista("C", "B", 5)
    G.agregarArista("B", "E", 3)
    G.agregarArista("E", "F", 6)
    G.agregarArista("A", "C", 6)
    G.agregarArista("A", "H", 11)
    G.agregarArista("H", "E", 5)
    G.agregarArista("H", "D", 9)

    vertices_posibles = ["A","B","C","D","E","F","H"]
    try:
        vertice = str(input("\nIntroduzca el vértice para aplicar el algoritmo de Prim: "))
        if (vertice not in vertices_posibles):
            print("\nError, el vértice introducido no pertenece al grafo.")
            print("Vértices del grafo: A, B, C, D, E, F, H.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

        else:
            prim(G,vertice) #llamamos a la funcion prim
            Conexiones,N=prim(G,vertice) #guardamos las conexiones y el grafo

            G.draw(name= "Grafo inicial", mapon= True) #dibujamos el grafo inicial
            G.draw(name="Recorrido", edge_route = route) #dibujamos el grafo con su recorrido
            N.draw(name= "Aristas") #dibujamos el grafo con las aristas

            print(Conexiones)  #imprimimos las conexiones

    except ValueError:
        print("\nError, ha ocurrido algo inesperado.")
        input("Pulse ENTER para finalizar.")
        quit() #Salimos del programa

if __name__ == "__main__":
    route = [] #creamos una lista para almacenar las conexiones
    main() #llamamos al programa principal

#FIN.
input("\nPulse ENTER para finalizar.")