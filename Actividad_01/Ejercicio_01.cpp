//Programa: Ejercicio_01.cpp
/*
Propósito:
    Cree dos nuevas clases de puertas, una llamada PuertaNOR y otra llamada PuertaNAND. Las puertas
    NAND funcionan como puertas AND que tienen una NOT conectada a la salida. Las puertas NOR
    funcionan como puertas OR que tienen una NOT conectada a la salida. Cree la clase XOR.
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 15/02/2022

#include "Clase_Puertas_01_02.hpp"
int main()
{
    //Definimos las variables.
    PuertaNAND pnand(" NAND ");
    PuertaNOR pnor(" NOR ");
    PuertaXOR pxor(" XOR ");
    PuertaNOT pnot(" NOT ");

    //Introducimos los valores de los pines (0 o 1)==(true o false)
    pnand.setNextPin(1);
    pnand.setNextPin(1);
    pnor.setNextPin(0);
    pnor.setNextPin(0);

    //Conectamos las puertas lógicas.
    Conector c1(&pnand, &pxor);
    Conector c2(&pnor, &pxor);
    Conector c3(&pxor, &pnot);

    // Montamos el circuito 
    cout<<"\nEl circuito de puertas logicas es el siguiente:"<<endl;
    cout << pnot.getLabel() << "(";
    cout << "(" << pnand.getPinA() << pnand.getLabel() << pnand.getPinB() << ")";
    cout << pxor.getLabel();
    cout << "(" << pnor.getPinA() << pnor.getLabel() << pnor.getPinB() << ")";
    cout << ") \n\nEl resultado es " << pnot.getOutput() << endl;

    //Finalizamos el programa.
    cout<<("\nPulsa ENTER para finalizar")<<endl;
    cin.get();
    return 0;
}