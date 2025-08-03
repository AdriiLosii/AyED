#include "Class_Colas_Prioridad.hpp"
using namespace std;

int main() {
   
    push(10,4);
    push(5,6);
    cout<<peek()<<endl;
    push(6, 0);
    push(2, 1);
    cout<<pop()<<endl;
    cout<<pop()<<endl;
    cout<<peek()<<endl;
    
    return 0;
}