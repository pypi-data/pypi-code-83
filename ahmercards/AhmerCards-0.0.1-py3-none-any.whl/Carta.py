'''
#Upalo=Nonetiene un número entre 1 y 12 (el 8 y el 9 no los incluimos) y un palo (espadas, bastos, oros y copas)

La baraja estará compuesta por un conjunto de cartas, 40 exactamente.

Las operaciones que podrá realizar la baraja son:

barajar: cambia de posición todas las cartas aleatoriamente
'''

class Carta:
    global numero
    palo=['espadas','bastos','oros','copas']
    totalcartas=40
    def __init__(self,numero,palo):
        self.numero=numero
        self.palo=palo

    def str(self):
        print(self.numero ,self.palo)

    def getpalo(self):
     return self.palo

    def getnumero(self):
        return self.numero
