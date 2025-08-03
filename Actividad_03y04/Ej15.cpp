//Programa: Ej15.cpp
/*
Propósito:
    Implementa el método tamano (__len__) para la implementación del TAD Vector
    Asociativo o mapa de las tablas hash, de manera que sea O(1).
*/
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 19/04/2022

//Incluimos la clase.
#include "Class_Tablas_Hash_15.hpp"

int main()
{
    //Definimos las variables.
    TablaHash Tabla;
    int opcion = 6;
    int clave;
    string item;

    //Mostramos el menú.
    while (opcion != 5)
    {
        cout << "\n¿Qué operación desea realizar?" << endl;
        cout << "\t1) Mostrar la tabla hash." << endl;
        cout << "\t2) Agregar un ítem." << endl;
        cout << "\t3) Obtener el item asociado a una clave." << endl;
        cout << "\t4) Obtener el tamaño de la tabla." << endl;
        cout << "\t5) Salir." << endl;

        try //Lectura de datos validada.
        {
            cout << "\nOpción: ";
            cin >> opcion;

            if (cin.fail())
            {
                cin.clear();
                throw 1;
            }

            switch (opcion)
            {
                case 1:
                    cout << Tabla << endl; //Mostramos la tabla.
                    break;
                
                case 2:
                    cout << "\nIntroduzca la clave del item a agregar: ";
                    cin >> clave;

                    if (cin.fail())
                    {
                        cin.clear();
                        throw 1;
                    }

                    cout << "Introduzca el item a agregar: ";
                    cin >> item;

                    if (cin.fail())
                    {
                        cin.clear();
                        throw 1;
                    }

                    Tabla.agrega(clave, item); //Llamamos a la función para agregar el item a la tabla.
                    break;
                
                case 3:
                    cout << "\nIntroduzca la clave del item a obtener: ";
                    cin >> clave;
                    if (cin.fail())
                    {
                        cin.clear();
                        throw 1;
                    }

                    cout << "Item: " << Tabla.obten(clave) << endl; //Mostramos el resultado.
                    break;

                case 4:
                    cout << "\nTamaño tabla: " << Tabla.__len__() << endl; //Mostramos el tamaño de la tabla.
                    break;
                
                case 5:
                    break;
                
                default: //Si se introduce un número mayor a 5.
                    cout << "\nError, ha ocurrido algo inesperado.\n" << endl;
                    cout << "Pulsa ENTER para finalizar.";
                    cin.ignore();cin.ignore();
                    return 0;
            }
        }
        catch(...) //Si hay algún problema en la lectura de datos.
        {
            cout << "\nError, ha ocurrido algo inesperado.\n" << endl;
            cout << "Pulsa ENTER para finalizar.";
            cin.ignore();cin.ignore();cin.ignore();
            return 0;
        }
    }

    //Finalizamos el programa.
    cout<< "\nPulsa ENTER para finalizar.";
    cin.ignore();cin.get();
    return 0;
}