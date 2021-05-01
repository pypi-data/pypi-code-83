from calculador_de_elementos_estruturais.pegadores import PegadorPilar
from calculador_de_elementos_estruturais.calculadores import CalculadorPilar

class PilarDeMadeira:

    def __init__(self):
        self.circulo_ou_retangulo = PegadorPilar.escolhe_tipo_elemento()
        self.dimensoes = PegadorPilar.pega_dimensoes(self)
        self.comprimento = PegadorPilar.pega_comprimento()
        self.flexao_composta, self.momentos = PegadorPilar.pega_cargas()
        self.classe, self.categoria, self.duracao = PegadorPilar.pega_classe_categoria_e_duracao()
        self.classe_umidade = PegadorPilar.pega_classe_umidade()
        self.Fc0k = PegadorPilar.pega_Fc0k(self)
        self.kmod, self.kmods = PegadorPilar.pega_kmod(self)
        self.Ec0m = PegadorPilar.pega_Ec0m(self)

        self.area = CalculadorPilar.calcula_area(self)
        self.inercia = CalculadorPilar.calcula_inercia(self)
        self.modulo_resistencia = CalculadorPilar.calcula_resistencia(self)
        self.raio_giracao = CalculadorPilar.calcula_raio_giracao(self)
        self.indice_esbeltez = CalculadorPilar.calcula_indice_esbeltez(self)
        self.fc0d = CalculadorPilar.calcula_fc0d(self)
        self.tensao_normal = CalculadorPilar.calcula_tensao_normal(self)
        self.tensao_momento_fletor = CalculadorPilar.calcula_tensao_momento_fletor(self)
        self.modulo_elasticidade = CalculadorPilar.calcula_modulo_elasticidade(self)
        self.excentricidade = CalculadorPilar.retorna_excentricidade(self)

        print(self)

    def verificacao_parte_1(self):
        verificacao = ((self.tensao_normal/self.fc0d)**2 +
                       self.tensao_momento_fletor[1]/self.fc0d +
                       0.5 * (self.tensao_momento_fletor[0]/self.fc0d))
        if verificacao < 1:
            return 'Passou!', round(verificacao, 6)
        else:
            return 'Não passou!', round(verificacao, 6)

    def verificacao_parte_2(self):
        verificacao = ((self.tensao_normal/self.fc0d)**2 +
                       0.5 * (self.tensao_momento_fletor[1]/self.fc0d) +
                       self.tensao_momento_fletor[0]/self.fc0d)
        if verificacao < 1:
            return 'Passou!', round(verificacao, 6)
        else:
            return 'Não passou!', round(verificacao, 6)

    def verificacao_parte_3(self):
        if type(self.excentricidade) == type(None):
            return ''

        elif type(self.excentricidade) == type(tuple()):
            calculo_verificacao = round(((self.tensao_normal/self.fc0d) +
                                   (self.excentricidade[0] / self.fc0d)), 6)
            if calculo_verificacao <= 1:
                verificacao = 'Passou!'
            else:
                verificacao = 'Não passou!'

            z_ou_y = (('eiy', 'e1y', 'Mzd', 'σMzd', 'Z', 'eyd'), ('eiz', 'e1z', 'Myd', 'σMyd', 'Y', 'ezd'))
            
            return f'''\033[1mExcentricidade acidental (ea)\033[0m: {round(self.excentricidade[4][0], 6)} mm
\033[1m{z_ou_y[self.excentricidade[3]][0]}\033[0m: {round(self.excentricidade[4][1], 6)} mm
\033[1m{z_ou_y[self.excentricidade[3]][1]}\033[0m: {round(self.excentricidade[4][2], 6)} mm
\033[1mEc0m\033[0m: {self.Ec0m} MPa
\033[1mMódulo de Elasticidade (Ec0ef)\033[0m: {self.modulo_elasticidade} kN/m²
\033[1mFe\033[0m: {round(self.excentricidade[2], 3)} kN
\033[1m{z_ou_y[self.excentricidade[3]][5]}\033[0m: {round(self.excentricidade[4][-1], 3)} mm
\033[1mNovo Momento Fletor em {z_ou_y[self.excentricidade[3]][4]} ({z_ou_y[self.excentricidade[3]][2]})\033[0m: {round(self.excentricidade[1], 3)} kNm
\033[1mNova Tensão Momento Fletor em {z_ou_y[self.excentricidade[3]][4]} ({z_ou_y[self.excentricidade[3]][3]})\033[0m: {round(self.excentricidade[0], 3)} MPa

\033[1mVerificação Parte 4\033[0m: {calculo_verificacao} <= 1
        \033[1m{verificacao}\033[0m
    '''

        elif type(self.excentricidade) == type(list()):

            calculo_verificacao_z = ((self.tensao_normal/self.fc0d) +
                                   (self.excentricidade[0][0] / self.fc0d))
            if calculo_verificacao_z <= 1:
                verificacao_z = 'Passou!'
            else:
                verificacao_z = 'Não passou!'

            calculo_verificacao_y = ((self.tensao_normal/self.fc0d) +
                                   (self.excentricidade[1][0] / self.fc0d))
            if calculo_verificacao_y <= 1:
                verificacao_y = 'Passou!'
            else:
                verificacao_y = 'Não passou!'

            return f'''\033[1mExcentricidade acidental (ea)\033[0m: {round(self.excentricidade[0][4][0], 6)} mm
\033[1mEc0m\033[0m: {self.Ec0m} MPa
\033[1mMódulo de Elasticidade (Ec0ef)\033[0m: {self.modulo_elasticidade} kN/m²
            
\033[1mVerificação em Z:\033[0m
\033[1meiy\033[0m: {round(self.excentricidade[0][4][1], 6)} mm
\033[1me1y\033[0m: {round(self.excentricidade[0][4][2], 6)} mm
\033[1mFe\033[0m: {round(self.excentricidade[0][2], 3)} kN
\033[1meyd\033[0m: {round(self.excentricidade[0][4][-1], 3)} mm
\033[1mNovo Momento Fletor em Z (Mzd)\033[0m: {round(self.excentricidade[0][1], 3)} kNm
\033[1mNova Tensão Momento Fletor em Z (σMzd)\033[0m: {round(self.excentricidade[0][0], 3)} MPa

\033[1mVerificação Parte 4 em Z\033[0m: {round(calculo_verificacao_z, 6)} <= 1
        \033[1m{verificacao_z}\033[0m

\033[1mVerificação em Y:\033[0m
\033[1meiz\033[0m: {round(self.excentricidade[1][4][1], 6)} mm
\033[1me1z\033[0m: {round(self.excentricidade[1][4][2], 6)} mm
\033[1mFe\033[0m: {round(self.excentricidade[1][2], 3)} kN
\033[1mezd\033[0m: {round(self.excentricidade[1][4][-1], 3)} mm
\033[1mNovo Momento Fletor em Y (Myd)\033[0m: {round(self.excentricidade[1][1], 3)} kNm
\033[1mNova Tensão Momento Fletor em Y (σMyd)\033[0m: {round(self.excentricidade[1][0], 3)} MPa

\033[1mVerificação Parte 4 em Y\033[0m: {round(calculo_verificacao_y, 6)} <= 1
        \033[1m{verificacao_y}\033[0m
    '''

    def __str__(self):
        return f'''

\033[1mÁrea (A)\033[0m: {round(self.area, 6)} cm²
\033[1mMomento de Inércia em z (Iz)\033[0m: {round(self.inercia[0], 6)} cm⁴
\033[1mMomento de Inércia em y (Iy)\033[0m: {round(self.inercia[1], 6)} cm⁴
\033[1mMódulo de Resistência em z (Wz)\033[0m: {round(self.modulo_resistencia[0], 6)} cm³
\033[1mMódulo de Resistência em y (Wy)\033[0m: {round(self.modulo_resistencia[1], 6)} cm³
\033[1mRaio de Giração em z (iz)\033[0m: {round(self.raio_giracao[0], 6)} cm
\033[1mRaio de Giração em y (iy)\033[0m: {round(self.raio_giracao[1], 6)} cm
\033[1mÍndice de Esbeltez em z (λz)\033[0m: {round(self.indice_esbeltez[0], 6)}
\033[1mÍndice de Esbeltez em y (λy)\033[0m: {round(self.indice_esbeltez[1], 6)}

\033[1mResistência a Compressão (Fc0k)\033[0m: {self.Fc0k} MPa
\033[1mKmod1, Kmod2, Kmod3\033[0m: {self.kmods}
\033[1mKmod\033[0m: {self.kmod}
\033[1mResistência da Madeira (Fc0d)\033[0m: {self.fc0d} MPa

\033[1mTensão Normal (σNd)\033[0m: {round(self.tensao_normal, 6)} MPa
\033[1mTensão Momento Fletor em z (σMz)\033[0m: {round(self.tensao_momento_fletor[0], 6)} MPa
\033[1mTensão Momento Fletor em y (σMy)\033[0m: {round(self.tensao_momento_fletor[1], 6)} MPa

\033[1mVerificação Parte 3.1\033[0m: {round(self.verificacao_parte_1()[1], 6)} < 1
        \033[1m{self.verificacao_parte_1()[0]}\033[0m

\033[1mVerificação Parte 3.2\033[0m: {round(self.verificacao_parte_2()[1], 6)} < 1
        \033[1m{self.verificacao_parte_2()[0]}\033[0m

{self.verificacao_parte_3()}




'''
