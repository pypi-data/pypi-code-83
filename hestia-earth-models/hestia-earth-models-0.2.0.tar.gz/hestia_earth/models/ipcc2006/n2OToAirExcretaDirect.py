from hestia_earth.schema import EmissionMethodTier

from hestia_earth.models.log import logger
from hestia_earth.models.utils.constant import Units, get_atomic_conversion
from hestia_earth.models.utils.input import get_animal_product_N_total
from hestia_earth.models.utils.emission import _new_emission
from . import MODEL
from .utils import get_N_N2O_excreate_coeff_from_primary_product

TERM_ID = 'n2OToAirExcretaDirect'


def _emission(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_1.value
    return emission


def _run(cycle: dict, N_total: float):
    coefficient = get_N_N2O_excreate_coeff_from_primary_product(cycle)
    value = N_total * coefficient * get_atomic_conversion(Units.KG_N2O, Units.TO_N)
    return [_emission(value)]


def _should_run(cycle: dict):
    N_total = get_animal_product_N_total(cycle)
    should_run = N_total > 0
    logger.info('term=%s, should_run=%s', TERM_ID, should_run)
    return should_run, N_total


def run(cycle: dict):
    should_run, N_total = _should_run(cycle)
    return _run(cycle, N_total) if should_run else []
