#organiza as pastas de arquivos, movendo e renomeando
#fonte: https://www.youtube.com/watch?v=qbW6FRbaSl0
from forg import *
import os
import sys
import importlib_resources
import json
import time
import pandas as pd

# def insert_list_df(lista, DataFrame quadroDados, String tipo):
#     tipo = 
#     quadroDados.insert(0, "Extension", lista, True)
#     for l in lista:
#         quadroDados.insert(1, "mime", tipo, True)
#     return quadroDados


def forg():
    VIDEOEXT = [".avi",".mp4",".mpeg",".m4v",".mov",".ogv",".ts",".webm",".3gp",".3g2",".wmv",".mkv"]
    APPLICATIONSEXT = [".abw",".arc",".azw",".bin",".bz",".bz2",".csh",".dmg",".eot",".epub",".gz",".jar",".js",".json",".jsonld",".cda",".mpkg",".ogx",".ogg",".php",".rar",".sh",".swf",".tar",".vsd",".xhtml",".xls",".xlsx",".xml",".xul",".zip",".7z",".pkg",".pem",".pkpass"]
    AUDIOEXT = [".aac",".mid",".midi",".mp3",".m4a",".oga",".opus",".wav",".weba",".wma",".m3u8"]
    IMAGEEXT = [".bmp",".gif",".ico",".jpeg",".jpg",".JPG",".png",".svg",".tif",".tiff",".webp",".png",".dwg",".ai",".cdr",".psd"]
    FONTEXT = [".otf",".ttf",".woff",".woff2"]
    DOCUMENTEXT  = [".doc",".docx",".htm",".html",".ics",".odp",".ods",".odt",".pdf",".ppt",".pptx",".rtf",".txt",".ppsx",".notesairdropdocument",".xlsm",".torrent",".srt",".css",".csv",".mjs",".key",".pages"]
    BOOKEXT = [".mobi",".azw3",".djvu"]
    RECEITAEXT = [".rec",".dec",".dbk"]
    #data_dir = os.path.join(os.path.dirname(__file__), 'tests', 'data')
    
    extensoes = {'video': VIDEOEXT,
    'application': APPLICATIONSEXT,
    'audio': AUDIOEXT,
    'image': IMAGEEXT,
    'font': FONTEXT,
    'document': DOCUMENTEXT,
    'book': BOOKEXT,
    'receita':RECEITAEXT
    }

    extensoes_list = [VIDEOEXT]
    extensoes_list.append(APPLICATIONSEXT)
    extensoes_list.append(AUDIOEXT)
    extensoes_list.append(IMAGEEXT)
    extensoes_list.append(FONTEXT)
    extensoes_list.append(DOCUMENTEXT)
    extensoes_list.append(BOOKEXT)
    extensoes_list.append(RECEITAEXT)
    formato = ".docx"
    mime = "other"
    
    confirma = input(Gerar forg? y | n‘)
    if confirma != "y":
        print("You cancelled forg. Nothing changed!")
        sys.exit()
    #data_path = os.path.join(data_dir, 'message.eml')
    #ocsv = importlib_resources.files('data').joinpath('filesext.csv')
    #with ocsv.open() as fp:
     #   my_bytes = fp.read()
        #print(my_bytes)

    #print(ocsv)``

    #df = pd.DataFrame(Extensoes)
    #mime = pd.DataFrame()
    
    folder_to_track = os.getcwd() # '/Users/rodrigofreitas/Documents' #
    folder_destination = folder_to_track + "/forg"



    #CREATE PASTA FORG IF IT DOESN'T EXISTS
    if not os.path.isdir(folder_to_track + "/forg"):
        os.makedirs(folder_to_track + "/forg")


    for filename in os.listdir(folder_to_track):

        #pega extensao
        lfilext = filename.split('.')
        filext = lfilext[-1]
        componto = "." + filext.lower()
        for i in range(len(extensoes_list)):
            for j in range(len(extensoes_list[i])):
                tupla = str(extensoes_list[i][j])
                if tupla == componto:
                    print(i)
                    if i == 0:
                        mime = "video"
                    elif i == 1:
                        mime = "application"
                    elif i == 2:
                        mime = "audio"
                    elif i == 3:
                        mime = "images"
                    elif i == 4:
                        mime = "fonts"
                    elif i == 5:
                        mime = "documents"
                    elif i == 6:
                        mime = "books"
                    elif i == 7:
                        mime = "receita"
        #checa tipo de midia
        # mime = df.loc[df.Extension == componto,'mime']
        
        # checa se ja existe a pasta, se nao, cria a pasta
        destEnd = folder_destination + "/" + mime
        if not os.path.isdir(destEnd):
            os.makedirs(destEnd)
            print("created folder : ", destEnd)
        src = folder_to_track + "/" + filename
        new_destination = destEnd + "/" + filename
        os.rename(src, new_destination)

def main():
    forg()              
#main
if __name__ == '__main__':
    main()