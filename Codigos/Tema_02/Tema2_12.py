# Tema2_12
import random
from Class_Estructuras_lineales import Cola
from Class_Impresion import Impresora, Tarea


def simulacion(numeroSegundos, paginasPorMinuto):

    impresoraLaboratorio = Impresora(paginasPorMinuto)
    colaImpresion = Cola()
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
    print("Tiempo de espera promedio %6.2f segundos  %6.2f minutos  %3d tareas restantes." % (
        esperaPromedio, esperaPromedio/60, colaImpresion.tamano()))


def nuevaTareaImpresion():
    numero = random.randrange(1, 181)
    if numero == 180:
        return True
    else:
        return False


for tasaImpresion in range(1, 11):
    print("\n\t\tTasa de impresión:",tasaImpresion)
    for i in range(10):
        simulacion(3600, tasaImpresion)