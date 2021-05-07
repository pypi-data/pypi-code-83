from hestia_earth.schema import TermTermType
from hestia_earth.utils.tools import list_sum

from hestia_earth.models.utils.input import filter_by_term_type_and_lookup, \
    get_organic_fertilizer_P_total, get_total_phosphate


def get_liquid_slurry_sludge_ratio(cycle: dict):
    lss_inputs = filter_by_term_type_and_lookup(
        cycle.get('inputs', []), TermTermType.ORGANICFERTILIZER,
        col_name='OrganicFertilizerClassification',
        col_value='Liquid, Slurry, Sewage Sludge'
    )
    P_total = get_organic_fertilizer_P_total(cycle)
    P_lss = list_sum(get_total_phosphate(lss_inputs))
    return P_lss / P_total if P_total > 0 else 0
