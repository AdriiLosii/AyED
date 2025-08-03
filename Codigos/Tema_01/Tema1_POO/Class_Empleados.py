from Class_Personas import Persona


class Empleado(Persona):
    def __init__(self, nombre, edad, empresa, email):
        super().__init__(nombre, edad)
        self.empresa = empresa
        self.email = email

    def __str__(self):
        cadena = super().__str__()
        cadena += " en " + self.empresa
        cadena += ": " + self.email
        return cadena
