from hestia_earth.schema import EmissionMethodTier
from hestia_earth.utils.model import find_term_match

from hestia_earth.models.log import logger
from hestia_earth.models.utils.input import get_organic_fertilizer_N_total
from hestia_earth.models.utils.emission import _new_emission
from .utils import get_nh3_nox, get_no3_value, COEFF_NH3NOX_N20
from . import MODEL

TERM_ID = 'n2OToAirOrganicFertilizerIndirect'
NO3_TERM_ID = 'no3ToGroundwaterOrganicFertilizer'
NH3_TERM_ID = 'nh3ToAirOrganicFertilizer'
NOX_TERM_ID = 'noxToAirOrganicFertilizer'


def _emission(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_1.value
    return emission


def _run(cycle: dict, N_total: float, no3: list):
    nh3, nox = get_nh3_nox(cycle, NH3_TERM_ID, NOX_TERM_ID)
    no3 = get_no3_value(no3)
    value = COEFF_NH3NOX_N20 * (N_total * 0.2 if nox == 0 or nh3 == 0 else nh3 + nox) + no3
    return [_emission(value)]


def _should_run(cycle: dict):
    N_total = get_organic_fertilizer_N_total(cycle)
    no3 = find_term_match(cycle.get('emissions', []), NO3_TERM_ID).get('value', [])
    should_run = N_total > 0 and len(no3) > 0
    logger.info('term=%s, should_run=%s', TERM_ID, should_run)
    return should_run, N_total, no3


def run(cycle: dict):
    should_run, N_total, no3 = _should_run(cycle)
    return _run(cycle, N_total, no3) if should_run else []
