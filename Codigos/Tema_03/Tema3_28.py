#Tema3_28
# Devuelve el maximo beneficio alcanzable con los objetos de pesos p y beneficios b, teniendo un peso M disponible, asi como la solucion que lo produce
def mochila_d_pd4(p,b,M):
    n= len(p)
    ant =[[0,[]] for m in range(M+1)]
    for i in range(1,n+1):
        act =[[0,[0 for j in range(i)]]]
        for m in range(1,M+1):
            if p[i-1]<=m and b[i-1]+ant[m-p[i-1]][0] > ant[m][0]:
                act.append([b[i-1]+ant[m-p[i-1]][0],ant[m-p[i-1]][1][:]+[1]])
            else:
                act.append([ant[m][0],ant[m][1][:]+[0]])
        ant = act
    return act[M]

p = [2, 5, 3, 6, 1]
b = [28, 33, 5, 12, 20]
M = 10
t = mochila_d_pd4(p, b, M)
print("Maximo beneficio",t)
