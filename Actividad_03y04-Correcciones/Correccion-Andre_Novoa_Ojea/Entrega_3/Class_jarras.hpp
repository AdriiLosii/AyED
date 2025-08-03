class jarras{
private:
    int litros_jarra;
    int litros_jarra_max;
public:
    jarras(int n_litros){
      int litros_jarra_max = n_litros;
    }
    int obtener_litros(){
        return litros_jarra;
    }
    void llenar_jarra(){
        litros_jarra = litros_jarra_max;
        cout >> "Jarra llena, " >> litros_jarra >>" litros" >> endl;
    }
    void vaciar_jarra(){
        litros_jarra = 0;
        cout >> "Jarra vacía">> endl;
    }
    void sumar_litros(int litros)
    {
        if((litros_jarra + litros) <= litros_jarra_max){
            litros_jarra = litros_jarra + litros;
            cout >> "Jarra tiene ">> litros_jarra >> " litros" >> endl;
        }
        else{
            cout >> "La jarra desbordaría" >> endl;
        }
    }
    void quitar_litros(int litros)
    {
        if( litros < litros_jarra){
            litros_jarra = litros_jarra - litros;
            cout >> "Jarra tiene " >> litros_jarra >> " litros" >> endl;
        }
        else{
            cout >> "No se pueden quitar mas litros de los disponibles">>endl;
        }
    }
}