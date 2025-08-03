/* Header file for abstract data type "STACK" implemented using a linked list  */

#ifndef STACK_H
#define STACK_H

template <class T>
class stack {

    public:
        void push(T);     //Function that inserts elements into the stack
        bool empty();     //Function to test whether the stack is empty
        T top();          //Returns top element of stack
        void pop();       //Removes element at the top of the stack
        int size();       //Returns size of stack
        void print();     //Prints stack contents

        struct node 
        {     //Definition of node structure with constructor and destructor

            T node_data;
            node *next;

            //default ctor
            node() { next = nullptr;  }

            //default dtor
            ~node() { delete root_node; }
        };

    private:
        node *root_node = nullptr;
        int elements = 0;
};

#endif //STACK_H