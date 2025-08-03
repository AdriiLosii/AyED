//ClasesC_12.cpp  Ejemplo de utilización de clase
#include <iostream>
#include <ostream>
#include <cstring>
#include <vector>

class Persona
{
private:
    std::string nombre;
    int edad;

public:
    static const int max_edad;
    Persona(){}; // El constructor y el destructor no hacen nada.
    ~Persona(){};
    const std::string &dev_nombre(void) const { return nombre; };
    /*
    Devolvemos una referencia esta función, al estar declarada completamente en la declaración de la clase, se considera inline.
    El "const" extra impide que el código que haya dentro de este método modifique el objeto al que pertenece.
    */
    const int dev_edad(void) const;
    void pon_edad(const int &x)
    {
        if (x <= max_edad)
            edad = x;
    };

    void pon_nombre(const std::string &x) { nombre = x; };
    /*
        Paso de parámetro por referencia para que sea más rápido le añadimos el const 
        para que a pesar de ser por referencia no pueda ser modificado dentro de la función.
    */

    friend std::ostream &operator<<(std::ostream &of, Persona &x);
};

// Este método se declara fuera de la clase pero se le indica que va a ser inline.
inline const int Persona::dev_edad(void) const
{
    return edad;
}

std::ostream &operator<<(std::ostream &of, Persona &x)
{
    of << x.nombre << ' ' << x.edad << std::endl;
    return of;
};

const int Persona::max_edad = 130; // Inicialización de una constante. Debe hacerse fuera de la clase
typedef std::vector<Persona> Vect_personas;
using namespace std;

int main(void)
{
    Vect_personas agenda;
    Persona aux;
    string nombre;
    int edad;
    do
    {
        cout << "\nIntroduzca nombre: - FIN terminar - " << endl;
        cin >> nombre;
        cout << "\nIntroduzca edad: " << endl;
        cin >> edad;
        aux.pon_nombre(nombre);
        aux.pon_edad(edad);
        agenda.push_back(aux);

    } while (nombre != "FIN");
    cout << endl;
    for (unsigned int n = 0; n < agenda.size() - 1; n++)
        // n sólo vive durante el bucle
        cout << "Nombre: " << agenda[n].dev_nombre() << "\nEdad: " << agenda[n].dev_edad() << endl;
    // o también, utilizando el op sobrecargado <<, cout << agenda[n] << endl;
}