#include <iostream>
#include <cstdlib>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

#include "Class_Binarytree.hpp"
using namespace std;

void preorder(BinaryTree *tree)
{
    if (tree){
        cout << tree->getRootVal() << endl;
        preorder(tree->getLeftChild());
        preorder(tree->getRightChild());
    }
}

void postorder(BinaryTree *tree)
{
    if (tree != NULL){
        postorder(tree->getLeftChild());
        postorder(tree->getRightChild());
        cout << tree->getRootVal() << endl;
    }
}

void inorder(BinaryTree *tree)
{
    if (tree != NULL){
        inorder(tree->getLeftChild());
        cout << tree->getRootVal();
        inorder(tree->getRightChild());
    }
}

class Operator {
    public:
    int add(int x, int y)
    {
        return x + y;
    }

    int sub(int x, int y)
    {
        return x - y;
    }

    int mul(int x, int y)
    {
        return x * y;
    }

    int div(int x, int y)
    {
        return x / y;
    }
};

int to_int(string str) 
{
    stringstream convert(str);
    int x = 0;
    convert >> x;
    return x;
}

string t_string(int num) 
{
    string str;
    ostringstream convert;
    convert << num;
    str = convert.str();
    return str;
}

string postordereval(BinaryTree *tree)
{
    Operator Oper;
    BinaryTree *res1 = tree->getLeftChild();
    BinaryTree *res2 = tree->getRightChild();
    if (tree) 
    {
        if (res1 && res2) 
        {
            if (tree->getRootVal() == '+') 

                return t_string(Oper.add(to_int(postordereval(res1)), to_int(postordereval(res2))));

            else if (tree->getRootVal() == '-') 

                return t_string(Oper.sub(to_int(postordereval(res1)), to_int(postordereval(res2))));

            else if (tree->getRootVal() == '*') 

                return t_string(Oper.mul(to_int(postordereval(res1)), to_int(postordereval(res2))));

            else 

                return t_string(Oper.div(to_int(postordereval(res1)), to_int(postordereval(res2))));

        } 
        else 

            return tree->getRootVal();


    }
}



string evaluate(BinaryTree *parseTree) 
{
    Operator Oper;

    BinaryTree *leftC = parseTree->getLeftChild();
    BinaryTree *rightC = parseTree->getRightChild();

    if (leftC && rightC) 
    {
        if (parseTree->getRootVal() == '+') 

            return t_string(Oper.add(to_int(evaluate(leftC)), to_int(evaluate(rightC))));

        else if (parseTree->getRootVal() == '-') 

            return t_string(Oper.sub(to_int(evaluate(leftC)), to_int(evaluate(rightC))));

        else if (parseTree->getRootVal() == '*') 

            return t_string(Oper.mul(to_int(evaluate(leftC)), to_int(evaluate(rightC))));

        else 

            return t_string(Oper.div(to_int(evaluate(leftC)), to_int(evaluate(rightC))));

    } 
    else 

        return parseTree->getRootVal();

}

string printexp(BinaryTree *tree)
{
    string sVal;
    if (tree)
    {
        sVal = "(" + printexp(tree->getLeftChild());
        sVal = sVal + tree->getRootVal();
        sVal = sVal + printexp(tree->getRightChild()) + ")";
    }
    return sVal;
}
