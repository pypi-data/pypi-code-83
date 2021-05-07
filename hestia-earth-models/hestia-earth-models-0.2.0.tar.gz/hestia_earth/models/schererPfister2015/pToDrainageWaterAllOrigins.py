from hestia_earth.schema import EmissionMethodTier
from hestia_earth.utils.tools import list_sum

from hestia_earth.models.log import logger
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.input import get_organic_fertilizer_P_total
from hestia_earth.models.utils.measurement import _most_relevant_measurement_value
from .utils import get_liquid_slurry_sludge_ratio
from . import MODEL

TERM_ID = 'pToDrainageWaterAllOrigins'


def _emission(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_1.value
    return emission


def _run(cycle: dict, drainageClass: list, P_total: float):
    lss_ratio = get_liquid_slurry_sludge_ratio(cycle)
    value = 0.07 * (1 + P_total * 0.2/80 * lss_ratio) * (6 if list_sum(drainageClass) > 3 else 0)
    return [_emission(value)]


def _should_run(cycle: dict):
    end_date = cycle.get('endDate')
    site = cycle.get('site', {})
    measurements = site.get('measurements', [])
    drainageClass = _most_relevant_measurement_value(measurements, 'drainageClass', end_date)
    P_total = get_organic_fertilizer_P_total(cycle)

    should_run = len(drainageClass) > 0 and P_total > 0
    logger.info('term=%s, should_run=%s', TERM_ID, should_run)

    return should_run, drainageClass, P_total


def run(cycle: dict):
    should_run, drainageClass, P_total = _should_run(cycle)
    return _run(cycle, drainageClass, P_total) if should_run else []
