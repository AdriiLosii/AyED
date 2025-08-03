#include <iostream>
#include <chrono>
using namespace std;
const int MAXN = 10000000;

int busca(int v[], int x)
{
    for (int i = 0; i <= MAXN; i++)
        if (v[i] == x)
            return i;
    return -1;
}

int main()
{
    int n, x;
    static int v[MAXN + 1]; /* Vector donde buscar y su talla */

    for (int i = 0; i <= MAXN; i++)
        v[i] = i;

    //cout << "Dato a buscar: "<<endl; cin >> x;
    puts("MEJOR CASO");

    clock_t begin = clock();
    x = 0;
    n = busca(v, 0);
    clock_t end = clock();
    double elapsed_secs = double(end - begin);
    cout << "Posicion de " << x << ": " << n << endl;
    cout << "Este algoritmo requirio " << elapsed_secs << " milisegundos\n"
         << endl;

    puts("CASO MEDIO");
    begin = clock();
    x = MAXN / 2;
    n = busca(v, 0);
    end = clock();
    elapsed_secs = double(end - begin);
    cout << "Posicion de " << x << ": " << n << endl;
    cout << "Este algoritmo requirio " << elapsed_secs << " milisegundos\n"
         << endl;

    puts("CASO PEOR");
    begin = clock();
    x = MAXN;
    n = busca(v, 0);
    end = clock();
    elapsed_secs = double(end - begin);
    cout << "Posicion de " << x << ": " << n << endl;
    cout << "Este algoritmo requirio " << elapsed_secs << " milisegundos\n"
         << endl;

    return 0;
}