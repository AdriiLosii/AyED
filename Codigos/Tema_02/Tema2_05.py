#Tema2_05
from Class_Estructuras_lineales import Pila


def convertirBase(numeroDecimal, base):
    digitos = "0123456789ABCDEF"

    pilaresto = Pila()

    while numeroDecimal > 0:
        resto = numeroDecimal % base
        pilaresto.incluir(resto)
        numeroDecimal = numeroDecimal // base

    nuevaCadena = ""
    while not pilaresto.estaVacia():
        nuevaCadena = nuevaCadena + digitos[pilaresto.extraer()]

    return nuevaCadena


print(convertirBase(421, 2))
print(convertirBase(421, 16))
