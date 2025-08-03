/*
Programa: Ej07.cpp
Propósito:
    Implementa un montículo binario como un montículo máx.
Fecha: 03/05/2022
*/


//Incluimos la clase.
#include "Class_MaxHeap_07.hpp"


int main()
{
    //Definimos el montículo binario.
    vector<int> vect_inicial = {0}; //Este '0' no será ningun valor del montículo, simplemente lo utilizamos para pasar un vector al constructor.
    MonticuloBinario *monticulo = new MonticuloBinario(vect_inicial);

    //Definimos las variables.
    int opcion = 6;
    float num;

    //Mostramos el menú.
    while (opcion != 5)
    {
        cout << "\n¿Qué operación desea realizar?" << endl;
        cout << "\t1) Agregar un número al montículo." << endl;
        cout << "\t2) Borrar el valor máximo del montículo." << endl;
        cout << "\t3) Mostrar el valor máximo del montículo." << endl;
        cout << "\t4) Mostrar el vector del montículo." << endl;
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
                    cout << "\nIntroduzca el número a agregar: ";
                    cin >> num;

                    if (cin.fail())
                    {
                        cin.clear();
                        throw 1;
                    }

                    monticulo->agrega(num);
                    break;
                
                case 2:
                    monticulo->borraMax();
                    cout << "\nPulse ENTER para continuar.";
                    cin.ignore();cin.ignore();
                    break;
                
                case 3:
                    monticulo->encuentraMax();
                    cout << "\nPulse ENTER para continuar.";
                    cin.ignore();cin.ignore();
                    break;

                case 4:
                    cout << "Montículo: "; monticulo->mostrarMonticulo();
                    cout << "\nPulse ENTER para continuar.";
                    cin.ignore();cin.ignore();
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
    cout << "\nPulsa ENTER para finalizar.";
    cin.get();cin.ignore();
    return 0;
}