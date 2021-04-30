import pkg_resources
import pandas as pd
from sortedcontainers import SortedSet

def df_to_patterns(df : pd.DataFrame) :
    transactions = []
    for idx, row in df.iterrows() :
        transaction = SortedSet()
        for col in df.columns:
            item = (col, df.loc[idx].at[col])
            transaction.add(item)
        transactions.append(transaction)
    return transactions

def get_simple_housing() :
    return pd.DataFrame({
        'property-type' : ['cottage', 'cottage', 'cottage', 'appartment', 'appartment', 'appartment'],
        'state': ['v. good', 'v. good', 'excellent', 'excellent', 'good', 'good'],
        'rooms' : [5, 3, 3, 5, 4, 3],
        'surface' : [120, 55, 50, 85, 52, 45]
    }, index=[0, 1, 2, 3, 4, 5]), pd.Series([510, 410, 350, 320, 140, 125], index=[0, 1, 2, 3, 4, 5])

## Fetch the CPU dataset
def get_cpu() :
    cpu_types = {'Data': str, 'Ext': str, 'CHMIN' : int}
    stream = pkg_resources.resource_stream(__name__, 'resources/datasets/cpu.data')
    cpu = pd.read_csv(stream, dtype=cpu_types)
    y = cpu['ERP']
    del cpu['ERP']

    return cpu, y

def get_wine_quality() :
    winequality = pd.read_csv('hipar/resources/datasets/winequality.csv')
    winequality = winequality.dropna().reset_index(drop=True)
    y = winequality['quality']
    del winequality['quality']

    return winequality, y

def get_ifv_vine_diseases(simplified=False, target_variable='mfi', sample_size=None, remove_zeros=False) :
    vine_types = {'stade_pheno' : str, 'insee_parcelle' : str}
    vine_diseases = pd.read_csv('hipar/resources/datasets/vine_diseases_clean.csv',
                                dtype=vine_types, error_bad_lines=False)

    if remove_zeros :
        vine_diseases = vine_diseases.loc[vine_diseases[target_variable] > 0.0].reset_index(drop=True)

    if sample_size is not None :
        vine_diseases = vine_diseases.sample(n=sample_size)
    vine_diseases = vine_diseases.dropna().reset_index(drop=True)

    vine_diseases = vine_diseases[vine_diseases['type_suivi'] == 'TNT']
    columns = ['ETP', 'ETP_sum_4w', 'HR', 'HR_sum_4w', 'RG', 'RG_sum_4w', 'RR_dry_days', 'RR_rainy_days', 'RR_sum',
               'RS', 'T_growing_day_degree', 'T_sum', 'T_sum_amplitude', 'TN_above_11c', 'TX_above_25c', 'V10', 'V10_sum_4w',
               'cepage', 'commune_parcelle', 'latitude', 'longitude', target_variable,
               target_variable + '_avg_4w', 'semaine_obs', 'stade_pheno', 'year' ]
    if simplified :
        columns = [x for x in columns if x not in ['ETP', 'HR', 'RG', 'V10', 'insee_parcelle', 'latitude', 'longitude']]
    vine_diseases = vine_diseases[columns]




    vine_diseases = vine_diseases.reset_index(drop=True)
    y = vine_diseases[target_variable]
    del vine_diseases[target_variable]


    return vine_diseases, y