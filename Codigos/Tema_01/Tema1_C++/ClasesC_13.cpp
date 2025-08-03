//ClasesC_13.cpp  Ejemplo de utilización de claseA
class Pareja
{
    // atributos
    double a, b;
public:
    // métodos
    double getA();
    double getB();    
    void   setA(double n);
    void   setB(double n);
};

// implementación de los métodos de la clase Pareja
//
double Pareja::getA() { return a; }
double Pareja::getB() { return b; }
void Pareja::setA(double n) { a = n; }
void Pareja::setB(double n) { b = n; }
//Subclase Suma 
class Suma : public Pareja
{
    // atributos de Suma
    double resultado;
public:
    // métodos de Suma
    double calcular();
};
// implementación de Suma
double Suma::calcular() 
{ 
    return getA() + getB(); 
}