//Programa: Ejercicio_06.cpp
/*
Propósito:
    Implementar la clase de uso común Clase Hora, de manera que sea robusta y completarla con 
    métodos necesarios
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 19/02/2022


#include "Clase_Hora_06.hpp"
using namespace std;

int main()
{
    //Definimos las fechas.
    Hora hora1(16, 30, 13);
    Hora hora2(19, 17, 40);

    //Mostramos las horas.
    cout << "Hora introducida 1: " << hora1 << endl;
    cout << "Hora introducida 2: " << hora2 << endl;

    //Utilizamos las funciones implementadas en la clase.
    cout << "\n¿Horas iguales? " << (hora1 == hora2) << endl;
    cout << "¿Horas distintas? " << (hora1 != hora2) << endl;
    cout << "¿Hora 1 mayor que hora 2? " << (hora1 > hora2) << endl;
    cout << "¿Hora 1 menor que hora 2? " << (hora1 < hora2) << endl;
}