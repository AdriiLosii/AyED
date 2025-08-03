from Class_Grafos import Grafo
class grafoBEP(Grafo):
    def __init__(self):
        super().__init__()
        self.tiempo = 0

    def bep(self):
        for unVertice in self:
            unVertice.asignarColor('blanco')
            unVertice.asignarPredecesor(-1)
        for unVertice in self:
            if unVertice.obtenerColor() == 'blanco':
                self.visitabep(unVertice)

    def visitabep(self,verticeInicio):
        verticeInicio.asignarColor('gris')
        self.tiempo += 1
        verticeInicio.asignarDescubrimiento(self.tiempo)
        for siguienteVertice in verticeInicio.obtenerConexiones():
            if siguienteVertice.obtenerColor() == 'blanco':
                siguienteVertice.asignarPredecesor(verticeInicio)
                self.visitabep(siguienteVertice)
        verticeInicio.asignarColor('negro')
        self.tiempo += 1
        verticeInicio.asignarFinalizacion(self.tiempo)