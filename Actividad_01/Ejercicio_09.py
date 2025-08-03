"""
Programa: Ejercicio_09.py
Propósito:
    En un juego de dados, todos los participantes tienen el mismo número de dados (con n caras, de la 1 
    a la n). En cada turno, cada jugador tira todos sus dados, sumando cada dado para obtener una 
    puntuación. Gana el jugador con mejor puntuación tras x turnos.
Fecha:21/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


from Clase_Dados_09 import *

#Petición de datos
num_jugadores = input("Introduzca el número de jugadores: ")
turnos = input("Introduce el número de turnos: ")
num_caras = input("Introduce el número de caras que tienen los dados: ")

config_juego = Dados(num_jugadores, turnos, num_caras)
jugadores = config_juego.añadir_jugador()
puntuaciones = config_juego.puntos()
config_juego.asociar_puntuaciones(jugadores, puntuaciones)
config_juego.ganador(jugadores, puntuaciones)

input("\nPulse ENTER para finalizar.")