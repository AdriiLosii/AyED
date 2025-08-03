"""
Programa: Ej07.py
Propósito: 
    Realiza la especificación informal del TAD Cola Doble
Fecha: 15/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


#Importación de módulos.
from Class_Colas_dobles_07 import ColaDoble


#Definimos la cola.
colaDoble = ColaDoble()

print("\n(Cola doble)\n")

#Mostramos los resultados.
print("Cola doble:",colaDoble)
print("¿Está vacía?",colaDoble.estaVacia())
print("Tamaño:",colaDoble.tamano())

#Añadimos los elementos a la cola.
print("\n\t * Añadimos ítems a la cola doble * \n")
colaDoble.agregarFinal(4)
colaDoble.agregarFinal('perro')
colaDoble.agregarFrente('gato')
colaDoble.agregarFrente(True)
colaDoble.agregarFinal(-8.4)

#Mostramos los resultados.
print("¿Está vacía?",colaDoble.estaVacia())
print("Cola doble:",colaDoble)
print("Tamaño:",colaDoble.tamano())
print("Borrar final:",colaDoble.borrarFinal())
print("Borrar frente:",colaDoble.borrarFrente())
print("Cola doble:",colaDoble)
print("Tamaño:",colaDoble.tamano())


#FIN.
input("\nPulse ENTER para finalizar.")