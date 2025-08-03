# Tema2_09
from Class_Conjuntos import *

def main():
    q = Conjunto()
    q2 = Conjunto()
    q3=Conjunto()
    q.inserta(4)
    q.inserta('Perro')
    q.inserta("hola")
    q.inserta(8.4)
    
    q2.inserta('Perro')
    q2.inserta(6)
    q2.inserta(8.4)
    q2.inserta("adios")

    q3.inserta("hola")
    q3.inserta(8.4)
    print("Conjunto original: ", q)
    print("Segunda conjunto ",q2)

    print("Tamaño del primer conjunto: ", q.tamaño())
    print("Pertenece 4 al primer conjunto: ", q.pertenece(4))
    print("Eliminamos la palabra perro del primer", q.elimina(4))
    print("Conjunto original: ", q)
    print("Esta es la unión de los 2 conjuntos",q.union(q2))
    print("Esta es la interseccion de los 2 conjuntos",q.interseccion(q2))
    print("Esta es la diferencia de los 2 conjuntos",q.diferencia(q2))
    print("Q2 esta incluido en q1 de los 2 conjuntos",q.incluye(q3))


main()
