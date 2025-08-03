#include<bits/stdc++.h> 
using namespace std;
// class representing a tree node
class Node {
    public:
    int data;
    int priority;
    Node *next;
    
    Node(int d, int p) {
        data = d;
        priority = p;
        next = NULL;
    }
};
// function to create a new node
Node* newNode(int x, int p) {
    Node *node = new Node(x, p);
    return node;
}
// Variable representing the head of linked list
Node *head = NULL;
void push(int x, int p) {
    // Create a new node
    Node *node = newNode(x, p);
    
    // If head is null, this is the first node to be added
    // so make head = newNode
    if (head == NULL) {
        head = node;
        return;
    }
    
    Node *temp = head;
    Node *prev = NULL;
    
    // search for first node having priority less than p
    while (temp != NULL && temp->priority > p) {
        prev = temp;
        temp = temp->next;
    }
    
    if (temp == NULL) {
        // no node with priority less than this node (Case 1)
        prev->next = node;
    } else {
        if (prev == NULL) {
            // all the nodes have priority less than p (Case 2)
            // add this node at the starting
            node->next = head;
            head = node;
        } else {
            // Case 3
            // add this node before the node with priority less than p
            node->next = temp;
            prev->next = node;
        }
    }
}
int pop() {
    // head of the linked list contains the maximum priority element
    if (head != NULL) {
        int data = head->data;
        // removing the highest priority element
        head = head->next;
        return data;
    }
    return -1;
}
int peek() {
    // head of the linked list contains the maximum priority element
    if (head != NULL) {
        return head->data;
    }
    return -1;
}
