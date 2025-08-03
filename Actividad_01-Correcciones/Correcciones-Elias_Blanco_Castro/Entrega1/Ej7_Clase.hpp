#include <iostream>
#include <math.h>
using namespace std;

class Polinomio {
public:
    Polinomio();
    Polinomio(const Polinomio& p);
    Polinomio(int n, double []);
    int getOrden()const;
    double getCoef(int p)const;
    double* calcular(int limite);
    double evaluar (double) const;
    ~Polinomio(void);
    Polinomio& operator= (const Polinomio& p);
    Polinomio operator+ (const Polinomio&) const;
    Polinomio& operator+= (const Polinomio& p);
    bool operator< (const Polinomio& p) const;
    bool operator== (const Polinomio& p);
    friend ostream& operator<< (ostream& o, const Polinomio& p);
    friend Polinomio operator- (const Polinomio& p);
private:
    int orden;
    double *coef;
};

Polinomio::Polinomio(int n, double *v)
{
    orden=n;
    coef=new double[n+1];
    for(int i=0;i<(n+1);i++)
        coef[i]=v[i];
}
Polinomio::Polinomio(){ coef = 0;}
Polinomio::Polinomio(const Polinomio& p)
{
    orden = p.orden;
    coef = new double[orden+1];
    for(int i=0;i<orden+1;i++)
        coef[i]=p.coef[i];
}
int Polinomio::getOrden()const
{
return orden;
}
double Polinomio::getCoef(int n) const
{
return coef[n];
}
double Polinomio::evaluar(double d) const{
    double res = 0;
    for(int i = 0; i < orden + 1; i++)
        res += pow(d, i) * coef[i];
    return res;
}
bool Polinomio::operator< (const Polinomio& p) const {
    return this->evaluar(0.0) < p.evaluar(0.0);
}
double* Polinomio::calcular(int limite)
{
    double *p=new double[limite+1];
    double suma;
    for(int i=0;i<=limite;i++){
        suma=0;
        for(int j=0;j<=orden;j++)
            suma+=pow((double)i,j)*coef[j];
        p[i]=suma;
}
    return p;
}
Polinomio::~Polinomio(void)
{
    delete[] coef;
}
//Comprobar si son iguales
Polinomio& Polinomio::operator= (const Polinomio& p)
{
    if(this == &p) return *this;
    delete[] coef;
    coef = new double[p.orden + 1];
    for(int i=0;i<p.orden+1;i++)
        this->coef[i]=p.coef[i];
    this->orden = p.orden;
    return *this;
}
Polinomio& Polinomio::operator+= (const Polinomio& p)
{
    *this = *this + p;
    return *this;
}
//Comprobar si los polinomios son iguales
bool Polinomio::operator== (const Polinomio& p)
{
    if(this->orden != p.orden) return false;
    int i = 0;
    while((coef[i] == p.coef[i]) && (i < orden + 1)) i++;
    return (i == orden+1);
}
//Suma de polinomios
Polinomio Polinomio::operator+ (const Polinomio& p) const {
    int sum_ord = this->orden > p.orden ? this->orden : p.orden;
    int ordenMin = this->orden < p.orden ? this->orden : p.orden;
    double * sum_coef = new double [sum_ord + 1];
    for (int i = 0; i < ordenMin + 1; i++) sum_coef[i] = this->coef[i] + p.coef[i];
    for (int i = ordenMin + 1; i < sum_ord + 1; i++)
        sum_coef[i] = this->orden > p.orden ? this->coef[i] : p.coef[i];
    int i = sum_ord;
    while(abs(sum_coef[i--]) < 1e-5) sum_ord--;
    return Polinomio(sum_ord, sum_coef);
}
//Resta de polinomios
Polinomio operator- (const Polinomio& p) {
    double * c = new double(p.getOrden() + 1);
    for (int i = 0; i < p.getOrden() + 1; i++)
        c[i] = -p.getCoef(i);
    return Polinomio(p.getOrden(), c);
}
ostream& operator<< (ostream& o, const Polinomio& p) {
    for (int i = p.orden; i > 0; i--)
        o << p.coef[i] << "x^" << i << " + ";
    o << p.coef[0];
    return o;
}
