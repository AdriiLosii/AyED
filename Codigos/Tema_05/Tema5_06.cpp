#include <iostream>
#include <vector>
using namespace std;

#include "Class_binheap.hpp"


int main(){
    int arr[] = {9, 5, 6, 2, 3};
    vector<int> a(arr,arr+(sizeof(arr)/ sizeof(arr[0])));

    vector<int> vec;
    vec.push_back(0);

    BinHeap *bh = new BinHeap(vec);
    bh->buildheap(a);

    cout << bh->delMin() << endl;
    cout << bh->delMin() << endl;
    cout << bh->delMin() << endl;
    cout << bh->delMin() << endl;
    cout << bh->delMin() << endl;

    return 0;
}
