import random


class Jugador(object):

    def __init__(self, nombre, dinero):
        """Constructor de clase Jugador"""
        if not isinstance(nombre, str):
            raise ValueError("constructor Jugador: nombre debe ser un string")
        if not isinstance(dinero, int):
            raise ValueError("constructor Jugador: dinero debe ser un int")
        if dinero <= 0:
            raise Exception("contructor Jugador: ningun jugador puede aposta con menos o 0€")

        self.__nombre = nombre
        self.__dinero = dinero
        self.__dinero_apostado = 1
        self.__porras_ganada = 0
        self.__resultados_deseados = []  # cada vez se reinicia
        self.__poora = True

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def dinero(self):
        return self.__dinero

    @dinero.setter
    def dinero(self, valor):
        self.__dinero = valor

    @property
    def resultados_deseados(self):
        return self.__resultados_deseados

    @property
    def poora(self):
        return self.__poora

    @poora.setter
    def poora(self, valor):
        self.__poora = valor

    @property
    def porras_ganada(self):
        return self.__porras_ganada

    @porras_ganada.setter
    def porras_ganada(self, valor):
        self.__porras_ganada = valor

    def aumentarDinero(self, dinero_poora):
        self.__dinero = self.__dinero + dinero_poora

    def vaciarResultados(self):
        self.__resultados_deseados.clear()

    def quitarDinero(self):
        self.__dinero -= 1
        print("Jugador: [" + self.__nombre + "], dinero apostado " + str(self.__dinero_apostado) + "€, le queda " + str(
            self.__dinero) + "€")

    def resultadoDeseado(self, tot_partidos):
        for partido in range(tot_partidos):  # minimo dos partidos diarios
            equipo_uno = random.randint(0, 3)  # numero rnd que va de 0 a 3
            equipo_dos = random.randint(0, 3)
            resultado = [equipo_uno, equipo_dos]
            self.__resultados_deseados.append(resultado)
            if partido + 1 == 1:
                partido_n = "primer"
            elif partido + 1 == 2:
                partido_n = "segundo"
            else:
                partido_n = "tercer"
            print("resultado deseado " + partido_n + " partido : " + str(equipo_uno) + " - " + str(equipo_dos))
        print("")

    def __str__(self):
        return "Al jugador [" + self.__nombre + "] le quedan [" + str(self.__dinero) + "€] y ha ganado [" + str(
            self.__porras_ganada) + " porra/s]"


class POOra(object):

    def __init__(self, jugadores):
        """Constructor de clase Porra"""
        self.__jugadores = jugadores
        self.__dinero_porra = 0

    @property
    def dinero_porra(self):
        return self.__dinero_porra

    @dinero_porra.setter
    def dinero_porra(self, valor):
        self.__dinero_porra = valor

    def empezarJuego(self):
        for jornada in range(38):
            print("JORNADA N. " + str(jornada + 1))
            partidos = Partido()
            tot_partidos = partidos.generarPartidosDiarios()  # para cada jornada genero de dos a maximo tres partidos
            print("PARTIDOS DIARIOS: " + str(tot_partidos) + "\n")
            for jugador in self.__jugadores:  # cada jugador dice su resultado
                if jugador.dinero >= 1:  # si el jugador tiene mas de 1euro puede apostar
                    self.__dinero_porra += 1  # añado el dinero a la porra
                    jugador.quitarDinero()  # quito el dinero al jugador
                    jugador.resultadoDeseado(tot_partidos)  # genero el resultado para los dos partidos
                else:  # si no tiene dinero se tiene que quitar de la Poora
                    jugador.poora = False

            # llega el momento de generar el resultado de cada partido
            partidos.resultadoPartidos(tot_partidos)

            print("Dinero en la porra " + str(self.__dinero_porra) + "€\n")

            # compruebo si alguien ha ganado minimo dos veces
            for jugador in self.__jugadores:
                # si el jugador tiene mas o = a 0 € quiere decir que esta en el juego,
                # si no nilo compruebo
                if jugador.poora:
                    contador = 0
                    for p in range(tot_partidos):
                        if partidos.resultados_diarios[p] == jugador.resultados_deseados[p] and self.__dinero_porra > 0:
                            contador += 1
                            if contador >= 2:
                                jugador.aumentarDinero(self.__dinero_porra)  # aumentamos el dinero del jugador
                                print('\033[92m' + "WIN! - Jugador [" + jugador.nombre + "] ha ganado [" + str(
                                    self.__dinero_porra) + "€], en total tiene [" + str(
                                    jugador.dinero) + "€]" + '\033[0m' + "\n")
                                self.__dinero_porra = 0  # vaciamos el dinero de la porra
                                jugador.porras_ganada = jugador.porras_ganada + 1

                # vacio la lista de los resultados deseados para cada Jugador
                jugador.vaciarResultados()

            # ya que la jornada se ha acabado vacio la lista de los resultados para Partido
            partidos.vaciarResultados()

        # al final se imrimen los resultados de cada jugador
        print("RESULTADO FINAL")
        for jugador in self.__jugadores:
            print(jugador)


class Partido(object):

    def __init__(self):
        self.__partidos_diarios = 0
        self.__resultados_diarios = []  # se reinicia cada dia

    @property
    def resultados_diarios(self):
        return self.__resultados_diarios

    def generarPartidosDiarios(self):
        self.__partidos_diarios = random.randint(2, 3)  # minimo dos hasta tres partidos diarios
        return self.__partidos_diarios

    def resultadoPartidos(self, tot_partidos):
        for partido in range(tot_partidos):  # minimo dos partidos diarios
            equipo_uno = random.randint(0, 3)  # numero rnd que va de 0 a 3
            equipo_dos = random.randint(0, 3)
            resultado = [equipo_uno, equipo_dos]
            self.__resultados_diarios.append(resultado)
            print(str(partido + 1) + " partido : " + str(equipo_uno) + " - " + str(equipo_dos))
        print("")

    def vaciarResultados(self):
        self.__resultados_diarios.clear()
