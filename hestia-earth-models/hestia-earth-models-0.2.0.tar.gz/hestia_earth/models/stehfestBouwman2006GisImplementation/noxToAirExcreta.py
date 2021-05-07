from hestia_earth.schema import EmissionMethodTier

from hestia_earth.models.log import logger
from hestia_earth.models.utils.product import get_animal_product_N_total
from hestia_earth.models.utils.emission import _new_emission
from . import MODEL
from .noxToAirAllOrigins import _should_run, _get_value

TERM_ID = 'noxToAirExcreta'


def _emission(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_1.value
    return emission


def _run(cycle: dict, country_id: str, N_total: float):
    noxToAirAllOrigins = _get_value(country_id, N_total)
    value = get_animal_product_N_total(cycle)
    return [_emission(value * noxToAirAllOrigins / N_total)]


def run(cycle: dict):
    should_run, country_id, N_total, *args = _should_run(cycle)
    return _run(cycle, country_id, N_total) if should_run else []
