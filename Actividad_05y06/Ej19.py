"""
Programa: Ej19.py
Propósito:
    Modifica la función de búsqueda en profundidad para producir un ordenamiento topológico.
Fecha: 13/05/2022
"""


from Class_Grafos_19 import *
import os
import networkx as nx
import matplotlib.pyplot as plt
os.system('clear')


#Creamos la función para visualizar el grafo.
def draw(grafo, name=None, arrows=True, mapon=None, edge_route=None, label_color = "black"):
        G = nx.DiGraph()
        for v in range(1, 7):
            G.add_node(v)

        for v in grafo:
            G.add_edge(v[0], v[1], dis=v[2])

        pos = nx.spring_layout(G, seed=777)
        edge_labels = dict([((u,v,),d['dis']) for u,v,d in G.edges(data=True)])

        nx.draw_networkx_nodes(G, pos, node_color=range(1,7), edgecolors="black", cmap=plt.cm.Blues)

        nx.draw_networkx_edges(G, pos, arrows=arrows, arrowstyle="-|>", arrowsize=10, edge_color="#010056")
        
        if edge_route:
            nx.draw_networkx_edges(G, pos, edge_color="red", edgelist=edge_route)
        
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif', font_color=label_color)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        ax = plt.gca()
        ax.margins(0.20)
        ax.set_axis_off()
        plt.title(name)
        plt.show()

#Buscamos el máximo del grafo.
def maximo(grafo):
    nums=[]
    for item in grafo:
        nums.append(item[1])
    return max(nums)

#Realizamos una función de ayuda, la cuál se ejecuta recursivamente
def BEP_ayuda(grafo,cp,inicio2,tamanho,t, route=[]):
    #Lo repetimos tantas veces como hijos haya
    for i in range(len(inicio2)):
        #La T es para mejor estética
        t += 1
        print('\t'*t,'Vas desde el punto {} al punto {} con un costo de {}'.format(inicio2[i][0],inicio2[i][1],inicio2[i][2]))
        route.append([inicio2[i][0],inicio2[i][1]])
        #Desde la clase colaprioridad obetenemos las conexiones en el grafo
        verticeactual=cp.obtenerConexiones(inicio2[i][1])
        #Si no tiene más hijos, es decir, ha llegado al final, se notifica
        if len(verticeactual)==0:
            print('\nHas llegado al final del grafo (NODO {}) por este camino, no tienes ningun vertice adyacente al que salir.'.format(tamanho))
            draw(grafo, name="Recorrido", arrows=False, edge_route=route)
            print('Volvemos al nodo anterior \n\n')
            t -= 2
            route.clear()
        for verticeSiguiente in verticeactual:
            #Obtenemos las conexiones de cada hijo
            vertice=cp.obtenerConexiones(verticeSiguiente[1])
            t+=1
            #Printamos el resultado
            print('\t'*t,'Ahora sales desde el punto {} al punto {} con un costo de {}'.format(verticeSiguiente[0],verticeSiguiente[1],verticeSiguiente[2]))
            route.append([verticeSiguiente[0],verticeSiguiente[1]])
            if verticeSiguiente[1]==tamanho:
                print('\nHas llegado al final del grafo (NODO {}) por este camino, no tienes ningun vertice adyacente al que salir.'.format(tamanho))
                draw(grafo, name="Recorrido", arrows=False, edge_route=route)
                print('Volvemos al nodo anterior \n\n')
                t-=2
                route.clear()
            #Realizamos la recursividad 
            BEP_ayuda(grafo,cp,vertice,tamanho,t, route)

#Realizamos la función de búsqueda 
def BEP_topografica(grafo):
    #Iniciamos desde el 1
    inicio=1
    #Bucamos el tamaño del grafo
    tamanho=maximo(grafo)
    #Llamamos a la clase colaprioridad
    cp=ColaPrioridad(tamanho)
    #Contruímos el montículo con el grado
    cp.construirMonticulo(grafo)
    inicio2=[[0,inicio,0]]

    for i in range(len(inicio2)):
        route = []
        #Obtenemos los primeros hijos disponibles
        verticeactual=cp.obtenerConexiones(inicio2[i][1])
        t=0
        for verticeSiguiente in verticeactual:
            #Printamos los primeros caminos disponibles
            print('\n\n****Para tomar este camino, primero debes de salir desde el punto {} al punto {}:****'.format(verticeSiguiente[0],verticeSiguiente[1]))
            route.append([verticeSiguiente[0],verticeSiguiente[1]])
            vertice=cp.obtenerConexiones(verticeSiguiente[1])
            #Llamamos a la función de ayuda
            BEP_ayuda(grafo,cp,vertice,tamanho,t, route)

#Llamamos a la función main donde ejeutaremos todo en orden
def main():

    print('\t\t\t\t\t\t***** INICIO *****')
    #Creamos el grafo
    grafo=[
        [1,2,10],
        [1,3,15],
        [1,5,5],
        [2,3,7],
        [3,4,7],
        [3,6,10],
        [4,5,7],
        [5,6,13],
    ]
    #Llamamos el grafo a la función
    draw(grafo, name="Grafo original")
    BEP_topografica(grafo)
    print('No hay nodo anterior, todos los caminos posibles han sido ejecutados, fin del grafo.')

#Llamamos a la función main
if __name__ == '__main__':
    main()
