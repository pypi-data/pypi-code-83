#from calculador_de_elementos_estruturais.viga_de_madeira import VigaDeMadeira
#from calculador_de_elementos_estruturais.pilar_de_madeira import PilarDeMadeira

from viga_de_madeira import VigaDeMadeira
from pilar_de_madeira import PilarDeMadeira

class MenuPrincipal:

    def __init__(self):
        print('\n\nBem vindo ao Calculador de Estruturas do 4º TE. A seguir, um pequeno tutorial de uso.\n\n')
        print('Quando aparecer um seletor, por exemplo: \n (1) Opção 1 \n (2) Opção 2')
        print('Digite somente o número que está dentro dos parênteses. Por exemplo, se sua a opção desejada for a 2,')
        print('digite apenas "2" (sem as aspas).\n')
        print('Não é necessário digitar as unidades dos valores, apenas o número é necessário.')
        print('Caso a unidade seja digitada, erros ocorrerão.\n')
        print('Caso seja necessário digitar algum valor decimal, separe as casas decimais por ponto, e não por vírgula.')
        print('Exemplo: O valor decimal é "1,2", você deve digitar "1.2"\n\n')

        while True:
            mensagem = '''Qual elemento estrutural irá ser calculado?
            
                (1) Pilar
                (2) Viga
                
                '''

            elemento = int(input(mensagem))

            if elemento == 1:
                PilarDeMadeira()
            elif elemento == 2:
                VigaDeMadeira()
            else:
                raise ValueError('Digite um valor válido.')
