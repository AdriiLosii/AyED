"""
Programa: Ej02.py
Propósito:
    Modifica las funciones construirArbolAnalisis y evaluar para que puedan manejar las sentencias
    booleanas (and, or, y not). Recuerda que “not” es un operador unario, por lo que esto complicará un poco
    la realización del código.
Fecha: 07/05/2022
"""


from operator import *
from Class_Estructuras_lineales import Pila
from Class_Arboles_02 import ArbolBinario
import operator  #versiones funcionales de muchos operadores utilizados comúnmente


def construirArbolAnalisis(expresionAgrupada):   #Definimos la funcion que se encarga de crer un arbol de analisis
   
    numero=""
    for simbolo in expresionAgrupada:
        if simbolo in ['(','+', '-', '*', '/','AND','OR','NOT', ')']:  #Todos los simbolos posibles
            numero += " "+simbolo+" "
        else:
            numero += simbolo
    listaSimbolos = numero.split()
    
    for simbolo in listaSimbolos:   #Asignamos a 1 y 0 las sentencias booleanas correspondientes (True y False)
        if simbolo=='1':
            listaSimbolos[listaSimbolos.index(simbolo)]=True
        elif simbolo=='0':
            listaSimbolos[listaSimbolos.index(simbolo)]=False

    pilaPadres = Pila()
    arbolExpresion = ArbolBinario('')
    pilaPadres.incluir(arbolExpresion)
    arbolActual = arbolExpresion
    
    for i in listaSimbolos:   #Recorremos la sentencia que se nos presente
        if i == '(':
            arbolActual.insertarIzquierdo('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoIzquierdo()
        elif i not in ['+', '-', '*', '/', ')','OR','AND','NOT','']:
            arbolActual.asignarValorRaiz((i))
            padre = pilaPadres.extraer()
            arbolActual = padre
        elif i in ['+', '-', '*', '/','OR','AND','NOT','']:
            arbolActual.asignarValorRaiz(i)
            arbolActual.insertarDerecho('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoDerecho()
        elif i in['NOT']:
            arbolActual.asignarValorRaiz(i)
            arbolActual.insertarDerecho('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoDerecho()
        elif i == ')':
            arbolActual = pilaPadres.extraer()
        else:
            raise ValueError
        
    return arbolExpresion


def evaluar(arbolAnalisis):   #Definimos la funcion que se encargara de evaluar la sentencia correspondiente
    operadores = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv,'OR':operator.or_,'AND':operator.and_,'NOT':NOT}
    
    hijoIzquierdo = arbolAnalisis.obtenerHijoIzquierdo()   #Obtenemos los valores de los hijos izquierdos y derecho del árbol
    hijoDerecho = arbolAnalisis.obtenerHijoDerecho()

    if hijoIzquierdo and hijoDerecho:    #Si la sentencia dispone de ambos hjos, los evaluamos , si no evaluamos solamente el que tenga
        fn = operadores[arbolAnalisis.obtenerValorRaiz()]
        ev=fn(evaluar(hijoIzquierdo),evaluar(hijoDerecho))
        return ev
    elif hijoDerecho:
        fn = operadores[arbolAnalisis.obtenerValorRaiz()]
        ev=fn(evaluar(hijoDerecho))
        return ev
    
    elif hijoIzquierdo:
        fn = operadores[arbolAnalisis.obtenerValorRaiz()]
        ev=fn(evaluar(hijoIzquierdo))
        return ev
        
    else:
        
        return arbolAnalisis.obtenerValorRaiz()
    

def NOT(valor):  #Creamos una funcion específica para hacer NOT, ya que no funciona igual que AND y OR puesto que es unario no binario

    if valor == "1" or valor == True:
        return False
    else:
        return True


#Programa principal:
#Definimos las expresiones y las evaluamos, mostrando el resultado.
exp1 = "((1 OR 0) AND 1)"
exp2 = "NOT (0 OR 1)"
miArbolAnalisis = construirArbolAnalisis(exp1)
res1 = evaluar(miArbolAnalisis)
print("\nExpresión 1 ->",exp1,"=",res1)

miArbolAnalisis = construirArbolAnalisis(exp2)
res2 = evaluar(miArbolAnalisis)
print("\nExpresión 2 ->",exp2,"=",res2)

#FIN.
input("\nPulse ENTER para finalizar.")