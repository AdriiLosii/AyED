from Class_Estudiantes import Estudiante


def lee_estudiante():  # Esto no es un método, sino una función
    nombre = input('Nombre: ')
    grupo = input('Grupo(A, B o C): ')
    nota = float(input('Nota de Examen: '))
    entregada = input('Práctica entregada (S/N): ')
    practica = entregada == 'S' or entregada == 's'
    return Estudiante(nombre, grupo, nota, practica)


def lee_y_añade_estudiante(lista):
    estudiante = lee_estudiante()
    lista.append(estudiante)


def acta(lista):
    for estudiante in lista:
        print(estudiante.nombre, estudiante.calificacion())


def nota_media(lista):
    suma = 0
    cantidad = 0
    for estudiante in lista:
        if estudiante.practica:
            suma += estudiante.nota
            cantidad += 1
    if cantidad != 0:
        return suma/cantidad
    else:
        return 0.0


def porcentaje_de_practicas_entregadas(lista):
    if len(lista) != 0:
        cantidad = 0
        for estudiante in lista:
            if estudiante.practica:
                cantidad += 1
        return cantidad/len(lista)*100
    else:
        return 0.0


def mejores_estudiantes(lista):
    nota_mas_alta = 0
    mejores = []
    for estudiante in lista:
        if estudiante.practica:
            if estudiante.nota > nota_mas_alta:
                mejores = [estudiante]
                nota_mas_alta = estudiante.nota
            elif estudiante.nota == nota_mas_alta:
                mejores.append(estudiante)
    return mejores


pepe = Estudiante('Pepe Garcia', 'A', 7.7, True)
print(pepe.calificacion())
