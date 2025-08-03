"""Modifica el algoritmo de evaluación en notación sufija para que pueda manejar
errores y que pueda manejar operandos de más de una cifra int o float"""
from multiprocessing.sharedctypes import Value
from Class_Estructuras_lineales import Pila


def evaluacionNotacionSufija(expresionSufija):

    try:

        pilaOperandos = Pila()
        listaSimbolos = expresionSufija.split()
        print(listaSimbolos)

        for simbolo in listaSimbolos:

            elemento = ""

            if (simbolo in '+-*/'):
                operando2 = pilaOperandos.extraer()
                operando1 = pilaOperandos.extraer()
                resultado = hacerAritmetica(simbolo, operando1, operando2)
                pilaOperandos.incluir(resultado)
            
            else:

                for caracter in simbolo:
                    elemento+=caracter
                
                pilaOperandos.incluir(float(elemento))


            
        
        return pilaOperandos.extraer()
    
    except ZeroDivisionError:
        print("ERROR: no se puede dividir entre 0")
    except IndexError:
        print("ERROR: no se ha escrito la expresión correctamente")
    except ValueError:
        print("ERROR: se ha escrito uno o varios operandos de manera incorrecta")
    except:
        print("ERROR: ha ocurrido un error inesperado")


def hacerAritmetica(operador, operandoIzquierda, operandoDerecha):
    if operador == "*":
        return operandoIzquierda * operandoDerecha
    elif operador == "/":
        return operandoIzquierda / operandoDerecha
    elif operador == "+":
        return operandoIzquierda + operandoDerecha
    else:
        return operandoIzquierda - operandoDerecha


print(evaluacionNotacionSufija('4 -5 61 * +'))
print(evaluacionNotacionSufija('7 8.23 + 3 2 + /'))
print(evaluacionNotacionSufija("3.3 0 /"))
print(evaluacionNotacionSufija('- 4 2'))
print(evaluacionNotacionSufija('3.3-2 9 *'))
