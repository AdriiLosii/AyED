#Tema3_13 Esquema
def Mochila(peso,beneficio,M):
    n=len(peso)
    solucion = [0.0 for i in range(n)]
    peso_actual = 0.0
    while peso_actual < M:
        i = mejor_objeto_restante(peso,beneficio)
        if peso[i] + peso_actual <= M:
            solucion[i] = 1
            peso_actual = peso_actual + peso[i]
        else:
            solucion[i] = (M-peso_actual)/peso[i]
            peso_actual = M
    return solucion
