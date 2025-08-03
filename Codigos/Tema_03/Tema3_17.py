#Tema3_17
def EsFactible(k,j,c):
    for i in range(k):
        if c[i]==j or (i-c[i])==(k-j) or (i+c[i])==(k+j):
            return False
    return True

def reinas(c,n):
    k = len(c)
    if k == n:
        return c
    for j in range(n):
        if EsFactible(k,j,c):
            v = c [:] + [j]
            s = reinas(v,n)
        if s != None:
            return s
    return None

