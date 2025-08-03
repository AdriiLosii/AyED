"""
Programa: Ej05.py
Propósito:
    Problema de Simulación: Tareas de impresión Disponemos en un laboratorio de una 
    impresora antigua capaz de procesar 10 páginas por minuto en calidad de borrador. 
    Suele haber 10 usuarios por hora, imprimiendo hasta 2 veces en ese tiempo, y la 
    extensión de estas tareas oscila entre 1 y 20 páginas. ¿Podrá la impresora actual 
    manejar la carga de tareas si fuera ajustada para imprimir con una mejor calidad, pero 
    con una tasa de página más lenta? (Tema2_12.py y Tema2_12.cpp) Simular distintas 
    situaciones de la impresora.
Fecha: 19/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importamos las clases.
from Class_Impresion_05 import *


#Creamos la función.
def simulacion(numeroSegundos, paginasPorMinuto):

    impresoraLaboratorio = Impresora(paginasPorMinuto)
    colaImpresion = Cola()
    tiemposEspera = []
    contador = 0

    for segundoActual in range(numeroSegundos):

        if nuevaTareaImpresion():
            contador += 1
            tarea = Tarea(segundoActual)
            colaImpresion.agregar(tarea)

        if (not impresoraLaboratorio.ocupada()) and (not colaImpresion.estaVacia()):
            tareaSiguiente = colaImpresion.avanzar()
            tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
            impresoraLaboratorio.iniciarNueva(tareaSiguiente)

        impresoraLaboratorio.tictac()

    esperaPromedio = sum(tiemposEspera)/float(len(tiemposEspera))

    print("Tiempo de espera promedio %6.2f segundos  %6.2f minutos  %3d tareas restantes." % (esperaPromedio, esperaPromedio/60, colaImpresion.tamano()))

#Creamos la función.
def nuevaTareaImpresion():
    #Probabilidad 1/180 de que haya una nueva tarea.
    numero = random.randrange(1, 181)
    if numero == 180:
        return True
    else:
        return False


#Programa principal.
for tasaImpresion in range(1, 11):
    print("\n\t\tTasa de impresión:",tasaImpresion)
    for i in range(10):
        simulacion(3600, tasaImpresion) #(tiempo en segundos, páginas por minuto)

#Conclusión.
print("\nComo se puede comprobar, a partir de una tasa de impresión mayor o igual a 5 páginas por segundo\nla impresora sería capaz de manejar la carga de tareas en la mayoría de casos (en las situaciones actuales).")

#FIN.
input("\nPulse ENTER para finalizar.")