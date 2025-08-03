from Class_Puertas import *


def main():
    c1 = PuertaAND("C1")
    c2 = PuertaAND("C2")
    c3 = PuertaOR("C3")
    c4 = PuertaNOT("C4")
    c1 = Conector(c1, c3)
    c2 = Conector(c2, c3)
    c3 = Conector(c3, c4)
    print(c4.obtenerSalida())


main()
