//Programa: Ej11.cpp
/*
Propósito:
    Elabora estrategias alternativas para elegir el valor pivote en el ordenamiento rápido.
    Reimplementa el algoritmo y haz un Benchmark de las mismas en conjuntos de datos
    aleatorios. ¿Bajo qué criterios estas estrategias funcionan mejor o peor que la
    estrategia de los apuntes?
*/
//Autor: Gabriel Iglesias Sotelo y Adrián Losada Álvarez
//Fecha: 19/04/2022


//Incluimos las bibliotecas.
#include <iostream>
#include <vector>
#include <chrono> //Para usar el temporizador.
using namespace std::chrono;
using namespace std;


//Definimos las funciones creadas.
void print(int vector[], int tamano);
int particion_pivotePrimero(int vector[], int tamano, int primero, int ultimo);
void quickSort_pivotePrimero(int vector[], int tamano, int primero, int ultimo);

int particion_pivoteUltimo(int vector[], int tamano, int primero, int ultimo);
void quickSort_pivoteUltimo(int vector[], int tamano, int primero, int ultimo);

int particion_pivoteAleatorio(int vector[], int tamano, int primero, int ultimo);
void quickSort_pivoteAleatorio(int vector[], int tamano, int primero, int ultimo);

int particion_pivoteMediana(int vector[], int tamano, int primero, int ultimo);
void quickSort_pivoteMediana(int vector[], int tamano, int primero, int ultimo);
int encontrar_mediana(int vector[], int tamano, int primero, int ultimo);

void vector_aleatorio(int vector_analisis[], int i);


