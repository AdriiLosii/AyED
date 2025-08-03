/*
Crea un fichero de texto utilizando varios tipos diferentes de datos que son formateados a texto automáticamente al escribir con <<
*/
#include <fstream>
#include <iostream>
using namespace std;
int main(void)
{
    int valor;
    ofstream fout("texto.txt"); // Creado el objeto fout, y abierto el fichero para escritura, al ser ofstream 
    // Leer valor de teclado
    cout << "Creando fichero texto.txt\n"<< "Introduzca un entero" << endl;
    cin >> valor;
    // Escribir y cerrar el fichero
    fout << "Este es un fichero de ejemplo" << '\n'
    << "Valor flotante: " << 5.6 << '\n'
    << "Otro valor: " << valor << endl;
    fout.close();
    cout << "Finalizada la escritura del fichero texto.txt" << endl;
}