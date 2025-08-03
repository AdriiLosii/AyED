#include <iostream>
#include <ostream>
#include <cstring>
#include "ClasesC_10.hpp"

class Persona_Dir_Completa : public Persona
{
private:
    std::string direccion;
    std::string telef;
    unsigned int codpostal;

public:
    // El constructor y el destructor no hacen nada
    // El constructor llama al constructor de Persona
    Persona_Dir_Completa() : Persona(){};
    ~Persona_Dir_Completa(){};
    const std::string &dev_direccion(void) const
    {
        return direccion;
    };
    const std::string &dev_telefono(void) const
    {
        return telef;
    };
    const unsigned int &dev_codpostal(void) const
    {
        return codpostal;
    };
    void pon_direccion(const std::string &x)
    {
        direccion = x;
    };
    void pon_telef(const std::string &x)
    {
        telef = x;
    };
    void pon_codpostal(const unsigned int &x)
    {
        codpostal = x;
    };
};