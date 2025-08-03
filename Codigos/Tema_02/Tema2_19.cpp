#include <iostream>  //se podria quitar, dado que esta en la clase
#include <ostream>  //se podria quitar, dado que esta en la clase
#include "Class_Listas_Ordenadas.hpp"
using namespace std;  //se podria quitar, dado que esta en la clase

// similar to unordered lists except it orders the data

int main()
{
    OrderedList mylist;
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
    cout << "MY LIST: " << endl
         << mylist;
    return 0;
}
