class Jugador:
    def __init__(self, id):
        self.id = id
        self.nombre = "Jugador %d" % id
        self.vivo = True

    def disparar(self, r):
        disparo = r.disparar()
        if not disparo:
            print("%s está de suerte y se ha librado... Sigue vivo." % self.nombre)
        else:
            print("Un valiente menos... %s ha muerto." % self.nombre)
            self.vivo = False

    def isVivo(self):
        return self.vivo