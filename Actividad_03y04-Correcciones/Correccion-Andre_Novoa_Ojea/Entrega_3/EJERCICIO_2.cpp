/*
Tienes dos jarras, una de 4 litros y otra de 3 litros. Ninguna de las jarras tiene
marcas en ella. Hay una bomba que se puede utilizar para llenar las jarras con
agua. ¿Cómo se pueden obtener exactamente dos litros de agua en la jarra de 4
litros?

Lleno la jarra de 4, 
vacio la de 4 en la de 3, y me queda 1 litro en la de 4, 
Vacio la de 3 en el suelo, 
pongo el litro de la de 4 en la de 3, 
lleno la de 4 y relleno la de 3(que ya tenia un litro)
me quedan 2 litros en la de 4


*/
#include <Class_jarras.hpp>
#include <iostream>

void Litros_jarras(){
    cout << "Jarra de 4 litros" << endl;
    cout << jarra_2.obtener_litros << endl;
    cout << "Jarra de 3 litros" << endl;
    cout << jarra_1.obtener_litros << endl
}
int main(){
    jarras jarra_1(3), jarra_2(4);  
     
    cout << "Llenamos la jarra de 4" << endl;
    jarra_2.llenar_jarra;
    jarra_1.vaciar_jarra;
    Litros_jarras();
    cout << "Llenamos la jarra de 3 con la de 4" << endl;
    jarra_2.quitar_litros(3);
    jarra_1.sumar_litros(3);
    Litros_jarras();
    cout << "Vaciamos la de 3" << endl;
    jarra_1.vaciar_jarra;
    Litros_jarras();
    cout << "El litro sobrante en la de 4 lo pasamos a la de 3" <<endl;
    jarra_2.quitar_litros(1);
    jarra_1.sumar_litros(1);
    Litros_jarras();
    cout << "Llenamos de nuevo la de 4" << endl;
    jarra_2.llenar_jarra;
    Litros_jarras();
    cout << "Llenamos de nuevo la jarra de 3 con la de 4" << endl;
    jarra_2.quitar_litros(2);
    jarra_1.sumar_litros(2);
    Litros_jarras();
    cout << "Terminamos con 2 litros en la jarra de 4" << endl;
}



