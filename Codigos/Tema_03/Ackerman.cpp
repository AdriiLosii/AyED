//ejemplo función ackermann
#include <iostream>
using namespace std;

unsigned int ackermann(unsigned int m, unsigned int n)
{
    if (m == 0)
        //Base case
        return n + 1;

    if (n == 0)
        return ackermann(m - 1, 1); // restar, moviendose al caso base
    /*observad una llamada a la función ackermann como parámetro para otra llamada a la función ackermann. 
    Aquí es donde se vuelve irrealmente complicado.
    */
    return ackermann(m - 1, ackermann(m, n - 1)); //resta aqui tambien
}

int main()
{
    //calcula la función de ackermann.
    //Reemplazar los parámetros 1,2 con 4,3 y vereis qué sucede
    cout << ackermann(1, 2) << endl;
    return 0;
}
