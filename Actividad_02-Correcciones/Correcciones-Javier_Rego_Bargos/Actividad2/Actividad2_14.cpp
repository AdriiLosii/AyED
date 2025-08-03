#include <iostream> //se podria quitar, dado que esta en la clase
#include <ostream>  //se podria quitar, dado que esta en la clase
#include "Class_Listas_No_Ordenadas.hpp"
using namespace std;  //se podria quitar, dado que esta en la clase


int main()
{
    UnorderedList mylist;
    mylist.add(1);
    mylist.add(2);
    mylist.add(3);
    mylist.add(4);
    mylist.add(5);
    mylist.add(6);
    
    cout<<"Mostramos el tamano de la lista"<<endl;

    cout << "Tamano: " << mylist.size() << endl;

    mylist.add(8);

    cout << "TAMANO: " << mylist.size() << endl;

    mylist.remove(2);
   
    cout << "TAMANO: " << mylist.size() << endl;
    
    mylist.remove(3);

    cout << "Tamano: " << mylist.size() << endl;
    
    cout << "Mi lista es: " << endl
         << mylist;
    return 0;
}
