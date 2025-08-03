#include <iostream>
using namespace std;

//Clase de complejos.
class Complex{

private:
 double real,imag;

public:
 Complex(){
  real=imag=0;
 }
 ///////////////////////////////////////////////////
 Complex(double r){
  real=r;
  imag=0;
 }
    ///////////////////////////////////////////////////
 Complex(double r, double i){
  real=r;
  imag=i;
 }
    ///////////////////////////////////////////////////
 Complex(Complex &obj){
  real=obj.real;
  imag=obj.imag;
 }
    //Suma de los complejos.
 Complex add(Complex c){
        Complex Add;
  Add.real = real + c.real;
  Add.imag = imag + c.imag;
        return Add;
 }
    // Operador para la resta de complejos .
 Complex sub(Complex c){
  Complex Sub;
  Sub.real = real - c.real;
  Sub.imag = imag - c.imag;
  return Sub;
 }
    //Multiplicacion de comlpejos.
 Complex mult(Complex c){
        Complex Mult;
  Mult.real = real*c.real - imag*c.imag;
  Mult.imag = real*c.imag - c.real*imag;
  return Mult;
 }
    //Division de complejos.
 Complex div(Complex c){
  Complex Div;
  Div.real = (real*c.real + imag*c.imag)/(c.real*c.real + c.imag*c.imag);
  Div.imag = (imag*c.real + real*c.imag)/(c.real*c.real + c.imag*c.imag);
  return Div;
 }
    // Enseña el numero complejo con la parte real e imaginaria.
 void print(){
        cout<<real<<"+"<<imag<<"i"<<endl<<endl;
 }
    // Coge la parte real.
 double getReal() const{
  return real;
 }
    // Coge la parte imaginaria
 double getImag() const{
  return imag;
 }
 
};
