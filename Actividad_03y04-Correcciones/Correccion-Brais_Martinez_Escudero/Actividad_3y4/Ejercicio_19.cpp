
#include <bits/stdc++.h>
#include<stdio.h>
#define numeros_max 500
using namespace std;

void cambiar(int *xp, int *yp)
{
	int temp = *xp;
	*xp = *yp;
	*yp = temp;
}

void busqueda_burbuja(int arr[], int n)
{
	int i, j;
	for (i = 0; i < n-1; i++)	
	
	for (j = 0; j < n-i-1; j++)
		if (arr[j] > arr[j+1])
			cambiar(&arr[j], &arr[j+1]);
}

void seleccion_corta(int arr[], int n)
{
	int i, j, min_idx;

	for (i = 0; i < n-1; i++)
	{
		min_idx = i;
		for (j = i+1; j < n; j++)
		if (arr[j] < arr[min_idx])
			min_idx = j;

		cambiar(&arr[min_idx], &arr[i]);
	}
}


void inserccion_corta(int arr[], int n)
{
	int i, llave, j;
	for (i = 1; i < n; i++)
	{
		llave = arr[i];
		j = i - 1;

		while (j >= 0 && arr[j] > llave)
		{
			arr[j + 1] = arr[j];
			j = j - 1;
		}
		arr[j + 1] = llave;
	}
}

void mostrar_Array(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		cout << arr[i] << " ";
	cout << endl;
}


int main()
{
    const int tamano=500;
    int tiempoInicial, tiempoFinal,tiempoInicial2, tiempoFinal2,tiempoInicial3, tiempoFinal3;
	int arr[tamano];
	int n = sizeof(arr)/sizeof(arr[0]);
    for (int i=0;i<tamano;i++)
        arr[i]=1+rand()%50000;

    tiempoInicial = clock();
	busqueda_burbuja(arr, n);
	cout<<"Lista ordenada mediante el método burbuja: \n";
	mostrar_Array(arr, n);
    tiempoFinal = clock();
	printf("El tiempo  es de %d segundos", tiempoFinal - tiempoInicial);
    tiempoInicial2 = clock();
    seleccion_corta(arr, n);
    cout<<"Lista ordenada por seleccion: ";
	mostrar_Array(arr, n);
    tiempoFinal2 = clock();
	printf("El tiempo  es de %d segundos", tiempoFinal2 - tiempoInicial2);
    tiempoInicial3 = clock();
    inserccion_corta(arr, n);
    cout<<"Lista ordenada por inserccion: ";
	mostrar_Array(arr, n);
    tiempoFinal3 = clock();
	printf("El tiempo  es de %d segundos\n", tiempoFinal3 - tiempoInicial3);
    return 0;
}
