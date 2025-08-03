# Tema3_11 Esquema
def Algoritmo_Voraz(Conjunto_Entrada):
    Conjunto = Conjunto_Entrada
    Solucion = []
    encontrada = False
    while not EsVacio(Conjunto) and not encontrada:
        x = Seleccionar_Mejor_Candidato(Conjunto)
        Conjunto = Conjunto - [x]
        if EsFactible(Solucion + [x]):
            Solucion = Solucion + [x]
        if EsSolucion(Solucion):
            encontrada = True
    return Solucion
