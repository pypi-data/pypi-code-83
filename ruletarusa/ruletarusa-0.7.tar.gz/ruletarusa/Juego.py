from ruletarusa.Revolver import *
from ruletarusa.Jugador import *
import pickle


class Juego:
    def __init__(self, numero_jugadores):
        self.jugadores = []
        self.revolver = Revolver()

        nj = self.verificarNumeroJugadores(numero_jugadores)

        for i in range(nj):
            self.jugadores.append(Jugador(i + 1))

        inputfile = "juego.dat"
        binary_file = open(inputfile, mode='wb')
        pickle.dump(self, binary_file)

    def finJuego(self):
        fin_juego = False

        for i in range(len(self.jugadores)):
            estado_jugador = self.jugadores[i].isVivo()

            if not estado_jugador:
                fin_juego = True

        return fin_juego

    def ronda(self):
        for i in range(len(self.jugadores)):
            print("El valiente %s coge el revolver y se apunta..." % self.jugadores[i].nombre)
            self.jugadores[i].disparar(self.revolver)

            if not self.jugadores[i].vivo:
                break

    def verificarNumeroJugadores(self, numero_jugadores):
        if numero_jugadores < 1 or numero_jugadores > 6:
            numero_jugadores = 6
        return numero_jugadores

