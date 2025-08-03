class Listin:
    def __init__(self):
        self.listin={}

    def añadir(self, nombre, telefono):
        if nombre in self.listin:
            if not telefono in self.listin[nombre]:
                self.listin[nombre].append(telefono)
        else:
            self.listin[nombre]=[telefono]

    def consultar(self, nombre):
        if nombre in self.listin:
            return self.listin[nombre]
        else:
            return []

    def eliminar(self, nombre):
        if nombre in self.listin:
            del self.listin[nombre]
#Fin de la clase
