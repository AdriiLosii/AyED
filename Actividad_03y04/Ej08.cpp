//Programa: Ej08.cpp
/*
Propósito:
    Generaliza el programa 2 de esta actividad:
        Tienes dos jarras, una de X litros y otra de Y litros, con X>Y. Ninguna de las jarras
        tiene marcas en ella. Hay una bomba que se puede utilizar para llenar las jarras
        con agua. ¿Cómo se pueden obtener exactamente X/2 litros de agua en la jarra de
        X litros?
*/
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 29/03/2022


#include "Class_Jarras_08.hpp" //Incluimos la clase.

//Definimos las funciones creadas.
void resolver_jarras(Jarra jarra_X, Jarra jarra_Y, int tam_jarra_X, int tam_jarra_Y, int objetivo);

int main()
{
    //Definimos las variables.
    int tam_jarra_X; //Jarra X (grande).
    int tam_jarra_Y; //Jarra Y (pequeña).

    //Validamos la lectura de datos.
    try
    {
        //Solicitamos los datos.
        cout << "Introduce el tamaño de la jarra X (Debe de ser un número par): ";
        cin >> tam_jarra_X;

        cout << "Introduce el tamaño de la jarra Y: ";
        cin >> tam_jarra_Y;

        //Verificamos que: el tamaño X sea mayor que el tamaño Y, que el tamaño X sea un número par y que el valor introducido sea un entero.
        if ((tam_jarra_X <= tam_jarra_Y) or (tam_jarra_X%2 != 0) or (cin.fail()))
        {
            cin.clear();
            throw 1;
        }

        //Definimos las variables.
        Jarra jarra_X(tam_jarra_X);
        Jarra jarra_Y(tam_jarra_Y);
        int objetivo = tam_jarra_X/2; //Litros objetivo.

        //Llamamos a la función para resolver el problema.
        resolver_jarras(jarra_X, jarra_Y, tam_jarra_X, tam_jarra_Y, objetivo);
    
        //Finalizamos el programa.
        cout<<("Pulsa ENTER para finalizar.");
        cin.get();
        return 0;
    }

    catch(...)
    {
        printf("\033c"); //Borramos la pantalla
        cout << "\nError, ha ocurrido algo inesperado.\n" << endl;
        exit (-1); //Finalizamos el programa.
    }
}

//Creamos la función.
void resolver_jarras(Jarra jarra_X, Jarra jarra_Y, int tam_jarra_X, int tam_jarra_Y, int objetivo)
{
    //Realizamos los pasos descritos:
    cout << "\nLlenamos la jarra de " << tam_jarra_X << "L." << endl;
    jarra_X.llenar();
    cout << "Litros en la jarra de " << tam_jarra_X << "L: " << jarra_X.tamano() << " litros." << endl;
    cout << "Litros en la jarra de " << tam_jarra_Y << "L: " << jarra_Y.tamano() << " litros." << endl;

    cout << "\nPasamos el agua de la jarra de " << tam_jarra_X << "L a la de " << tam_jarra_Y << "L y vaciamos esta última." << endl;
    jarra_X.transvasar_a(jarra_Y);
    jarra_Y.vaciar();
    cout << "Litros en la jarra de " << tam_jarra_X << "L: " << jarra_X.tamano() << " litros." << endl;
    cout << "Litros en la jarra de " << tam_jarra_Y << "L: " << jarra_Y.tamano() << " litros." << endl;

    //Comprobamos si el resultado es el deseado.
    if(jarra_X.tamano() == objetivo)
    {
        cout << "\n\tRESUELTO." << endl << endl;
    }

    else
    {
        cout << "\nPasamos el agua de la jarra de " << tam_jarra_X << "L a la de " << tam_jarra_Y << "L y rellenamos la jarra de " << tam_jarra_X << "L." << endl;
        jarra_X.transvasar_a(jarra_Y);
        jarra_X.llenar();
        cout << "Litros en la jarra de " << tam_jarra_X << "L: " << jarra_X.tamano() << " litros." << endl;
        cout << "Litros en la jarra de " << tam_jarra_Y << "L: " << jarra_Y.tamano() << " litros." << endl;

        //Comprobamos si el resultado es el deseado.
        if(jarra_X.tamano() == objetivo)
        {
            cout << "\n\tRESUELTO." << endl << endl;
        }

        else
        {
            cout << "\nPasamos el agua de la jarra de " << tam_jarra_X << "L a la de " << tam_jarra_Y << "L." << endl;
            jarra_X.transvasar_a(jarra_Y);
            cout << "Litros en la jarra de " << tam_jarra_X << "L: " << jarra_X.tamano() << " litros." << endl;
            cout << "Litros en la jarra de " << tam_jarra_Y << "L: " << jarra_Y.tamano() << " litros." << endl;

            //Comprobamos si el resultado es el deseado.
            if(jarra_X.tamano() == objetivo)
                cout << "\n\tRESUELTO." << endl << endl;

            else
                cout << "\n\tNO ES POSIBLE RESOLVER ESTE CASO." << endl << endl;
        }
    }
}