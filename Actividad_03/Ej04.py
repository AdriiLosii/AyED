"""
Programa: Ej04.py
Propósito:
    Usando el algoritmo de programación dinámica para dar las vueltas, encuentra el
    menor número de monedas que se podrían usar para completar unas vueltas de 33
    céntimos. Además de las monedas usuales, supón que disponemos de una moneda de
    8 céntimos. Realizar una simulación con distintas cantidades a devolver y distintos
    valores de monedas.
Fecha: 04/04/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


def vueltasProgDin(listValMonedas,vueltas,minMonedas,monedasUsadas):

   for centavos in range(vueltas+1):
      conteoMonedas = centavos

      nuevaMoneda = 1
      for j in [m for m in listValMonedas if m <= centavos]:
            if minMonedas[centavos-j] + 1 < conteoMonedas:
               conteoMonedas = minMonedas[centavos-j]+1
               nuevaMoneda = j
      minMonedas[centavos] = conteoMonedas
      monedasUsadas[centavos] = nuevaMoneda

   return minMonedas[vueltas]

def imprimirMonedas(monedasUsadas,vueltas):

   moneda = vueltas
   while moneda > 0:
      estaMoneda = monedasUsadas[moneda]
      print(estaMoneda)
      moneda -= estaMoneda

def numero_de_monedas():

    try:
        num=int(input("Dame el numero de monedas que tiene el pais donde vas a hacer el cambio: "))
        return num
    except ValueError:
        print("Ha ocurrido un error en la lectura de datos")
    
def cantidad_a_cambiar():

    try:
        return int(input("\nCuanto dinero quieres cambiar?  "))

    except ValueError:
        print("Ha ocurrido un error en la lectura de datos")
        input("Pulse ENTER para finalizar.")
        quit() #Salimos del programa

def valores_monedas(num):

    monedas=[]

    for i in range (0,num):

        x=int(input("Dame el valor de tu moneda numero {0} (en centavos):  ".format(i+1)))
        monedas.append(x)

    return(monedas)


def main():

    while True:
        try:
            cantidad = cantidad_a_cambiar()
            num=numero_de_monedas()
            
            listaM = valores_monedas(num)
            monedasUsadas = [0]*(cantidad+1)
            conteoMonedas = [0]*(cantidad+1)

            print("Dar unas vueltas de",cantidad,"centavos requiere")
            print(vueltasProgDin(listaM,cantidad,conteoMonedas,monedasUsadas),"monedas")
            print("Tales monedas son:")
            imprimirMonedas(monedasUsadas,cantidad)

            break
        except:
            print("\nError, ha ocurrido algo inesperado.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

    


main()
