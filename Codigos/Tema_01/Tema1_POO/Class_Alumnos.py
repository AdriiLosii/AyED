class Alumno:
    """Representa alumnos en un colegio, con dni, nombre y edad."""
    def __init__(self,dni,nombre,edad):
        self.dni=dni
        self.nombre=nombre
        self.edad=edad
    def __str__(self):
        return str.format("{0}: {1} ({2})",\
            self.dni,self.nombre,self.edad)

