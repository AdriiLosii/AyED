from itertools import takewhile


PAQUETES = (
    ("Paquete 1", 2, 3), ("Paquete 2", 3, 4), ("Paquete 3", 4, 8), ("Paquete 4", 5, 8),
    ("Paquete 5", 9, 10))

def proceso_valor(item):
    nombre, peso, valor = item
    return float(valor)

def proceso_peso(item):
    nombre, peso, valor = item
    proceso_peso.peso_maximo -= peso
    return proceso_peso.peso_maximo >= 0    


proceso_peso.peso_maximo = 20


carga_lista = list(takewhile(proceso_peso, reversed(sorted(PAQUETES, key=proceso_valor))))

sumacarga = 0
sumavalor = 0

for item in carga_lista:
    print (item[0] + ' Peso :%i' % item[1] + ' valor :%i' % item[2])
    sumacarga = sumacarga + item[1]
    sumavalor = sumavalor + item[2] 

print ('')
print ('Peso total paquetes: %i' % sumacarga)
print ('Valor total paquetes: %i' % sumavalor)