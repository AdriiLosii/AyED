#include <iostream>
#include "class_cola.cpp"
using namespace std;


void imprimir(Cola x)
{
    for (int i=0; i<x.length(); i++)
    {
        cout<<x.getItemAtIndex(i)<<" ";
    }
    cout<<endl;
}


int main()
{

    Cola cola;
    cout<<"Cola vacia?: "<<cola.isEmpty()<<endl;
    cola.add(1); cola.add(2); cola.add(3.342); cola.add(-4);    cola.add(5); cola.add(4); cola.add(63);    cola.add(34);
    
    imprimir(cola);

    cola.del(3.342);

    imprimir(cola);

    cout<<"cola vacia?: "<<cola.isEmpty()<<endl;
    cout<<"longitud: "<<cola.length()<<endl;
    cout<<"elemento en la posicion 5: "<<cola.getItemAtIndex(5)<<endl;
    cout<<"existe el elemento '4'?: "<<cola.search(4)<<endl;
    cout<<"existe el elemento '-147'?: "<<cola.search(-147)<<endl;
    cout<<"extrayendo el elemento en la posicion 4: "<<cola.extract(4)<<endl;
    imprimir(cola);
    cout<<"extrayendo el elemento en la ultima posicion: "<<cola.extract()<<endl;
    imprimir(cola);

    

    

}