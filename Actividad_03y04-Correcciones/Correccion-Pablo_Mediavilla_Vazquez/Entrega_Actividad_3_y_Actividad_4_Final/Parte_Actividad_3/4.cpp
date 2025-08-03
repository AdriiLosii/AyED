#include <iostream>
#include <vector>
using namespace std;

int HacerCambio(vector<int> ValoresMonedas, int Cambio, vector<int> minMonedas, vector<int> MonedasUsadas)
{

    for (int cents = 0; cents < Cambio+1; cents++)
    {

        int contadorMonedas = cents;
        int nuevaMoneda = 1;

        for ( int j : ValoresMonedas)
        {

            if ( j<= cents)
            {

                if (minMonedas[cents-1] + 1 < contadorMonedas)
                {

                    contadorMonedas = minMonedas[cents-j] + 1;
                    nuevaMoneda = j;

                }

            }

        }
        
        minMonedas[cents] = contadorMonedas;
        MonedasUsadas[cents] = nuevaMoneda;

    }

    return minMonedas[Cambio];

}

vector <int> Hacercambio2(vector<int> ValoresMonedas, int Cambio, vector<int> minMonedas, vector<int> MonedasUsadas)
{

    for (int cents = 0; cents < Cambio + 1; cents++)
    {

        int contadorMonedas = cents;
        int nuevaMoneda = 1;

        for (int j : ValoresMonedas)
        {
            if (j <= cents)
            {
                if (minMonedas[cents-j] + 1 < contadorMonedas)
                {
                    contadorMonedas = minMonedas[cents-j] + 1;
                    nuevaMoneda = j;

                }
            }

        }

        minMonedas[cents] = contadorMonedas;
        MonedasUsadas[cents] = nuevaMoneda;

    }

    return MonedasUsadas;

}

void mostrarMonedas(vector <int> MonedasUsadas, int cambio)
{

    int moneda = cambio;

    while (moneda > 0)
    {

        int estaMoneda = MonedasUsadas[moneda];
        cout << estaMoneda << endl;
        moneda = moneda - estaMoneda;

    }

}

int main()
{

    vector <int> clist = {1, 5, 8, 10, 21, 25};
    int n = 189;
    vector<int> minMonedas(n + 1, 0);
    vector<int> MonedasUsadas(n + 1, 0);
    vector<int> contadorMonedas(n + 1, 0);

    cout << "Haciendo el cambio de " << n << "requiere" << endl;
    cout << HacerCambio(clist, n, minMonedas, MonedasUsadas) << " monedas." << endl;
    cout << "Equivale a: " << endl;
    mostrarMonedas(Hacercambio2(clist, n, minMonedas, MonedasUsadas), n);
    cout << "Lista usada: " << endl;
    vector<int> MonedasUsadas2 = Hacercambio2(clist, n, minMonedas, MonedasUsadas);
    cout << "[";

    for (unsigned int i = 0; i<MonedasUsadas2.size(); i++)
        cout << MonedasUsadas2[i] << ", ";

    cout << "]" << endl;

    return 0;
}