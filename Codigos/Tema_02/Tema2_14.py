# Tema2_14
from Class_Estructuras_lineales import ColaDoble
def main():
    d = ColaDoble()

    print("Cola Vacía? ", d.estaVacia())
    d.agregarFinal("Cebra")
    print("Cola Vacía? ", d.estaVacia())

    d.agregarFrente("Tortuga") 
    d.agregarFrente("Panda")
    d.agregarFinal("Pez_Gato") 
    d.agregarFinal("Jirafa")

    print("Tamaño cola: ", d.tamano())
    print("Primer item: ", d.frente())
    print("Ultimo item: ", d.ultimo())

    print("\n")
    print("Items en la cola: ")
    for i in range(d.tamano()):
        print(d.inspeccionar(i), end=" ")
    print("\n")

    d.borrarFinal()
    d.borrarFrente()

    print("Primer item: ", d.frente())
    print("Ultimo item: ", d.ultimo())
    print("Tamaño cola: ", d.tamano())

    print("\n")
    print("Items en la cola: ")
    for i in range(d.tamano()):
        print(d.inspeccionar(i), end=" ")
    print("\n")
main()
