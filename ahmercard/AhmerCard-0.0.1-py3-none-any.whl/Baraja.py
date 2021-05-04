'''La baraja estará compuesta por un conjunto de cartas, 40 exactamente.

Las operaciones que podrá realizar la baraja son:

barajar: cambia de posición todas las cartas aleatoriamente
'''
import pickle
from random import random
from Cardspck.Carta import Carta


class Baraja:
    Numerodecartas = 40
    carta=[]
    cartasdisponible = 40

    def __init__(self):
        self.carta = [self.Numerodecartas]
        self.posAleatoria = 0
        self.Crearbaraja()
        self.barajar()


    def Crearbaraja(self):
        self.c = Carta.palo
        for i in range(4):
            for j in range(10):
                if j != 7 or j != 8:
                    if j >= 9:
                        # ahmer = ((i * (12 - 2)) + j-2)
                        a = Carta(j + 1, self.c[i])
                        self.carta.append(a)
                    else:
                        a = Carta(j + 1, self.c[i])
                        self.carta.append(a)
        print("Se han barajado las cartas")

    def barajar(self):
        self.posAleatoria = 0
        self.c = Carta.palo

        for i in range(40):
            num = (int)(random() * (0 - (self.Numerodecartas - 1 + 1)) + (self.Numerodecartas - 1 + 1))
            self.posAleatoria = num

            self.c = self.carta[i]
            self.carta[i] = self.carta[self.posAleatoria]
            self.carta[self.posAleatoria] = self.c
            self.posSiguienteCarta = 0

    def siguienteCarta(self):
        c = Carta
        if self.posSiguienteCarta == self.Numerodecartas:
            print("Ya no hay mas cartas, barajea de nuevo")
        else:
            self.posSiguienteCarta += 1
            c = self.carta[self.posSiguienteCarta]
        print("Numero= " + str(c.numero), "Palo= " + c.palo)
        return c

    def darCartas(self, numCartas):
        if numCartas > self.Numerodecartas:
            print("No se puede dar mas cartas de las que hay")

        elif self.cartasdisponible < numCartas:
            print("No hay suficientes cartas que mostrar")

        else:
            cartasDar = [numCartas]

            for i in range(5):
                cartasDar.append(self.siguienteCarta())

    def cartasDisponible(self):
        self.cartasdisponible = self.Numerodecartas - self.posSiguienteCarta
        print(self.cartasdisponible)

    def cartasMonton(self):
        if self.cartasdisponible == self.Numerodecartas:
            print("No se ha sacado ninguna carta")

        else:
            for i in range(self.posSiguienteCarta):
                a = self.carta[i]
                b = a.numero
                c = a.palo
                print("numero= " + str(b), "palo= " + c)

    def Guardar(self):
        fichero = ("cartas", "wb")
        pickle.dump(self.carta, fichero)
        fichero.close()
        for p in self.carta:
            print(p.numero)


    def mostrarBaraja(self):
        if self.cartasDisponible() == 0:
            print("No hay cartas que mostrar")
        else:
            for i in range(self.posSiguienteCarta):
                print("Numero= " + str(self.carta[i].numero) + "Palo= " + self.carta[i].palo)
