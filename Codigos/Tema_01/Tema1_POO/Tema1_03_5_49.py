"""
    Mismo problema resuelto sin el uso de Clases. Tema5_49
    Construyamos un programa que gestione un listín telefónico que permita asociar a una persona más de un teléfono. 
    A través de un menú podremos seleccionar diferentes acciones: añadir y/o eliminar teléfonos y  consultar el listín.
"""
def añadir(listin, nombre, telefono):
    if nombre in listin:
        if not telefono in listin[nombre]:
            listin[nombre].append(telefono)
    else:
        listin[nombre]=[ telefono ]

def consultar(listin, nombre):
    if nombre in listin:
        return listin[nombre]
    else:
        return []

def eliminar(listin, nombre):
    if nombre in listin:
        del listin[nombre]

def menu():
    opcion=0
    while opcion<1 or opcion>4:
        print('\tEscoge una opción:')
        print('\t\t1) Añadir teléfonos.')
        print('\t\t2) Consultar el listín.')
        print('\t\t3) Eliminar persona del listín.')
        print('\t\t4) Escribir todo el listín.')
        print('\t\t5) Salir.')

        opcion=int(input('\t Opción? '))
    return opcion

#programa principal
listin={}
opcion=0
while opcion!=5:
    opcion=menu()
    if opcion==1:
        nombre=input('Nombre: ')
        telefono= input('Teléfono: ')
        añadir(listin,nombre,telefono)
        mas=input('¿Deseas añadir otro teléfono a {0} (s/n)? '.format(nombre))
        while mas=='s':
            telefono= input('Teléfono: ')
            añadir(listin,nombre,telefono)
            mas=input('¿Deseas añadir otro teléfono a {0} (s/n)? '.format(nombre))
    elif opcion==2:
        nombre=input('Nombre: ')
        telefonos=consultar(listin, nombre)
        for telefono in telefonos:
            print (telefono)
    elif opcion==3:
            nombre=input('Nombre: ')
            eliminar(listin, nombre)
    elif opcion==4:
            print(listin)


                  
