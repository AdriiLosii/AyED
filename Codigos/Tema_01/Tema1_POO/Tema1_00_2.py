# Creo una estructura para los clientes
class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.apellidos, self.dni)


# Y otra para las empresas
class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    def borrar_cliente(self, dni=None):
        for i, c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c), "> BORRADO")
                return
        print("Cliente no encontrado")


# Ahora utilizaré ambas estructuras
# Creo un par de clientes
hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")

# Creo una empresa con los clientes iniciales
empresa = Empresa(clientes=[hector, juan])

# Muestro todos los clientes
print("==LISTADO DE CLIENTES==")
"""
print(empresa.clientes[0])
print(empresa.clientes[1])
"""
for c in empresa.clientes:
    print(c)

# Consulto clientes por DNI
print("\n==MOSTRAR CLIENTES POR DNI==")
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("11111111Z")

# Borro un cliente por DNI
print("\n==BORRAR CLIENTES POR DNI==")
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")

# Muestro de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
for c in empresa.clientes:
    print(c)
