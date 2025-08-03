class Jarra:

    def __init__(self,capacidad):

        self.jarra=0
        self.capacidad=capacidad

    def __str__(self):
        return str(self.jarra) 

    def llenar(self):

        self.jarra = self.capacidad

    def vaciar(self):

        self.jarra = 0


    def trasladar(self,OtraJarra):
        if self.jarra+OtraJarra.jarra>OtraJarra.capacidad:
            self.jarra-=OtraJarra.capacidad-OtraJarra.jarra
            OtraJarra.llenar()
        else:
            OtraJarra.jarra+=self.jarra
            self.jarra=0
            