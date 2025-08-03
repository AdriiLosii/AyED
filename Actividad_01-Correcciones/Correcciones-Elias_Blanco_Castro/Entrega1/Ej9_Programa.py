import random
class Dado:
    def __init__(self):
        self.ultimo_resultado = 0

    def tirada(self,n):
        self.ultimo_resultado = random.randint(1, n)
        return self.ultimo_resultado

    def __str__(self):
        return str(self.ultimo_resultado)
class Jugador:
    """Representa a un jugador que tiene x dados."""
    def __init__(self, nombre, num_dados):
        """Crea un nuevo jugador.

            :param nombre: El nombre del jugador.
            :param num_dados: El num. de dados para la partida."""

        self.nombre = nombre
        self.num_dados = num_dados
        self.dados = []
        self.ultima_tirada = []
        for i in range(num_dados):
            self.dados += [Dado()]

    def tirada(self,n):
        """Realiza una tirada con todos los dados."""

        self.ultima_tirada = []

        for dado in self.dados:
            self.ultima_tirada += [dado.tirada(n)]

        return self.ultima_tirada

    def __str__(self):
        toret = self.nombre + ": "

        for x in self.ultima_tirada:
            toret += str(x) + ' '

        return toret.strip()


class Juego:
    """Representa un juego de y jugadores e x turnos.
        Permitirá incorporar jugadores.
        El método juega() lanza los y turnos, guardando
        los resultados parciales y la puntuación total."""

    def __init__(self, num_turnos, num_dados):
        """Crea un nuevo juego.
                :param num_turnos: El num. de turnos a jugar.
                :param num_dados: El num. de dados para todos. """

        self.num_turnos = num_turnos
        self.num_dados = num_dados
        self.jugadores = []
        self.puntos_max = []
        self.puntos_parciales = []
        self.turnos = []

    def inserta_jugador(self, nombre):
        self.jugadores += [Jugador(nombre, self.num_dados)]

    def juega(self,n):
        self.puntos_max = [0] * len(self.jugadores)
        self.turnos = []

        for _ in range(self.num_turnos):
            self.puntos_parciales = [[]] * len(self.jugadores)

            for i, jugador in enumerate(self.jugadores):
                pts = jugador.tirada(n)
                self.puntos_max[i] += sum(pts)
                self.puntos_parciales[i] = list(jugador.ultima_tirada)

            self.turnos += [list(self.puntos_parciales)]

    def __str__(self):
        toret = str.format("Juego de {0} turnos y {1} dados.\n\n",
                            self.num_turnos, self.num_dados)

        for puntos in self.turnos:
            for i, pts in enumerate(puntos):
                toret += self.jugadores[i].nombre + ": " + str(pts)

                toret += '\n'
            toret += '\n'

        toret += "Puntuaciones finales:\n"
        for i, pts in enumerate(self.puntos_max):
            toret += self.jugadores[i].nombre + ": " + str(pts) + '\n'

        return toret

if __name__ == "__main__":
    x=int(input("número de turnos"))
    n=int(input("número de dados y de caras"))
    juego = Juego(x, n)
    juego.inserta_jugador("Anxo")
    juego.inserta_jugador("Mauro")
    juego.inserta_jugador("Simón")
    juego.inserta_jugador("Manuel")
    juego.inserta_jugador("Gio")
    juego.inserta_jugador("Sergio")
    juego.inserta_jugador("Elias")
    juego.juega(n)
    print(juego)
