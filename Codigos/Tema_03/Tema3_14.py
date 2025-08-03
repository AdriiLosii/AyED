# Tema3_14 Esquema
# Backtracking rápido
# (encontrar una solución)
def backtracking(nodo):
    if EsSolucion(nodo):
        return nodo
    for v in Expandir(nodo):
        if EsFactible(v):
            s = backtracking(v)
            if s != None:
                return s
    return None
