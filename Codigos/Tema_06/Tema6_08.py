
#Tema6_08
from Class_Grafos import Grafo, Vertice
from Class_Monticulos import MonticuloBinario 
from Class_Estructuras_lineales import ColaPrioridad

def prim(G,inicio):
    cp = ColaPrioridad()
    for v in G:
        v.asignarDistancia(sys.maxsize)
        v.asignarPredecesor(None)
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in G])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtenerConexiones():
          nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
          if verticeSiguiente in cp and nuevoCosto<verticeSiguiente.obtenerDistancia():
              verticeSiguiente.asignarPredecesor(verticeActual)
              verticeSiguiente.asignarDistancia(nuevoCosto)
              cp.decrementarClave(verticeSiguiente,nuevoCosto)

