from hestia_earth.schema import EmissionMethodTier
from hestia_earth.utils.tools import list_sum

from hestia_earth.models.log import logger
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.input import (get_animal_product_P_total,
                                             get_inorganic_fertilizer_P_total,
                                             get_organic_fertilizer_P_total)
from hestia_earth.models.utils.measurement import _most_relevant_measurement_value
from . import MODEL
from .utils import get_liquid_slurry_sludge_ratio

TERM_ID = 'pToSurfacewaterAllOrigins'


def _emission(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_1.value
    return emission


def _run(cycle: dict, slope: list, P_total: float, inorg_p_total: float, excrete_p_total: float):
    lss_ratio = get_liquid_slurry_sludge_ratio(cycle)
    value_slope = 0 if list_sum(slope) < 3 else 1
    value_lss = lss_ratio if lss_ratio else 0
    value_inorg_lss = 1 + inorg_p_total * 0.2/80 + P_total * 0.7/80 * (value_lss)
    value = value_slope * (value_inorg_lss + (P_total * value_lss + excrete_p_total) * 0.4/80)
    return [_emission(value)]


def _should_run(cycle: dict):
    end_date = cycle.get('endDate')
    site = cycle.get('site', {})
    measurements = site.get('measurements', [])
    slope = _most_relevant_measurement_value(measurements, 'slope', end_date)
    inorg_p_total = get_inorganic_fertilizer_P_total(cycle)
    excrete_p_total = get_animal_product_P_total(cycle)
    P_total = get_organic_fertilizer_P_total(cycle)

    should_run = P_total > 0 and inorg_p_total > 0 and excrete_p_total > 0 and len(slope) > 0
    logger.info('term=%s, should_run=%s', TERM_ID, should_run)

    return should_run, slope, P_total, inorg_p_total, excrete_p_total


def run(cycle: dict):
    should_run, slope, P_total, inorg_p_total, excrete_p_total = _should_run(cycle)
    return _run(cycle, slope, P_total, inorg_p_total, excrete_p_total) if should_run else []
