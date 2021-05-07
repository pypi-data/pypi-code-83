from hestia_earth.utils.tools import list_sum

from hestia_earth.models.log import logger
from hestia_earth.models.utils.impact_assessment import get_product
from hestia_earth.models.utils.indicator import _new_indicator


def _indicator(term: str, value: float):
    logger.info('term=%s, value=%s', term.get('@id'), value)
    indicator = _new_indicator(term)
    indicator['value'] = value
    return indicator


def _run_emission(product: dict):
    def run(emission: dict):
        economic_value = product.get('economicValueShare') / 100
        product_value = list_sum(product.get('value', [0]))
        emission_value = list_sum(emission.get('value', [0]))
        return _indicator(emission.get('term', {}), emission_value / product_value * economic_value)
    return run


def _should_run(impact_assessment: dict):
    product = get_product(impact_assessment)
    economic_value = product.get('economicValueShare') if product else None
    should_run = economic_value is not None
    logger.info('should_run=%s', should_run)
    return should_run, product


def run(impact_assessment: dict):
    should_run, product = _should_run(impact_assessment)
    emissions = impact_assessment.get('cycle', {}).get('emissions', [])
    return list(map(_run_emission(product), emissions)) if should_run else []
