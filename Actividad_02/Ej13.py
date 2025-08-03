"""
Programa: Ej13.py
Propósito: 
    ¿Cuál es el resultado de ejecutar en orden inverso los dos pasos del método agregar
    de la Lista_No_Ordenada? ¿Qué tipo de referencia resultaría? ¿Qué tipos de
    problemas pueden resultar?
Fecha: 17/03/2022
Autores: Adrián Losada Álvarez y Gabriel Iglesias Sotelo
"""


######################## Código al final ########################

"""
Pregunta: ¿Cuál es el resultado de ejecutar en orden inverso los dos pasos del método agregar de la Lista_No_Ordenada?
Respuesta:
Si invertimos los pasos del método 'agregar':

def agregar(self,item):
1 ->    temp = Nodo(item)
2 ->    self.cabeza = temp
3 ->    temp.asignarSiguiente(self.cabeza)

Las instrucciones en orden serían:
1-> Crear el nodo con el valor introducido 'item' y que apunte a siguiente = 'None'.
    Visualmente:
    temp = |item| -> None

2-> Definimos la cabeza de la lista como el nodo creado en el paso 1.
    Visualmente:
    self.cabeza = temp = |item| -> None

3-> Al nodo creado en el paso 1 le asignamos como nodo siguiente la cabeza de la lista. Y como self.cabeza = temp (paso 2), lo que estamos haciendo es que el nodo temp apunte a si mismo.
    Visualmente:
                                            _________
                                           |         |
    temp.asignarSiguiente(self.cabeza) =   -->|item|-^ ,   que da lugar a: |item| -> |item| -> |item| -> ... (infinito)

Por lo tanto, estaríamos creando un nodo con el valor 'item' que apunta a sí mismo.

Pregunta: ¿Qué tipo de referencia resultaría?
Respuesta:
Se formaría una lista infinita.

Pregunta: ¿Qué tipos de problemas pueden resultar?
Respuesta:
A la hora de recorrer la lista, el programa no tendría forma de saber cuando parar, ya que se trata de una lista infinita.
Por lo tanto, los métodos como tamano() y borrar() o buscar() si se introduce un número distinto a 'item', no funcionarán debido a que estarían ejecutando un bucle infinito.
Cada vez que se quiere "agregar" un nuevo ítem el programa lo que hará será reemplazar el valor anterior del nodo por el nuevo.
"""

#Importamos la clase.
from Class_Listas_No_Ordenadas_13 import ListaNoOrdenada

print("\nComprobación de la pregunta: ¿Qué tipos de problemas pueden resultar?")
print("Comenta y descomenta en el código las llamadas a la función para comprobar los errores.")
print("Pulsa CTRL + C para detener el programa.")

lista = ListaNoOrdenada()

item = 3
lista.agregar(item) #Agregamos el item a la lista.

#Si intentamos mostrar la lista, la terminal no mostrará nada ya que para realizar el método es necesario recorrer la lista hasta el final.
#print("Lista:",lista)

#Si intentamos mostrar el tamaño de la lista, este tampoco se mostrará, por la misma razón (lista infinita).
#print("Tamaño:",lista.tamaño())

#Si borramos/buscamos un ítem:
#Caso favorable: El ítem es el mismo que el ítem del nodo.
print("Busca 3:",lista.buscar(item))
print("Borra 3:",lista.borrar(item))

#Caso no favorable: El ítem es distinto al ítem del nodo.
item = 5
#print("Busca 5:",lista.buscar(item))
#print("Borrar 5:",lista.borrar(item))

#FIN.
input("\nPulse ENTER para finalizar.")