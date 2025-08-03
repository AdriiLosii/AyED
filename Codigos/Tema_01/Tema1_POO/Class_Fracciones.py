class Fraccion:
     def __init__(self,arriba,abajo):
          self.num = arriba
          self.den = abajo

     def __str__(self):
          return str(self.num)+"/" +str(self.den)

     def __add__(self,otraFraccion):
          nuevoNum = self.num*otraFraccion.den + self.den*otraFraccion.num
          nuevoDen = self.den * otraFraccion.den
          comun = mcd(nuevoNum,nuevoDen)
          return Fraccion(nuevoNum//comun,nuevoDen//comun)

     def __sub__(self,otraFraccion):
          nuevoNum = self.num*otraFraccion.den - self.den*otraFraccion.num
          nuevoDen = self.den * otraFraccion.den
          comun = mcd(nuevoNum,nuevoDen)
          return Fraccion(nuevoNum//comun,nuevoDen//comun)

     def __mul__(self,otraFraccion):
          nuevoNum = self.num*otraFraccion.num
          nuevoDen = self.den * otraFraccion.den
          comun = mcd(nuevoNum,nuevoDen)
          return Fraccion(nuevoNum//comun,nuevoDen//comun)

     def __truediv__(self,otraFraccion):
          nuevoNum = self.num*otraFraccion.den
          nuevoDen = self.den * otraFraccion.num
          comun = mcd(nuevoNum,nuevoDen)
          return Fraccion(nuevoNum//comun,nuevoDen//comun)

     def __eq__(self, otro):
          primerNum = self.num * otro.den
          segundoNum = otro.num * self.den

          return primerNum == segundoNum


def mcd(m,n): #Esto no es un método, es una funcion
     while m%n != 0:
          mViejo = m
          nViejo = n
          m = nViejo
          n = mViejo%nViejo
     return n

