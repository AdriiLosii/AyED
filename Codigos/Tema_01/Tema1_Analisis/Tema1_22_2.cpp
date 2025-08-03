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

    auto t1 = chrono::high_resolution_clock::now();
    x = 0;
    n = busca(v, x);
    auto t2 = chrono::high_resolution_clock::now();
    chrono::duration<int64_t, nano> elapsed = t2 - t1; //if you want milliseconds you should use: std::chrono::duration<double,milli>
    cout << "Posicion de " << x << ": " << n << endl;
    cout << "Este algoritmo requirio " << elapsed.count() << " nanoseconds." << endl;

    puts("CASO MEDIO");
    t1 = chrono::high_resolution_clock::now();
    x = MAXN / 2;
    n = busca(v, x);
    t2 = chrono::high_resolution_clock::now();
    elapsed = t2 - t1;
    cout << "Posicion de " << x << ": " << n << endl;
    cout << "Este algoritmo requirio " << elapsed.count() << " nanoseconds." << endl;

    puts("CASO PEOR");
    t1 = chrono::high_resolution_clock::now();
    x = MAXN;
    n = busca(v, x);
    t2 = chrono::high_resolution_clock::now();
    elapsed = t2 - t1;
    cout << "Posicion de " << x << ": " << n << endl;
    cout << "Este algoritmo requirio " << elapsed.count() << " nanoseconds." << endl;

    return 0;
}