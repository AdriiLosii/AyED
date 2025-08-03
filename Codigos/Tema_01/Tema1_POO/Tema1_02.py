from Class_Clientes import Cliente

juan = Cliente('Juan Perez', '12345678Z', 19)
pepe = Cliente('Pepe Lopez', '23456789D', 20)
toni = Cliente('Antonio Perez', '87654321Q', 20)
clientes = [toni, juan, pepe]
print(juan)
print('Las iniciales de ', juan.nombre, 'son ', juan.iniciales())
copia=juan.copia()
copia.edad=20
print(copia)