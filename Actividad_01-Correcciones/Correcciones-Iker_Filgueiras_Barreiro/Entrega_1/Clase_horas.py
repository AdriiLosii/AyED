class Hora:

    def __init__(self,hora,mins,seg):

        if type(hora) != int or hora <1 or hora >24:#Comprobamos que las horas sean un numero entero entre 0 y 24.

            raise Exception("La hora introducida tiene que ser un entero entre 1 y 24.")

        if type(mins) != int or mins <0 or mins >60:#Comprobamos que los minutos sean un numero entero entre 0 y 60.

            raise Exception("Los miutos introducidos tienen que ser un entero entre 1 y 12.")

        if type(seg) != int  or seg <0 or seg >60:#Comprobamos que los segundos sean un numero entero entre 0 y 60.

            raise Exception("Los segundos introducidos tienen que ser un entero.")



        self.hora=hora

        self.mins=mins

        self.seg=seg


    def __str__(self): #Definimos el formato de la fecha.

        return '{0}:{1}:{2}'.format(self.hora,self.mins,self.seg)


    
    
    def iguales(self,hora1):#Comprobamos si tanto la hora como los minutos como los segundos  son iguales.

        return self.hora == hora1.hora and self.mins == hora1.mins and self.seg == hora1.seg



    def __ne__(self,hora1):#Comprobamos si la hora o los minutos o los segundos son distintos distinto.

        return self.hora != hora1.hora and self.mins != hora1.mins and self.seg != hora1.seg



    def __it__(self,hora1):

        if self.hora<hora1.hora:#Comprobamos si la hora de la primera es menor que la de la segunda.

            return True

        elif self.hora>hora1.hora:#Comprobamos si la hora de la primera es mayor que la de la segunda.

            return False

        if self.mins<hora1.mins:#Comprobamos si los minutos de la primera son menor que los de la segunda.

            return True

        elif self.mins>hora1.mins:#Comprobamos si los minutos de la primera son mayor que los de la segunda.

            return False

        return self.seg<hora1.seg #Comprobamos si los segundos de la primera son menor que los de la segunda.



    def __gt__(self,hora1):

        if self.hora>hora1.hora:#Comprobamos si la hora de la primera es mayor que la de la segunda.

            return True

        elif self.hora<hora1.hora:#Comprobamos si la hora de la primera es menor que la de la segunda.

            return False

        if self.mins>hora1.mins:#Comprobamos si los minutos de la primera son mayor que los de la segunda.

            return True

        elif self.mins<hora1.mins:#Comprobamos si los minutos de la primera son menor que los de la segunda.

            return False

        return self.seg>hora1.seg#Comprobamos si los segundos de la primera son mayor que los de la segunda

    

    def __le__(self,hora1):

        if self.hora < hora1.hora:#Comprobamos si la hora de la primera es menor que la de la segunda.

            return True

        elif self.hora == hora1.hora:#Comprobamos si la hora de la primera es igual que la de la segunda.

            if self.mins <= hora1.mins:#Comprobamos si los minutos de la primera son menor o igual que los de la segunda.

                return True

            elif self.seg <= hora1.seg:#Comprobamos si los segundos de la primera son menor o igual que los de la segunda

                return True

        return False



    def __ge__(self,hora1):

        if self.hora > hora1.hora:#Comprobamos si la hora de la primera es mayor que la de la segunda.

            return True

        elif self.hora == hora1.hora:#Comprobamos si la hora de la primera es igual que la de la segunda.

            if self.mins >= hora1.mins:#Comprobamos si los minutos de la primera son mayor o igual que el de la segunda.

                return True

            elif self.seg >= hora1.seg:#Comprobamos si los segundos de la primera son mayor o igual que los de la segunda.

                return True

        return False