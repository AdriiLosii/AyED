#include <iostream>
#include <cstdlib>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


class BinaryTree {

    private:
        string key;
        BinaryTree *leftChild;
        BinaryTree *rightChild;
    public:
        BinaryTree(string rootObj){
            this->key = rootObj;
            this->leftChild = NULL;
            this->rightChild = NULL;
        }

        void insertLeft(string newNode){
            if (this->leftChild == NULL){
            this->leftChild = new BinaryTree(newNode);
            }
            else {
            BinaryTree *t = new BinaryTree(newNode);
            t->leftChild = this->leftChild;
            this->leftChild = t;
            }
        }

        void insertRight(string newNode){
            if (this->rightChild == NULL){
            this->rightChild = new BinaryTree(newNode);
            }
            else {
            BinaryTree *t = new BinaryTree(newNode);
            t->rightChild = this->rightChild;
            this->rightChild = t;
            }
        }

        BinaryTree *getRightChild(){
            return this->rightChild;
        }

        BinaryTree *getLeftChild(){
            return this->leftChild;
        }

        void setRootVal(string obj){
            this->key = obj;
        }

        string getRootVal(){
            return this->key;
        }
};