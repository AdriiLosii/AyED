#Tema5_03
from Class_Estructuras_lineales import Pila
from Class_Arboles import ArbolBinario

def construirArbolAnalisis(expresionAgrupada):
    listaSimbolos = expresionAgrupada.split()
    print(listaSimbolos)
    pilaPadres = Pila()
    arbolExpresion = ArbolBinario('')
    pilaPadres.incluir(arbolExpresion)
    arbolActual = arbolExpresion
    for i in listaSimbolos:
        if i == '(':
            arbolActual.insertarIzquierdo('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoIzquierdo()
        elif i not in ['+', '-', '*', '/', ')']:
            arbolActual.asignarValorRaiz(int(i))
            padre = pilaPadres.extraer()
            arbolActual = padre
        elif i in ['+', '-', '*', '/']:
            arbolActual.asignarValorRaiz(i)
            arbolActual.insertarDerecho('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoDerecho()
        elif i == ')':
            arbolActual = pilaPadres.extraer()
        else:
            raise ValueError
    return arbolExpresion

miArbolAnalisis = construirArbolAnalisis ("( ( 10 + 5 ) * 3 )")
print(miArbolAnalisis) # Imprimir el objeto árbol pero no muestra los valores en los nodos

