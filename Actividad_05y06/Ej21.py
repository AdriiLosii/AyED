"""
Programa: Ej21.py
Propósito:
    Escribe el método transponer para la clase Grafo.
Fecha: 12/05/2022
"""

#Importamos la clase.
from Class_Grafos_21 import *

#Programa principal.
def main():
    #Definimos el grafo.
    g = Grafo()

    #Agregamos los vértices al grafo.
    g.agregarVertice('A')
    g.agregarVertice('B')   
    g.agregarVertice('C')
    g.agregarVertice('D')
    g.agregarVertice('E')
    g.agregarVertice('F')
    g.agregarVertice('G')

    #Creamos las conexiones del grafo.
    g.agregarArista('A','B',1)
    g.agregarArista('A','C',13)
    g.agregarArista('A','F',6)
    g.agregarArista('B','G',11)
    g.agregarArista('C','D',1)
    g.agregarArista('D','E',7)
    g.agregarArista('D','F',5)
    g.agregarArista('E','G',1)
    g.agregarArista('F','G',4)
    
    #Mostramos el grafo inicial.
    print("\nConexiones del grafo inicial:")
    print(g)
    g.draw(name="Grafo inicial")

    #Llamamos a la función para transponer el grafo y lo mostramos.
    grafo_transpuesto = g.transponer_grafo()
    print(grafo_transpuesto)
    grafo_transpuesto.draw(name="Grafo transpuesto")


#Llamamos al programa principal.
main()

#FIN.
input("\nPulse ENTER para finalizar.")