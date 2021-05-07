from functools import reduce
from hestia_earth.utils.model import find_term_match
from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name
from hestia_earth.utils.tools import list_sum, safe_parse_float

from hestia_earth.models.log import logger
from hestia_earth.models.data.impact_assessments import _load_impacts


def _get_impacts_dict():
    def merge_emission(prev: dict, emission: dict):
        key = emission.get('term', {}).get('@id')
        prev[key] = prev.get(key, []) + [float(emission.get('value'))]
        return prev

    def merge_impact(prev: dict, impact: dict):
        key = impact.get('product', {}).get('@id')
        prev[key] = reduce(merge_emission, impact.get('emissionsResourceUse', []), prev.get(key, {}))
        return prev

    impacts = _load_impacts()
    return reduce(merge_impact, impacts, {})


def get_product(impact_assessment: dict) -> dict:
    """
    Get the full `Product` from the `ImpactAssessment.cycle`.

    Parameters
    ----------
    impact_assessment : dict
        The `ImpactAssessment`.

    Returns
    -------
    dict
        The `Product` of the `ImpactAssessment`.
    """
    product = impact_assessment.get('product', {})
    products = impact_assessment.get('cycle', {}).get('products', [])
    return find_term_match(products, product.get('@id'), None)


def _emission_value(lookup, lookup_col: str):
    def get_value(emission: dict):
        term_id = emission.get('term', {}).get('@id')
        # TODO: remove replace - when fixed in utils
        data = get_table_value(lookup, 'termid', term_id, column_name(lookup_col).replace('-', ''))
        value = emission.get('value', 0)
        coefficient = safe_parse_float(data)
        logger.debug('term=%s, value=%s, coefficient=%s', term_id, value, coefficient)
        return value * coefficient
    return get_value


def impact_value(impact: dict, lookup_col: str) -> float:
    lookup = download_lookup('emission.csv', True)
    return list_sum(list(map(_emission_value(lookup, lookup_col), impact.get('emissionsResourceUse', []))))
