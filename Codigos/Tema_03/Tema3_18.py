#Tema3_18
def precompute_table(v):
    global t #t[k]=sum_{i=k+1-->len(v)-1}v[i]
    t =[0]
    for i in range(len(v)-1,0,-1):
        t.insert(0,t[0]+v[i])
def suma_enteros(x,v,suma,M):
    global t #t[k]=sum_{i=k+1-->len(v)-1}v[i]
    k = len(x)
    n = len(v)
    if k==n: # es solucion: suma = M
        return [x]
    ls = []
    # if EsFactible x[k]=1
    if suma+v[k] <= M and suma+v[k]+t[k] >= M:
        ls = ls+suma_enteros(x[:]+[1],v,suma+v[k],M)
    # if EsFactible x[k]=0
    if suma+t[k] >= M:
        ls = ls+suma_enteros(x[:]+[0],v,suma,M)
    return ls
