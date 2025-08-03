#include <iostream>
#include <cstdlib>
#include <cstddef>
#include <string>
#include "Class_AVL.hpp"

using namespace std;



int main(){

    BinarySearchTreeAVL *mytree = new BinarySearchTreeAVL();
    mytree->put(3, "red");
    mytree->put(4, "blue");
    mytree->put(6, "yellow");
    mytree->put(2, "at");

    cout << mytree->get(6) << endl;
    cout << mytree->get(2) << endl;

    return 0;
}

