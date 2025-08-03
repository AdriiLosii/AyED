#include <iostream>
#include <ctime>
using namespace std;

int N2_1(int n, double &m)
{
    clock_t begin = clock();
    m=0.0;
    m=double(n)*double(n); 
    clock_t end = clock();
    double elapsed_secs = double(end - begin) /CLOCKS_PER_SEC;
    return elapsed_secs;
}


int N2_2(int n, double &m)
{
    clock_t begin = clock();
    m=0.0;
    for(int i = 0; i < n; i++)
        m= m + n;
    clock_t end = clock();
    double elapsed_secs = double(end - begin) /CLOCKS_PER_SEC;
    return elapsed_secs;
}

int N2_3(int n, double &m)
{
    clock_t begin = clock();
    m=0.0;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
        m= m + 1;
    clock_t end = clock();
    double elapsed_secs = double(end - begin) /CLOCKS_PER_SEC;
    return elapsed_secs;
}

int main()
{

    int n;
    double m,tiempo;
    cout<< "Dame un valor para n "<<endl;
    cin >>n;
    
    tiempo=N2_1(n,m);
    cout << "El resultado es "<<m<< " y requirio "<<tiempo<< " segundos"<<endl;

    tiempo=N2_2(n,m);
    cout << "El resultado es "<<m<< " y requirio "<<tiempo<< " segundos"<<endl;

    tiempo=N2_3(n,m);
    cout << "El resultado es "<<m<< " y requirio "<<tiempo<< " segundos"<<endl;

}
