#Tema3_07
def moverDisco(desde,hacia):
    print("mover disco de",desde,"a",hacia)

def moverTorre(altura,origen,destino,intermedio):
    if altura >= 1:
        moverTorre(altura-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        moverTorre(altura-1,intermedio,destino,origen)

moverTorre(4,"A","B","C")
