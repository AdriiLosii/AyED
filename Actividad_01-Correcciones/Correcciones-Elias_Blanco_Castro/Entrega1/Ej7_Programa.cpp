
#include "ej7.hpp"
using std::cout;
using std::endl;
//Funcion principal
int main(void)
{
    //Definimos las variables
    double v[]={-5, -1, 2, 7};
    Polinomio pol(3, v);
    cout << endl << "pol(x) = " << pol << endl;
    double v1[] = {1, 4, 1, 1};
    //Comprobacion de igualdad 
    Polinomio pol1(3, v1);
    cout << endl << "pol1(x) = " << pol1 << endl;
    //Suma 
    Polinomio pol2(pol + pol1); 
    cout << endl << "pol2(p + pol1) = " << pol2 << endl; 
    cout << endl << "pol(x) += pol1(x) = " << (pol += pol1) << endl; 
    //Resta 
    Polinomio p3(-pol); 
    cout << endl << "p3(-p) = " << p3 << endl;
    cout << endl << "pol(0) < pol1(0) = " << (pol < pol1) << endl;
return 0;
}