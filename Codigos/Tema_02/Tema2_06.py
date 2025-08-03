# Tema2_06
from Class_Estructuras_lineales import Pila


def infija_a_sufija(expresionInfija):
    precedencia = {}
    precedencia["*"] = 3
    precedencia["/"] = 3
    precedencia["+"] = 2
    precedencia["-"] = 2
    precedencia["("] = 1
    pilaOperadores = Pila()
    listaSufija = []
    listaSimbolos = expresionInfija.split()

    for simbolo in listaSimbolos:
        if simbolo in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or simbolo in "0123456789":
            listaSufija.append(simbolo)
        elif simbolo == '(':
            pilaOperadores.incluir(simbolo)
        elif simbolo == ')':
            simboloTope = pilaOperadores.extraer()
            while simboloTope != '(':
                listaSufija.append(simboloTope)
                simboloTope = pilaOperadores.extraer()
        else:
            while (not pilaOperadores.estaVacia()) and (precedencia[pilaOperadores.inspeccionar()] >= precedencia[simbolo]):
                listaSufija.append(pilaOperadores.extraer())
            pilaOperadores.incluir(simbolo)

    while not pilaOperadores.estaVacia():
        listaSufija.append(pilaOperadores.extraer())
    return " ".join(listaSufija)


def normaliza(expr):
    Nexpr = ""
    for c in expr:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or c in "*+/-" or c in "0123456789":
            Nexpr = Nexpr+c+' '
    return Nexpr


print(infija_a_sufija(normaliza("A*B+C*D")))
print(infija_a_sufija("( A + B ) * C - ( D - E ) * ( F + G )"))
