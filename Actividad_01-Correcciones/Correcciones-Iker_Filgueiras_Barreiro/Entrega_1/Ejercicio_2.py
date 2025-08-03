from Clase_puertasLogicas import *

entradaA=(int(input("Introduce el valor de señal de la entrada A (0 o 1): ")))
entradaB=(int(input("Introduce el valor de señal de la entrada B (0 o 1): ")))
entradaC=(int(input("Introduce el valor de señal de la entrada C (0 o 1): ")))
entradaD=(int(input("Introduce el valor de señal de la entrada D (0 o 1): ")))

pAND1=PuertaAND("p1", entradaA, entradaB)
pAND2=PuertaAND("p2", entradaC, entradaD)
pOR1=PuertaOR("p3", pAND1.salida(), pAND2.salida())
pNOT1=PuertaNOT("p4", pOR1.salida())
print("El resultado de la primera ecuación es: ", pNOT1.salida())


pNAND1=PuertaNAND("p5", entradaA, entradaB)
pNAND2=PuertaNAND("p6", entradaC, entradaD)
pAND3=PuertaAND("p7", pNAND1.salida(), pNAND2.salida())

print("El resultado de la primera ecuación es: ", pAND3.salida())

if pNOT1.salida() == pAND3.salida():
    print("Las salidas de las dos ecuaciones coinciden por lo que son equivalentes.")
else:
    print("Las salidas de las dos ecuaciones no coinciden por lo que no son equivalentes.")