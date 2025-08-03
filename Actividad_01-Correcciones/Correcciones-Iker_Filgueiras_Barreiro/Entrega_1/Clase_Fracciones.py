class Fraccion:



    def __init__(self,arriba,abajo):

          if type(arriba) != int or type(abajo) != int: #Comprobamos si el denominador y el numerador son numeros enteros.

               raise Exception("El denominador o el numerador no son numeros enteros")

          else:

               if abajo< 0: #De igual fomra comprobamos si hay algun numero negativo y le hacemos el vaor absoluto.

                    self.num = arriba

                    self.den = abs(abajo)

               else:

                    self.num = arriba

                    self.den = abajo



    def __str__(self): #Definimos el formato de las fracciones.

          return str(self.num)+"/" +str(self.den)





    def __add__(self,otraFraccion): #Creamos la funcion suma.

          nuevoNum = self.num*otraFraccion.den + self.den*otraFraccion.num #El numerador lo calcularemos multiplicando en cruz las dos fracciones y sumando.

          nuevoDen = self.den * otraFraccion.den #El denominador lo calcularemos multiplicando ambos denominadores.

          comun = mcd(nuevoNum,nuevoDen)# Simplificamos la fraccion con el minimo comun multiplo.

          return Fraccion(nuevoNum//comun,nuevoDen//comun) #Por ultimo imprimos en formarto la suma.



    def __sub__(self,otraFraccion):

          nuevoNum = self.num*otraFraccion.den - self.den*otraFraccion.num #El numerador lo calcularemos multiplicando en cruz las dos fracciones y restando.

          nuevoDen = self.den * otraFraccion.den #El denominador lo calcularemos multiplicando ambos denominadores.

          comun = mcd(nuevoNum,nuevoDen)# Simplificamos la fraccion con el minimo comun multiplo.

          return Fraccion(nuevoNum//comun,nuevoDen//comun)#Por ultimo imprimos en formarto la resta.



    def __mul__(self,otraFraccion):

          nuevoNum = self.num*otraFraccion.num #El numerador lo calcularemos mutiplicando ambos numeradores.

          nuevoDen = self.den * otraFraccion.den #El denominador lo calcularemos mutiplicando ambos nominadores.

          comun = mcd(nuevoNum,nuevoDen)# Simplificamos la fraccion con el minimo comun multiplo.

          return Fraccion(nuevoNum//comun,nuevoDen//comun)#Por ultimo imprimos en formarto la multipluicacion.



    def __truediv__(self,otraFraccion):

          nuevoNum = self.num*otraFraccion.den #El numerador lo calcularemos mutiplicando el numerador de la primera por el denominador de la segunda.

          nuevoDen = self.den * otraFraccion.num #El denominador lo calcularemos mutiplicando el denominador de la primera por el numerador de la segunda.

          comun = mcd(nuevoNum,nuevoDen)# Simplificamos la fraccion con el minimo comun multiplo.

          return Fraccion(nuevoNum//comun,nuevoDen//comun)#Por ultimo imprimos en formarto la division.



    def __eq__(self, otro):

          primerNum = self.num * otro.den #Multipicamos en cruz para obtener dos numeros.

          segundoNum = otro.num * self.den



          return primerNum == segundoNum #Comprobamos si los numeros son iguales.

    

    def __ge__(self, otraFraccion):

        dc=self.den*otraFraccion.den #Multiplicamos los dos denominadores.

        return self.num*(dc/self.den) >= otraFraccion.num*(dc/otraFraccion.den) #Multiplicamos el numerador de cada una de las fracciones por el numero anterior entre el denominador de la misma y se comprueba.



    def __gt__(self, otraFraccion):

        dc=self.den*otraFraccion.den #Multiplicamos los dos denominadores.

        return self.num*(dc/self.den) > otraFraccion.num*(dc/otraFraccion.den) #Multiplicamos el numerador de cada una de las fracciones por el numero anterior entre el denominador de la misma y se comprueba.



    def __le__(self, otraFraccion):

        dc=self.den*otraFraccion.den #Multiplicamos los dos denominadores.

        return self.num*(dc/self.den) <= otraFraccion.num*(dc/otraFraccion.den) #Multiplicamos el numerador de cada una de las fracciones por el numero anterior entre el denominador de la misma y se comprueba.



    def __it__(self, otraFraccion):

        dc=self.den*otraFraccion.den #Multiplicamos los dos denominadores.

        return self.num*(dc/self.den) < otraFraccion.num*(dc/otraFraccion.den) #Multiplicamos el numerador de cada una de las fracciones por el numero anterior entre el denominador de la misma y se comprueba.

    

    def __ne__(self, otraFraccion):

        primerNum=self.num*otraFraccion.den #Multipicamos en cruz para obtener dos numeros.

        segundoNum=otraFraccion.num*self.den



        return primerNum != segundoNum #Comprobamos si los numeros son iguales.









def mcd(m,n): 

     while m%n != 0:

          mViejo = m

          nViejo = n

          m = nViejo

          n = mViejo%nViejo

     return n



