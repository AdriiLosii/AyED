#Tema2_04
from Class_Estructuras_lineales import Pila


def dividirPor2(numeroDecimal):
    pilaresto = Pila()

    while numeroDecimal > 0:
        resto = numeroDecimal % 2
        pilaresto.incluir(resto)
        numeroDecimal = numeroDecimal // 2

    cadenaBinaria = ""
    while not pilaresto.estaVacia():
        cadenaBinaria = cadenaBinaria + str(pilaresto.extraer())

    return cadenaBinaria


print(dividirPor2(421))
