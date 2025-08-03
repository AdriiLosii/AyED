class Fraccion:
     def __init__(self,arriba,abajo):
            self.num = arriba
            self.den = abajo

     def __str__(self):
          return str(self.num)+"/" +str(self.den)

     @staticmethod
     def mcd (m,n):
          while n != 0:
               m,n =n,m%n 
          return m

     def __add__(self,otraFraccion):
          nuevoNum = self.num*otraFraccion.den + self.den*otraFraccion.num
          nuevoDen = self.den * otraFraccion.den
          comun = self.mcd(nuevoNum,nuevoDen)
          return Fraccion(nuevoNum//comun,nuevoDen//comun)
 
     def __sub__(self,otraFraccion):
          nuevoNum = self.num*otraFraccion.den - self.den*otraFraccion.num
          nuevoDen = self.den * otraFraccion.den
          comun = self.mcd(nuevoNum,nuevoDen)
          return Fraccion(nuevoNum//comun,nuevoDen//comun)

     def __mul__(self,otraFraccion):
          nuevoNum = self.num*otraFraccion.num
          nuevoDen = self.den * otraFraccion.den
          comun = self.mcd(nuevoNum,nuevoDen)
          return Fraccion(nuevoNum//comun,nuevoDen//comun)

     def __truediv__(self,otraFraccion):
          nuevoNum = self.num*otraFraccion.den
          nuevoDen = self.den * otraFraccion.num
          comun = self.mcd(nuevoNum,nuevoDen)
          return Fraccion(nuevoNum//comun,nuevoDen//comun)

     def __eq__(self, otro):
          primerNum = self.num * otro.den
          segundoNum = otro.num * self.den
          return primerNum == segundoNum

