//ClasesC_09.cpp Ejemplo de utilización de estructuras 
#include <iostream>
#include <vector>
struct Persona {
    std::string nombre;
    int edad;
};

typedef std::vector<Persona> Vect_personas;
using namespace std;
int main(void)
{
    Vect_personas agenda;
    Persona aux;
    do {
        cout << "\nIntroduzca nombre: - FIN terminar - " << endl;
        cin >> aux.nombre;
        cout << "\nIntroduzca edad: " << endl;
        cin >> aux.edad;
        agenda.push_back(aux);
    } while(aux.nombre!="FIN");

    cout << endl;
    for (unsigned int n = 0; n<agenda.size()-1; n++)
        // n sólo vive durante el bucle
        cout << "Nombre: " << agenda[n].nombre << "\nEdad: " << agenda[n].edad << endl;
}