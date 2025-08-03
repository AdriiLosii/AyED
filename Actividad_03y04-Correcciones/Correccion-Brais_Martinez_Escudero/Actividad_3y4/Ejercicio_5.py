
    

def Mochila(peso,beneficio,M):
    n= len(peso)
    ant =[0 for m in range(M+1)]
    act =[0 for m in range(M+1)]
    d =[[0 for m in range(M+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for m in range(1,M+1) :
            if peso[i-1]<=m and beneficio[i-1]+ ant[m-peso[i-1]] > ant[m]:
                act[m]=beneficio[i-1]+ ant[m-peso[i-1]]
                d[i][m]=1
            else:
                act[m]= ant[m]
                d[i][m]=0
        ant = act[:]
    x =[]
    m=M
    for i in range(n,0,-1):
        x.insert(0,d[i][m])
        if d[i][m]==1:
            m=m-peso[i-1]
    return x,act[M]


peso = [2, 3, 4, 7, 8, 18]
beneficio = [3, 5, 8, 8, 12, 20]
M = 35
A,B = Mochila(peso, beneficio, M)
print("Maximo beneficio",B)
print("Lista de escogidos",A)

peso = [7, 8, 10, 14]
beneficio = [4, 7, 7, 20]
M = 32
C,D = Mochila(peso, beneficio, M)
print("Maximo beneficio",D)
print("Lista de escogidos",C)