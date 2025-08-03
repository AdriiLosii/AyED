//ClasesC_10.cpp
#include <string>
class Persona {
    public:
    Persona() {}; // Este constructor no hace nada.
    Persona(std::string &x, int ed = 0) : nombre(x), edad(ed) {};
        // Este constructor acepta un nombre o un nombre y una edad, e incializa nombre y edad con esos datos.
        // El cuerpo del constructor está vacío.
    ~Persona() {}; // El destructor no precisa hacer nada pq no hay nada que liberar. Suele utilizarse el destructor para liberar memoria que haya sido reservada dentro del objeto.
    std::string nombre;
    int edad;
};