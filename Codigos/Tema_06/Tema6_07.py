#Tema6_07
from Class_Grafos import Grafo, Vertice
from Class_Monticulos import MonticuloBinario 
from Class_Estructuras_lineales import ColaPrioridad

def dijkstra(unGrafo,inicio):
    cp = ColaPrioridad() #Realmente se implementa con un Montículo binario
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = verticeActual.obtenerDistancia() + verticeActual.obtenerPonderacion(verticeSiguiente)
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia( nuevaDistancia )
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente,nuevaDistancia)
