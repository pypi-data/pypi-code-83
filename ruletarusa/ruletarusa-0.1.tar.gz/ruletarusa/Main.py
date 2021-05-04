import pickle
import sys
from Juego import *


def menu():
    """Funció que conté el menú del programa"""
    print("---------------------- RULETA RUSA ------------------------")
    print("-----------------------------------------------------------")


numero_jugadores = int(input("Indica el número de jugadores: "))
juego = Juego(numero_jugadores)

while not juego.finJuego():
    print()
    menu()
    juego.ronda()

print("Juego terminado.")

inputfile = "ruletarusa.dat"
binary_file = open(inputfile, mode='wb')
pickle.dump(juego, binary_file)
