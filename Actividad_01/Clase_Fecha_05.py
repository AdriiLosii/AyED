"""
Programa: Clase_Fecha_05.py
Propósito: Reescribir la clase común Clase Fecha, de manera que sea robusta y completarla con métodos
necesarios
Fecha:19/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


class Fecha:
    def __init__(self,fecha):
        if (len(fecha) != 3): #Comprobamos que se introdujera el dia, el mes y el año
            print("Error, ha ocurrido algo inesperado.")
            input("Pulse ENTER para finalizar.")
            quit() #Salimos del programa
        else:

            for i in range(3): #Comprobamos que los datos introducidos sean de tipo int
                try:
                    fecha[i] = int(fecha[i])
                except ValueError:
                    print("Error, ha ocurrido algo inesperado.")
                    input("Pulse ENTER para finalizar.")
                    quit() #Salimos del programa

            self.dia=int(fecha[0])
            self.mes=int(fecha[1])
            self.año=int(fecha[2])

    def __str__(self):
        return '{0}/{1}/{2}'.format(self.dia,self.mes,self.año)

    def comprueba_fecha(self):  #metodo para validar la fecha

        if (self.dia < 0 or self.mes < 0 or self.año < 0):  #comprobamos que es positivo
            return False

        else:
            #Comprobamos si el mes es adecuado y si el dia coincide con el mes
            if self.mes in [1,3,5,7,8,10,12]:   #Meses de 31 días.
                if 1<=self.dia<=31:
                    return True
                else:
                    return False

            elif self.mes in [4,6,9,11]:    #Meses de 30 días
                if 1<=self.dia<=30 :
                    return True
                else:
                    return False

            elif self.mes==2:   #Febrero
                if self.año%4==0 and (self.año%100!=0 or self.año%400==0):  #Si el año es bisiesto
                    if 1<=self.dia<=29 :
                        return True
                    else:
                        return False
                else:
                    if 1<=self.dia<=28 :
                        return True
                    else:
                        return False

            else:
                return False

    def bisiesto(self):
        return self.año%4==0 and (self.año%100!=0 or self.año%400==0)

    def es_menor(self,fecha):
        
        if self.año < fecha.año:
            return True
        else:
            if self.mes < fecha.mes:
                return True
            else:
                return self.dia < fecha.dia
    
    def es_mayor(self, fecha):

        if self.año > fecha.año:
            return True
        else:
            if self.mes > fecha.mes:
                return True
            else:
                return self.dia > fecha.dia
    
    def es_distinto(self, fecha):

        return (self.año != fecha.año or self.mes != fecha.mes or self.dia != fecha.dia)

    def es_igual(self, fecha):

        return (self.año == fecha.año and self.mes == fecha.mes and self.dia == fecha.dia)