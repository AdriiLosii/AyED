#Tema3_26
# Devuelve el maximo beneficio alcanzable con los objetos de pesos p y beneficios b, teniendo un peso M disponible
def mochila_d_pd2(p,b,M):
    n= len (p)
    ant =[0 for m in range(M+1)]
    act =[0 for m in range(M+1)]
    for i in range(1,n+1):
        for m in range(1,M+1):
        # si se puede introducir el objeto i y el beneficio es mayor que no haciendolo, lo introducimos
            if p[i-1] <=m and b[i-1]+ ant[m-p[i-1]] > ant[m]:
                act[m]=b[i-1]+ ant[m-p[i-1]]
            # en caso contrario, no lo introducimos
            else:
                act[m]= ant[m]
        ant = act[:]
    return act[M]


p = [2, 5, 3, 6, 1]
b = [28, 33, 5, 12, 20]
M = 10
t = mochila_d_pd2(p, b, M)
print("Maximo beneficio",t)