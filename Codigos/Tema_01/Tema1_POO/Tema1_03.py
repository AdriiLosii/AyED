from Class_Agenda import Listin


def menu():
    opcion = 0
    while opcion < 1 or opcion > 4:
        print('\tEscoge una opción:')
        print('\t\t1) Añadir teléfonos.')
        print('\t\t2) Consultar el listín.')
        print('\t\t3) Eliminar persona del listín.')
        print('\t\t4) Salir.')

        opcion = int(input('\t Opción? '))
    return opcion


# programa principal
listin = Listin()

opcion = 0
while opcion != 4:
    opcion = menu()
    if opcion == 1:
        nombre = input('Nombre: ')
        telefono = input('Teléfono: ')
        listin.añadir(nombre, telefono)
        mas = input(
            '¿Deseas añadir otro teléfono a {0} (s/n)? '.format(nombre))
        while mas == 's':
            telefono = input('Teléfono: ')
            listin.añadir(nombre, telefono)
            mas = input(
                '¿Deseas añadir otro teléfono a {0} (s/n)? '.format(nombre))
    elif opcion == 2:
        nombre = input('Nombre: ')
        telefonos = listin.consultar(nombre)
        for telefono in telefonos:
            print(telefono)
    elif opcion == 3:
        nombre = input('Nombre: ')
        listin.eliminar(nombre)
