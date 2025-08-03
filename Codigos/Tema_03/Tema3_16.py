# Tema3_16 Esquema
# Backtracking para optimizacion
# (encontrar la mejor solucion)
def backtracking(nodo):
    if EsSolucion(nodo):
        mejor_sol = nodo
    else:
        mejor_sol = None
    for v in Expandir(nodo):
        if EsFactible(v):
            ms = backtracking(v)
        if mejor_sol == None or f(ms) > f(mejor_sol):
            mejor_sol = ms
    return mejor_sol
