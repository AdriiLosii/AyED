#include <iostream> //se podria quitar, dado que esta en la clase
#include <ostream>  //se podria quitar, dado que esta en la clase
#include "Class_Listas_No_Ordenadas.hpp"
using namespace std;  //se podria quitar, dado que esta en la clase


int main()
{
    UnorderedList mylist;
    mylist.add(31);
    mylist.add(77);
    mylist.add(17);
    mylist.add(93);
    mylist.add(26);
    mylist.add(54);

    cout << "SIZE: " << mylist.size() << endl;
    cout << "contains 93?\t" << mylist.search(93) << endl;
    cout << "contains 100?\t" << mylist.search(100) << endl
         << endl;

    mylist.add(100);
    cout << "contains 100?\t" << mylist.search(100) << endl
         << endl;
    cout << "SIZE: " << mylist.size() << endl;

    mylist.remove(54);
    cout << "SIZE: " << mylist.size() << endl;
    mylist.remove(93);
    cout << "SIZE: " << mylist.size() << endl;
    mylist.remove(31);
    cout << "SIZE: " << mylist.size() << endl;
    mylist.search(93);

    cout << "MY LIST: " << endl
         << mylist;
    return 0;
}
