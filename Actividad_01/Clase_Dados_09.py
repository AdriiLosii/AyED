"""
Programa: Clase_Dados_09.py
Propósito:
    En un juego de dados, todos los participantes tienen el mismo número de dados (con n caras, de la 1 
    a la n). En cada turno, cada jugador tira todos sus dados, sumando cada dado para obtener una 
    puntuación. Gana el jugador con mejor puntuación tras x turnos.
Fecha:21/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


import random

class Dados:
    def __init__(self, num_jugadores, turnos, num_caras):
        try:
            #Validamos los datos
            if (int(num_jugadores) <= 0 or int(turnos) <= 0 or int(num_caras) <= 1):
                print("Error, ha ocurrido algo inesperado.")
                input("Pulse ENTER para finalizar.")
                quit() #Salimos del programa

            self.num_jugadores = int(num_jugadores)
            self.turnos = int(turnos)
            self.num_caras = int(num_caras)

        except ValueError:
            print("Error, ha ocurrido algo inesperado.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa
    
    #Creamos la función para añadir los jugadores
    def añadir_jugador(self):
        try:
            lista_jugadores = []
            for i in range(self.num_jugadores):
                jugador = str(input("Introduce el nombre del jugador {0} ".format(i+1)))
                lista_jugadores.append(jugador)
                print ("Jugador {0} añadido con éxito.\n".format(jugador))
            
            return lista_jugadores

        except ValueError():
            print("Error, ha ocurrido algo inesperado.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa

    def puntos(self):
        lista_puntos = []
        suma = 0
        for i in range(self.num_jugadores):
            for j in range(self.turnos):
                suma += random.randint(1, self.num_caras)
            
            lista_puntos.append(suma)
            suma = 0

        return lista_puntos

    def asociar_puntuaciones(self, jugadores, puntuaciones):
        print("Puntuaciones:")
        for i, j in zip(jugadores, puntuaciones):
            print(i,"->",j)

    def ganador(self, jugadores, puntuaciones):
        puntos = max(puntuaciones)
        print("El ganador es: {0} con {1} puntos!".format(jugadores[puntuaciones.index(puntos)], puntos))