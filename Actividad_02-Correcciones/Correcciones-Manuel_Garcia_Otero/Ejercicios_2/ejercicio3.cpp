#include <iostream>
#include <cmath>
#include <stack>
#include <string>
#include <vector>
using namespace std;



float toFloat(string x)
{
    float resultado;
    int decimales=0;
    bool punto = true;

    for (int i=x.length()-1; i>=0; i--)     //Bucle for. Cuenta los decimales del operando
    {
        if (x[i]=='.')
        {
            punto = false;
        }
        else if (punto)
        {
            decimales++;
        }
    }

    if (decimales==x.length())
    {
        decimales=0;
    }

    int i = x.length()-1;

    while (i>=0 && x[i]!='.')
    {   
        switch (x[i])
        {
        case ('0'):
            resultado += 0*(pow(10,-decimales));
            break;
        
        case ('1'):
            resultado += 1*(pow(10,-decimales));
            break;
        
        case ('2'):
            resultado += 2*(pow(10,-decimales));
            break;
        
        case ('3'):
            resultado += 3*(pow(10,-decimales));
            break;
        
        case ('4'):
            resultado += 4*(pow(10,-decimales));
            break;
        
        case ('5'):
            resultado += 5*(pow(10,-decimales));
            break;
        
        case ('6'):
            resultado += 6*(pow(10,-decimales));
            break;

        case ('7'):
            resultado += 7*(pow(10,-decimales));
            break;

        case ('8'):
            resultado += 8*(pow(10,-decimales));
            break;

        case ('9'):
            resultado += 9*(pow(10,-decimales));
            break;
        
        default:
            break;
        }

        decimales--;
        i--;
    }

    decimales++;

    while (i>=0)
    {   
        switch (x[i])
        {
        case ('0'):
            resultado += 0*(pow(10,-decimales));
            break;
        
        case ('1'):
            resultado += 1*(pow(10,-decimales));
            break;
        
        case ('2'):
            resultado += 2*(pow(10,-decimales));
            break;
        
        case ('3'):
            resultado += 3*(pow(10,-decimales));
            break;
        
        case ('4'):
            resultado += 4*(pow(10,-decimales));
            break;
        
        case ('5'):
            resultado += 5*(pow(10,-decimales));
            break;
        
        case ('6'):
            resultado += 6*(pow(10,-decimales));
            break;

        case ('7'):
            resultado += 7*(pow(10,-decimales));
            break;

        case ('8'):
            resultado += 8*(pow(10,-decimales));
            break;

        case ('9'):
            resultado += 9*(pow(10,-decimales));
            break;
        
        default:
            break;
        }

        decimales--;
        i--;
    }

    return resultado;
}

void showstack(stack<string> s)
{
    while (!s.empty())
    {
        cout << s.top() << '\t';
        s.pop();
    }
    cout << '\n';
}

int main()
{       
    stack<string> stack;

    string expresion = "123 2.5 3.1 4 5 * + * +";
    string operando;
    int elementos=0;

    vector<string> vector_expresion;

    for (int i=0; i<expresion.length(); i++)
    {
        if (expresion[i] != ' ' && expresion[i] != '+' && expresion[i] != '+' && expresion[i] != '-' && expresion[i] != '*' && expresion[i] != '/')
        {
            operando.push_back(expresion[i]);
        }
        else if (expresion[i] == ' ' && operando!="")
        {
            vector_expresion.push_back(operando);
            operando = "";
            elementos++;
        }
        else if (expresion[i]!=' ')
        {
            switch (expresion[i])
            {
                case ('+'):
                    vector_expresion.push_back("+");
                    break;
                case ('-'):
                    vector_expresion.push_back("-");
                    break;
                case ('*'):
                    vector_expresion.push_back("*");
                    break;
                case ('/'):
                    vector_expresion.push_back("/");
                    break;
                default:
                    break;
            }
            
            elementos++;
            
        }
        
    }

    vector_expresion.push_back("tapa");

    cout<<"Expresión en forma de array:"<<endl<<"[ ";

    for (int i=0; i<vector_expresion.capacity(); i++)
    {
        cout<<vector_expresion[i]<<" ";
    }

    
    cout<<" ]"<<endl<<endl<<"Elementos: "<<elementos<<endl<<endl;

    

    for (int i=0; i<elementos; i++)
    {
        if (vector_expresion[i]!="+" && vector_expresion[i]!="-" && vector_expresion[i]!="*" && vector_expresion[i]!="/")
        {
            stack.push(vector_expresion[i]);
            cout<<"STACK: ";
            showstack(stack);
        }
        if (vector_expresion[i]=="+")
        {
            stack.push(vector_expresion[i]);
            cout<<"STACK: ";
            showstack(stack);
            stack.pop();

            float penultimo = toFloat(stack.top());     stack.pop();
            float antepenultimo = toFloat(stack.top());     stack.pop();
            float total = antepenultimo+penultimo;
            stack.push(to_string(total));
            cout<<"STACK: ";
            showstack(stack);
        }
        else if (vector_expresion[i]=="-")
        {
            stack.push(vector_expresion[i]);
            cout<<"STACK: ";
            showstack(stack);
            stack.pop();

            float penultimo = toFloat(stack.top());     stack.pop();
            float antepenultimo = toFloat(stack.top());     stack.pop();
            float total = antepenultimo-penultimo;
            stack.push(to_string(total));
            cout<<"STACK: ";
            showstack(stack);
        }
        else if (vector_expresion[i]=="*")
        {
            stack.push(vector_expresion[i]);
            cout<<"STACK: ";
            showstack(stack);
            stack.pop();

            float penultimo = toFloat(stack.top());     stack.pop();
            float antepenultimo = toFloat(stack.top());     stack.pop();
            float total = antepenultimo*penultimo;
            stack.push(to_string(total));
            cout<<"STACK: ";
            showstack(stack);
        }
        else if (vector_expresion[i]=="/")
        {
            stack.push(vector_expresion[i]);
            cout<<"STACK: ";
            showstack(stack);
            stack.pop();

            float penultimo = toFloat(stack.top());     stack.pop();
            float antepenultimo = toFloat(stack.top());     stack.pop();
            float total = antepenultimo/penultimo;
            stack.push(to_string(total));
            cout<<"STACK: ";
            showstack(stack);
        }
    }
}