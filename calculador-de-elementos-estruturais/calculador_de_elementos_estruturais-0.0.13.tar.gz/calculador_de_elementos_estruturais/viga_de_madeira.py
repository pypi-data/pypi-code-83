from calculador_de_elementos_estruturais.pegadores import PegadorViga
from calculador_de_elementos_estruturais.calculadores import CalculadorViga

class VigaDeMadeira:

    def __init__(self):
        self.circulo_ou_retangulo = PegadorViga.escolhe_tipo_elemento()
        self.dimensoes = PegadorViga.pega_dimensoes(self)
        self.comprimento = PegadorViga.pega_comprimento()
        self.peso_proprio, self.carga_acidental = PegadorViga.pega_cargas()
        self.classe, self.categoria, self.duracao = PegadorViga.pega_classe_categoria_e_duracao()
        self.classe_umidade = PegadorViga.pega_classe_umidade()
        self.Fc0k = PegadorViga.pega_Fc0k(self)
        self.kmod, self.kmods = PegadorViga.pega_kmod(self)
        self.Ec0m = PegadorViga.pega_Ec0m(self)

        self.area = CalculadorViga.calcula_area(self)
        self.inercia = CalculadorViga.calcula_inercia(self)
        self.modulo_resistencia = CalculadorViga.calcula_resistencia(self)
        self.carga_permanente = CalculadorViga.calcula_carga_permanente(self)
        self.momento_fletor = CalculadorViga.calcula_momento_fletor(self)
        self.tensao_normal = CalculadorViga.calcula_tensao_normal(self)
        self.fc0d = CalculadorViga.calcula_fc0d(self)
        self.flecha_maxima = CalculadorViga.calcula_flecha_maxima(self)
        self.modulo_elasticidade = CalculadorViga.calcula_modulo_elasticidade(self)
        self.flecha_efetiva = CalculadorViga.calcula_flecha_efetiva(self)

        print(self)

    def compara_estado_limite_ultimo(self):
        if self.tensao_normal <= self.fc0d:
            return 'Passou!'
        else:
            return 'Não passou!'

    def compara_flecha(self):
        if self.flecha_efetiva <= self.flecha_maxima:
            return 'Passou!'
        else:
            return 'Não passou!'

    def __str__(self):
        return f'''

\033[1mÁrea (A)\033[0m: {round(self.area, 6)} m²
\033[1mMomento de Inércia (Iz)\033[0m: {round(self.inercia, 6):.6f} m⁴
\033[1mMódulo de Resistência (Wz)\033[0m: {round(self.modulo_resistencia, 6)} m³
\033[1mCarga Permanente (gk)\033[0m: {round(self.carga_permanente, 6)} kN/m
\033[1mMomento Fletor Máximo (Mzd)\033[0m: {round(self.momento_fletor, 6)} kNm
\033[1mTensão Máxima (σMzd)\033[0m: {round(self.tensao_normal, 6)} MPa
\033[1mResistência a Compressão (Fc0k)\033[0m: {self.Fc0k} MPa
\033[1mKmod1, Kmod2, Kmod3\033[0m: {self.kmods}
\033[1mKmod\033[0m: {self.kmod}
\033[1mResistência da Madeira (Fc0d)\033[0m: {self.fc0d} MPa

\033[1mVerificação Parte 3\033[0m: {round(self.tensao_normal, 6)} <= {self.fc0d}
        \033[1m{self.compara_estado_limite_ultimo()}\033[0m

\033[1mFlecha Limite (Vlim)\033[0m: {self.flecha_maxima} mm
\033[1mEc0m\033[0m: {self.Ec0m} MPa
\033[1mModulo de Elasticidade Efetivo (Eef)\033[0m: {self.modulo_elasticidade} kN/m²
\033[1mFlecha Efetiva (Vef)\033[0m: {round(self.flecha_efetiva, 6)} mm

\033[1mVerificação Parte 4\033[0m: {round(self.flecha_efetiva, 6)} <= {self.flecha_maxima}
        \033[1m{self.compara_flecha()}\033[0m




'''