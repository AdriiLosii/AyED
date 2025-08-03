# Tema4_13
def ordenamientoPorSeleccion(unaLista):
    for llenarSlot in range(len(unaLista)-1, 0, -1):
        posicionDelMayor = 0
        for ubicacion in range(1, llenarSlot+1):
            if unaLista[ubicacion] > unaLista[posicionDelMayor]:
                posicionDelMayor = ubicacion

        unaLista[llenarSlot],unaLista[posicionDelMayor] = unaLista[posicionDelMayor],unaLista[llenarSlot]


unaLista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
ordenamientoPorSeleccion(unaLista)
print(unaLista)
