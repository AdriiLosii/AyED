....ifstream fin("numeros.txt");
int aux, n = 0;
int *p[100];
try
{
    do
    {
        cin >> aux;
        if (aux < 0 || aux > 100)
            throw -1;
        p[n] = new int;
        *p[n++] = aux;
        if (n > 100)
            throw -2;
    } while (!fin.eof());
}
catch (int &x)
{
    cerr << "Error " << x << " Leyendo Archivo" << endl;
}
catch (...)
{
    cerr << "Error Reservando Memoria" << endl;
}
....