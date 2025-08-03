/*15. Dada una lista de números en orden aleatorio, escribe un algoritmo que funcione en
tiempo 𝑶(𝒏log(𝒏)) para encontrar el k-ésimo número más pequeño de la lista.
*/

#include <algorithm>
#include <iostream>
using namespace std;
 
// Funcion para devolver el k-esimo numero mas pequeño  
int kthSmallest(int arr[], int n, int k)
{
    // Sortea el array dado
    sort(arr, arr + n);
 
    // Devuelve el k-esimo numero mas pequeño del array sorteado
    return arr[k - 1];
}
 
// Codigo principal
int main()
{
    int arr[] = { 12, 3, 5, 7, 19 };
    int n = sizeof(arr) / sizeof(arr[0]), k = 2;
    cout << "El k-esimo numero mas pequeno es: " << kthSmallest(arr, n, k);
    return 0;
}