#include <iostream>
#include <cstdlib>
#include <cstddef>
#include <string>

using namespace std;

//The TreeNode class represents a node, or vertex, in a tree heirarchy.
class TreeNode{

    public:
        int key;
        int balanceFactor;
        string payload;
        TreeNode *leftChild;
        TreeNode *rightChild;
        TreeNode *parent;

        // Using Optional parameters make it
        // easy for us to create a TreeNode under several different circumstances.
        TreeNode(int key, string val, TreeNode *parent = NULL, TreeNode *left = NULL, TreeNode *right = NULL){
            this->key = key;
            this->payload = val;
            this->leftChild = left;
            this->rightChild = right;
            this->parent = parent;
        }

        // Returns a pointer to the left child of this node.
        // If null, the child doesn't exist.
        TreeNode *hasLeftChild(){
            return this->leftChild;
        }

        //Returns a pointer to the right child of this node.
        //If null, the child doesn't exist.
        TreeNode *hasRightChild(){
            return this->rightChild;
        }

        //Returns a boolean indicating if this node is the left child of its parent.
        bool isLeftChild(){
            return this->parent && this->parent->leftChild == this;
        }

        //Returns a boolean indicating if this node is the right child of its parent.
        bool isRightChild(){
            return this->parent && this->parent->rightChild == this;
        }


        //Returns a boolean indicating if this node is a root node (has no parent).
        bool isRoot(){
            return !this->parent;
        }

        //Returns a boolean indicating if this node has no children.
        bool isLeaf(){
            return !(this->rightChild || this->leftChild);
        }

        // Returns a boolean indicating if this node has children.
        bool hasAnyChildren(){
            return this->rightChild || this->leftChild;
        }

        //Returns a boolean indicating if this node has both children.
        bool hasBothChildren(){
            return this->rightChild && this->leftChild;
        }


        //Removes this node from the tree it exists in,
        //making it the root node of its own tree.
        void spliceOut(){
            if (this->isLeaf()){
                if (this->isLeftChild()){
                    this->parent->leftChild = NULL;
                }
                else{
                    this->parent->rightChild = NULL;
                }
            }
            else if (this->hasAnyChildren()){
                if (this->hasLeftChild()){
                    if (this->isLeftChild()){
                        this->parent->leftChild = this->leftChild;
                    }
                    else{
                        this->parent->rightChild = this->rightChild;
                    }
                    this->leftChild->parent = this->parent;
                }
                else{
                    if (this->isLeftChild()){
                        this->parent->leftChild = this->rightChild;
                    }
                    else{
                        this->parent->rightChild = this->rightChild;
                    }
                    this->rightChild->parent = this->parent;
                }
            }
        }

        // Uses same properties of binary search tree
        // that cause an inorder traversal to print out the
        // nodes in the tree from smallest to largest.
        TreeNode *findSuccessor(){
            TreeNode *succ = NULL;
            if (this->hasRightChild()){
                succ = this->rightChild->findMin();
            }
            else{
                if (this->parent){
                    if (this->isLeftChild()){
                        succ = this->parent;
                    }
                    else{
                        this->parent->rightChild = NULL;
                        succ = this->parent->findSuccessor();
                        this->parent->rightChild = this;
                    }
                }
            }
            return succ;
        }

        //Finds the leftmost node out of all of this node's children.
        TreeNode *findMin(){
            TreeNode *current = this;
            while (current->hasLeftChild()){
                current = current->leftChild;
            }
            return current;
        }

        //Sets the variables of this node. lc/rc are left child and right child.
        void replaceNodeData(int key, string value, TreeNode *lc = NULL, TreeNode *rc = NULL){
            this->key = key;
            this->payload = value;
            this->leftChild = lc;
            this->rightChild = rc;
            if (this->hasLeftChild()){
                this->leftChild->parent = this;
            }

            if (this->hasRightChild()){
                this->rightChild->parent = this;
            }
        }
};

