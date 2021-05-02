from pandas import DataFrame
from abc import abstractmethod, ABC


informacoes_classe = {'Classe': ('C20', 'C30', 'C40', 'C60'),
                      'Fc0k': (20, 30, 40, 60),
                      'Ec0m': (9500, 14500, 19500, 24500)}
tabela_classe = DataFrame(informacoes_classe, index=(1, 2, 3, 4))

informacoes_kmod1 = {'Permanente': 0.6,
                     'Longa Duração': 0.7,
                     'Média Duração': 0.8,
                     'Curta Duração': 0.9,
                     'Instantânea': 1.1}

duracoes = ('Permanente', 'Longa Duração', 'Média Duração', 'Curta Duração', 'Instantânea')

informacoes_kmod2 = {'1': 1,
                     '2': 1,
                     '3': 0.8,
                     '4': 0.8}

informacoes_kmod3 = {'1ª Categoria': 1, '2ª Categoria': 0.8}

categorias = ('1ª Categoria', '2ª Categoria')


class Pegador(ABC):

    @staticmethod
    @abstractmethod
    def pega_dimensoes(elemento):
        pass

    @staticmethod
    @abstractmethod
    def pega_comprimento():
        pass

    @staticmethod
    @abstractmethod
    def pega_cargas():
        pass

    @staticmethod
    def escolhe_tipo_elemento():

        mensagem = f'''O elemento é retangular ou circular?

                        (1) Circular
                        (2) Retangular

                    '''

        circulo_ou_retangulo = input(mensagem)
        if circulo_ou_retangulo in ('1', '2'):
            return circulo_ou_retangulo
        else:
            raise ValueError('Digite um valor válido.')

    @staticmethod
    def pega_classe():
        mensagem_classe = '''Informe a classe da madeira. 

                (1) C20
                (2) C30
                (3) C40
                (4) C60

                '''

        classe = int(input(mensagem_classe))
        if classe not in (1, 2, 3, 4):
            raise ValueError('Digite um valor válido para classe. ')

        return classe

    @staticmethod
    def pega_categoria():
        mensagem_categoria = '''Informe a categoria da madeira.

                (1) 1ª categoria
                (2) 2ª categoria

                '''

        categoria = int(input(mensagem_categoria))
        if categoria not in (1, 2):
            raise ValueError('Digite um valor válido para categoria. ')

        return categoria

    @staticmethod
    def pega_duracao():
        mensagem_duracao = '''Informe a duração do carregamento.

                (1) Permanente
                (2) Longa Duração
                (3) Média Duração
                (4) Curta Duração
                (5) Instantânea

                '''

        duracao = int(input(mensagem_duracao))
        if duracao not in (1, 2, 3, 4, 5):
            raise ValueError('Digite um valor válido para duração. ')

        return duracao
        
    @staticmethod
    def pega_classe_umidade():
        umidade = int(input('Informe a umidade ambiente. '))

        if umidade <= 65:
            classe_umidade = '1'
        elif 65 < umidade <= 75:
            classe_umidade = '2'
        elif 75 < umidade <= 85:
            classe_umidade = '3'
        else:
            classe_umidade = '4'

        return classe_umidade

    @staticmethod
    def pega_Fc0k(elemento):
        fc0k = tabela_classe.loc[elemento.classe, 'Fc0k']
        return fc0k

    @staticmethod
    def pega_kmods(elemento):
        duracao = duracoes[elemento.duracao - 1]
        kmod1 = informacoes_kmod1[duracao]

        kmod2 = informacoes_kmod2[elemento.classe_umidade]

        categoria = categorias[elemento.categoria - 1]
        kmod3 = informacoes_kmod3[categoria]

        return {'1': kmod1, '2': kmod2, '3': kmod3}

    @staticmethod
    def pega_Ec0m(elemento):
        Ec0m = tabela_classe.loc[elemento.classe, 'Ec0m']
        return Ec0m


class PegadorViga(Pegador):

    @staticmethod
    def pega_dimensoes(viga):
        if viga.circulo_ou_retangulo == '1':
            diametro = float(input('Informe o diâmetro em centímetro da peça. '))
            return {'d': diametro / 100}
        else:
            base = float(input('Informe a medida da base em centímetro da peça. '))
            altura = float(input('Informe a medida da altura em centímetro da peça. '))
            return {'b': base / 100, 'h': altura / 100}

    @staticmethod
    def pega_comprimento():
        comprimento = float(input('Informe o comprimento em metro da viga. '))
        return comprimento

    @staticmethod
    def pega_peso_proprio():
        peso_proprio = float(input('Informe o peso próprio da viga. '))

        return peso_proprio

    @staticmethod
    def pega_carga_acidental():
        carga_acidental = float(input('Informe a carga acidental da viga. '))
        
        return carga_acidental


class PegadorPilar(Pegador):

    @staticmethod
    def pega_dimensoes(pilar):
        if pilar.circulo_ou_retangulo == '1':
            diametro = float(input('Informe o diâmetro em centímetro da peça. '))
            return {'d': diametro}
        else:
            base = float(input('Informe a medida da base em centímetro da peça. '))
            altura = float(input('Informe a medida da altura em centímetro da peça. '))
            return {'b': base, 'h': altura}

    @staticmethod
    def pega_comprimento():
        comprimento = float(input('Informe o comprimento em metro do pilar. '))
        return comprimento * 100

    @staticmethod
    def pega_flexao_composta():
        flexao_composta = float(input('Informe o esforço de Flexão Composta (Nd) do pilar. '))

        return flexao_composta

    @staticmethod
    def pega_momentos():
        momento_z = float(input('Informe o Momento Fletor no eixo Z (Mzd) do pilar. '))
        momento_y = float(input('Informe o Momento Fletor no eixo Y (Myd) do pilar. '))

        return {'z': momento_z, 'y': momento_y}