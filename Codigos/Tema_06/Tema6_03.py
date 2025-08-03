#Tema6_03
from Class_Grafos import Grafo
from Class_Estructuras_lineales import Cola

def bea(g,inicio):
    inicio.asignarDistancia(0)
    inicio.asignarPredecesor(None)
    colaVertices = Cola()
    colaVertices.agregar(inicio)
    print('inicio',inicio)
    while (colaVertices.tamano() > 0):
        verticeActual = colaVertices.avanzar()
        for vecino in verticeActual.obtenerConexiones():
            if (vecino.obtenerColor() == 'blanco'):
                vecino.asignarColor('gris')
                print('vecino',vecino)
                vecino.asignarDistancia(verticeActual.obtenerDistancia() + 1)
                vecino.asignarPredecesor(verticeActual)
                colaVertices.agregar(vecino)
        verticeActual.asignarColor('negro')

def construirGrafo(archivoPalabras):
    d = {}
    g = Grafo()
    archivo = open(archivoPalabras,'r')
    print("Construimos el grafo \n\n")
    for linea in archivo:
        palabra = linea[:-1]
        for i in range(len(palabra)):
            recipiente = palabra[:i] + '_' + palabra[i+1:]
            if recipiente in d:
                d[recipiente].append(palabra)
            else:
                d[recipiente] = [palabra]
    for recipiente in d.keys():
        for palabra1 in d[recipiente]:
            for palabra2 in d[recipiente]:
                if palabra1 != palabra2:
                    g.agregarArista(palabra1,palabra2)
    return g

g=construirGrafo("test2.txt")

for k in dict.values(g.listaVertices):
    print(k)

print('Empiezo recorrido \n\n\n')
input("Pulsa una tecla")

for k in dict.values(g.listaVertices):
    bea(g,k)
    #print(k)
    #input()

def recorrer(y):
    print(' Recorro\n\n')
    x = y
    print(x)
    while (x.obtenerPredecesor()):
        print(x.obtenerId())
        x = x.obtenerPredecesor()
        print(x)
    print(x.obtenerId())


recorrer(g.obtenerVertice('SAGE'))
input("\n\nPulsa una tecla")

for k in dict.values(g.listaVertices):
    bea(g,k)

for k,v in dict.items(g.listaVertices):
    print("{0}: {1}".format(k,v))
