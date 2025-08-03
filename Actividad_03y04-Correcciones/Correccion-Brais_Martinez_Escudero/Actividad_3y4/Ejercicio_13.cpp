#include <iostream>
#include <vector>
using namespace std;
#include <ctime>

bool sequentialSearch1(vector<int> avector, int item) 
{
    unsigned int pos = 0;
    bool found = false;

    while (pos < avector.size() && !found) 
        if (avector[pos] == item) 
            found = true;
        else 
            pos++;
    return found;
    cout<<"ok"<<endl;
}

bool orderedSequentialSearch2(vector<int> avector, int item) 
{
    unsigned int pos = 0;
    bool found = false;
    bool stop = false;
    while (pos < avector.size() && !found && !stop) 
        if (avector[pos] == item) 
            found = true;
        else 
            if (avector[pos] > item) 
                stop = true;
            else 
                pos++;
    return found;
}
bool binarySearch1(vector<int> avector, int item) 
{
    int first = 0;
    int last = avector.size() - 1;
    bool found = false;

    while (first <= last && !found) 
    {
        int midpoint = (first + last) / 2;
        if (avector[midpoint] == item) 
            found = true;
        else 
            if (item < avector[midpoint]) 
                last = midpoint - 1;
            else 
                first = midpoint + 1;
    }
    return found;
}
bool binarySearch2(int arr[], int item, int start, int end) 
{
    if (end >= start) 
    {
        int mid = start + (end - start) / 2;
        if (arr[mid] == item)
            return true;
        if (arr[mid] > item)
            return binarySearch2(arr, item, start, mid - 1);
        else 
            return binarySearch2(arr, item, mid + 1, end);
    }

    return false;
}

bool binarySearchHelper(int arr[], int size, int item) 
{
    return binarySearch2(arr, item, 0, size);
}
bool binarySearch3(vector<int> alist, int item) 
{
      if (alist.size() == 0) 
              return false;
      else 
      {
              int midpoint = alist.size() / 2;
              if (alist[midpoint] == item) 
                      return true;
              else 
                      if (item < alist[midpoint]) 
                        {
                              vector<int> lefthalf(alist.begin(), alist.begin() + midpoint);
                              return binarySearch3(lefthalf, item);
                        }
                      else 
                        {
                              vector<int> righthalf(alist.begin() + midpoint + 1, alist.end());
                              return binarySearch3(righthalf, item);
                        }
      }
    
}

int bensmarksecuencial1(vector<int> vector){
    float t,f,tiempo,media;
    media = 0;
    for(int i = 0;i < 100;i++){
        t = clock();
        sequentialSearch1(vector, 69);
        f = clock();
        tiempo = f-t;
        media = media + tiempo;
    }
    return media/100;
}
int bensmarksecuencial2(vector<int> vector){
    float t,f,tiempo,media;
    media = 0;
    for(int i = 0;i < 100;i++){
        t = clock();
        sequentialSearch1(vector, 69);
        f = clock();
        tiempo = f-t;
        media = media + tiempo;
    }
    return media/100;
}
int bensmarkbin1(vector<int> vector){
    float t,f,tiempo,media;
    media = 0;
    for(int i = 0;i < 100;i++){
        t = clock();
        binarySearch1(vector, 69);
        f = clock();
        tiempo = f-t;
        media = media + tiempo;
    }
    return media/100;
}
int bensmarkbin2(int arr[], int size){
    float t,f,tiempo,media;
    media = 0;
    for(int i = 0;i < 100;i++){
        t = time(0);
        binarySearchHelper(arr,size, 69);
        f = time(0);
        tiempo = f-t;
        media = media + tiempo;
    }
    return media/100;
}
int bensmarkbin3(vector<int> vector){
    float t,f;
    double media,time;
    media = 0;
    for(int i = 0;i < 100;i++){
        t = clock();
        binarySearch3(vector, 69);
        f = clock();
        time = t-f;
        media = media + time;
    }
    return media/100;
}

int main() 
{
    // Vector initialized using an array
    int arr[200] = {0};
    for ( int i = 0; i < 200; ++i )
      arr[ i ] = i+1;
    int arrLength = sizeof(arr) / sizeof(arr[0]);
    vector<int> vectorordenado(arr,arr+(sizeof(arr)/sizeof(arr[0])));

    int arra[200] = {0};
    for ( int i = 0; i < 200; ++i )
      arra[ i ] = rand()%500;
    vector<int> vectoraleatorio(arra,arra+(sizeof(arra)/sizeof(arra[0])));

    cout<< "Tiempo medio en busqueda secuencial metodo 1: " <<bensmarksecuencial1(vectoraleatorio)<<endl;
    cout<< "Tiempo medio en busqueda secuencial metodo 2: " <<bensmarksecuencial2(vectorordenado)<<endl;
    cout<< "Tiempo medio en busqueda binaria metodo 1: " <<bensmarkbin1(vectorordenado)<<endl;
    cout<< "Tiempo medio en busqueda binaria metodo 2: " <<bensmarkbin2(arr,arrLength)<<endl;
    cout<< "Tiempo medio en busqueda binaria metodo 3: " <<bensmarkbin3(vectorordenado)<<endl;
    return 0;
}