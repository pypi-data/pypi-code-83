import pickle
import sys

inputfile = "ruletarusa.dat"
if len(sys.argv) >= 2:
    print("\n\nFitxer d'entrada: " + sys.argv[1])
    inputfile = sys.argv[1]
binary_file = open(inputfile, mode='rb')
while True:
    try:
        jugador = pickle.load(binary_file)
        print(jugador.ronda())
    except EOFError:
        break