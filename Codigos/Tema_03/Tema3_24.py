#Tema3_24
# Solucion y maximo beneficio alcanzable con los objetos 0..i-1, teniendo un peso m disponible en la mochila
def mochila_d_rec(i,m,p,b):
    # base de la recurrencia : 0 objetos
    if i ==0:
        return[],0
    # opcion 1: el objeto i-1 NO se introduce
    sol_NO,max_b_NO = mochila_d_rec(i-1,m,p,b)
    # opcion 2: el objeto i-1 SI se introduce
    if p[i-1]<=m:
        sol_SI,max_b_SI = mochila_d_rec(i-1,m-p[i-1],p,b)
        if b[i-1] + max_b_SI > max_b_NO:
            return [1]+sol_SI,b[i-1]+max_b_SI
    return [0]+sol_NO,max_b_NO

