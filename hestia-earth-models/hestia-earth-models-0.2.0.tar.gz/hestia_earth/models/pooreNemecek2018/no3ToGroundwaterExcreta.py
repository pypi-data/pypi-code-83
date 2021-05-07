from hestia_earth.schema import EmissionMethodTier

from hestia_earth.models.log import logger
from hestia_earth.models.utils.product import get_animal_product_N_total
from hestia_earth.models.utils.emission import _new_emission
from . import MODEL
from .no3ToGroundwaterAllOrigins import _should_run, _get_value

TERM_ID = 'no3ToGroundwaterExcreta'


def _emission(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_2.value
    return emission


def _run(cycle: dict, content_list_of_items: list):
    noxToAirAllOrigins = _get_value(content_list_of_items)
    value = get_animal_product_N_total(cycle)
    return [_emission(value * noxToAirAllOrigins)]


def run(cycle: dict):
    should_run, content_list_of_items = _should_run(cycle)
    return _run(cycle, content_list_of_items) if should_run else []
