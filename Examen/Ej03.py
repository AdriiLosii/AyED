from Class_ArbolesBinariosBusqueda_03 import ArbolBinarioBusqueda


arbol = ArbolBinarioBusqueda()

lista = ["G","B","Q","A","C","K","F","P","D","E","R","H"]

for i in lista:
    arbol.agregar(i, i)

print("a)", end=" ");arbol.preorden()
print("b)", end=" ");arbol.inorden()
print("c)", end=" ");arbol.postorden()
print("d)", end=" ");arbol.anchura()

print("Cantidad de nodos en el árbol:",arbol.nodos())
print("Cantidad de nodos hoja en el árbol:",arbol.hojas())
print("Profundidad del árbol:",arbol.profundidad())