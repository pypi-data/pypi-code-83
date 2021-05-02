from tqdm import tqdm
import requests
import zipfile
import io
import os

year_range = [1994, 1996, 1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020]
UF_range = ['RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'MG', 'ES', 'RJ',
            'SP', 'PR', 'SC', 'RS', 'MS', 'MT', 'GO', 'DF']

def extract_data(file,path = './data'):

    """Função para descompactar os arquivos .zip com os dados

    Args:
    file: str. Nome do arquivo a ser descompactado
    path: str. Caminho para o qual o arquivo será descompactado

    Returns:
    Os arquivos que compõe o arquivo original .zip descompactados especificados em 'file'
    na pasta dada pelo caminho 'path'
    """

    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(path)


def votos_munzona_candidato(year, extract = False):
    
    """Função para baixar o arquivo .zip com os dados de votos por candidato por município e zona eleitoral

    Args:
    year: int. Ano da eleição
    extract: boolean. Inserir argumento como True caso deseje-se extrair os arquivos
    automaticamente após baixá-los. False apenas 

    Returns:
    Os arquivos que compõe o arquivo original .zip descompactados especificados em 'file'
    na pasta dada pelo caminho especificado no print statement na função
    """

    year = year
    if year not in year_range:
        print('O ano escolhido não corresponde a um ano de eleições válido')
        print('Favor escolher um ano dentre os apresentados a seguir')
        print(year_range)
    else:
        url = "https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_{}.zip".format(year)
        fname = "votos_por_candidato_{}.zip".format(year)
        response = requests.get(url, stream=True)
        total_size_in_bytes= int(response.headers.get('content-length', 0))
        block_size = 1024 #1 Kibibyte
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(fname, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("ERROR, something went wrong")
        if extract == True:
            extract_data(fname, path='./data/{}/votos_candidato'.format(year))
            print('\n Os arquivos com os dados foram extraídos para o caminho ./data/{}/votos_munzona_candidato'.format(year))


def votos_munzona_geral(year, extract = False):

    """Função para baixar o arquivo .zip com os dados de votos gerais por município e zona eleitoral

    Args:
    year: int. Ano da eleição
    extract: boolean. Inserir argumento como True caso deseje-se extrair os arquivos
    automaticamente após baixá-los. False apenas 

    Returns:
    Os arquivos que compõe o arquivo original .zip descompactados especificados em 'file'
    na pasta dada pelo caminho especificado no print statement na função
    """

    year = year
    if year not in year_range:
        print('O ano escolhido não corresponde a um ano de eleições válido')
        print('Favor escolher um ano dentre os apresentados a seguir:')
        print(year_range)
    else:
        url = "https://cdn.tse.jus.br/estatistica/sead/odsele/detalhe_votacao_munzona/detalhe_votacao_munzona_{}.zip".format(year)
        fname = "votos_gerais_{}.zip".format(year)
        response = requests.get(url, stream=True)
        total_size_in_bytes= int(response.headers.get('content-length', 0))
        block_size = 1024 #1 Kibibyte
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(fname, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("ERROR, something went wrong")
        if extract == True:
            extract_data(fname, path='./data/{}/votos_munzona_geral'.format(year))
            print('\n Os arquivos com os dados foram extraídos para o caminho ./data/{}/votos_munzona_geral'.format(year))

def votos_secao_geral(year, extract = False):

    """Função para baixar o arquivo .zip com os dados de votos gerais seção eleitoral

    Args:
    year: int. Ano da eleição
    extract: boolean. Inserir argumento como True caso deseje-se extrair os arquivos
    automaticamente após baixá-los. False apenas 

    Returns:
    Os arquivos que compõe o arquivo original .zip descompactados especificados em 'file'
    na pasta dada pelo caminho especificado no print statement na função
    """

    year = year
    if year not in year_range:
        print('O ano escolhido não corresponde a um ano de eleições válido')
        print('Favor escolher um ano dentre os apresentados a seguir:')
        print(year_range)
    else:
        url = "https://cdn.tse.jus.br/estatistica/sead/odsele/detalhe_votacao_secao/detalhe_votacao_secao_{}.zip".format(year)
        fname = "votos_gerais_{}.zip".format(year)
        response = requests.get(url, stream=True)
        total_size_in_bytes= int(response.headers.get('content-length', 0))
        block_size = 1024 #1 Kibibyte
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(fname, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("ERROR, something went wrong")
        if extract == True:
            extract_data(fname, path='./data/{}/votos_secao'.format(year))
            print('\n Os arquivos com os dados foram extraídos para o caminho ./data/{}/votos_secao_geral'.format(year))


def votos_secao_candidato(state, year, extract = False):

    """Função para baixar o arquivo .zip com os dados de votos por candidato por seção eleitoral.
    Como a granularidade dos dados é muito elevada os arquivos ficam muito pesados. Desta forma o TSE
    optou por separar o download por estado.

    Args:
    state: str. Estado - usar sigla da com duas letras.
    year: int. Ano da eleição
    extract: boolean. Inserir argumento como True caso deseje-se extrair os arquivos
    automaticamente após baixá-los. False apenas 

    Returns:
    Os arquivos que compõe o arquivo original .zip descompactados especificados em 'file'
    na pasta dada pelo caminho especificado no print statement na função
    """
    year = year
    state = str(state.upper())
    if year not in UF_range:
        print('O estado escolhido não corresponde a uma UF válida')
        print('Favor escolher uma UF dentre as apresentadas a seguir')
        print(UF_range)
    if year not in year_range:
        print('O ano escolhido não corresponde a um ano de eleições válido')
        print('Favor escolher um ano dentre os apresentados a seguir:')
        print(year_range)
    else:
        url = "https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/votacao_secao_{}_{}.zip".format(year, state)
        fname = "votos_gerais_{}.zip".format(year)
        response = requests.get(url, stream=True)
        total_size_in_bytes= int(response.headers.get('content-length', 0))
        block_size = 1024 #1 Kibibyte
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(fname, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("ERROR, something went wrong")
        if extract == True:
            extract_data(fname, path='./data/{}/votos_secao_{}'.format(year,state))
            print('\n Os arquivos com os dados foram extraídos para o caminho ./data/{}/votos_secao_candidato_{}'.format(year,state))