"""
Programa: Ej04.py
Propósito:
    Usando el algoritmo de programación dinámica para dar las vueltas, encuentra el
    menor número de monedas que se podrían usar para completar unas vueltas de 33
    céntimos. Además de las monedas usuales, supón que disponemos de una moneda de
    8 céntimos. Realizar una simulación con distintas cantidades a devolver y distintos
    valores de monedas.
Fecha: 04/04/2022
Autores: Gabriel Iglesias Sotelo y Adrián Losada Álvarez 
"""


#Creamos la función para dar la vueltas.
def vueltasProgDin(listValMonedas, vueltas, minMonedas, monedasUsadas):

   for centavos in range(vueltas+1):  
        conteoMonedas = centavos
        nuevaMoneda = 1

        for j in [m for m in listValMonedas if m <= centavos]:
                if minMonedas[centavos-j] + 1 < conteoMonedas:
                    conteoMonedas = minMonedas[centavos-j]+1
                    nuevaMoneda = j
        minMonedas[centavos] = conteoMonedas
        monedasUsadas[centavos] = nuevaMoneda

   return minMonedas[vueltas]  #Devolvemos las monedas minimas

#Creamos la función para mostrar el valor de las monedas usadas.
def imprimirMonedas(monedasUsadas, vueltas):

    moneda = vueltas
    while (moneda > 0):
        estaMoneda = monedasUsadas[moneda]
        print("Moneda de:",estaMoneda, "centavo(s).")
        moneda -= estaMoneda

#Creamos la función para solicitar el valor de las monedas.
def valores_monedas(num):

    monedas=[]

    for i in range (0, num):
        try:
            valor = int(input("Dame el valor de tu moneda numero {0} (en centavos):  ".format(i+1)))  #Se pide cada moneda
            if (valor <= 0):
                raise ValueError()

            monedas.append(valor)

        except ValueError:
            print("\nError, ha ocurrido algo inesperado.")   #Notificamos error en la lectura de datos
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

    return(monedas)  #Devolvemos las monedas


#Programa principal:
try:

    cantidad = int(input("\n¿Cuánto dinero quieres cambiar?\n")) #Solicitamos el cambio.
    if (cantidad < 0):
        raise ValueError()

    num_monedas = int(input("Dame el numero de monedas que tiene el pais donde vas a hacer el cambio: ")) #Solicitamos el número de monedas totales.
    if (num_monedas <= 0):
        raise ValueError()

    listaM = valores_monedas(num_monedas) #Llamamos a la función para pedir los valores de las monedas.

    monedasUsadas = [0]*(cantidad+1)
    conteoMonedas = [0]*(cantidad+1)

    #Mostramos los resultados.
    print("\nDar unas vueltas de",cantidad,"centavos requiere:",vueltasProgDin(listaM, cantidad, conteoMonedas, monedasUsadas),"monedas")
    print("Tales monedas son:")
    imprimirMonedas(monedasUsadas,cantidad)

    #FIN.
    input("\nPulse ENTER para finalizar.")

except ValueError:
    print("\nError, ha ocurrido algo inesperado.")   #Notificamos error en la lectura de datos
    input("Pulse ENTER para finalizar.")
    quit() #Salimos del programa