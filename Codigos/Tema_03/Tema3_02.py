#Tema3_02
from Estructuras_lineales import Pila
pilaResultados = Pila()

def aCadena(n,base):
    cadenaConversion = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            pilaResultados.incluir (cadenaConversion[n])
        else:
            pilaResultados.incluir (cadenaConversion[n%base])
        n = n // base
    resultado = ""
    while not pilaResultados.estaVacia():
        resultado = resultado + str(pilaResultados.extraer())
    return resultado

num=int(input("Dame un numero decimal: "))
base=int(input("A que base <16 lo quieres transformar: " ))
print(aCadena(num,base))