//Programa principal.
int main() {
    //Creamos un vector de enteros aleatorios:
    const int tamano = 20;
    int vector[tamano];
    int opcion;

    srand(time(0)); //Utilizamos la hora del sistema para que rand() no genere siempre los mismos números.
    //Rellenamos el array.
    for (int i = 0; i < tamano; i++)
    {
        vector[i] = 1 + rand() % (tamano*2);
    }

    //Mostramos el vector inicial.
    cout << "\nVector sin ordenar: "; print(vector, tamano);

    //Mostramos el menú.
    cout << "\n¿Qué variante de Quick Sort quieres usar?" << endl;
    cout << "\t1) Pivote = Primer valor." << endl;
    cout << "\t2) Pivote = Último valor." << endl;
    cout << "\t3) Pivote = Valor aleatorio." << endl;
    cout << "\t4) Pivote = Mediana de 3 valores." << endl;

    try //Lectura de datos validada.
    {
        cout << "\nOpcion: ";
        cin >> opcion;

        if (cin.fail())
        {
            cin.clear();
            throw 1;
        }

        switch (opcion)
        {
            case 1:
                //Llamamos a la función para ordenar el vector y lo mostramos.
                quickSort_pivotePrimero(vector, tamano, 0, tamano-1);
                cout << "Vector ordenado: "; print(vector, tamano);
                break;
               
            case 2:
                //Llamamos a la función para ordenar el vector y lo mostramos.
                quickSort_pivoteUltimo(vector, tamano, 0, tamano-1);
                cout << "Vector ordenado: "; print(vector, tamano);
                break;
                
            case 3:
                //Llamamos a la función para ordenar el vector y lo mostramos.
                quickSort_pivoteAleatorio(vector, tamano, 0, tamano-1);
                cout << "Vector ordenado: "; print(vector, tamano);
                break;

            case 4:
                //Llamamos a la función para ordenar el vector y lo mostramos.
                quickSort_pivoteMediana(vector, tamano, 0, tamano-1);
                cout << "Vector ordenado: "; print(vector, tamano);
                break;
                
            default: //Si se introduce un número mayor a 5.
                cout << "\nError, ha ocurrido algo inesperado.\n" << endl;
                cout << "Pulsa ENTER para finalizar.";
                cin.ignore();cin.ignore();
                return 0;
        }
    }
    catch(...) //Si hay algún problema en la lectura de datos.
    {
        cout << "\nError, ha ocurrido algo inesperado.\n" << endl;
        cout << "Pulsa ENTER para finalizar.";
        cin.ignore();cin.ignore();cin.ignore();
        return 0;
    }


    cout << "\nPulsa ENTER para comenzar el análisis.";
    cin.ignore();cin.ignore();

    ////////////////// ANALISIS //////////////////

    cout << "\n\t\t * Análisis: * \n";
    //Realizamos un test de velocidad para comprobar cual es la complejidad temporal de cada función.
    const int tamano_max = 9999;
    int vector_analisis[tamano_max];
    int ejecuciones = 0;
    auto microseg_totales_primero = 0;
    auto microseg_totales_ultimo = 0;
    auto microseg_totales_aleatorio = 0;
    auto microseg_totales_mediana = 0;

    cout << "T[microsegundos]" << endl;
    cout << "Tamaño vectores        T. primero        T. Ultimo        T. Aleatorio        T. Mediana" << endl; //Mostramos el tamaño de las listas y los tiempos de ejecución.
    for (int i = 1000; i < tamano_max + 1; i+=100)
    {
        //Creamos el vector.
        vector_aleatorio(vector_analisis, i);
        auto inicio_primero = high_resolution_clock::now(); //Iniciamos el cronómetro.
        quickSort_pivotePrimero(vector_analisis, i, 0, i-1); //Llamamos a la función.
        auto fin_primero = high_resolution_clock::now(); //Finalizamos el cronómetro.
        auto tiempo_primero= duration_cast<microseconds>(fin_primero-inicio_primero); //Calculamos el tiempo.
        microseg_totales_primero += tiempo_primero.count();

        //Creamos el vector.
        vector_aleatorio(vector_analisis, i);
        auto inicio_ultimo = high_resolution_clock::now(); //Iniciamos el cronómetro.
        quickSort_pivoteUltimo(vector_analisis, i, 0, i-1);; //Llamamos a la función.
        auto fin_ultimo = high_resolution_clock::now(); //Finalizamos el cronómetro.
        auto tiempo_ultimo = duration_cast<microseconds>(fin_ultimo-inicio_ultimo); //Calculamos el tiempo.
        microseg_totales_ultimo += tiempo_ultimo.count();

        //Creamos el vector.
        vector_aleatorio(vector_analisis, i);
        auto inicio_aleatorio = high_resolution_clock::now(); //Iniciamos el cronómetro.
        quickSort_pivoteAleatorio(vector_analisis, i, 0, i-1);; //Llamamos a la función.
        auto fin_aleatorio = high_resolution_clock::now(); //Finalizamos el cronómetro.
        auto tiempo_aleatorio = duration_cast<microseconds>(fin_aleatorio-inicio_aleatorio); //Calculamos el tiempo.
        microseg_totales_aleatorio += tiempo_aleatorio.count();

        //Creamos el vector.
        vector_aleatorio(vector_analisis, i);
        auto inicio_mediana = high_resolution_clock::now(); //Iniciamos el cronómetro.
        quickSort_pivoteMediana(vector_analisis, i, 0, i-1);; //Llamamos a la función.
        auto fin_mediana = high_resolution_clock::now(); //Finalizamos el cronómetro.
        auto tiempo_mediana = duration_cast<microseconds>(fin_mediana-inicio_mediana); //Calculamos el tiempo.
        microseg_totales_mediana += tiempo_mediana.count();

        ejecuciones += 1;

        //Mostramos los datos.
        cout << "      " << i << "                 " << tiempo_primero.count() << "               " << tiempo_ultimo.count() << "              " << tiempo_aleatorio.count() << "               " << tiempo_mediana.count() << endl;
    }

    //Conclusion.
    cout << "\nIMPORTANTE: En este benchmark no compararemos los tiempo entre funciones directamente, ya que cada función necesita operaciones distintas antes de realizar el Quick Sort." << endl;
    cout << "Por lo tanto, nos tendremos que fijar en la 'columna' de cada función y analizarla por separado." << endl;
    cout << "El objetivo de cada función es buscar un pivote mejor, para así evitar en mayor medida dividir el vector en una lista de 0 ítems y otra de tamaño n-1, n-2, etc... conviertiendo este método de ordenación en uno de orden O(n²)." << endl;
    cout << "Observando detenidamente las columnas por separado: " << endl;
    cout << "Pueden observarse algunas anomalías en los tiempos de ejecución de todas las funciones, esto se debe a lo mencionado anteriormente." << endl;
    cout << "Conclusión: En la primera y segunda columna pueden verse tiempo anómalos más a menudo que en la tercera o la cuarta, ya que en estas últimas el valor del pivote no es fijo," << endl;
    cout << "siendo menos probable el problema de elegir como valor pivote un elemento posicionado al principio o al final de la lista ordenada." << endl;

    //Finalizamos el programa.
    cout<< "\nPulsa ENTER para finalizar.";
    cin.ignore();
    return 0;
}

