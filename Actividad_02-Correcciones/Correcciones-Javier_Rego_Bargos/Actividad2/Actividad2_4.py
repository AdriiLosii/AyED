# Tema2_09
from Class_Estructuras_lineales import Cola

def main():
    q = Cola()
    q2 = Cola()
    q3 = Cola()
    q.agregar(4)
    q.agregar('Perro')
    q.agregar(True)
    q.agregar(8.4)
    q2.agregar('gato')
    q2.agregar(False)
    q2.agregar(4.4)

    print("Cola original: ", q)
    print("Segunda cola ",q2)
    print("Cola Vacía? ", q.estaVacia())

    print("Tamaño de la cola: ", q.tamano())

    print("Frente de la cola: ", q.frente())
    # quitamos uno de la cola

    q.avanzar()
    print("Cola modificada: ", q)
    print("Principio de la cola: ", q.ultimo())
    print("Cola modificada: ", q)
    q.concatenacion(q3,q2)
    print(q3)
    


main()
