"""
Programa: Class_Grafos_17.py
Propósito:
    ¿Cuál es el tiempo de ejecución O-grande para el algoritmo de Prim del árbol de expansión mínimo?
Fecha: 10/05/2022
"""


from Class_Vertices_17 import Vertice
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].\
            agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())

    def draw(self, name=None, arrows=True, mapon=None, edge_route=None, label_color = "black"):
        G = nx.DiGraph()
        node_c = []
        for v in self.listaVertices.values():
            G.add_node(v.id)

        for v in self.listaVertices.values():
            l = [x.id for x in v.conectadoA]
            d = [v.conectadoA[x] for x in v.conectadoA]
            i = v.id
            node_c.append(v.color)
            for j in d:
                #print(i, l[d.index(j)],j)
                G.add_edge(i, l[d.index(j)], dis=j)

        pos = nx.spring_layout(G, seed=3504)
        edge_labels = dict([((u,v,),d['dis']) for u,v,d in G.edges(data=True)])

        if mapon:
            nx.draw_networkx_nodes(G, pos, node_color=range(self.numVertices), edgecolors="black", cmap=plt.cm.Blues)
        else:
            nx.draw_networkx_nodes(G, pos, node_color=node_c, edgecolors="black")

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