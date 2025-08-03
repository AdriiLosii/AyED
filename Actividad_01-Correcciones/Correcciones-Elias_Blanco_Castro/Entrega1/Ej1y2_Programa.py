#Este programa comprueba si las ecuaciones NOT((A and B) or (C and D)) y 
# NOT(A and B) and NOT (C and D) son equivalentes
from Ej1y2_Clase import *

def main():

    print("\nEste programa compara NOT((A&&B) || (C&&D)) con (NOT(A&&B) && NOT(C&&D))")
    salidas1 = []
    salidas2 = []

    for i in range(0, 2, 1):
        for j in range(0, 2, 1):
            for k in range(0, 2, 1):
                for l in range(0, 2, 1):
                    datos = [i, j, k, l]
                    print(datos)
                    c1 = PuertaAND("C1")
                    c2 = PuertaAND("C2")
                    c3 = PuertaNOR("C3")
                    Conector(c1, c3)
                    Conector(c2, c3)

                    salidas1.append(c3.obtenerSalida(datos))
                    
                    c4 = PuertaNAND("C4")
                    c5 = PuertaNAND("C5")
                    c6 = PuertaAND("C6")
                    Conector(c4, c6)
                    Conector(c5, c6)
                    
                    salidas2.append(c6.obtenerSalida(datos))

    print(salidas1, "~~~", salidas2)

    if (salidas1 == salidas2):

        print("\nLas ecuaciones devuelven los mismo resultados")

    else:

        print("\nLas ecuaciones devuelven resultados distintos")



main()
