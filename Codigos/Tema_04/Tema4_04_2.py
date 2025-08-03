#Tema4_04
def busquedaBinaria(unaLista,primero,ultimo,item):
    if primero == ultimo:
        return False
    else:
        puntoMedio = (primero+ultimo)//2
        if unaLista[puntoMedio]==item:
          return True
        else:
          if item<unaLista[puntoMedio]:
            return busquedaBinaria (unaLista,primero,puntoMedio,item)
          else:
            return busquedaBinaria (unaLista,puntoMedio+1,ultimo,item)

listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(busquedaBinaria(listaPrueba,0,len(listaPrueba)-1,3))
print(busquedaBinaria(listaPrueba,0,len(listaPrueba)-1,13))
