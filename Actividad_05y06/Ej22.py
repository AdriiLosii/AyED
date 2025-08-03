"""
Programa: Ej22.py
Propósito:
    Utilizando la búsqueda en anchura, escribe un algoritmo que puede determinar la ruta más corta de cada
    vértice a cada uno de los otros vértices. Esto se llama el problema de la ruta más corta de todas las parejas.
Fecha: 13/05/2022
"""


from Class_Grafos_22 import *

#Programa principal.
#Definimos el grafo.
G = Grafo()

#Agregamos los vértices al grafo.
G.agregarVertice("H")
G.agregarVertice("J")
G.agregarVertice("Z")
G.agregarVertice("W")
G.agregarVertice("R")
G.agregarVertice("K")
G.agregarVertice("Y")
G.agregarVertice("L")
G.agregarVertice("T")

#Creamos las conexiones en el grafo.
G.agregarArista("H", "J", 3)
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

#Llamamos a la función.
G.bfs(G.obtenerVertice("H"))

#FIN.
input("\nPulse ENTER para finalizar.")