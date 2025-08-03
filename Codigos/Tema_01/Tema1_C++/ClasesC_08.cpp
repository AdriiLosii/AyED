//ClasesC_08.cpp
#include <iostream>
template <class T>
T media(T &a, T & b){
    return (a+b)/2;
}
using namespace std;
int main(void){
int a,b; float c,d;
    cout << "Introduzca dos valores enteros:" << endl;
    cin >> a >> b;
    cout << endl << "La media es " << media(a,b) << endl;
    cout << "Introduzca dos valores float:" << endl;
    cin >> c >> d;
    cout << endl << "La media es " << media(c,d) << endl;
}
