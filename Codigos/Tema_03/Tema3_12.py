#Tema3_12
monedas =[500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
def Devolver_Cambio(cantidad,monedas):
    n = len(monedas)
    cambio = [0 for i in range(n)]
    for i in range(n):
        while monedas[i] < cantidad:
            cantidad = cantidad-monedas[i]
            cambio[i] = cambio[i]+1
    return cambio
