"""
Programa: Ej12.py
Propósito:
    Haciendo caso omiso de las ponderaciones, realiza una búsqueda en anchura en el grafo de la pregunta 
    anterior.
Fecha: 11/05/2022
"""


#Importamos las clases.
from Class_Grafos_12 import Grafo
from Class_Estructuras_lineales import Cola

def bea(g):
    edge_route=[]
    for vertices in dict.values(g.listaVertices): 
        vertInicio = vertices
        break 

    vertInicio.asignarDistancia(0)
    vertInicio.asignarPredecesor(None)
    colaVertices = Cola()
    colaVertices.agregar(vertInicio)
    while (colaVertices.tamano() > 0):
        verticeActual = colaVertices.avanzar()
        print("Vertice:",verticeActual.obtenerId())
        for vecino in verticeActual.obtenerConexiones(): 
            if (vecino.obtenerColor() == 'white'): 
                vecino.asignarColor('grey')
                vecino.asignarDistancia(verticeActual.obtenerDistancia() + 1)
                vecino.asignarPredecesor(verticeActual)
                colaVertices.agregar(vecino)
                edge_route.append((verticeActual.obtenerId(),vecino.obtenerId()))
        g.draw(name = "Vertice: " + str(verticeActual.obtenerId()), arrows = False, edge_route = edge_route)
        verticeActual.asignarColor('black')
    print(edge_route)
    g.draw(name = "Fin de BEA", arrows = False, edge_route = edge_route, label_color = "white")

g = Grafo()
for i in range(1, 6):
    g.agregarVertice(i)

g.agregarArista(1,2,10)
g.agregarArista(1,3,15)
g.agregarArista(1,6,5)
g.agregarArista(2,3,7)
g.agregarArista(3,4,7)
g.agregarArista(3,6,10)
g.agregarArista(4,5,7)
g.agregarArista(6,4,5)
g.agregarArista(5,6,13)

g.draw(name = "Grafo inicial", mapon=True)
print('\nBEA')
bea(g)

#FIN.
input("\nPulse ENTER para finalizar.")