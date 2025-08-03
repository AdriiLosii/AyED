#Tema3_10 Esquema
def Divide_y_Venceras(p):
    if EsCasoBase(p):
        s = ResuelveCasoBase(p)
    else :
        lista_subp = Divide(p)
        lista_subs = list()
        for subp in lista_subp:
            subs = Divide_y_Venceras(subp)
            lista_subs.append(subs)
            s = Combina(lista_subs)
    return s
    