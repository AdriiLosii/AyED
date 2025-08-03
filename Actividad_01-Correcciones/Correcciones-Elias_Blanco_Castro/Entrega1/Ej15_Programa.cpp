#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    try
    {
        
    vector <int> lista;
    vector<int> diferentes;
    lista={1, 9, 7, 23, 79, 13, 2, -6, 732};
    int k=1;

    for(int t=0; t<lista.capacity(); t++)
    {
        int cnta_diferentes=0;
        for(int h=0; h<diferentes.capacity(); h++)
        {
            k=k+1;
            if (lista[t]==diferentes[h])
            {
                cnta_diferentes++;
            }
        }
        if (cnta_diferentes==0)
        {
            diferentes.push_back(lista[t]);
        }
    }

    
    while (k>diferentes.capacity() || k<1)
    {
        cout<<"Introduzca un número menor o igual que la longitud de la lista: ";
        cin>>k;
        cout<<endl;  
    }
    
    sort(diferentes.begin(), diferentes.end());
    
    cout<<"El "<<k<<"o menor de la lista es: "<<diferentes[k-1]<<endl;
    }
    catch(...)
    {
        cout<<"Ha ocurrido un error"<<endl;
    }
}