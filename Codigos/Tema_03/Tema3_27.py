#Tema3_27
def mochila_d_pd3(p,b,M):
    n= len(p)
    ant =[0 for m in range(M+1)]
    act =[0 for m in range(M+1)]
    d =[[0 for m in range(M+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for m in range(1,M+1) :
            if p[i-1]<=m and b[i-1]+ ant[m-p[i-1]] > ant[m]:
                act[m]=b[i-1]+ ant[m-p[i-1]]
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
            m=m-p[i-1]
    return x,act[M]

p = [2, 5, 3, 6, 1]
b = [28, 33, 5, 12, 20]
M = 10
x,t = mochila_d_pd3(p, b, M)
print("Maximo beneficio",t)
print("Lista de escogidos",x)