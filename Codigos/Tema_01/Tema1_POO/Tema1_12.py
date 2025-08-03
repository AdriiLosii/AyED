from Class_Alumnos import Alumno
from Class_Asignaturas import Asignatura


if __name__ == "__main__":
    asignatura1 = Asignatura("Introducción a Python")
    asignatura2 = Asignatura("Matemáticas")
    alumno1 = Alumno('11222333A', "Jose", 25)
    alumno2 = Alumno('99999999B', "Jaimito", 55)
    asignatura1.inserta(alumno1)
    asignatura1.inserta(alumno2)
    asignatura2.inserta(alumno2)
    print(str(asignatura1))
    print(str(asignatura2))
