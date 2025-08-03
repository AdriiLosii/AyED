//Programa: Ej10.cpp
/*
Propósito:
    Implementar el método anexar una nueva lista para ListaNoOrdenada. ¿Cuál es la
    complejidad de tiempo del método que creaste?
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 13/03/2022

//Incluimos la clase.
#include "Class_Listas_No_Ordenadas_10.hpp"
#include <stdlib.h> //Para usar rand().
#include <chrono> //Para usar el temporizador.
using namespace std::chrono;

//Definimos las funciones creadas.
ListaDesordenada crea_lista_aleatoria(int n);

int main()
{
    //Definimos las variables.
    ListaDesordenada lista_1;
    ListaDesordenada lista_2;
    ListaDesordenada lista_anexada;

    //Agregamos los elementos a las listas.
    lista_1.agrega(1);
    lista_1.agrega(78);
    lista_1.agrega(25);
    lista_1.agrega(13);

    lista_2.agrega(56);
    lista_2.agrega(13);
    lista_2.agrega(9);
    lista_2.agrega(32);
    lista_2.borra(9);

    //Mostramos las listas y su tamaño.
    cout << "Lista 1: " << lista_1 << endl;
    cout << "Tamaño lista 1: " << lista_1.tamano() << endl << endl;

    cout << "Lista 2: " << lista_2 << endl;
    cout << "Tamaño lista 2: " << lista_2.tamano() << endl << endl;

    //Mostramos la lista anexada, creada concatenando las 2 listas.
    lista_anexada = lista_1.anexa(lista_2);
    cout << "Lista anexada: " << lista_anexada << endl;
    cout << "tamaño lista anexada: " << lista_anexada.tamano() << endl << endl;


    ////////////////// ANALISIS //////////////////

    cout << "\n\t\t * Análisis: * \n";
    //Realizamos un test de velocidad para comprobar cual es la complejidad temporal del método creado.
    ListaDesordenada lista_anexada_test;
    int ejecuciones = 0;
    auto miliseg_totales = 0;

    for (int i = 500; i < 15000+1; i+=500)
    {
        //Creamos las listas aleatorias.
        ListaDesordenada lista_1_test = crea_lista_aleatoria(i);
        ListaDesordenada lista_2_test = crea_lista_aleatoria(i);
        
        auto inicio = high_resolution_clock::now(); //Iniciamos el cronómetro.

        lista_1_test.anexa(lista_2_test); //Llamamos a la función.

        auto fin = high_resolution_clock::now(); //Finalizamos el cronómetro.

        auto tiempo = duration_cast<milliseconds>(fin-inicio); //Calculamos el tiempo (en milisegundos).

        miliseg_totales += tiempo.count();
        ejecuciones += 1;

        cout << "Tamaño listas: " << i << ", tiempo ejecución: " << tiempo.count() << " milisegundos." << endl; //Mostramos el tamaño de las listas y los tiempos de ejecución.
    }

    //Media y conclusión.
    cout << "\nMedia de tiempo: " << (miliseg_totales/ejecuciones) << " milisegundos" << endl;
    cout << "\nComo el método creado está formado por 2 bucles, uno for() y otro while(), independientes y\ncomo se puede comprobar por los tiempos mostrados arriba, la complejidad\nde tiempo del método es lineal (O(n))." << endl;

    //Finalizamos el programa.
    cout<<("\nPulsa ENTER para finalizar.");
    cin.get();
    return 0;
}

//Creamos la función.
ListaDesordenada crea_lista_aleatoria(int n)
{
    ListaDesordenada lista;

    for (int i = 0; i < n; i++)
    {
        lista.agrega(rand() % n);
    }

    return lista;
}