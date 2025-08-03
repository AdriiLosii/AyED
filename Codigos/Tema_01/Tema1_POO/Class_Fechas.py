class Fecha:
    def __init__(self,dia,mes,año):
        self.dia=dia
        self.mes=mes
        self.año=año

    def __str__(self):
        return '{0}/{1}/{2}'.format(self.dia,self.mes,self.año)

    def bisiesto(self):
        return self.año%4==0 and (self.año%100!=0 or self.año%400==0)

    def es_menor(self,fecha1):
        if self.año<fecha1.año:
            return True
        elif self.año>fecha1.año:
            return False
        if self.mes<fecha1.mes:
            return True
        elif self.mes>fecha1.mes:
            return False
        return self.dia<fecha1.dia
    
