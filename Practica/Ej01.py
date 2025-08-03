#Importamos la clase
from Class_ArbolBinario_01 import ArbolBinario

#Programa principal:
arbolBin = ArbolBinario(30)

#Agregamos números al árbol.
arbolBin.insertarIzquierdo(5)
arbolBin.obtenerHijoIzquierdo().insertarIzquierdo(3)
arbolBin.obtenerHijoIzquierdo().insertarDerecho(7)
arbolBin.insertarDerecho(50)
arbolBin.obtenerHijoDerecho().insertarIzquierdo(46)
arbolBin.obtenerHijoDerecho().insertarDerecho(80)
#arbolBin.obtenerHijoDerecho().obtenerHijoDerecho().insertarIzquierdo(79)

#Mostramos los elementos del árbol.
print("raiz:",arbolBin.obtenerValorRaiz())
print("hijoIzq de la raiz:",arbolBin.obtenerHijoIzquierdo().obtenerValorRaiz())
print("hijoIzq del hijoIzq:",arbolBin.obtenerHijoIzquierdo().obtenerHijoIzquierdo().obtenerValorRaiz())
print("hijoDer del hijoIzq:",arbolBin.obtenerHijoIzquierdo().obtenerHijoDerecho().obtenerValorRaiz())
print("hijoDer de la raiz:",arbolBin.obtenerHijoDerecho().obtenerValorRaiz())
print("hijoIzq del hijoDer:",arbolBin.obtenerHijoDerecho().obtenerHijoIzquierdo().obtenerValorRaiz())
print("hijoDer del hijoDer:",arbolBin.obtenerHijoDerecho().obtenerHijoDerecho().obtenerValorRaiz())
#print("hijoIzq del hijoDer del hijoDer del nodo raíz:",arbolBin.obtenerHijoDerecho().obtenerHijoDerecho().obtenerHijoIzquierdo().obtenerValorRaiz())



#APARTADO A)

#Mostramos los resultados.
print("\nNúmero de nodos del árbol:",arbolBin.numNodos(arbolBin))
print("Número de nodos hojas del árbol:",arbolBin.numHojas(arbolBin))
print("Profundidad del árbol:",arbolBin.profundidad(arbolBin))



#APARTADO B)

print("Recorrido inorden del árbol binario:", end = " ");arbolBin.inorden(arbolBin)
arbolEspejo = arbolBin.espejo(arbolBin)
print("\nRecorrido inorden del árbol binario espejo:", end = " ");arbolEspejo.inorden(arbolEspejo)

#Fin.
input("\nPulse ENTER para finalizar.")