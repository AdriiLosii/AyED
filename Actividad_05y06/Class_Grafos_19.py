"""
Programa: Class_Grafos_19.py
Propósito:
    Modifica la función de búsqueda en profundidad para producir un ordenamiento topológico.
Fecha: 13/05/2022
"""


#Con tuplas
import sys 

class ColaPrioridad:
    #Realizamos el init
    def __init__(self,tamanho):
        self.cola=[0]
        self.tamanoActual = 0
        self.distancia=[]
        for i in range(tamanho):
            self.distancia.append([0,sys.maxsize])
        self.veces_hasta_a=[]
        for i in range(tamanho):
            self.veces_hasta_a.append(0)

    #Realizamos la función para agregar valores
    def agregar(self,k):
      self.cola.append(k)
      self.tamanoActual = self.tamanoActual + 1
      self.infiltArriba(self.tamanoActual)

    #Buscamos el primer valor de la cola
    def primero(self):
        if len(self.cola)==0:
            return None
        maximo=self.cola[0][2]
        for elemento in self.cola:
            if elemento[2]>maximo:
                maximo=elemento[2]
                
        for element in self.cola:
            if element[2] == maximo:
                return element

    #Buscamos y borramos el valor máximo de la cola
    def extrae(self):
        if len(self.cola)==0:
            return None
        indice=1
        for i in range(1,len(self.cola)):
            if self.cola[i][2]>self.cola[indice][2]:
                indice=i
        aux=self.cola[indice]
        del self.cola[indice]
        return aux

    #Verificamos el tamaño de la cola
    def tamanho(self):
        return self.tamanoActual

    #Verificamos si está vacía la cola
    def estaVacia(self):
        return len(self.cola)==0

    def infiltArriba(self,i):
        print(self.cola[i])
        while i // 2 > 0:
            if self.cola[i][2] < self.cola[i//2][2]:
                #los intercambio
                self.cola[i//2][2],self.cola[i][2] = self.cola[i][2],self.cola[i//2][2]
            i = i // 2

    def infiltAbajo(self,i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.cola[i][2] > self.cola[hm][2]:
                #los intercambio
                self.cola[i][2],self.cola[hm][2] = self.cola[hm][2],self.cola[i][2]
            i = hm

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanoActual:
          return i * 2
      else:
          if self.cola[i*2] < self.cola[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    #Eliminamos el valor mínimo 
    def eliminarMin(self):
      valorSacado = self.cola[1]
      self.cola[1] = self.cola[self.tamanoActual]
      self.tamanoActual = self.tamanoActual - 1
      self.cola.remove(self.cola[1])
      return valorSacado

    #Añadimos varios valores juntos
    def construirMonticulo(self,unaLista):
        for item in unaLista:
            self.cola.append(item)
            self.tamanoActual += 1

    #Realizamos una función para obtener las conexiones del valor pasado a ¡l resto de grafos
    def obtenerConexiones(self,adonde):
        i=0
        siguientes=[]
        for verticeSiguientes in self.cola:
            if verticeSiguientes!=0:
                i+=1
                if adonde == verticeSiguientes[0]:
                    siguientes.append(verticeSiguientes)
        return siguientes

    #Realizamos la función decrementar clave, donde vamos verificando la mínima distancia a todos los puntos del programa
    def decrementarClave(self,verticeSiguiente,inicio,j,y):        
        if verticeSiguiente[0]!=0:
            if verticeSiguiente[0] == inicio:
                suma_distancia = 0
                suma_distancia += verticeSiguiente[2]
            else:
                suma_distancia = self.distancia[verticeSiguiente[0]-1][1] 
                suma_distancia += verticeSiguiente[2]

            if self.distancia[verticeSiguiente[1]-1][1] > suma_distancia: 
                y += 1               
                self.distancia[verticeSiguiente[1]-1][1] = suma_distancia
                self.distancia[verticeSiguiente[1]-1][0] = verticeSiguiente[1]
                self.veces_hasta_a[verticeSiguiente[1]-1]=j
                
                print('\n***Este es el paso número {} donde la distancia que modificamos es del punto {} al punto {} y queda una distancia de {} hasta el punto A realizando solamente {} recorrido(s). ***'.format(y,verticeSiguiente[0],verticeSiguiente[1],suma_distancia,j))

        self.distancia[0]=[1,0]
        return self.distancia,self.veces_hasta_a,y

    def dibujar(self):
        print(self.cola)