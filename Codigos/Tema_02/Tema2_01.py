# Tema2_01
from Class_Estructuras_lineales import Pila

p = Pila()

print(p.estaVacia())
p.incluir(4)
p.incluir('perro')
print(p.inspeccionar())
p.incluir(True)
print(p.tamano())
print(p.estaVacia())
p.incluir(8.4)
print(p.extraer())
print(p.extraer())
print(p.tamano())
print(p)
