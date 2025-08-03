#include "Class_Binarytree.hpp"

using namespace std;

int main() 
{
    BinaryTree *r = new BinaryTree('a');
    cout << r->getRootVal() << endl;
    cout << r->getLeftChild() << endl;
    r->insertLeft('b');
    cout << r->getLeftChild() << endl;
    cout << r->getLeftChild()->getRootVal() << endl;
    r->insertRight('c');
    cout << r->getRightChild() << endl;
    cout << r->getRightChild()->getRootVal() << endl;
    r->getRightChild()->setRootVal('d');
    cout << r->getRightChild()->getRootVal() << endl;

    return 0;
}
