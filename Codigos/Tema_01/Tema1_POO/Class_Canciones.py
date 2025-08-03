class Cancion:

    def __init__(self, autor, titulo,duracion):
        self.duracion = duracion
    def __len__ (self ):
        return self.duracion

cancion = Cancion("Queen", "Don't Stop Me Now",210) 

print(len(cancion))
print(cancion.__len__())
