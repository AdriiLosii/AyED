#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void genera_alea(int datos[], int frecs[], int, int);
void moda1(int &, int &, int edades[], int);
void moda2(int &, int &, int edades[], int, int);
void moda3(int &, int &, int frecs[], int);

int main() /* modax.c: cálculo de la moda */
{
    int maxFrec, moda, MAXDATOS, MAXEDAD;
    cout << "Dame el tamanho de la muestra ";
    cin >> MAXDATOS;
    int edades[MAXDATOS];

    cout << "Dame la edad maxima ";
    cin >> MAXEDAD;

    int frecs[MAXEDAD];

    genera_alea(edades, frecs, MAXEDAD, MAXDATOS);

    clock_t begin = clock();
    moda1(maxFrec, moda, edades, MAXDATOS);
    clock_t end = clock();

    cout << "Leidos " << MAXDATOS << " datos Moda= " << moda << "  frecuencia= " << maxFrec << endl;
    cout << "Este algoritmo requirio " << (end - begin) << " milisegundos\n"
         << endl;

    begin = clock();
    moda2(maxFrec, moda, edades, MAXEDAD, MAXDATOS);
    end = clock();

    cout << "Leidos " << MAXDATOS << " datos Moda= " << moda << "  frecuencia= " << maxFrec << endl;
    cout << "Este algoritmo requirio " << (end - begin) << " milisegundos\n"
         << endl;

    begin = clock();
    moda3(maxFrec, moda, frecs, MAXEDAD);
    end = clock();

    cout << "Leidos " << MAXDATOS << " datos Moda= " << moda << "  frecuencia= " << maxFrec << endl;
    cout << "Este algoritmo requirio " << (end - begin) << " milisegundos\n"
         << endl;

    return 0;
}

void genera_alea(int datos[], int frecs[], int MAXEDAD, int MAXDATOS)
{
    // Inicializa vector de frecuencias
    for (int edad = 0; edad < MAXEDAD; edad++)
        frecs[edad] = 0;
    // inicialización del generador aleatorio
    srand(time(NULL));
    // generación de n números entre 1 y 100
    for (int i = 0; i < MAXDATOS; i++)
    {
        datos[i] = rand() % MAXEDAD + 1;
        frecs[datos[i]]++;
    }
}

void moda1(int &maxFrec, int &moda, int edades[], int MAXDATOS)
{
    // moda1.c: cálculo (ineficiente) de la moda
    int frec = 0;
    maxFrec = 0; // Explora n veces edades[] para determinar cuál es la edad que mas se repite (moda)
    for (int i = 0; i < MAXDATOS; i++)
    {
        frec = 0;
        for (int j = 0; j < MAXDATOS; j++)
            if (edades[i] == edades[j])
                frec++;
        if (frec > maxFrec)
        {
            maxFrec = frec;
            moda = edades[i];
        }
    }
}

void moda2(int &maxFrec, int &moda, int edades[], int MAXEDAD, int MAXDATOS)
{
    // moda2.c: cálculo (poco eficiente) de la moda
    int frec = 0;
    maxFrec = 0; // Explora edades[] maxEdad veces para determinar cuál es la edad que mas se repite (moda)
    for (int i = 0; i < MAXEDAD; i++)
    {
        frec = 0;
        for (int j = 0; j < MAXDATOS; j++)
            if (edades[j] == i)
                frec++;
        if (frec > maxFrec)
        {
            maxFrec = frec;
            moda = i;
        }
    }
}

void moda3(int &maxFrec, int &moda, int frecs[], int MAXEDAD)
{
    maxFrec = 0;
    for (int edad = 0; edad < MAXEDAD; edad++) // máx. frecuencia (moda)
        if (frecs[edad] > maxFrec)
        {
            maxFrec = frecs[edad];
            moda = edad;
        }
}
