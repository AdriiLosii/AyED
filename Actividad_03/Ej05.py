"""
Programa: Ej05.py
Propósito: 
    Supón que eres un científico de la computación/ladrón de arte que se ha colado en
    una galería de arte importante. Dispones sólo de una mochila para sacar las obras de
    arte robadas, que sólo puede contener W “kilos de arte”; no obstante, para cada pieza
    de arte conoces su valor y su peso. Escribe una función de programación dinámica
    para maximizar tus ganancias, con distintas capacidades de la mochila y distintos
    valores/pesos de los ítems.
Fecha: 04/04/2022
Autores: Gabriel Iglesias Sotelo y Adrián Losada Álvarez 
"""


def mochila(p,b,M):
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

def introducir_valor(num):

    objeto=[]

    for i in range (0,num):

        x=int(input("Dame el valor de tu objeto numero {0}:  ".format(i+1)))
        objeto.append(x)

    return(objeto)

def introducir_peso(num):

    objeto=[]

    for i in range (0,num):

        x=int(input("Dame el peso de tu objeto numero {0}:  ".format(i+1)))
        objeto.append(x)

    return(objeto)


try:
    num=int(input("Dime cuantos objetos tiene la lista: "))
    p = introducir_valor(num)
    b = introducir_peso(num)
    M = 10
    x,t = mochila(p, b, M)
    print("\nMaximo beneficio: ",t)
    print("Lista de escogidos: ",x)

except ValueError:
    print("Ha ocurrido un error en la lectura de datos")
    input("Pulsa ENTER para finalizar")
    quit()