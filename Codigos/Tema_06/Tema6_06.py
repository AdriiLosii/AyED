#Tema6_05
from Class_Grafos import Grafo

def grafoDelCaballo(tamanoTablero):
    grafoCbllo = Grafo()
    for fil in range(tamanoTablero):
       for col in range(tamanoTablero):
           idNodo = pos_A_Id_Nodo(fil,col,tamanoTablero)
           posicionesNuevas = generarMovLegales(fil,col,tamanoTablero)
           for e in posicionesNuevas:
               nid = pos_A_Id_Nodo(e[0],e[1],tamanoTablero)
               grafoCbllo.agregarArista(idNodo,nid)
    return grafoCbllo

def pos_A_Id_Nodo(fila, columna, tamano_del_tablero):
    return (fila * tamano_del_tablero) + columna


def generarMovLegales(x,y,tamanoTablero):
    nuevosMovimientos = []
    desplazamientosEnL = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in desplazamientosEnL:
        nuevoX = x + i[0]
        nuevoY = y + i[1]
        if coordLegal(nuevoX,tamanoTablero) and coordLegal(nuevoY,tamanoTablero):
            nuevosMovimientos.append((nuevoX,nuevoY))
    return nuevosMovimientos

def coordLegal(x,tamanoTablero):
    return x >= 0 and x < tamanoTablero

def ordenPorDisp(n):
    listaRes = []
    for v in n.obtenerConexiones():
        if v.obtenerColor() == 'blanco':
            c = 0
            for w in v.obtenerConexiones():
                if w.obtenerColor() == 'blanco':
                    c = c + 1
            listaRes.append((c,v))
    listaRes.sort(key=lambda x: x[0])
    return [y[1] for y in listaRes]


def MueveCaballo(n,ruta,u,limite):
        u.asignarColor('gris')
        ruta.append(u)
        if n < limite:
            listaVecinos = list(ordenPorDisp(n))
            i = 0
            hecho = False
            while i < len(listaVecinos) and not hecho:
                if listaVecinos[i].obtenerColor() == 'blanco':
                    hecho = MueveCaballo(n+1,ruta,listaVecinos[i],limite)
                i = i + 1
            if not hecho:  # prepararse para retroceder
                ruta.pop()
                u.asignarColor('blanco')
        else:
            hecho = True
        return hecho

