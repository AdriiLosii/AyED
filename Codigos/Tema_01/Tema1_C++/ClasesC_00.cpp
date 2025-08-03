operator operador
// Sobrecarga de operadores aritméticos y de asignación
class Punto
{
  //...
  public:
    //...
    Punto operator * (const Punto &p); 
    Punto operator / (const Punto &p); 
    Punto operator += (const Punto &p);
    //...
};
//implementación de función miembro sobrecargada p1*p2

inline Punto Punto::operator * (const Punto& p)
{
  return Punto (x * p.x, y * p.y, z * p.z);
}
//p1/p2
