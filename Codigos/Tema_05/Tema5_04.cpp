#include "Class_Binarytree2.hpp"

class Operator 
{
    public:
        int add(int x, int y){
            return x + y;
        }

        int sub(int x, int y){
            return x - y;
        }

        int mul(int x, int y){
            return x * y;
        }

        int div(int x, int y){
            return x / y;
        }
};

BinaryTree *buildParseTree(string fpexp){
    string buf;
    stringstream ss(fpexp);
    vector<string> fplist;
    while (ss >> buf){
        fplist.push_back(buf);
    }
    stack<BinaryTree*> pStack;
    BinaryTree *eTree = new BinaryTree("");
    pStack.push(eTree);
    BinaryTree *currentTree = eTree;

    string arr[] = {"+", "-", "*", "/"};
    vector<string> vect(arr,arr+(sizeof(arr)/ sizeof(arr[0])));

    string arr2[] = {"+", "-", "*", "/", ")"};
    vector<string> vect2(arr2,arr2+(sizeof(arr2)/ sizeof(arr2[0])));

    for (unsigned int i = 0; i<fplist.size(); i++){

        if (fplist[i] == "("){
            currentTree->insertLeft("");
            pStack.push(currentTree);
            currentTree = currentTree->getLeftChild();
        }

        else if (find(vect.begin(), vect.end(), fplist[i]) != vect.end()){
            currentTree->setRootVal(fplist[i]);
            currentTree->insertRight("");
            pStack.push(currentTree);
            currentTree = currentTree->getRightChild();
        }

        else if (fplist[i] == ")"){
            currentTree = pStack.top();
            pStack.pop();
        }

        else if (find(vect2.begin(), vect2.end(), fplist[i]) == vect2.end()) {
            try {
                currentTree->setRootVal(fplist[i]);
                BinaryTree *parent = pStack.top();
                pStack.pop();
                currentTree = parent;
            }

            catch (string ValueError ){
                cerr <<"token " << fplist[i] << " is not a valid integer"<<endl;
            }
        }
    }
    return eTree;
}

int to_int(string str) 
{
    stringstream convert(str);
    int x = 0;
    convert >> x;
    return x;
}

string t_string(int num) {
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
    if (tree) {
        if (res1 && res2) {
            if (tree->getRootVal() == "+") {
                return t_string(Oper.add(to_int(postordereval(res1)), to_int(postordereval(res2))));
            } else if (tree->getRootVal() == "-") {
                return t_string(Oper.sub(to_int(postordereval(res1)), to_int(postordereval(res2))));
            } else if (tree->getRootVal() == "*") {
                return t_string(Oper.mul(to_int(postordereval(res1)), to_int(postordereval(res2))));
            } else {
                return t_string(Oper.div(to_int(postordereval(res1)), to_int(postordereval(res2))));
            }
        } else {
            return tree->getRootVal();
        }

    }
}

int main() {

    BinaryTree *pt1 = buildParseTree("( ( 10 + 5 ) * 3 )");

    cout<<postordereval(pt1)<<endl;

    BinaryTree *pt2 = buildParseTree("( ( 10 + 5 ) * ( 3 + 4 ) )");

    cout<<postordereval(pt2)<<endl;

    return 0;
}

