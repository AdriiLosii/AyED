#include <iostream>
#include "class_cola_8.cpp"
using namespace std;





int main()
{
    Cola array;

    int a=-7;

   cout<<"cabeza: "<<array.getCabeza()<<endl;
    array.add(1.2);
   cout<<"cabeza: "<<array.getCabeza()<<endl;
    array.add(-3);
    cout<<"cabeza: "<<array.getCabeza()<<endl;
    array.add(50);
    cout<<"cabeza: "<<array.getCabeza()<<endl;
    array.add(a);
    cout<<"cabeza: "<<array.getCabeza()<<endl;
    array.add(7.003);
    cout<<"cabeza: "<<array.getCabeza()<<endl;
    array.add(2);
    cout<<"cabeza: "<<array.getCabeza()<<endl;
    array.add(-20);
    cout<<"cabeza: "<<array.getCabeza()<<endl;

    cout<<array.getItemAtIndex(1)<<endl;
    cout<<array.length()<<endl;
    cout<<"array entero: [";

    for (int i=0; i<array.length(); i++)
    {
        cout<<array.getItemAtIndex(i)<<"  ";
    }

    cout<<"]"<<endl<<"terminado"<<endl;
    
   float b = array.extract();
   cout<<b<<endl;

   cout<<"array entero: [";

    for (int i=0; i<array.length(); i++)
    {
        cout<<array.getItemAtIndex(i)<<"  ";
    }

    cout<<"]"<<endl<<"terminado"<<endl;
}
