#include <iostream>
#include <string>
using namespace std;

// creates a class with a logic gate that returns the label, and boolean value
class LogicGate
{
public:
    LogicGate(string n)
    {
        label = n;
    }
    string getLabel()
    {
        return label;
    }
    bool getOutput()
    {
        output = performGateLogic();
        return output;
    }
    virtual bool performGateLogic()
    {
        cout << "ERROR! performGateLogic BASE" << endl;
        return false;
    }

    virtual void setNextPin(bool source)
    {
        cout << "ERROR! setNextPin BASE" << endl;
    }

private:
    string label;
    bool output;
};

//class that allows for the gates to have two inputs
class BinaryGate : public LogicGate
{
public:
    BinaryGate(string n) : LogicGate(n)
    {
        pinATaken = false;
        pinBTaken = false;
    }
    bool getPinA()
    {
        if (pinATaken == false)
        {
            cout << "Enter Pin A input for gate " << getLabel() << ": ";
            cin >> pinA;
            pinATaken = true;
        }
        return pinA;
    }
    bool getPinB()
    {
        if (pinBTaken == false)
        {
            cout << "Enter Pin B input for gate " << getLabel() << ": ";
            cin >> pinB;
            pinBTaken = true;
        }
        return pinB;
    }
    virtual void setNextPin(bool source)
    {
        if (pinATaken == false)
        {
            pinA = source;
            this->pinATaken = true;
        }
        else if (pinBTaken == false)
        {
            pinB = source;
            this->pinBTaken = true;
        }
    }

private:
    bool pinA, pinATaken, pinB, pinBTaken;
};

//allows for the creation of a logic gate with  one input
class UnaryGate : public LogicGate
{
public:
    UnaryGate(string n) : LogicGate(n)
    {
        pinTaken = false;
    }
    bool getPin()
    {
        if (pinTaken == false)
        {
            cout << "Enter Pin input for gate " << getLabel() << ": ";
            cin >> pin;
            pinTaken = true;
        }
        return pin;
    }
    virtual void setNextPin(bool source)
    {
        if (pinTaken == false)
        {
            pin = source;
            pinTaken = true;
        }
        else
            return;
    }

private:
    bool pin, pinTaken;
};

//Class that sets up the logic for an "and" gate
class AndGate : public BinaryGate
{
public:
    AndGate(string n) : BinaryGate(n){};

    virtual bool performGateLogic()
    {
        bool a = getPinA();
        bool b = getPinB();
        if (a == 1 && b == 1)
            return true;
        else
            return false;
    }
};

//class that sets up the logic for an "or" gate
class OrGate : public BinaryGate
{
public:
    OrGate(string n) : BinaryGate(n){};

    virtual bool performGateLogic()
    {
        bool a = getPinA();
        bool b = getPinB();
        if (a == 1 || b == 1)
            return true;
        else
            return false;
    }
};

//class that sets up the logic for a "not" gate
class NotGate : public UnaryGate
{
public:
    NotGate(string n) : UnaryGate(n){};

    virtual bool performGateLogic()
    {
        if (getPin())
            return false;
        else
            return true;
    }
};

// class that sets up logic for the connection of one gate to another
class Connector
{
public:
    Connector(LogicGate *fgate, LogicGate *tgate)
    {
        fromgate = fgate;
        togate = tgate;
        tgate->setNextPin(fromgate->getOutput());
    }
    LogicGate *getFrom()
    {
        return fromgate;
    }
    LogicGate *getTo()
    {
        return togate;
    }

private:
    LogicGate *fromgate, *togate;
};
