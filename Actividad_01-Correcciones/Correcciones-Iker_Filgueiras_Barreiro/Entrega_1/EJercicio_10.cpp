//Completar la clase Fracción en C++ para que sea como la desarrollada en Python

#include "Class_Fracciones.cpp"

int main(){
    Fraction x(2,2);
    Fraction y(2,8);

    //La division
    cout<<"La division de: ("<< x << ") / (" << y << ") es igual a "<< x/y << endl;

    //La multiplicacion
    cout<<"La multiplicacion de: ("<< x << ") * (" << y << ") es igual a "<< x*y << endl;

    //La suma
    cout<<"La suma de: ("<< x << ") + (" << y << ") es igual a "<< x+y << endl;

    //La resta
    cout<<"La resta de: ("<< x << ") - (" << y << ") es igual a "<< x-y << endl;

    //Comprobaciones
    //Si "x" es distinto de "y"
    if (x!=y){
        cout<< "x es distinto de y"<< endl;

        //Una vez sabemos que son distintos comprobamos cual es mayor
        if (x>y){
        cout<< "x es mayor que y"<< endl;
        }

        else{
        cout<< "x es menor a y"<< endl;
        }
    }

    //Si "x" no es distinto de "y" es que son iguales
    else{
        cout<< "x es igual a y"<< endl;
    }

    return 0;
}