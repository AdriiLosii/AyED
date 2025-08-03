//Programa: Ej10.cpp
/*
Propósito:
    Utilizando las fórmulas de desempeño de la tabla hash que se dan en el Tema 4,
    calcula el número promedio de comparaciones necesarias cuando la tabla está
        10% completa
        25% completa
        50% completa
        75% completa
        90% completa
        99% completa
    ¿En qué punto crees que la tabla hash es demasiado pequeña? Explícalo.  
*/
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 12/04/2022

//Incluimos las bibliotecas.
#include <iostream>
#include <cmath>

using namespace std;

//Definimos las funciones creadas.
float prueba_lineal_exito(float landa);
float prueba_lineal_fracaso(float landa);
float encadenamiento_exito(float landa);
float encadenamiento_fracaso(float landa);

//Programa principal.
int main()
{
    for (int i = 0; i < 100; i++)
    {
        if (i == 10 or i == 25 or i == 50 or i == 75 or i == 90 or i == 99)
        {
            cout << "\n\t\t" <<i << "% COMPLETA:" << endl;

            cout << "\n(Usando direccionamiento abierto con prueba lineal):" << endl;
            cout << "Número promedio de comparaciones en caso de éxito: " << prueba_lineal_exito(i/100.0) << endl;
            cout << "Número promedio de comparaciones en caso de fracaso: " << prueba_lineal_fracaso(i/100.0) << endl;

            cout << "\n(Usando encadenamiento):" << endl;
            cout << "Número promedio de comparaciones en caso de éxito: " << encadenamiento_exito(i/100.0) << endl;
            cout << "Número promedio de comparaciones en caso de fracaso: " << encadenamiento_fracaso(i/100.0) << endl;
        }   
    }

    cout << "\n\nPregunta: ¿En qué punto crees que la tabla hash es demasiado pequeña?" << endl;
    cout << "Respuesta: \nEn el caso de usar direccionamiento abierto con prueba lineal, observando los valores," << endl;
    cout << "podemos ver que al estar un 50% completa, en caso de fracaso, el caso promedio de comparaciones es de 2.5, un valor aceptable," << endl;
    cout << "pero sin embargo, al estar un 75% completa, este valor pasa a ser 8.5 comparaciones promedias." << endl;
    cout << "Por lo tanto, la tabla hash es demasiado pequeña cuando está más de un 50% completa." << endl;

    cout << "\nEn el caso de usar encadenamiento, se puede observar que el valor promedio de comparaciones no aumenta demasiado," << endl;
    cout << "esto se debe a que este método puede almacenar varios ítems en una misma ubicación, ya que cada slot de la tabla es una referencia a una cadena de ítems," << endl;
    cout << "de esta forma, cada vez que se produce una colisión, el elemento se coloca en el slot adecuado, pero esto genera un nuevo problema," << endl;
    cout << "y es que, un incremento en las colisiones implica un incremento en el número de ítems en cada slot de la tabla," << endl;
    cout << "es decir, a medida que más y más ítems obtienen como valor hash la misma posición, aumenta la dificultad de buscar el ítem de la colección." << endl;

    //Finalizamos el programa.
    cout<< "\nPulsa ENTER para finalizar.";
    cin.get();
    return 0;
}


//Creamos la función.
float prueba_lineal_exito(float landa)
{
    return (1.0/2) * (1 + (1 / (1 - landa)));
}

//Creamos la función.
float prueba_lineal_fracaso(float landa)
{
    return (1.0/2) * (1 + pow((1 / (1 - landa)), 2));
}

//Creamos la función.
float encadenamiento_exito(float landa)
{
    return (1 + (landa/2));
}

//Creamos la función.
float encadenamiento_fracaso(float landa)
{
    return landa;
}