//Programa: Ej01.cpp
/*
Propósito:
    Convierte las siguientes expresiones infijas a expresiones prefijas (usa el método de
    agrupar completamente) y evaluarlas dando valores a los operandos:
        (A+B)*(C+D)*(E+F)
        A+((B+C)*(D+E))
        A*B*C*D+E+F
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 11/03/2022

//Incluimos las bibliotecas.
#include <iostream>
#include <stack>
#include <string>
#include <cstring>
#include <cmath>

using namespace std;

//Definimos las funciones creadas.
stack<char> prefijo(string infijo);
void mostrar_pila(stack<char> prefijo);
int operar_prefijo(stack<char> prefijo);
int opera(char operador, int operando1, int operando2);

int main(){

    //Definimos las formas infijas.
    //////  MODIFICA A CONTINUACIÓN LOS VALORES DE A,B,C... (SOLO NÚMEROS INT DE 1 CIFRA)   //////
    string infijo_1 = "(1+2)*(3+4)*(5+6)"; //(A+B)*(C+D)*(E+F)
    string infijo_2 = "1+((2+3)*(4+5))"; //A+((B+C)*(D+E))
    string infijo_3 = "1*2*3*4+5+6"; //A*B*C*D+E+F

    stack<char> prefijo_1 = prefijo(infijo_1); //Llamamos a la función para convertir la forma infija a prefija.
    mostrar_pila(prefijo_1); //Llamamos a la función para mostrar la forma prefija 1.
    cout << " = " << operar_prefijo(prefijo_1) << endl; //Llamamos a la función para operar la forma prefija 1.

    stack<char> prefijo_2 = prefijo(infijo_2); //Llamamos a la función para convertir la forma infija a prefija.
    mostrar_pila(prefijo_2); //Llamamos a la función para mostrar la forma prefija 2.
    cout << " = " << operar_prefijo(prefijo_2) << endl; //Llamamos a la función para operar la forma prefija 2.

    stack<char> prefijo_3 = prefijo(infijo_3); //Llamamos a la función para convertir la forma infija a prefija.
    mostrar_pila(prefijo_3); //Llamamos a la función para mostrar la forma prefija 3.
    cout << " = " << operar_prefijo(prefijo_3) << endl; //Llamamos a la función para operar la forma prefija 3.

    //Finalizamos el programa.
    cout<<("Pulsa ENTER para finalizar");
    cin.get();
    return 0;
}

//Creamos la función.
stack<char> prefijo(string infijo){
    //Definimos las variables.
    string invertido = "";
    stack<char> auxiliar;
    stack<char> pila_prefija;
    stack<char> pila_operadores;
    string nums_letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    string op = "+*-/^)";

    //Invertimos el orden de la string "infijo"
    for (char i : infijo)
    {
        auxiliar.push(i);
    }

    while (!auxiliar.empty())
    {
        invertido = invertido + auxiliar.top();
        auxiliar.pop();
    }

    //Recorremos la forma infija de derecha a izquierda.
    for (char caracter : invertido)
    {
        if (nums_letras.find(caracter) <= nums_letras.length()) //Si el carácter actual de la pila está en "nums_letras".
            pila_prefija.push(caracter); //Añadimos el operando a la lista de la forma prefija.
            
        else if (op.find(caracter) <= op.length()) //Si el carácter actual de la pila está en "op".
            pila_operadores.push(caracter); //Añadimos el operador a la pila de operadores.
            
        else if (caracter == '(')
        {
            while (pila_operadores.top() != ')'){ //Mientras que en la pila no se llega al paréntesis que cierra:
                pila_prefija.push(pila_operadores.top()); //Añadimos el operador a la pila de la forma prefija.
                pila_operadores.pop(); //Eliminamos el operador de la pila de los operadores.
            }
            pila_operadores.pop(); //Eliminamos el paréntesis que cierra de la lista de los operadores.
        }
        else if (caracter == ' ') //Si hay espacios en blanco, los ignoramos.
            continue;
        else
        {
            printf("\033c"); //Borramos la pantalla
            cout << "\nError, ha ocurrido algo inesperado.\n" << endl;
            exit (-1); //Finalizamos el programa.
        }
    }    

    //Vaciamos la pila de los operadores (si es que queda alguno), añadiéndolos a la pila prefija.
    while (!pila_operadores.empty()){
        pila_prefija.push(pila_operadores.top());
        pila_operadores.pop();
    }

    return pila_prefija; //Devolvemos la pila de la forma prefija al programa principal.
}

//Creamos la función.
void mostrar_pila(stack<char> prefijo){
    stack<char> auxiliar = prefijo; //Creamos una pila auxiliar para no modificar la original.

    while (!auxiliar.empty()) //Mientras la lista no está vacía.
    {
        cout << auxiliar.top(); //Mostramos el último elemento añadido a la pila.
        auxiliar.pop(); //Eliminamos el último elemento añadido a la pila
    }
}

//Creamos la función.
int operar_prefijo(stack<char> prefijo){
    //Definimos las variables.
    stack<int> operadores;
    stack<char> invertida;
    string nums_letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    //Rellenamos la lista "invertida" con la pila "prefijo" dada la vuelta.
    while (!prefijo.empty())
    {
        invertida.push(prefijo.top());
        prefijo.pop();
    }

    //Realizamos las operaciones
    while (!invertida.empty())
    {
        if (nums_letras.find(invertida.top()) <= nums_letras.length())
        {
            operadores.push(int(invertida.top() - 48)); //Pasamos de char a int con "int()" y después le restamos 48 para obtener el valor entero real.
            invertida.pop();
        }
        else
        {
            //Guardamos el valor del segundo operando en una variable y lo eliminamos de la pila.
            int operando2 = operadores.top();
            operadores.pop();

            //Guardamos el valor del primer operando en una variable y lo eliminamos de la pila.
            int operando1 = operadores.top();
            operadores.pop();

            //Llamamos a la función para que realice la operación correspondiente según el operador encontrado, guardamos el resultado en la pila de resultados y borramos el operador de la expresión.
            int resultado = opera(invertida.top(), operando1, operando2);
            operadores.push(resultado);
            invertida.pop();
        }
    }

    return operadores.top(); //Devolvemos el último valor restante de la pila, es decir, el resultado final.
}

//Creamos la función.
int opera(char operador, int operando1, int operando2)
{
    //Realiza las operaciones dependiendo del operador que se encuentre.
    if (operador == '*')
        return (operando1 * operando2);
    else if (operador == '/')
        return (operando1 / operando2);
    else if (operador == '+')
        return (operando1 + operando2);
    else
        return (operando1 - operando2);
}