//Creamos la función que cree el vector del análisis.
void vector_aleatorio(int vector_analisis[], int tam)
{
    srand(time(0)); //Utilizamos la hora del sistema para que rand() no genere siempre los mismos números.
    //Rellenamos el array.
    for (int i = 0; i < tam; i++)
    {
        vector_analisis[i] = 1 + rand() % tam;
    }
}

//Creamos la función que muestra el array.
void print(int vector[], int tamano) 
{
    for (unsigned i=0; i < tamano; i++) 
        cout<<vector[i]<<" ";
    cout<<endl;
}


//Creamos la función que divide el array y hace los intercambios.
int particion_pivotePrimero(int vector[], int tamano, int primero, int ultimo) 
{
    int valor_pivote = vector[primero];
    int pos_izq = primero;
    int pos_der = ultimo;

    //Mientras que las marcas no se crucen.
    while(pos_izq < pos_der)
    {
        //Avanzamos la marca derecha mientras que el valor de la marca sea mayor que el valor del pivote.
        while(vector[pos_der] > valor_pivote)
            pos_der--;

        //Avanzamos la marca izquierda mientras que no se cruce con la derecha o el valor de la marca sea menor o igual que el valor del pivote.
        while(pos_izq < pos_der && vector[pos_izq] <= valor_pivote)
            pos_izq++;

        if (pos_izq < pos_der)
            swap(vector[pos_der], vector[pos_izq]);
    }
    swap(vector[pos_der], vector[primero]);

    return pos_der;
}

//Creamos la función recursiva que ordena el vector dado.
void quickSort_pivotePrimero(int vector[], int tamano, int primero, int ultimo) //QuickSort -> pivote = primer elemento del vector.
{
    int pos_particion;

    if (primero < ultimo)
    {
        pos_particion = particion_pivotePrimero(vector, tamano, primero, ultimo); //Obtenemos la posición por donde se dividirá el vector.

        quickSort_pivotePrimero(vector, tamano, primero, pos_particion-1); //Llamamos a la función para ordenar la mitad izquierda del vector.
        quickSort_pivotePrimero(vector, tamano, pos_particion+1, ultimo); //Llamamos a la función para ordenar la mitad derecha del vector.
    }
}


//Creamos la función que divide el array y hace los intercambios.
int particion_pivoteUltimo(int vector[], int tamano, int primero, int ultimo) 
{
    int valor_pivote = vector[ultimo];
    int pos_izq = primero - 1;

    //Recorremos con la marca derecha el vector de izquierda a derecha.
    for (int pos_der = primero; pos_der <= ultimo - 1; pos_der++)
    {
        if (vector[pos_der] <= valor_pivote) //Si el valor del elemento de la marca derecha es menor o igual que el valor del pivote.
        {
            pos_izq++; //Avanzamos con la marca izquierda.
            swap(vector[pos_izq], vector[pos_der]); //Intercambiamos los valores, de esta forma el valor menor que el pivote queda a la izquierda.
        }
    }
    swap(vector[pos_izq + 1], vector[ultimo]); //Intercambiamos los valores, siendo el primero el valor menor y el segundo el valor mayor.

    return pos_izq + 1;
}

//Creamos la función recursiva que ordena el vector dado.
void quickSort_pivoteUltimo(int vector[], int tamano, int primero, int ultimo) //QuickSort -> pivote = último elemento del vector.
{
    int pos_particion;

    if (primero < ultimo)
    {
        pos_particion = particion_pivoteUltimo(vector, tamano, primero, ultimo); //Obtenemos la posición por donde se dividirá el vector.

        quickSort_pivoteUltimo(vector, tamano, primero, pos_particion-1); //Llamamos a la función para ordenar la mitad izquierda del vector.
        quickSort_pivoteUltimo(vector, tamano, pos_particion+1, ultimo); //Llamamos a la función para ordenar la mitad derecha del vector.
    }
}


