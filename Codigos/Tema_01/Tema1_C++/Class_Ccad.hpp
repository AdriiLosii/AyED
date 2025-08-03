// Class_Ccad.hpp
class Ccad
{
private:
    char *pDatos;
    int nLongitud;

public:
    Ccad();  // Constructor
    ~Ccad(); // Destructor
    char *obtener(void)
    {
        return pDatos;
    }
    int obtenerlongitud(void)
    {
        return nLongitud;
    }
    char *copy(char *s);
    char *cat(char *s);
};
