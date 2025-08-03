"""
Programa: Ej11.py
Propósito:
    Crea el grafo correspondiente a la siguiente lista de aristas:
        de   a   costo
        1    2    10
        1    3    15
        1    6    5
        2    3    7
        3    4    7
        3    6    10
        4    5    7
        6    4    5
        5    6    13
Fecha: 10/05/2022
"""

#Importamos la clase.
from Class_Grafos_11 import Grafo

#Programa principal:
#Definimos el grafo.
grafo = Grafo()

#Agregamos el número de vértices del grafo.
for i in range(1, 6):
    grafo.agregarVertice(i)

#Creamos el grafo con los datos correspondientes.
grafo.agregarArista(1,2,10)
grafo.agregarArista(1,3,15)
grafo.agregarArista(1,6,5)
grafo.agregarArista(2,3,7)
grafo.agregarArista(3,4,7)
grafo.agregarArista(3,6,10)
grafo.agregarArista(4,5,7)
grafo.agregarArista(6,4,5)
grafo.agregarArista(5,6,13)

#Mostramos el grafo.
grafo.draw(name= "Grafo", mapon=True)

#FIN.
input("\nPulse ENTER para finalizar.")