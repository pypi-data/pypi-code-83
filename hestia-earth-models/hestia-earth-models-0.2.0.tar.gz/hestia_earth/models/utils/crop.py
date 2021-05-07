from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name
from hestia_earth.utils.tools import safe_parse_float

TONNE_TO_KG = 1000
HECTAR_TO_M2 = 10000


def get_crop_grouping(term_id: str):
    lookup = download_lookup('crop.csv', True)
    return get_table_value(lookup, 'termid', term_id, column_name('cropGroupingFAOSTAT'))


def get_emission_factor(factor: str, term_id: str, lookup_col: str):
    lookup = download_lookup(f"region-crop-cropGroupingFAOSTAT-{factor}.csv", True)
    return safe_parse_float(get_table_value(lookup, 'termid', term_id, column_name(lookup_col)), None)
