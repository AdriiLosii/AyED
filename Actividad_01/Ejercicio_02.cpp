//Programa: Ejercicio_02.cpp
/*
Propósito:
    Cree una serie de puertas que demuestren que la siguiente ecuación NOT((A and B) or (C and D)) es
    equivalente a NOT(A and B) and NOT (C and D). Asegúrese de usar algunas de sus nuevas puertas en
    la simulación.
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 15/02/2022


#include "Clase_Puertas_01_02.hpp"
int main()
{

    //Ponemos los titulos
    PuertaAND pand1(" AND ");
    PuertaAND pand2(" AND ");
    PuertaAND pand3(" AND ");
    PuertaNOT pnot(" NOT ");
    PuertaOR por(" OR ");

    //Definimos el valor de las entradas (aqui se modifican las entradas de los 4 circuitos)
    pand1.setNextPin(0);
    pand1.setNextPin(0);
    pand2.setNextPin(1);
    pand2.setNextPin(1);

    //Circuito 1:

    //Conectamos las puertas logicas con la funcion Conector del circuito 1
    Conector c1(&pand1, &por);
    Conector c2(&pand2, &por);
    Conector c3(&por, &pnot);

    //Mostramos el circuito y el resultado:
    cout<<"\nEl circuito 1 de puertas logicas es el siguiente:"<<endl;
    cout << pnot.getLabel() << "(";
    cout << "(" << pand1.getPinA() << pand1.getLabel() << pand1.getPinB() << ")";
    cout << por.getLabel();
    cout << "(" << pand2.getPinA() << pand2.getLabel() << pand2.getPinB() << ")";

    cout << ") \n\nEl resultado es " << pnot.getOutput() << endl;
  

    //Circuito 2:
    
    //Conectamos las puertas logicas con la funcion Conector del circuito 2
    Conector c4(&pand1, &pnot);
    Conector c5(&pand2, &pnot);
    Conector c6(&pnot, &pand2);

    //Mostramos el circuito y el resultado:
    cout<<"\nEl circuito 2 de puertas logicas es el siguiente:"<<endl;
    cout << pnot.getLabel();
    cout << "(" << pand1.getPinA() << pand1.getLabel() << pand1.getPinB() << ")";
    cout << pand3.getLabel();
    cout << pnot.getLabel();
    cout << "(" << pand2.getPinA() << pand2.getLabel() << pand2.getPinB() << ")";

    cout << "\n\nEl resultado es " << pnot.getOutput() << endl;


    //Utilizando las nuevas puertas lógicas (NAND, NOR, XOR):
    cout<<"\n\nCircuitos con las nuevas puertas lógicas (NAND, NOR, XOR):"<<endl;

    //Definimos las puertas
    PuertaNOR pnor(" NOR ");

    //Circuito 1:

    //Conectamos las puertas lógicas
    Conector c7(&pand1, &pnor);
    Conector c8(&pand2, &pnor);

    //Mostramos el circuito y el resultado:
    cout << "\nCircuito 1 de puertas lógicas es el siguiente:" << endl;
    cout << "(" << pand1.getPinA() << pand1.getLabel() << pand1.getPinB()<<")";
    cout << pnor.getLabel();
    cout << "(" << pand2.getPinA() << pand2.getLabel() << pand2.getPinB()<<")";

    cout << "\n\nEl resultado es " << pnor.getOutput() << endl;

    //Definimos las puertas
    PuertaNAND pnand1(" NAND ");
    PuertaNAND pnand2(" NAND ");

    //Definimos el valor de las entradas (En este caso será el mismo valor para todos los circuitos)
    pnand1.setNextPin(pand1.getPinA());
    pnand1.setNextPin(pand1.getPinB());
    pnand2.setNextPin(pand2.getPinA());
    pnand2.setNextPin(pand2.getPinB());

    //Circuito 2:

    //Conectamos las puertas lógicas
    Conector c9(&pnand1, &pand3);
    Conector c10(&pnand2, &pand3);

    //Mostramos el circuito y el resultado:
    cout << "\nCircuito 2 de puertas lógicas es el siguiente:" << endl;
    cout << "(" << pnand1.getPinA() << pnand1.getLabel() << pnand1.getPinB() << ")";
    cout << pand3.getLabel();
    cout << "(" << pnand2.getPinA() << pnand2.getLabel() << pnand2.getPinB() << ")";

    cout << "\n\nEl resultado es " << pand3.getOutput() << endl;

    cout << ("\nPulsa ENTER para finalizar") << endl;
    cin.get();
    return 0;        //Cerramos el main
}
