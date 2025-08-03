#include "Class_Tablas_Hash.hpp"
int main() {
    HashTable h;

    h.put(54, "cat");
    h.put(26, "dog");
    h.put(93, "lion");
    h.put(17, "tiger");
    h.put(77, "bird");
    h.put(31, "cow");
    h.put(44, "goat");
    h.put(55, "pig");
    h.put(20, "chicken");
    cout<<h<<endl;

    h.put(20,"chicken");
    h.put(17,"tiger");
    h.put(20,"duck");
    cout<<h.get(20)<<endl;
    cout<<h.get(99)<<endl;

    return 0;
}
