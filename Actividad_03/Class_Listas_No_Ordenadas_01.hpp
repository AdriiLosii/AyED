//Programa: Class_Listas_No_Ordenadas_01.hpp
/*
Propósito:
    Escribe una función recursiva para invertir una lista enlazada.
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 28/03/2022

#include <iostream>
#include <ostream>
using namespace std;
//creates a node class
class Nodo{

//Definimos el valor inicial del nodo y el puntero al siguiente nodo.
private:
    int valor;   //Valor en el nodo inicial.
    Nodo *siguiente; //Puntero al siguiente nodo.

public:
    Nodo(int valorInicial) //Constructor (Nodo inicial).
    {
        valor = valorInicial; //Asociamos el valor incial como la cabeza de la lista.
        siguiente = NULL; //El siguiente nodo se establece como NULL, ya que de momento no hay siguiente.
    }

    int obtenerValor() //Función que devuelve el valor del nodo dado.
    {
        return valor;
    }

    Nodo *obtenerSiguiente() //Puntero que devuelve el siguiente nodo.
    {
        return siguiente;
    }

    void establecerValor(int valorNuevo) //Función que establece valores en el nodo.
    {
        valor = valorNuevo;
    }

    void establecerSiguiente(Nodo *nuevoSiguiente) //Función que establece el siguiente nodo.
    {
        siguiente = nuevoSiguiente;
    }
};

//Crea una lista desordenada que apunta a la cabeza de la lista enlazada.
class ListaDesordenada
{
public:
    Nodo *cabezaNodo;

    ListaDesordenada() //Constructor (Asocia el valor NULL a la cabeza del nodo, es decir, no apunta a nada).
    {
        cabezaNodo = NULL;
    }

    bool vacia() //La cabeza del nodo está vacía si es = NULL.
    {
        return cabezaNodo == NULL;
    }

    void agrega(int objeto) //Crea un puntero "auxiliar" que añade el nuevo nodo a la cabeza de la lista.
    {
        Nodo *auxiliar = new Nodo(objeto);
        auxiliar->establecerSiguiente(cabezaNodo);
        cabezaNodo = auxiliar;
    }

    int tamano() //Crea un puntero "actual" que recorre la lista hasta llegar a "NULL" (final de la lista).
    {
        Nodo *actual = cabezaNodo;
        int contador = 0;
        while (actual != NULL)
        {
            contador++;
            actual = actual->obtenerSiguiente();
        }

        return contador;
    }

    bool busca(int objeto) //Crea un puntero "actual" que recorre la lista hasta que encuentra el objeto buscado, devuelve una variable booleana.
    {
        Nodo *actual = cabezaNodo;
        while (actual != NULL)
        {
            if (actual->obtenerValor() == objeto)
                return true;
            else
                actual = actual->obtenerSiguiente();
        }
        return false;
    }

    void borra(int objeto) //Utiliza los punteros "actual" y "anterior" para recorrer la lista, buscar el objeto y eliminarlo.
    {
        Nodo *actual = cabezaNodo;
        Nodo *anterior = NULL;
        bool encontrado = false;
        while (!encontrado)
            if (actual->obtenerValor() == objeto)
            {
                encontrado = true;
            }
            else
            {
                anterior = actual;
                actual = actual->obtenerSiguiente();
            }
        if (anterior == NULL)
        {
            cabezaNodo = actual->obtenerSiguiente();
        }
        else
        {
            anterior->establecerSiguiente(actual->obtenerSiguiente());
        }
    }

    //Creamos el método para invertir la lista dada.
    void invierteLista()
    {
        //Definimos las variables.
        Nodo *actual = cabezaNodo;

        if(actual != NULL) //Verificamos que la lista no esté vacía.
        {
            if (actual->obtenerSiguiente() == NULL) //Si es el último nodo.
                cabezaNodo = actual; //Establecemos el último nodo de la lista a invertir como cabeza de la lista invertida.

            else
            {
                borra(actual->obtenerValor()); //Borramos de la lista el valor actual
                invierteLista(); //Llamamos recursivamente al método.
                actual->obtenerSiguiente()->establecerSiguiente(actual); //Hacemos que el siguiente nodo apunte a su anterior (actual), invirtiendo así el orden de los enlaces entre nodos.
                actual->establecerSiguiente(NULL);
            }
        }

        else
            cout << ("\nLa lista está vacía.") << endl; //Mostramos el mensaje.
    }

    friend ostream& operator<<(ostream& os, const ListaDesordenada& lista);
};

ostream &operator<<(ostream &os, const ListaDesordenada &lista)
{
    Nodo *actual = lista.cabezaNodo;
    while (actual != NULL)
    {
        if (actual->obtenerSiguiente() != NULL) //Si no es el último objeto de la lista.
        {
            os << actual->obtenerValor() << " -> "; //Muestra el valor del nodo y " -> ".
            actual = actual->obtenerSiguiente();
        }
        else //Si es el último objeto de la lista.
        {
            os << actual->obtenerValor(); //SOlo muestra el valor del nodo.
            actual = actual->obtenerSiguiente();
        }
    }
    return os;
}