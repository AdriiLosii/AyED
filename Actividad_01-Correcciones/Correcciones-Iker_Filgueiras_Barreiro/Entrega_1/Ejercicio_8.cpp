#include <iostream>
#include "Class_Complejos.cpp"
using namespace std;

//***************MAIN***************************
int main(){

 double real1,imag1,real2,imag2;
//Pide los valores para los numeros complejos del objeto 1 y 2.
 cout<<"Introduce la parte real del primer numero: ";
    cin>>real1;
 cout<<"Introduce la parte imaginaria del primer numero: ";
 cin>>imag1;
    Complex obj1(real1,imag1);
 obj1.print();

 cout<<"Introducde la parte real del segundo numero: ";
 cin>>real2;
 cout<<"Introduce la parte imaginaria del segundo numero: ";
    cin>>imag2;
    Complex obj2(real2,imag2);
 obj2.print();

//Realiza las operaciones entre obj1 y obj2 para otro nuevo complejos llamado c con
 Complex c;
 c = obj1.add(obj2);
 cout<<"La suma entre obj1 y obj2 es : ("<<c.getReal()<<")+("<<c.getImag()<<")i"<<endl;
 c= obj1.sub(obj2);
 cout<<endl<<"La resta entre obj1 y obj2 es : ("<<c.getReal()<<")+("<<c.getImag()<<")i"<<endl;

 c= obj1.mult(obj2);
 cout<<endl<<"Multiplicacion es : ("<<c.getReal()<<")+("<<c.getImag()<<")i"<<endl;

 c= obj1.div(obj2);
 cout<<endl<<"La division entre obj1 y obj2 es : ("<<c.getReal()<<")+("<<c.getImag()<<")i"<<endl;
 return 0;
}