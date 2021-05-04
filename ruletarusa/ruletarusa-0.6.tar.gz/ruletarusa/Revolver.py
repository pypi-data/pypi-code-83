import random

class Revolver:
    def __init__(self):
        self.posicion_actual = random.randint(1, 6)
        self.posicion_bala = random.randint(1, 6)

    def disparar(self):
        disparo = False
        if self.posicion_actual == self.posicion_bala:
            disparo = True
        self.siguienteBala()
        return disparo

    def siguienteBala(self):
        if self.posicion_bala == 6:
            self.posicion_bala = 1
        else:
            self.posicion_bala = self.posicion_bala + 1

    def toString(self):
        print("Posición actual del revolver:")
        print("Posición actual: %d" % self.posicion_actual)
        print("Posición de la bala: %d" % self.posicion_bala)
