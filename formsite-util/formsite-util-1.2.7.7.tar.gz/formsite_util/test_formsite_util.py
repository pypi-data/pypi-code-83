from formsite_util.core import FormsiteInterface, FormsiteCredentials, FormsiteParams
import os
import pandas as pd
from pathlib import Path
EXAMPLE_DATA_DIR = r"C:\Users\Jakub Strnad\source\formsite-utility\example_results"



def LoadExampleData(ex_dir) -> tuple[str,list[str],pd.DataFrame,set[str]]:
    results=[]
    for file in os.listdir(ex_dir):
        if file.endswith(r'.pkl'):
            export = pd.read_pickle(f"{ex_dir}/{file}")
        with open(f"{ex_dir}/{file}", 'rb') as reader:
            if file.startswith(r'items'):
                items = reader.read().decode('utf-8')
                items = items.replace('\r\n','\n')
            if file.startswith(r'results'):
                res = reader.read().decode('utf-8')
                res = res.replace('\r\n','\n')
                results.append(res)
            if file.startswith(r'links'):
                links=reader.read().decode('utf-8')
                if '\r\n' in links:
                    links = set(links.split('\r\n'))
                else:
                    links = set(links.split('\n'))
    try:
        links.remove('')
    except KeyError:
        pass
    
    return items, results, export, links

def Process(items, results) -> tuple[pd.DataFrame, set]:
    interface = FormsiteInterface('',FormsiteCredentials('','fs4','wIbuk0'), params=FormsiteParams(timezone='America/Chicago'))
    interface.Data = interface._assemble_dataframe(items, results)
    return interface.Data, interface.ReturnLinks()

def test_processing(folder):
    items, results, export_final, links_final = LoadExampleData(folder)
    export_local, links_local = Process(items,results)

    assert links_local == links_final
    assert pd.concat([export_final,export_local]).drop_duplicates(keep=False).shape[0] == 0
    assert set(export_final.columns).symmetric_difference(export_local.columns) == set()

def test_download(links):
    pass


test_processing(r'C:/Users/Jakub Strnad/source/formsite-utility/example_results/fluvia')
test_processing(r'C:/Users/Jakub Strnad/source/formsite-utility/example_results/gaq')
test_processing(r'C:/Users/Jakub Strnad/source/formsite-utility/example_results/leda')
test_processing(r'C:/Users/Jakub Strnad/source/formsite-utility/example_results/mandovi')

test_download()