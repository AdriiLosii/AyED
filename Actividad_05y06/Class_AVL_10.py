"""
Programa: Class_AVL_10.py
Propósito:
    Dada la secuencia de claves enteras 20, 10, 30, 5, 25, 12, 3, 35, 22, 11, 6, 2, y la secuencia 100, 29, 71, 82, 48,
    39, 101, 22, 46, 17, 3, 20, 25, 10, representa gráficamente los árboles AVL correspondientes e indica en qué
    momento se efectuó una rotación.
Fecha: 07/05/2022
"""


from Class_Nodos_10 import *
import graphviz   #Importamos la libreria para poder dibujar los arboles


class ArbolBinarioBusquedaAVL:

    def __init__(self):
        self.raiz = None
        self.tamano = 0
        self.g = graphviz.Digraph('Arbol AVL')

    def muestra_graphviz(self, nodos, valores, aristas):
        #Establecemos cada numero como un nodo
        for i in range(len(nodos)):
            self.g.node(nodos[i], valores[i])

        self.g.edges(aristas)   #Realizamos las conexiones de cada nodo para crear la forma final del arbol

        self.g.format='png'  #Haacemos que sea un png
        self.g.render(directory='REPRESENTACIONES_EJ10', view=True).replace('\\', '/')   #Creamos una carpeta de destino

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano
    
    def __iter__(self):
        return self.raiz.__iter__()

    def agregar(self, clave, valor):
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
        self.tamano = self.tamano + 1
        
    def _agregar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                #Si el nodo actual requiere reequilibrio,  
                #entonces se realiza y no se requiere hacer ninguna nueva 
                #actualización a los padres.
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                #Si el nodo actual no requiere reequilibrio entonces se ajusta 
                #el factor de equilibrio del padre. 
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoDerecho)

    def __setitem__(self, c, v):
        self.agregar(c, v)

    def actualizarEquilibrio(self, nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                #Si el factor de equilibrio del padre no es cero, entonces 
                #el algoritmo continúa ascendiendo en el árbol
                #hacia la raíz, llamando recursivamente a actualizarEquilibrio 
                #con el padre como parámetro.
                self.actualizarEquilibrio(nodo.padre)

    def reequilibrar(self, nodo):
        if nodo.factorEquilibrio < 0:
            if nodo.hijoDerecho.factorEquilibrio > 0:
                print("Rotación a la derecha y a la izquierda el nodo:",nodo.clave)
                self.rotarDerecha(nodo.hijoDerecho)
                self.rotarIzquierda(nodo)
            else:
                print("Rotamos a la izquierda el nodo:",nodo.clave)
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
            if nodo.hijoIzquierdo.factorEquilibrio < 0:
                print("Rotamos a la izquierda y a la derecha el nodo:",nodo.clave)
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
            else:
                print("Rotamos a la derecha el nodo:",nodo.clave)
                self.rotarDerecha(nodo)

    def rotarIzquierda(self, rotRaiz):
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)

    def rotarDerecha(self, rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                rotRaiz.padre.hijoDerecho = nuevaRaiz
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 + max(rotRaiz.factorEquilibrio, 0)

    def obtener(self, clave):
        if self.raiz:
            res = self._obtener(clave, self.raiz)
            if res:
                return res.cargaUtil
            else:
                return None
        else:
            return None

    def _obtener(self, clave, nodoActual):
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave, nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave, nodoActual.hijoDerecho)

    def __getitem__(self, clave):
        res = self.obtener(clave)
        if res:
            return res
        else:
            raise KeyError('Error, la clave no esta en el arbol')

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.hijoIzquierdo)
            print(nodo.cargaUtil, end=" ")
            self.__inorden_recursivo(nodo.hijoDerecho)
            
    def inorden(self):
        print("Recorrido del árbol inorden: ", end="")
        self.__inorden_recursivo(self.raiz)
        print("")
              
    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.hijoIzquierdo)
            self.__postorden_recursivo(nodo.hijoDerecho)
            print(nodo.cargaUtil, end=" ")
            
    def postorden(self):
        print("Recorrido del árbol postorden: ", end="")
        self.__postorden_recursivo(self.raiz)
        print("")
        
    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.cargaUtil, end=" ")
            self.__preorden_recursivo(nodo.hijoIzquierdo)
            self.__preorden_recursivo(nodo.hijoDerecho)
        
    def preorden(self):
        print("Recorrido del árbol preorden: ", end="")
        self.__preorden_recursivo(self.raiz)
        print("")