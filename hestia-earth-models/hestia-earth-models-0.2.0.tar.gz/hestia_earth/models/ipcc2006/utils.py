from hestia_earth.utils.model import find_term_match, find_primary_product
from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name
from hestia_earth.utils.tools import list_sum, safe_parse_float

from hestia_earth.models.utils.constant import Units, get_atomic_conversion

COEFF_NH3NOX_N20 = 0.01 * get_atomic_conversion(Units.KG_N2O, Units.TO_N)


def get_nh3_nox(cycle: dict, nh3_term_id: str, nox_term_id: str):
    nh3 = list_sum(find_term_match(cycle.get('emissions'), nh3_term_id).get('value', [0]))
    nh3 = nh3 / get_atomic_conversion(Units.KG_NH3, Units.TO_N)
    nox = list_sum(find_term_match(cycle.get('emissions'), nox_term_id).get('value', [0]))
    nox = nox / get_atomic_conversion(Units.KG_NOX, Units.TO_N)
    return nh3, nox


def get_no3_value(no3: list):
    return (
        list_sum(no3) / get_atomic_conversion(Units.KG_NO3, Units.TO_N)
    ) * 0.0075 * get_atomic_conversion(Units.KG_N2O, Units.TO_N)


def get_N2ON_fertilizer_coeff_from_primary_product(cycle: dict):
    product = find_primary_product(cycle)
    term_id = product.get('term', {}).get('@id') if product else None
    lookup = download_lookup('crop.csv', True)
    percent = get_table_value(lookup, 'termid', term_id, column_name('N2ON_FERT')) if term_id else None
    return safe_parse_float(percent, 0.01)


def get_N_N2O_excreate_coeff_from_primary_product(cycle: dict):
    product = find_primary_product(cycle)
    term_id = product.get('term', {}).get('@id') if product else None
    # TODO: should use the coefficient from lookup table
    # lookup = download_lookup('animalProduct.csv', True)
    # percent = get_table_value(lookup, 'termid', term_id, column_name('<col>')) if term_id else None
    # return safe_parse_float(percent, 0.02)
    has_sheep_goat_products = term_id in ['sheep', 'goat']
    return 0.01 if has_sheep_goat_products else 0.02
