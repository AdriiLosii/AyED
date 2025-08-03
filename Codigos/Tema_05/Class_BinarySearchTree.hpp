#include "Class_TreeNode.hpp"

class BinarySearchTree{

    // references the TreeNode
    // that is the root of the binary search tree.
    private:
        TreeNode *root;
        int size;

        /*searches the binary tree comparing the new key to the key in the current node. If the new key is less than the current node, search the left subtree. If the new key is greater than the current node, search the right subtree.*/
        /* When there is no left (or right) child to search, we have found the position in the tree where the new node should be installed.*/
        /*To add a node to the tree, create a new TreeNode object and insert the object at the point discovered in the previous step.*/
        // this is all done recursively
        void _put(int key, string val, TreeNode *currentNode){
            if (key < currentNode->key){
                if (currentNode->hasLeftChild()){
                    this->_put(key, val, currentNode->leftChild);
                }
                else{
                    currentNode->leftChild = new TreeNode(key, val, currentNode);
                }
            }
            else{
                if (currentNode->hasRightChild()){
                    this->_put(key, val, currentNode->rightChild);
                }
                else{
                    currentNode->rightChild = new TreeNode(key, val, currentNode);
                }
            }
        }

        // Uses the same search method as _put, and returns
        // a TreeNode to get
        TreeNode  *_get(int key, TreeNode *currentNode){
            if (!currentNode){
                return NULL;
            }
            else if (currentNode->key == key){
                return currentNode;
            }
            else if (key < currentNode->key){
                return this->_get(key, currentNode->leftChild);
            }
            else{
                return this->_get(key, currentNode->rightChild);
            }
        }

    public:
        BinarySearchTree(){
            this->root = NULL;
            this->size = 0;

        }

        int length(){
            return this->size;
        }

        // Checks to see if the tree has a root,
        // if there is not a root then it will create a new TreeNode
        // and install it as the root of the tree.
        // If a root node is already in place than it calls _put
        // to search the tree
        void put(int key, string val){
            if (this->root){
                this->_put(key, val, this->root);
            }
            else{
                this->root = new TreeNode(key, val);
            }
            this->size = this->size + 1;
        }

        // prints string associated with key to console
        string get(int key){
            if (this->root){
                TreeNode *res = this->_get(key, this->root);
                if (res){
                    return res->payload;
                }
                else{
                    return 0;
                }
            }
            else{
                return 0;
            }
        }

        // checks to make sure the key of the root matches the key that is to be deleted.
        // In either case if the key is not found an error is raised.
        // If the node is found and has no childeren it is deleted
        // If the node has a single child, the child takes the place of the parent.
        // Look at explination for listing 10
        void del(int key){
            if (this->size > 1){
                TreeNode *nodeToRemove = this->_get(key, this->root);
                if (nodeToRemove){
                    this->remove(nodeToRemove);
                    this->size = this->size - 1;
                }
                else{
                    cerr << "Error, key not in tree" << endl;
                }
            }
            else if (this->size == 1 && this->root->key == key){
                this->root = NULL;
                this->size = this->size - 1;
            }
            else{
                cerr << "Error, key not in tree" << endl;
            }
        }

        void remove(TreeNode *currentNode){
            if (currentNode->isLeaf()){ //leaf
                if (currentNode == currentNode->parent->leftChild){
                    currentNode->parent->leftChild = NULL;
                }
                else{
                    currentNode->parent->rightChild = NULL;
                }
            }
            else if (currentNode->hasBothChildren()){ //interior
                TreeNode *succ = currentNode->findSuccessor();
                succ->spliceOut();
                currentNode->key = succ->key;
                currentNode->payload = succ->payload;
            }
            else{ // this node has one child
                if (currentNode->hasLeftChild()){
                    if (currentNode->isLeftChild()){
                        currentNode->leftChild->parent = currentNode->parent;
                        currentNode->parent->leftChild = currentNode->leftChild;
                    }
                    else if (currentNode->isRightChild()){
                        currentNode->leftChild->parent = currentNode->parent;
                        currentNode->parent->rightChild = currentNode->leftChild;
                    }
                    else{
                        currentNode->replaceNodeData(currentNode->leftChild->key,
                                                     currentNode->leftChild->payload,
                                                     currentNode->leftChild->leftChild,
                                                     currentNode->leftChild->rightChild);

                    }
                }
                else{
                    if (currentNode->isLeftChild()){
                        currentNode->rightChild->parent = currentNode->parent;
                        currentNode->parent->leftChild = currentNode->rightChild;
                    }
                    else if (currentNode->isRightChild()){
                        currentNode->rightChild->parent = currentNode->parent;
                        currentNode->parent->rightChild = currentNode->rightChild;
                    }
                    else{
                        currentNode->replaceNodeData(currentNode->rightChild->key,
                                                     currentNode->rightChild->payload,
                                                     currentNode->rightChild->leftChild,
                                                     currentNode->rightChild->rightChild);
                    }
                }
            }
        }
};