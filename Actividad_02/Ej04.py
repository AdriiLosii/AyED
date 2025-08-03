"""
Programa: Ej04.py
Propósito: 
    Implementa como un nuevo método de la clase, la concatenación de dos colas para 
    constituir una nueva
Fecha: 14/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""

#Importamos la clase.
from Class_Colas_04 import Cola

#Definimos las variables.
cola1 = Cola()
cola2 = Cola()
cola_concatenada = Cola()

#Rellenamos las listas.
cola1.agregar(4)
cola1.agregar('Perro')
cola1.agregar(True)
cola1.agregar(8.4)
cola1.agregar(-0.5)

cola2.agregar(2)
cola2.agregar("Gato")
cola2.agregar(False)
cola2.agregar(12.3)
cola2.agregar(-1.5)

#Mostramos el tamaño de las colas, las colas, los frentes y los últimos ítems de las colas.
print("\nTamaño de la cola 1: ", cola1.tamano())
print("Cola original 1: ", cola1)
print("Frente de la cola 1: ", cola1.frente())
print("Ultimo de la cola 1: ", cola1.ultimo())

print("\nTamaño de la cola 2: ", cola2.tamano())
print("Cola original 2: ", cola2)
print("Frente de la cola 2: ", cola2.frente())
print("Ultimo de la cola 2: ", cola2.ultimo())

cola_concatenada = cola1.concatena(cola2) #Llamamos a la función para crear la cola concatenada y la guardamos en una variable.
print("\nCola concatenada: ",cola_concatenada) #Mostramos la cola formada por concatenación.

cola_concatenada.avanzar()
print("\nCola concatenada: ",cola_concatenada) #Mostramos la cola formada por concatenación.

#FIN.
input("\nPulse ENTER para finalizar.")