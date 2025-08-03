#include "Class_Puertas.hpp"
int main()
{
    char stopme;

    //Setting labels
    AndGate gand1(" AND1 ");
    AndGate gand2(" AND2 ");
    OrGate gor3(" OR ");
    NotGate gnot4(" NOT ");

    // The inputs can be changed here!
    gand1.setNextPin(0);
    gand1.setNextPin(0);
    gand2.setNextPin(1);
    gand2.setNextPin(1);

    //making comnnections
    Connector c1(&gand1, &gor3);
    Connector c2(&gand2, &gor3);
    Connector c3(&gor3, &gnot4);

    // The output shows order of operators
    cout << gnot4.getLabel() << "(";
    cout << "(" << gand1.getPinA() << gand1.getLabel() << gand1.getPinB() << ")";
    cout << gor3.getLabel();
    cout << "(" << gand2.getPinA() << gand2.getLabel() << gand2.getPinB() << ")";
    cout << ") results in " << gnot4.getOutput() << endl;

    cin >> stopme; //holds open window under some conditions.
    return 0;
}
