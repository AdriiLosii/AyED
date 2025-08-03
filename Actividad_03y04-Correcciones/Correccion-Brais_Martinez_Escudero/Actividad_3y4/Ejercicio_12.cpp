#include <iostream>
#include <vector>
using namespace std;

//OrdenamientoBUrbuja
vector<int> bubbleSort(vector<int> avector) 
{
  for (int passnum = avector.size()-1; passnum > 0; passnum -= 1) 
    for (int i = 0; i < passnum; i++) 
        if (avector[i] > avector[i+1]) 
        {
            int temp = avector[i];
            avector[i] = avector[i+1];
            avector[i+1] = temp;
            for (unsigned int i = 0; i < avector.size(); i++) 
            cout<<avector[i]<< " ";
            cout<<""<<endl;
        }  
  return avector;
}

//Ordenamiento por seleccion

vector<int> selectionSort(vector<int> avector) 
{
    for (int fillslot = (avector.size() - 1); fillslot >= 0; fillslot--) 
    {
        int positionOfMax = 0;
        for (int location = 1; location < fillslot + 1; location++) 
            if (avector[location] > avector[positionOfMax]) 
                positionOfMax = location;

        int temp = avector[fillslot];
        avector[fillslot] = avector[positionOfMax];
        avector[positionOfMax] = temp;
        for (unsigned int i = 0; i < avector.size(); i++) 
            cout << avector[i] << " ";
        cout<<""<<endl;
    }
    cout<<""<<endl;
    return avector;
}

//Ordenamiento por insercion

vector<int> insertionSort(vector<int> avector) 
{
    for (unsigned int index=1; index<avector.size(); index++) 
    {
        int currentvalue = avector[index];
        int position = index;

        while (position>0 && avector[position-1]>currentvalue) 
        {
            avector[position] = avector[position-1];
            position--;
        }

        avector[position] = currentvalue;
        for (unsigned int i = 0; i < avector.size(); i++) 
            cout << avector[i] << " ";
        cout<<""<<endl;
    }

    return avector;
}

//Ordenamiento Shell
void printl(vector<int> avector) 
{
    for (unsigned int i=0; i<avector.size(); i++) 
        cout << avector[i] << " ";
    cout << endl;
}
vector<int> gapInsertionSort(vector<int> avector, int start, int gap) 
{
    for (unsigned int i = start + gap; i < avector.size(); i += gap) 
    {
        int currentvalue = avector[i];
        int position = i;

        while (position >= gap && avector[position - gap] > currentvalue) 
        {
            avector[position] = avector[position - gap];
            position -= gap;
        }
        avector[position] = currentvalue;
    }
    return avector;
}

//function shellsorts through the vector
vector<int> shellSort(vector<int> avector) 
{
    int subvectorcount = avector.size() / 2; //cuts vector by half
    while (subvectorcount > 0) 
    {
        for (int startposition = 0; startposition < subvectorcount; startposition++) 
            avector = gapInsertionSort(avector, startposition, subvectorcount);
            //runs avector through gapInsertionSort function

        cout << "After increments of size " << subvectorcount
             << " The vector is: " << endl;
        printl(avector);

        subvectorcount = subvectorcount / 2; //cuts vector in half
    }

    return avector;
}

vector<int> mergeSort(vector<int> avector) 
{
    cout<<"Splitting ";
    printl(avector);
    if (avector.size()>1) 
    {
        int mid = avector.size()/2;
        //C++ Equivalent to using Python Slices
        vector<int> lefthalf(avector.begin(),avector.begin()+mid);
        vector<int> righthalf(avector.begin()+mid,avector.begin()+avector.size());

        lefthalf = mergeSort(lefthalf);
        righthalf = mergeSort(righthalf);

        unsigned i = 0;
        unsigned j = 0;
        unsigned k = 0;
        while (i < lefthalf.size() && j < righthalf.size()) 
        {
            if (lefthalf[i] < righthalf[j]) 
            {
                avector[k]=lefthalf[i];
                i++;
            } else 
            {
                avector[k] = righthalf[j];
                j++;
            }
            k++;
        }

        while (i<lefthalf.size()) 
        {
            avector[k] = lefthalf[i];
            i++;
            k++;
        }

        while (j<righthalf.size()) 
        {
            avector[k]=righthalf[j];
            j++;
            k++;
        }

    }
    cout<<"Merging ";
    printl(avector);

    return avector;
}

//Ordenamiento Rapido

int partition(vector<int> &avector, int first, int last) 
{
  int pivotvalue = avector[first];

  int rightmark = last;
  int leftmark = first+1;

  bool done = false;

  while(not done)
  {
    while(leftmark<=rightmark and avector[leftmark]<=pivotvalue)
      leftmark++;
    while(rightmark>=leftmark and avector[rightmark]>=pivotvalue)
      rightmark--;
    if(rightmark<leftmark)
      done = true;
    else
      swap(avector[rightmark], avector[leftmark]);
  }

  swap(avector[rightmark], avector[first]);

  return rightmark;
}

//recursive function that quicksorts through a given vector
void quickSort(vector<int> &avector, int first, int last) 
{
  int splitpoint;

  if (first<last) 
  {
    splitpoint = partition(avector,first,last);

    quickSort(avector,first,splitpoint);
    quickSort(avector,splitpoint+1,last);
    printl(avector);
  }
}

int main() {
    // Vector initialized using a static array
    static const int arr[] = {54,26,93,17,77,31,44,55,20};
    vector<int> avector (arr, arr + sizeof(arr) / sizeof(arr[0]) );
    cout<<"Ordenamiento burbuja: "<<endl;
    vector<int> bvector = bubbleSort(avector);
    cout<<"Ordenamiento por selección: : "<<endl;
    vector<int> updatedAvector = selectionSort(avector);
    cout<<"Ordenamiento por inserción: "<<endl;
    vector<int> ivector = insertionSort(avector);
    cout<<"Ordenamiento por Shell: "<<endl;
    shellSort(avector);
    cout<<"Ordenamiento por mezcla: "<<endl;
    mergeSort(avector);
    cout<<"Ordenamiento Rapido: "<<endl;
    quickSort(avector,0,avector.size()-1);
    return 0;
}

