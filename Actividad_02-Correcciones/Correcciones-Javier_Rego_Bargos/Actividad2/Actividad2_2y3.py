from Class_Estructuras_lineales import Pila
def crear_cadena():
    
    cad=""
    for  i in range (0,1000000):
        cad=cad+str(i)
    return cad    

def evaluacionNotacionSufija(expresionSufija):
    pilaOperandos = Pila()
    listaSimbolos = expresionSufija.split()
    cad=crear_cadena()

    for simbolo in listaSimbolos:
        if simbolo in cad:
            pilaOperandos.incluir(int(simbolo))
        else:
            operando2 = pilaOperandos.extraer()
            operando1 = pilaOperandos.extraer()
            resultado = hacerAritmetica(simbolo, operando1, operando2)
            pilaOperandos.incluir(resultado)
            print(operando1,simbolo,operando2,"=",resultado)
    return pilaOperandos.extraer()


def hacerAritmetica(operador, operandoIzquierda, operandoDerecha):
    if operador == "*":
        return operandoIzquierda * operandoDerecha
    elif operador == "/":
        return operandoIzquierda / operandoDerecha
    elif operador == "+":
        return operandoIzquierda + operandoDerecha
    elif operador == ".":
        return operandoIzquierda+operandoDerecha/(10*len(str(operandoDerecha)))
    else:
        return operandoIzquierda - operandoDerecha
    


print("La primera operacion a evaluar es 2.5 31 * 4 + que es:",evaluacionNotacionSufija('2 5 . 31 * 4 +'),"\n")
print("La segunda operacion a evaluar es 1.5 22 + 3 + 4 + 5 + que es:",evaluacionNotacionSufija('1 5 . 22 + 3 + 4 + 5 +'))
print("La tercera operacion a evaluar es 123 2.5 3.1 4 5 * + * + que es:",evaluacionNotacionSufija('123 2 5 . 3 1 . 4 5 * + * +'))