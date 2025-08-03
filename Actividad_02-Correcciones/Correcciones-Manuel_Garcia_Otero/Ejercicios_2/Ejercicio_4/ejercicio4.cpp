#include <iostream>
#include "colas_sin_prioridad.cpp"
using namespace std;


void imprimir(ColaSinPrioridad x)
{
    for (int i=0; i<x.length(); i++)
    {
        cout<<x.getItemAtIndex(i)<<" ";
    }
    cout<<endl;
}



int main()
{

    ColaSinPrioridad cola;
    cola.add(0);    cola.add(-1);    cola.add(10);   cola.add(23);   cola.add(-44.2);

    ColaSinPrioridad cola2;
    cola2.add(45);  cola2.add(-53);  cola2.add(323.3);


    imprimir(cola);

    cola.advance();


    imprimir(cola);

    cola.advance();

    imprimir(cola);

    cola.add(-5.34);

    cout<<"frente: "<<cola.front()<<"   cola: "<<cola.back()<<"   tanaño: "<<cola.length()<<endl;

    imprimir(cola);

    cola.concatenate(cola2);

    imprimir(cola);

}