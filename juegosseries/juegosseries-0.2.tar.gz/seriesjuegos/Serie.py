import Entregable


class Serie(Entregable):

    def __init__(self, titulo, genero, creador):
        self.titulo = titulo
        self.numero_temp = 3
        self.entregado = False
        self.genero = genero
        self.creador = creador

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

    def set_numero_temp(self, numero_temp):
        self.numero_temp = numero_temp

    def get_numero_temp(self):
        return self.numero_temp

    def set_genero(self, genero):
        self.genero = genero

    def get_genero(self):
        return self.genero

    def set_creador(self, creador):
        self.creador = creador

    def get_creador(self):
        return self.creador

    def __str__(self):
        return "TITULO: " + self.titulo + "\n" + "NUMERO TEMPORADAS: " + str(self.numero_temp) + " ENTREGADO: " + str(self.entregado) + " GENERO: " + self.genero + " CREADOR: " + self.creador

    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return self.entregado

    def compareTo(self, objeto):
        if self.numero_temp > objeto.numero_temp:
            return self.titulo
        else:
            return objeto.titulo

