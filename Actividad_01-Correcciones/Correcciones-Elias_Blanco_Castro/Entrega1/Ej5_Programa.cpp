#include <cstdlib>
#include <iostream>
using namespace std;

class Fecha {

    private:

    int dia, mes, ano;

    bool fechavalida(int ndia, int nmes, int nano){

        if(ndia<1 || ndia>31) return false;

        else if (nmes<1 || nmes>12) return false;

        else switch(nmes)

        {

            case 4: case 6: case 9: case 11:

                if(ndia>30) return false;

                break;

            case 2:

                if (ndia>28)return false;

                break;

        }

        return true;

    }

    public:

    Fecha (int d=0, int m=0, int a=0) {

        // Constructor

        if(fechavalida(d,m,a)){

            dia=d; mes=m; ano=a;

        } else {

            cout<<"ERROR: Se trato de introducir fecha incorrecta"<<endl;

        }

    }

    int damedia(void){

        return dia;

    }

 

    int damemes(void){

        return mes;

    }

 

    int dameano(void){

        return ano;

    }

 

    void imprimefecha(void){

        cout<<damedia()<< "-" << damemes()<<"-" << dameano()<< endl;

    }

 

    void guardarfecha(int d=0, int m=0, int a=0){

        if(fechavalida(d,m,a)) {

            dia=d; mes=m; ano=a;

        } else {

            cout<<"ERROR: Introducir fecha incorrecta"<<endl;

        }

    }

};
int main(int argc, char *argv[])

{

    int dia_aux, ano_aux, mes_aux;

    Fecha diaA(20,4,2006), diaB(1,1,0); //Fecha de referencia

    cout <<endl<< "Introduzca dia: ";

    cin >> dia_aux;

    cout <<endl<< "Introduzca mes: ";

    cin >> mes_aux;

    cout <<endl<< "Introduzca ano: ";

    cin >> ano_aux;

    diaA.guardarfecha(dia_aux,mes_aux,ano_aux);

    cout<<"Fecha introducida: ";

    diaA.imprimefecha();

}