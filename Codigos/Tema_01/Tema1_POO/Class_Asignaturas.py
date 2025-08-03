class Asignatura:
    """ Representa asignaturas, guarda su nombre y lista de alumnos"""

    def __init__(self, nombre):
        """ Crea una asignatura tomando su nombre
        :param nombre: El nombre de la asignatura

        """
        self.nombre = nombre
        self.alumnos = []

    def inserta(self, alumno):
        """ Inserta un nuevo alumno
            :param alumno: El alumno a insertar.

        """
        self.alumnos += [alumno]

    def get_num_alumnos(self):
        """ Devuelve el número de alumnos en la asignatura.
            :return: El num. de alumnos.

        """
        return len(self.alumnos)

    def get_alumno(self, i):
        """ Devuelve un alumno de la asignatura, según su posición en el listado.
            :param i: El número de posición del alumno.
            :return: Un objeto de la clase Alumno.
        """

        return self.alumnos[i]

    def __str__(self):
        cadena = self.nombre + "\n\n"

        for alumno in self.alumnos:
            cadena += str(alumno) + '\n'
        return cadena
