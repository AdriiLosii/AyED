#include <iostream>
#include <ctime>
using namespace std;

double N2_1(double n, double &m)
{
    clock_t begin = clock();
    m = n * n;
    clock_t end = clock();
    double elapsed_secs = double(end - begin);
    return elapsed_secs;
}

double N2_2(double n, double &m)
{
    clock_t begin = clock();
    m = 0;
    for (int i = 0; i < n; i++)
        m = m + n;
    clock_t end = clock();
    double elapsed_secs = double(end - begin);
    return elapsed_secs;
}

double N2_3(double n, double &m)
{
    clock_t begin = clock();
    m = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            m = m + 1;
    clock_t end = clock();
    double elapsed_secs = double(end - begin);
    return elapsed_secs;
}

int main()
{

    double tiempo,n, m;;
    cout << "Dame un valor para n " << endl;
    cin >> n;

    tiempo = N2_1(n, m);
    cout << "El resultado es " << m << " y requirio " << tiempo << " milisegundos" << endl;

    tiempo = N2_2(n, m);
    cout << "El resultado es " << m << " y requirio " << tiempo << " milisegundos" << endl;

    tiempo = N2_3(n, m);
    cout << "El resultado es " << m << " y requirio " << tiempo << " milisegundos" << endl;
}
