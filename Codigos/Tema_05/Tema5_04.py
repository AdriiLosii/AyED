#Tema5_04
from Class_Estructuras_lineales import Pila
from Class_Arboles import ArbolBinario
import operator  #versiones funcionales de muchos operadores utilizados comúnmente

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

def evaluar(arbolAnalisis):
    operadores = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}

    hijoIzquierdo = arbolAnalisis.obtenerHijoIzquierdo()
        
    hijoDerecho = arbolAnalisis.obtenerHijoDerecho()

    if hijoIzquierdo and hijoDerecho:
        fn = operadores[arbolAnalisis.obtenerValorRaiz()]
        return fn(evaluar(hijoIzquierdo),evaluar(hijoDerecho))
    else:
        return arbolAnalisis.obtenerValorRaiz()

miArbolAnalisis = construirArbolAnalisis("( ( 10 + 5 ) * 3 )")
print(evaluar(miArbolAnalisis))

miArbolAnalisis = construirArbolAnalisis("( ( 10 + 5 ) * ( 3 + 4 ) )")
print(evaluar(miArbolAnalisis))
