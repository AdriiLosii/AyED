class Fecha:

    def __init__(self,dia,mes,año):

        if type(dia) != int or dia <1 or dia >31: #Comprobamos que los dias sean un numero entero entre 1 y 31.

            raise Exception("El dia introducido tiene que ser un entero entre 1 y 31.")

        if type(mes) != int or mes <1 or mes >12: #Comprobamos que los meses sean un numero entero entre 1 y 12.

            raise Exception("El dia introducido tiene que ser un entero entre 1 y 12.")

        if type(año) != int or año<0: #Comprobamos que los años seas un numero entero entre mayor que cero.

            raise Exception("El dia introducido tiene que ser un entero.")

        if type(mes) == 4 or mes == 6 or mes == 9 or  mes == 11: #Comprobamos que en los meses de 30 dias no sean superiores a estos.

            if type(dia)<1 or dia>30:
                raise Exception("El mes {0} no puede tener 30 dias".format(mes))
        
        if type(mes)==2: #Comprobamos que en febrero los dias no superan los 28
            
            if type(dia)<1 or dia>28:
                raise Exception("El mes {0} no puede tener 28 dias".format(mes))
            elif type(año)%4==0 and (año%100!=0 or año%400==0): #menos cuando es bisiesto que no puede superar los 29.
                if type(dia)<1 or dia>29:
                    raise Exception("El mes {0} no puede tener 29 dias".format(mes))




        self.dia=dia

        self.mes=mes

        self.año=año



    def __str__(self): #Definimos el formato de la fecha.

        return '{0}/{1}/{2}'.format(self.dia,self.mes,self.año)




    def bisiesto(self): #Comprobamos si un año es bisitiesto

        return self.año%4==0 and (self.año%100!=0 or self.año%400==0)

    

    def iguales(self,f): #Comprobamos si tanto el año como el mes como el dia son iguales.

        return self.año == f.año and self.mes == f.mes and self.dia == f.dia



    def __ne__(self,f): #Comprobamos si el año o el mes o el dia es distinto.

        return self.año != f.año or self.mes != f.mes or self.dia != f.dia



    def __it__(self,fecha1):

        if self.año<fecha1.año: #Comprobamos si el año de la primera es menor que el de la segunda.

            return True

        elif self.año>fecha1.año:#Comprobamos si el año de la primera es mayor que el de la segunda.

            return False

        if self.mes<fecha1.mes:#Comprobamos si el mes de la primera es menor que el de la segunda.

            return True

        elif self.mes>fecha1.mes:#Comprobamos si el mes de la primera es mayor que el de la segunda.

            return False

        return self.dia<fecha1.dia #Comprobamos si el dia de la primera es menor que el de la segunda.



    def __gt__(self,fecha1):

        if self.año>fecha1.año:#Comprobamos si el año de la primera es mayor que el de la segunda.

            return True

        elif self.año<fecha1.año:#Comprobamos si el año de la primera es menor que el de la segunda.

            return False

        if self.mes>fecha1.mes:#Comprobamos si el mes de la primera es mayor que el de la segunda.

            return True

        elif self.mes<fecha1.mes:#Comprobamos si el mes de la primera es menor que el de la segunda.

            return False

        return self.dia>fecha1.dia#Comprobamos si el dia de la primera es mayor que el de la segunda.

    

    def __le__(self,f):

        if self.año < f.año:#Comprobamos si el año de la primera es menor que el de la segunda.

            return True

        elif self.año == f.año: #Comprobamos si los años son iguales.

            if self.mes <= f.mes:#Comprobamos si el mes de la primera es menor o igual que el de la segunda.

                return True

            elif self.dia <= f.dia:#Comprobamos si el mes de la primera es menor o igual que el de la segunda.

                return True

        return False



    def __ge__(self,f):

        if self.año > f.año:#Comprobamos si el año de la primera es mayor que el de la segunda.

            return True

        elif self.año == f.año:#Comprobamos si los años son iguales.

            if self.mes >= f.mes:#Comprobamos si el mes de la primera es mayor o igual que el de la segunda.

                return True

            elif self.dia >= f.dia:#Comprobamos si el dia de la primera es mayot o igual que el de la segunda.

                return True

        return False

    

