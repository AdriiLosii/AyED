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

    bh->insert(5);
    bh->insert(7);
    bh->insert(3);
    bh->insert(11);

    cout << bh->delMin() << endl;
    cout << bh->delMin() << endl;
    cout << bh->delMin() << endl;
    cout << bh->delMin() << endl;

    return 0;
}



