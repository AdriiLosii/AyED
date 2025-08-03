//Programa: Clase_Hora_06.hpp
/*
Propósito:
    Implementar la clase de uso común Clase Hora, de manera que sea robusta y completarla con 
    métodos necesarios
*/ 
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 19/02/2022


#include <iostream>
using namespace std;

class Hora
{
    public:
        Hora(int horas_int, int min_int, int seg_int)
        {
            try{

                horas = horas_int;
                while (horas < 0 or horas > 23){
                    cout << "Introduzca la hora (formato 24h): " << endl;
                    cin >> horas;

                    if (cin.fail())
                    {
                        cin.clear();
                        throw 1;
                    }
                }
                

                min = min_int;
                while (min < 0 or min > 59){
                    cout << "Introduzca los minutos: " << endl;
                    cin >> min;

                    if (cin.fail())
                    {
                        cin.clear();
                        throw 1;
                    }
                }
                

                seg = seg_int;
                while (seg < 0 or seg > 59){
                    cout << "Introduzca los segundos: " << endl;
                    cin >> seg;

                    if (cin.fail())
                    {
                        cin.clear();
                        throw 1;
                    }
                }
            }
            catch (...){
                cout << "\nError, introduzca una hora válida." << endl;
                cout << "Pulse ENTER para finalizar." << endl;
                cin.ignore();
                exit(-1);
            }
        }

        bool operator==(Hora &otra_fecha){
            return (horas == otra_fecha.horas and min == otra_fecha.min and seg == otra_fecha.seg);
        }

        bool operator!=(Hora &otra_fecha){
            return (horas != otra_fecha.horas and min != otra_fecha.min and seg != otra_fecha.seg);
        }

        bool operator>(Hora &otra_fecha){
            if (horas > otra_fecha.horas)
                return true;
            else{
                if (horas == otra_fecha.horas and min > otra_fecha.min)
                    return true;
                else{
                    if (horas == otra_fecha.horas and min == otra_fecha.min and seg > otra_fecha.seg)
                        return true;
                    else
                        return false;
                }
            }
        }

        bool operator<(Hora &otra_fecha){
            if (horas < otra_fecha.horas)
                return true;
            else{
                if (horas == otra_fecha.horas and min < otra_fecha.min)
                    return true;
                else{
                    if (horas == otra_fecha.horas and min == otra_fecha.min and seg < otra_fecha.seg)
                        return true;
                    else
                        return false;
                }
            }
        }

        friend ostream &operator<<(ostream &stream, const Hora &hora_completa);

    private:
        int seg, min, horas;
};

ostream &operator<<(ostream &stream, const Hora &hora_completa)
{
    stream << hora_completa.horas << ":" << hora_completa.min << ":" << hora_completa.seg;

    return stream;
}