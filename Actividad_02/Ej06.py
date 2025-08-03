"""
Programa: Ej06.py
Propósito:
    Implementar el TAD Impresión usando Colas de Prioridad.
Fecha: 19/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importamos la clase.
from Class_Impresion_06 import *


#Creamos la función.
def simulacion(numeroSegundos, paginasPorMinuto):

    impresoraLaboratorio = Impresora(paginasPorMinuto)
    colaImpresion = ColaPrioridad()
    tiemposEspera = []

    for segundoActual in range(numeroSegundos):

        if nuevaTareaImpresion():
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
    numero = random.randrange(1, 181)
    if numero == 180:
        return True
    else:
        return False


#Programa principal.
for tasaImpresion in range(1, 11):
    print("\n\t\tTasa de impresión:",tasaImpresion)
    for i in range(10):
        simulacion(3600, tasaImpresion)

#FIN.
input("\nPulse ENTER para finalizar.")