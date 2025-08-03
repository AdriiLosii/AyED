class Estudiante:
    def __init__(self, nombre, grupo, nota, practica):
        self.nombre=nombre
        self.grupo=grupo
        self.nota=nota
        self.practica=practica

    def __str__(self): #Para poder imprimir en pantalla el estudiante
        cadena='Nombre: {0}\n'.format(self.nombre)
        cadena=cadena + 'Grupo: {0}\n'.format(self.grupo)
        cadena=cadena + 'Nota Examen: {0:3.1f}\n'.format(self.nota)
        if self.practica:
            cadena=cadena+'Practica Entregada'
        else:
            cadena=cadena+'Practica NO Entregada'
        return cadena

    def calificacion(self):
        if not self.practica:
            return 'Suspenso'
        else:
            if self.nota<5:
                return 'Suspenso'
            elif self.nota<7:
                return 'Aprobado'
            elif self.nota<8.5:
                return 'Notable'
            elif self.nota<10:
                return 'Sobresaliente'
            else:
                return 'Matricula de Honor'
#Fin de la clase Estudiante
