# Tema3_15 Esquema
# Backtracking exhaustivo
# (encontrar todas las soluciones)
def backtracking(nodo):
    lista_soluciones = []
    if EsSolucion(nodo):
        lista_soluciones.append(nodo)
    for v in Expandir(nodo):
        if EsFactible(v):
            ls = backtracking(v)
            lista_soluciones.extend(ls)
    return lista_soluciones