//Creamos la función que divide el array y hace los intercambios.
int particion_pivoteAleatorio(int vector[], int tamano, int primero, int ultimo)
{
    //Generamos un valor aleatorio entre el primer y último elemento del vector.
    srand(time(NULL));
    int aleatorio = primero + rand() % (ultimo - primero);

    swap(vector[aleatorio], vector[ultimo]); //Reposicionamos el pivote.
    int valor_pivote = vector[ultimo];
    int pos_izq = primero - 1;

    //Recorremos con la marca derecha el vector de izquierda a derecha.
    for (int pos_der = primero; pos_der <= ultimo - 1; pos_der++)
    {
        if (vector[pos_der] <= valor_pivote) //Si el valor del elemento de la marca derecha es menor o igual que el valor del pivote.
        {
            pos_izq++; //Avanzamos con la marca izquierda.
            swap(vector[pos_izq], vector[pos_der]); //Intercambiamos los valores, de esta forma el valor menor que el pivote queda a la izquierda.
        }
    }
    swap(vector[pos_izq + 1], vector[ultimo]); //Intercambiamos los valores, siendo el primero el valor menor y el segundo el valor mayor.

    return pos_izq + 1;
}

//Creamos la función recursiva que ordena el vector dado.
void quickSort_pivoteAleatorio(int vector[], int tamano, int primero, int ultimo) //QuickSort -> pivote = numero aleatorio entre primero y último.
{
    int pos_particion;

    if (primero < ultimo)
    {
        pos_particion = particion_pivoteAleatorio(vector, tamano, primero, ultimo); //Obtenemos la posición por donde se dividirá el vector.

        quickSort_pivoteAleatorio(vector, tamano, primero, pos_particion-1); //Llamamos a la función para ordenar la mitad izquierda del vector.
        quickSort_pivoteAleatorio(vector, tamano, pos_particion+1, ultimo); //Llamamos a la función para ordenar la mitad derecha del vector.
    }
}


//Creamos la función para encontrar la mediana de los 3 valores.
int encontrar_mediana(int vector[], int tamano, int primero, int ultimo)
{
    //Obtenemos la mediana de 3 elementos del array -> Primero, medio y ultimo.
    int medio = ultimo/2;
    int pos_mediana;

    if ((vector[primero] >= vector[medio] and vector[primero] <= vector[ultimo]) or (vector[primero] <= vector[medio] and vector[primero] >= vector[ultimo]))
        pos_mediana = primero;

    if ((vector[medio] >= vector[primero] and vector[medio] <= vector[ultimo]) or (vector[medio] <= vector[primero] and vector[medio] >= vector[ultimo]))
        pos_mediana = medio;

    if ((vector[ultimo] >= vector[primero] and vector[ultimo] <= vector[medio]) or (vector[ultimo] <= vector[primero] and vector[ultimo] >= vector[medio]))
        pos_mediana = ultimo;

    return pos_mediana;
}

//Creamos la función que divide el array y hace los intercambios.
int particion_pivoteMediana(int vector[], int tamano, int primero, int ultimo)
{
    int pos_mediana = encontrar_mediana(vector, tamano, primero, ultimo); //Obtenemos la posición de la mediana.
    swap(vector[pos_mediana], vector[ultimo]); //Reposicionamos el pivote.
    int valor_pivote = vector[ultimo];
    int pos_izq = primero - 1;

    //Recorremos con la marca derecha el vector de izquierda a derecha.
    for (int pos_der = primero; pos_der <= ultimo - 1; pos_der++)
    {
        if (vector[pos_der] <= valor_pivote) //Si el valor del elemento de la marca derecha es menor o igual que el valor del pivote.
        {
            pos_izq++; //Avanzamos con la marca izquierda.
            swap(vector[pos_izq], vector[pos_der]); //Intercambiamos los valores, de esta forma el valor menor que el pivote queda a la izquierda.
        }
    }

    swap(vector[pos_izq + 1], vector[ultimo]); //Intercambiamos los valores, siendo el primero el valor menor y el segundo el valor mayor.

    return pos_izq + 1;
}

//Creamos la función recursiva que ordena el vector dado.
void quickSort_pivoteMediana(int vector[], int tamano, int primero, int ultimo) //QuickSort -> pivote = mediana de 3 elementos.
{
    int pos_particion;

    if (primero < ultimo)
    {
        pos_particion = particion_pivoteMediana(vector, tamano, primero, ultimo); //Obtenemos la posición por donde se dividirá el vector.

        quickSort_pivoteMediana(vector, tamano, primero, pos_particion-1); //Llamamos a la función para ordenar la mitad izquierda del vector.
        quickSort_pivoteMediana(vector, tamano, pos_particion+1, ultimo); //Llamamos a la función para ordenar la mitad derecha del vector.
    }
}