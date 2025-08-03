//Programa: Ej02.cpp
/*
Propósito:
    Escribe un programa de POO para resolver el siguiente problema:
        Tienes dos jarras, una de 4 litros y otra de 3 litros. Ninguna de las jarras tiene
        marcas en ella. Hay una bomba que se puede utilizar para llenar las jarras con
        agua. ¿Cómo se pueden obtener exactamente dos litros de agua en la jarra de 4
        litros?
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 29/03/2022


#include "Class_Jarras_02.hpp" //Incluimos la clase.

//Definimos las funciones creadas.
void resolver_jarras(Jarra jarra_X, Jarra jarra_Y, int objetivo);

//Programa principal.
int main()
{
    //Definimos las variables.
    Jarra jarra_X(4);
    Jarra jarra_Y(3);
    int objetivo = 2; //Litros objetivo.

    //Llamamos a la función para resolver el problema.
    resolver_jarras(jarra_X, jarra_Y, objetivo);

    //Finalizamos el programa.
    cout<<("Pulsa ENTER para finalizar.");
    cin.get();
    return 0;
}

//Creamos la función.
void resolver_jarras(Jarra jarra_X, Jarra jarra_Y, int objetivo)
{
    //Realizamos los pasos descritos:
    cout << "\nLlenamos la jarra de 4L." << endl;
    jarra_X.llenar();
    cout << "Litros en la jarra de 4L: " << jarra_X.tamano() << " litros." << endl;
    cout << "Litros en la jarra de 3L: " << jarra_Y.tamano() << " litros." << endl;

    cout << "\nPasamos el agua de la jarra de 4L a la de 3L y vaciamos esta última." << endl;
    jarra_X.transvasar_a(jarra_Y);
    jarra_Y.vaciar();
    cout << "Litros en la jarra de 4L: " << jarra_X.tamano() << " litros." << endl;
    cout << "Litros en la jarra de 3L: " << jarra_Y.tamano() << " litros." << endl;

    cout << "\nPasamos el agua de la jarra de 4L a la de 3L y rellenamos la jarra de 4L." << endl;
    jarra_X.transvasar_a(jarra_Y);
    jarra_X.llenar();
    cout << "Litros en la jarra de 4L: " << jarra_X.tamano() << " litros." << endl;
    cout << "Litros en la jarra de 3L: " << jarra_Y.tamano() << " litros." << endl;

    cout << "\nPasamos el agua de la jarra de 4L a la de 3L." << endl;
    jarra_X.transvasar_a(jarra_Y);
    cout << "Litros en la jarra de 4L: " << jarra_X.tamano() << " litros." << endl;
    cout << "Litros en la jarra de 3L: " << jarra_Y.tamano() << " litros." << endl;

    //Comprobamos que el resultado sea el esperado.
    if(jarra_X.tamano() == objetivo)
    {
        cout << "\n\tRESUELTO." << endl << endl;
    }
}