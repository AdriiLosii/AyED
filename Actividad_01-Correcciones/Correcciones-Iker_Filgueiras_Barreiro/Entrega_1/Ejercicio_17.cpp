/*17. Escribir en lenguaje Python una función que calcule la suma de los elementos de un
vector. Calcular la complejidad temporal de dicha función y expresarla en notación
asintótica.
*/

#include <bits/stdc++.h>
using namespace std;
 
bool candidatos(int A[], int tam,
                           int sum)
{
    int l, r;
 
    sort(A, A + tam);
    l = 0;
    r = tam - 1;
    while (l < r) {
        if (A[l] + A[r] == sum)
            return 1;
        else if (A[l] + A[r] < sum)
            l++;
        else // A[i] + A[j] > sum
            r--;
    }
    return 0;
}
 
int main()
{
    int A[] = { 1, 4, 45, 6, 10, -8 };
    int n = 16;
    int tam = sizeof(A) / sizeof(A[0]);
 
    if (candidatos(A, tam, n))
        cout << "Array has two elements"
                " with given sum";
    else
        cout << "Array doesn't have two"
                " elements with given sum";
 
    return 0;
}