class Espectador:
    def __init__(self, nombre, edad, dinero):
        self.nombre = nombre
        self.edad = edad
        self.dinero = dinero


class Pelicula:
    def __init__(self, titulo, duracion, edadMinima, director):
        self.titulo = titulo
        self.duracion = duracion
        self.edadMinima = edadMinima
        self.director = director


class Cine:
    def __init__(self, pelicula, precio):
        self.pelicula = pelicula
        self.precio = precio
