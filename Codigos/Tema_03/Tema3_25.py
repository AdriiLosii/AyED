# Tema3_25
# Devuelve el maximo beneficio alcanzable con los objetos # de pesos p y beneficios b, teniendo un peso M disponible
def mochila_d_pd1(p, b, M):
    n = len(p)
    t = [[0 for m in range(M+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for m in range(1, M+1):
            # si se puede introducir el objeto i y el beneficio es mayor que no haciendolo, lo introducimos
            if p[i-1] <= m and b[i-1] + t[i-1][m-p[i-1]] > t[i-1][m]:
                t[i][m] = b[i-1] + t[i-1][m-p[i-1]]
            # en caso contrario, no lo introducimos
            else:
                t[i][m] = t[i-1][m]
    #return t[n][M]
    print("Maximo beneficio",t[n][M])
    return t


p = [2, 5, 3, 6, 1]
b = [28, 33, 5, 12, 20]
M = 10
t = mochila_d_pd1(p, b, M)
print(t)
