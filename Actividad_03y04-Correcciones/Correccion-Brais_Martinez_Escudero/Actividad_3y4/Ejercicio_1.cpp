#include <iostream> //se podria quitar, dado que esta en la clase
#include <ostream>  //se podria quitar, dado que esta en la clase
#include "Class_Listas_No_Ordenadas.hpp"
using namespace std;  //se podria quitar, dado que esta en la clase
UnorderedList mylist2;
UnorderedList mylist1;

void invertir(UnorderedList &lista){
    if (lista.isEmpty() == true){
        cout << "MI LISTA INVERTIDA: " << endl
         << mylist2;
    }
    else{
        mylist2.add(mylist1.primero());
        mylist1.remove(mylist1.primero());
        return invertir(mylist1);
    }
}

int main()
{
    //lista 1.
    mylist1.add(31);
    mylist1.add(77);
    mylist1.add(17);
    mylist1.add(93);
    mylist1.add(26);
    mylist1.add(54);

    cout << "MI LISTA: " << endl
         << mylist1;

    invertir(mylist1);
    return 0;

}
