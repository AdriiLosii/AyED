#Tema3_20
def fib_ite(n):
    f2 =1 # f2 es el termino F_{n-2}
    f1 =1 # f1 es el termino F_{n-1}
    for i in range(2,n+1) :
        f=f1+f2 # F_{n} = F_{n-1} + F_{n-2}
        f2=f1
        f1=f
    return f