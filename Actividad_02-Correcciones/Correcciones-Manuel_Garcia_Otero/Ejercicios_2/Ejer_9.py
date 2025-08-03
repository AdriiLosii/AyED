"""Escribe la especificación informal del TAD Conjunto. Enriquece la clase Conjunto con:
• Un método elimina que borre del conjunto un elemento dado
• Un método unión que devuelva el conjunto resultante de unir dos conjuntos
• Un método intersección que devuelva un conjunto con la intersección de dos
conjuntos
• Un método diferencia que devuelva un conjunto con la diferencia entre dos
conjuntos
• Un método incluye que consulta si un conjunto dado está incluido en el
conjunto"""

from Class_Conjuntos import *

print("Eliminar un elemento de un conjunto:")
con1=Conjunto()          #se demuestra el metodo elimina
con1.crear_aleatorio(10)
con1.inserta(3)
print(con1,"\n")
con1.elimina(3)
print(con1,"\n\n")


print("Unir dos conjuntos dados:")
con1=Conjunto()          #se demuestra el metodo union
con1.crear_aleatorio(10)
print(con1)
con2=Conjunto()          
con2.crear_aleatorio(10)
print(con2,"\n")
con1.union(con2)
print(con2,"\n\n")


print("Sacar la interseccion de dos conjuntos dados:")
con1=Conjunto()          #se demuestra el metodo interseccion
con1.crear_aleatorio(10)
print(con1)
con2=Conjunto()          
con2.crear_aleatorio(10)
print(con2,"\n")
print(con1.interseccion(con2),"\n\n")


print("Sacar la diferencia de dos conjuntos dados:")
con1=Conjunto()          #se demuestra el metodo diferencia
con1.crear_aleatorio(10)
print(con1)
con2=Conjunto()          
con2.crear_aleatorio(10)
print(con2,"\n")
print(con1.diferencia(con2),"\n\n")


print("Berificar si un conjunto incluye a otro:")
con1=Conjunto()          #se demuestra el metodo incluye
con1.crear_aleatorio(10)
print(con1)
con2=Conjunto()          
con2.crear_aleatorio(10)
print(con2,"\n")
print(con1.incluye(con2))

