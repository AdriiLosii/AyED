def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

unaLista = [54,26,93,17,77,31,44,55,20]
ordenamientoBurbuja(unaLista)


def ordenamientoPorSeleccion(unaLista):
   for llenarRanura in range(len(unaLista)-1,0,-1):
       posicionDelMayor=0
       for ubicacion in range(1,llenarRanura+1):
           if unaLista[ubicacion]>unaLista[posicionDelMayor]:
               posicionDelMayor = ubicacion

       temp = unaLista[llenarRanura]
       unaLista[llenarRanura] = unaLista[posicionDelMayor]
       unaLista[posicionDelMayor] = temp


ordenamientoPorSeleccion(unaLista)


def ordenamientoPorInsercion(unaLista):
   for indice in range(1,len(unaLista)):

     valorActual = unaLista[indice]
     posicion = indice

     while posicion>0 and unaLista[posicion-1]>valorActual:
         unaLista[posicion]=unaLista[posicion-1]
         posicion = posicion-1

     unaLista[posicion]=valorActual


ordenamientoPorInsercion(unaLista)



def ordenamientoDeShell(unaLista):
    contadorSublistas = len(unaLista)//2
    while contadorSublistas > 0:

      for posicionInicio in range(contadorSublistas):
        brechaOrdenamientoPorInsercion(unaLista,posicionInicio,contadorSublistas)

      print("Después de los incrementos de tamaño",contadorSublistas,
                                   "La lista es",unaLista)

      contadorSublistas = contadorSublistas // 2

def brechaOrdenamientoPorInsercion(unaLista,inicio,brecha):
    for i in range(inicio+brecha,len(unaLista),brecha):

        valorActual = unaLista[i]
        posicion = i

        while posicion>=brecha and unaLista[posicion-brecha]>valorActual:
            unaLista[posicion]=unaLista[posicion-brecha]
            posicion = posicion-brecha

        unaLista[posicion]=valorActual


ordenamientoDeShell(unaLista)





def ordenamientoPorMezcla(unaLista):
    print("Dividir ",unaLista)
    if len(unaLista)>1:
        mitad = len(unaLista)//2
        mitadIzquierda = unaLista[:mitad]
        mitadDerecha = unaLista[mitad:]

        ordenamientoPorMezcla(mitadIzquierda)
        ordenamientoPorMezcla(mitadDerecha)

        i=0
        j=0
        k=0
        while i < len(mitadIzquierda) and j < len(mitadDerecha):
            if mitadIzquierda[i] < mitadDerecha[j]:
                unaLista[k]=mitadIzquierda[i]
                i=i+1
            else:
                unaLista[k]=mitadDerecha[j]
                j=j+1
            k=k+1

        while i < len(mitadIzquierda):
            unaLista[k]=mitadIzquierda[i]
            i=i+1
            k=k+1

        while j < len(mitadDerecha):
            unaLista[k]=mitadDerecha[j]
            j=j+1
            k=k+1
    print("Mezclar ",unaLista)

ordenamientoPorMezcla(unaLista)




def ordenamientoRapido(unaLista):
   ordenamientoRapidoAuxiliar(unaLista,0,len(unaLista)-1)

def ordenamientoRapidoAuxiliar(unaLista,primero,ultimo):
   if primero<ultimo:

       puntoDivision = particion(unaLista,primero,ultimo)

       ordenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1)
       ordenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo)


def particion(unaLista,primero,ultimo):
   valorPivote = unaLista[primero]

   marcaIzq = primero+1
   marcaDer = ultimo

   hecho = False
   while not hecho:

       while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
           marcaIzq = marcaIzq + 1

       while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
           marcaDer = marcaDer -1

       if marcaDer < marcaIzq:
           hecho = True
       else:
           temp = unaLista[marcaIzq]
           unaLista[marcaIzq] = unaLista[marcaDer]
           unaLista[marcaDer] = temp

   temp = unaLista[primero]
   unaLista[primero] = unaLista[marcaDer]
   unaLista[marcaDer] = temp


   return marcaDer


ordenamientoRapido(unaLista)

