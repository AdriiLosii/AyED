/*Programa: Ej14.cpp
Propósito:
    Utiliza todas las funciones de búsqueda binaria (recursiva e iterativa). Genera una lista
    ordenada aleatoria de números enteros y realiza una prueba de referencia
    (Benchmark) para cada función. ¿Cuáles son sus resultados? ¿Puedes explicarlos?
Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
Fecha: 21/04/2022
*/


//Importamos las bibliotecas.
#include <iostream>
#include <vector>
#include <ctime> 
#include <random>
#include <algorithm>
#include <chrono> //Para usar el temporizador.
#include <stdlib.h>
using namespace std;
using namespace std::chrono;


//Definimos las funciones creadas.
void print(int vector[], int tamano);
bool busqueda_binaria(int vector[], int tamano, int num_buscar);
bool busqueda_binaria_recursiva(int vector[],int primero, int ultimo, int num_buscar);
void vector_aleatorio_ordenado(int vector_analisis[], int i);


//Programa principal:
int main() 
{
    //Creamos un vector de enteros aleatorios:
    const int tamano = 20;
    int vector[tamano];
    
    srand(time(0)); //Utilizamos la hora del sistema para que rand() no genere siempre los mismos números.
    //Rellenamos el array.
    for (int i = 0; i < tamano; i++)
    {
        vector[i] = 1 + rand() % (tamano*2);
    }

    //Ordenamos el vector.
    sort(vector, vector + tamano);
    
    //Definimos las variables.
    int num_buscar;
    bool busqueda = false;

    //Mostramos la lista ordenada.
    cout << "Lista aleatoria ordenada: ";
    print(vector, tamano);

    try //Lectura de datos validada.
    {
        cout << "\nIntroduzca el número que desea buscar: ";
        cin >> num_buscar;

        if (cin.fail() or num_buscar < 0)
        {
            cin.clear();
            throw 1;
        }
    }
    catch(...) //Si hay algún problema en la lectura de datos.
    {
        cout << "\nError, ha ocurrido algo inesperado.\n";
        cout << "Pulsa ENTER para finalizar.";
        cin.get();cin.ignore();cin.ignore();
        return 0;
    }

    cout << "\n1 -> Está en la lista." << endl;
    cout << "0 -> No está en la lista." << endl;

    cout << "\nFunción no recursiva:" << endl;
    cout << "¿El número " << num_buscar << ", está en la lista?: " << busqueda_binaria(vector, tamano, num_buscar) << endl;

    cout << "\nFunción recursiva:" << endl;
    cout << "¿El número " << num_buscar << ", está en la lista?: " << busqueda_binaria_recursiva(vector, 0, tamano-1, num_buscar) << endl;



    cout << "\nPulsa ENTER para comenzar el análisis.";
    cin.ignore();cin.ignore();

    /////////////////  ANÁLISIS:  /////////////////

    cout << "\n\t\t\t * Análisis: * \n";
    //Realizamos un test de velocidad para comprobar cual es la complejidad temporal de cada función.
    const int tamano_max = 99999;
    int vector_analisis[tamano_max];
    int num_aleatorio;
    int ejecuciones = 0;
    auto miliseg_tot_bin = 0;
    auto miliseg_tot_bin_recur = 0;

    //Mostramos el tamaño de las listas y los tiempos de ejecución.
    cout << "T[microsegundos]" << endl << endl;
    cout << "Tamaño vectores        T. Binario        T. Binario recursivo" << endl;
    for (int i = 1000; i < tamano_max + 1; i+=1000)
    {
        //Generamos un número aleatorio a buscar:
        num_aleatorio = 1 + rand() % i;

        //Creamos el vector.
        vector_aleatorio_ordenado(vector_analisis, i);

        //Obtenemos el tiempo de ejecución de la función de búsqueda binaria no recursiva.
        auto inicio_bin = high_resolution_clock::now(); //Iniciamos el cronómetro.
        busqueda_binaria(vector_analisis, i, num_aleatorio); //Llamamos a la función.
        auto fin_bin = high_resolution_clock::now(); //Finalizamos el cronómetro.
        auto tiempo_bin= duration_cast<nanoseconds>(fin_bin-inicio_bin); //Calculamos el tiempo.
        miliseg_tot_bin += tiempo_bin.count();

        //Obtenemos el tiempo de ejecución de la función de búsqueda binaria no recursiva.
        auto inicio_bin_rec = high_resolution_clock::now(); //Iniciamos el cronómetro.
        busqueda_binaria_recursiva(vector_analisis, 0, tamano-1, num_aleatorio); //Llamamos a la función.
        auto fin_bin_rec = high_resolution_clock::now(); //Finalizamos el cronómetro.
        auto tiempo_bin_rec = duration_cast<nanoseconds>(fin_bin_rec-inicio_bin_rec); //Calculamos el tiempo.
        miliseg_tot_bin_recur += tiempo_bin_rec.count();

        ejecuciones += 1;

        //Mostramos los datos.
        cout << "      " << i << "                 " << tiempo_bin.count() << "                    " << tiempo_bin_rec.count() << "              " << endl;
    }

    //Tiempos promedio.
    cout << "\n                  T. Binario        T. Binario recursivo" << endl;
    cout << "Tiempos promedio:     " << (miliseg_tot_bin/ejecuciones) << "                    " << (miliseg_tot_bin_recur/ejecuciones) << endl;

    //Conclusion.
    cout << "\nConclusión:" << endl;
    cout << "Como se puede comprobar, los tiempos de ejecución entre los dos métodos son bastante similares, ya que la complejidad temporal no deja de ser la misma para ambos." << endl;
    cout << "También se puede observar que los tiempos de ejecución a medida que aumenta el tamaño de la lista prácticamente no aumentan," << endl;
    cout << "esto se debe a que este método de búsqueda tiene una complejidad temporal O(logn) en el peor de los casos." << endl;

    //Finalizamos el programa.
    cout<<("\nPulsa ENTER para finalizar.");
    cin.get();
    return 0;
}


