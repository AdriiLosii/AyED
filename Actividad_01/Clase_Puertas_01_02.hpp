//Programa: Clase_Puertas_01.hpp
/*
Propósito:
    Cree dos nuevas clases de puertas, una llamada PuertaNOR y otra llamada PuertaNAND. Las puertas
    NAND funcionan como puertas AND que tienen una NOT conectada a la salida. Las puertas NOR
    funcionan como puertas OR que tienen una NOT conectada a la salida. Cree la clase XOR
Fecha:15/02/2022
Autores:Adrián Losada Álvarez y Gabriel Iglesias Sotelo
*/

#include <iostream>
#include <string>
using namespace std;

// creates a class with a logic gate that returns the label, and boolean value
class PuertaLogica
{
public:
    PuertaLogica(string n)
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


class PuertaBinaria : public PuertaLogica  //Permite la creacion de una puerta logica con dos entradas
{
public:
    PuertaBinaria(string n) : PuertaLogica(n)
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


class PuertaUnaria : public PuertaLogica   //Permite la creacion de una puerta logica con una entrada
{
public:
    PuertaUnaria(string n) : PuertaLogica(n)
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


class PuertaAND : public PuertaBinaria  //Clase que crea una puerta AND
{
public:
    PuertaAND(string n) : PuertaBinaria(n){};

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


class PuertaOR : public PuertaBinaria  //Clase que crea una puerta OR
{
public:
    PuertaOR(string n) : PuertaBinaria(n){};

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


class PuertaNOT : public PuertaUnaria  //Clase que crea una puerta NOT
{
public:
    PuertaNOT(string n) : PuertaUnaria(n){};

    virtual bool performGateLogic()
    {
        if (getPin())
            return false;
        else
            return true;
    }
};


class Conector   //Clase que establece la conexion logica entre dos puertas
{
public:
    Conector(PuertaLogica *fgate, PuertaLogica *tgate)
    {
        fromgate = fgate;
        togate = tgate;
        tgate->setNextPin(fromgate->getOutput());
    }
    PuertaLogica *getFrom()
    {
        return fromgate;
    }
    PuertaLogica *getTo()
    {
        return togate;
    }

private:
    PuertaLogica *fromgate, *togate;
};


class PuertaNOR : public PuertaBinaria   //Creamos una nueva clase que crea la puerta NOR
{
public:
    PuertaNOR(string n) : PuertaBinaria(n){};

    virtual bool performGateLogic()
    {
        bool a = getPinA();
        bool b = getPinB();
        if (a == 1 || b == 1)    //Puerta OR

            or_salida= true;
        else
            or_salida = false;

        if (or_salida == true)    //Puerta NOT, invierte la salida para crear la puerta correctamente
            return false;
        else
            return true;
    }

private:
    bool or_salida;  //Creamos una varuable auxiliar que nos guarda el resultado
};


class PuertaNAND : public PuertaBinaria   //Creamos una nueva clase que crea una puerta NAND
{
public:
    PuertaNAND(string n) : PuertaBinaria(n){};

    virtual bool performGateLogic()
    {
        bool a = getPinA();
        bool b = getPinB();
        if (a == 1 && b == 1)   //Puerta AND

            and_salida = true;
        else
            and_salida = false;

        if (and_salida == true)   //Puerta NOT, invierte la salida para crear la puerta correctamente
            return false;
        else
            return true;
    }

private:
    bool and_salida;   //Creamos una varuable auxiliar que nos guarda el resultado
};


class PuertaXOR : public PuertaBinaria  //Creamos una nueva clase que crea una puerta XOR
{
    public:
     PuertaXOR(string n) : PuertaBinaria(n){};

    virtual bool performGateLogic() 
    {
        bool a = getPinA();
        bool b = getPinB();
        if (a == b)            //Puerta XOR. Si ambas entradas son iguales devuelve un 0, sino un 1.

            return false;
        else
            return true;
    }
};