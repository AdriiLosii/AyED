class Hora:

    def __init__(self, hora, minuto, segundo):

        if hora > 23 or hora <0 or type(hora) != int:
            raise Exception("Error: Hora no valida")
        else:
            self.hora = hora

        if minuto > 59 or minuto <0 or type(minuto) != int:
            raise Exception("Error: Minuto no valido")
        else:
            self.minuto = minuto

        if segundo > 59 or segundo <0 or type(segundo) != int:
            raise Exception("Error: Segundo no valida")
        else:
            self.segundo = segundo


    def __str__(self):

        return '{0}:{1}:{2}'.format(self.hora,self.minuto,self.segundo)

    def partedeldia(self):

        if self.hora >= 0 and self.hora < 6:
            return "Madrugada"

        elif self.hora >= 6 and self.hora < 12:
            return "Mañana"

        elif self.hora >= 12 and self.hora < 21:
            return "Tarde"

        else:
            return "Noche"

    def es_menor(self,comparacion):
        if self.hora < comparacion.hora:
            return True
        elif self.hora > comparacion.hora:
            return False
        if self.minuto < comparacion.minuto:
            return True
        elif self.minuto > comparacion.minuto:
            return False
        if self.segundo == comparacion.segundo:
            return "Igual"
        return self.segundo < comparacion.segundo