//Creamos la función que cree el vector del análisis.
void vector_aleatorio_ordenado(int vector_analisis[], int tam)
{
    srand(time(0)); //Utilizamos la hora del sistema para que rand() no genere siempre los mismos números.
    //Rellenamos el array.
    for (int i = 0; i < tam; i++)
    {
        vector_analisis[i] = 1 + rand() % tam*4;
    }

    sort(vector_analisis, vector_analisis+tam);
}

//Creamos la función que muestra el array.
void print(int vector[], int tamano) 
{
    for (unsigned i=0; i < tamano; i++) 
        cout<<vector[i]<<" ";
    cout<<endl;
}

//Creamos la función.
bool busqueda_binaria(int vector[], int tamano, int num_buscar)
{
    int primero = 0;
    int final = tamano - 1;
    bool found = false;

    while (primero <= final && !found) //Mientras las posiciones primero y final no se junten y mientras no se encuentre el número.
    {
        int medio = (primero + final) / 2; //Obtenemos la posición central.
        if (vector[medio] == num_buscar)
            found = true;
        else 
            if (num_buscar < vector[medio]) //Si el valor del número es menor que el valor central.
                final = medio - 1; //El nuevo valor del punto final será el valor central - 1 (cogemos la mitad izquierda de la lista).
            else                    //Si no es así:
                primero = medio + 1; //El nuevo valor del punto inicial será el valor central + 1 (cogemos la mitad derecha de la lista).
    }

    return found;
}

//Creamos la función.
bool busqueda_binaria_recursiva(int vector[], int primero, int ultimo, int num_buscar) 
{
    if (primero > ultimo)
        return false;

    int medio = primero + (ultimo - primero)/2; //Obtenemos la posición central.

    if (num_buscar == vector[medio]) //Si el número que se busca es alguna de las posiciones.
        return true;

    else if (num_buscar < vector[medio]) //Si el elemento que se busca tiene un valor menor al elemento del medio de la lista.
        return busqueda_binaria_recursiva(vector, primero, medio-1, num_buscar); //Pasamos la mitad izquierda de la lista.

    else //Si el elemento que se busca tiene un valor mayor al elemento del medio de la lista.
        return busqueda_binaria_recursiva(vector, medio+1, ultimo, num_buscar); //Pasamos la mitad derecha de la lista.
}