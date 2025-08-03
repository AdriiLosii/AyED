# Tema2_10
from Class_Estructuras_lineales import Cola
from random import randint


def patata_Caliente(listaNombres, N):
    colaSimulacion = Cola()
    for nombre in listaNombres:
        colaSimulacion.agregar(nombre)

    while colaSimulacion.tamano() > 1:
        for i in range(N):
            colaSimulacion.agregar(colaSimulacion.avanzar())

        colaSimulacion.avanzar()

    return colaSimulacion.avanzar()


print(patata_Caliente(["Jose", "David", "Susana", "Juan", "Antonio", "Ana"], randint(1, 10)))
