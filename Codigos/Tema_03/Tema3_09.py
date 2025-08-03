#Tema3_09
from Class_Laberintos import Laberinto

PARTE_DEL_CAMINO = 'O'
INTENTADO = '.'
OBSTACULO = '+'
CALLEJON_SIN_SALIDA = '-'

def buscarDesde(laberinto, filaInicio, columnaInicio):
    laberinto.actualizarPosicion(filaInicio, columnaInicio)
   #  Verificar casos base:
   #  1. Hemos tropezado con un obstáculo, devolver False
    if laberinto[filaInicio][columnaInicio] == OBSTACULO :
        return False
    #  2. Hemos encontrado un cuadrado que ya ha sido explorado
    if laberinto[filaInicio][columnaInicio] == INTENTADO:
        return False
    # 3. Éxito, un borde exterior no ocupado por un obstáculo
    if laberinto.esSalida(filaInicio,columnaInicio):
        laberinto.actualizarPosicion(filaInicio, columnaInicio, PARTE_DEL_CAMINO)
        return True
    laberinto.actualizarPosicion(filaInicio, columnaInicio, INTENTADO)

    # De lo contrario, usamos cortocircuitos lógicos para probar 
    # cada dirección a su vez (si fuera necesario)
    encontrado = buscarDesde(laberinto, filaInicio-1, columnaInicio) or buscarDesde(laberinto, filaInicio+1, columnaInicio) or buscarDesde(laberinto, filaInicio, columnaInicio-1) or buscarDesde(laberinto, filaInicio, columnaInicio+1)
    if encontrado:
        laberinto.actualizarPosicion(filaInicio, columnaInicio,PARTE_DEL_CAMINO)
    else:
        laberinto.actualizarPosicion(filaInicio, columnaInicio,CALLEJON_SIN_SALIDA)
    return encontrado

miLaberinto = Laberinto('laberinto2.txt')
miLaberinto.dibujarLaberinto()
miLaberinto.actualizarPosicion(miLaberinto.filaInicio,miLaberinto.columnaInicio)

buscarDesde(miLaberinto, miLaberinto.filaInicio, miLaberinto.columnaInicio)
