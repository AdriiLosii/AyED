"""
Programa: Ej08.py
Propósito: 
    Implementar el TAD Colas de Prioridad, usando listas enlazadas ordenadas
Fecha: 15/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importamos la clase.
from Class_Colas_prioridad_08 import ColaPrioridad


#Definimos las variables.
cola = ColaPrioridad()

print("\n(Cola de prioridad max-heap)\n")

#Mostramos los resultados.
print("Cola: ",cola)
print("¿Está vacía?",cola.esta_Vacia())
print("Tamaño: ",cola.tamano())
print("Avanzar:",cola.avanzar())
print()

#Añadimos los elementos a la cola.
cola.agregar(5)
cola.agregar(10)
cola.agregar(3)
cola.agregar(-5.3)
cola.agregar(0)

#Mostramos los resultados.
print("Cola: ",cola)
print("¿Está vacía?",cola.esta_Vacia())
print("Tamaño: ",cola.tamano())
print("Primero: ",cola.primero())
print("Avanzar:",cola.avanzar())
print("Cola: ",cola)

#FIN.
input("\nPulse ENTER para finalizar.")