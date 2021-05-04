import seriesjuegos.Entregable

class Videojuego(seriesjuegos.Entregable):

    def __init__(self, titulo, genero, companya):
        self.titulo = titulo
        self.horas_estimadas = 10
        self.entregado = False
        self.genero = genero
        self.companya = companya

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

    def set_horas_estimadas(self, horas_estimadas):
        self.horas_estimadas = horas_estimadas

    def get_horas_estimadas(self):
        return self.horas_estimadas

    def set_genero(self, genero):
        self.genero = genero

    def get_genero(self):
        return self.genero

    def set_companya(self, companya):
        self.companya = companya

    def get_companya(self):
        return self.companya

    def __str__(self):
        return "TITULO: " + self.titulo + "\n" + "HORAS ESTIMADAS: " + str(self.horas_estimadas) + " ENTREGADO: " + str(self.entregado) + " GENERO: " + self.genero + " COMPAÑIA: " + self.companya

    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return self.entregado

    def compareTo(self, objeto):
        if self.horas_estimadas > objeto.horas_estimadas:
            return self.titulo
        else:
            return objeto.titulo
