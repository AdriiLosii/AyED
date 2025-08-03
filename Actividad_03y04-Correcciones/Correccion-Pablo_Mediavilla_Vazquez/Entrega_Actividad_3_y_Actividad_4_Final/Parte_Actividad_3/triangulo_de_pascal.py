tamaño = int(input("Introduce el tamaño del triángulo: "))
tri =[]
 
def pascal(n):
   fila = [1]
   k = [0]
   for x in range(max(n,0)):
      tri.append(fila)
      fila=[l+r for l,r in zip(fila+k,k+fila)]
   return n>=1
 
def imprime_triangulo_pascal(triangulo):
    longitud_elemento = triangulo[-1][len(triangulo[-1]) // 2]
    elemento_anchura = len(str(longitud_elemento))
    def format_fila(fila):
        return ' '.join([str(elemento).center(elemento_anchura) for elemento in fila])
    triangulo_anchura = len(format_fila(triangulo[-1]))
    for fila in triangulo:
        print(format_fila(fila).center(triangulo_anchura))
 
pascal(tamaño)
 
imprime_triangulo_pascal(tri)