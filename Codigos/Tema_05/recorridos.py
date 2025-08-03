from Class_Estructuras_lineales import Pila
from Class_Arboles import *
import operator  #versiones funcionales de muchos operadores utilizados comúnmente

def preorden(arbol):
    if arbol:
        print(arbol.obtenerValorRaiz())
        preorden(arbol.obtenerHijoIzquierdo())
        preorden(arbol.obtenerHijoDerecho())

def postorden(arbol):
    if arbol != None:
        postorden(arbol.obtenerHijoIzquierdo())
        postorden(arbol.obtenerHijoDerecho())
        print(arbol.obtenerValorRaiz())

def inorden(arbol):
    if arbol != None:
        inorden(arbol.obtenerHijoIzquierdo())
        print(arbol.obtenerValorRaiz())
        inorden(arbol.obtenerHijoDerecho())

def evalPostorden(arbol):
    operadores = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    res1 = None
    res2 = None
    if arbol:
        res1 = evalPostorden(arbol.obtenerHijoIzquierdo())
        res2 = evalPostorden(arbol.obtenerHijoDerecho())
    if res1 and res2:
        return operadores[arbol.obtenerValorRaiz()](res1,res2)
    else:
        return arbol.obtenerValorRaiz()

def imprimirExpresion(arbol):
    valorCadena = ""
    if arbol:
        valorCadena = '(' + imprimirExpresion(arbol.obtenerHijoIzquierdo())
        valorCadena = valorCadena + str(arbol.obtenerValorRaiz()) 
        valorCadena = valorCadena + imprimirExpresion(arbol.obtenerHijoDerecho())+')'
    return valorCadena

