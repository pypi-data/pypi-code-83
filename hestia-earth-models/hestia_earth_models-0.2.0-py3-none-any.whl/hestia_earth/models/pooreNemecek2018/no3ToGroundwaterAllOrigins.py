from hestia_earth.schema import EmissionMethodTier
from hestia_earth.utils.tools import list_average, list_sum

from hestia_earth.models.log import logger
from hestia_earth.models.utils.constant import Units, get_atomic_conversion
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.input import get_total_nitrogen
from hestia_earth.models.utils.product import get_animal_product_N_total, get_average_rooting_depth, residue_nitrogen
from hestia_earth.models.utils.measurement import _most_relevant_measurement_value
from . import MODEL

TERM_ID = 'no3ToGroundwaterAllOrigins'
MIN_ROOTING_DEPTH = 0.4
MAX_ROOTING_DEPTH = 1.3
MAX_CLAY = 50
MAX_SAND = 85
MIN_RAINFALL = 500
MAX_RAINFALL = 1300


def _low_leaching_conditions(rooting_depth: float, clay: float, sand: float, rainfall: float):
    return (
        rooting_depth > MAX_ROOTING_DEPTH or clay > MAX_CLAY or rainfall < MIN_RAINFALL
    ) and (
        rooting_depth > MIN_ROOTING_DEPTH or sand < MAX_SAND or rainfall < MAX_RAINFALL
    )


def _high_leaching_conditions(rooting_depth: float, clay: float, sand: float, rainfall: float):
    return (
        rooting_depth < MIN_ROOTING_DEPTH or sand > MAX_SAND or rainfall > MAX_RAINFALL
    ) and (
        rooting_depth > MAX_ROOTING_DEPTH or clay < MAX_CLAY or rainfall > MIN_RAINFALL
    )


def _other_leaching_conditions(*args):
    return True


NO3_LEACHING_FACTORS = {
    0.23: _high_leaching_conditions,
    0.067: _low_leaching_conditions,
    0.12: _other_leaching_conditions
}


def _emission(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_2.value
    return emission


def _should_run(cycle: dict):
    end_date = cycle.get('endDate')
    site = cycle.get('site', {})
    measurements = site.get('measurements', [])
    clay = _most_relevant_measurement_value(measurements, 'clayContent', end_date)
    sand = _most_relevant_measurement_value(measurements, 'sandContent', end_date)
    rainfall = _most_relevant_measurement_value(measurements, 'rainfallAnnual', end_date)
    rainfall = _most_relevant_measurement_value(
        measurements, 'rainfallLongTermAnnualMean', end_date) if len(rainfall) == 0 else rainfall

    rooting_depth = get_average_rooting_depth(cycle)

    should_run = len(clay) > 0 and len(sand) > 0 and len(rainfall) > 0 and rooting_depth > 0
    logger.info('term=%s, should_run=%s', TERM_ID, should_run)
    return should_run, [rooting_depth, list_average(clay), list_average(sand), list_average(rainfall)]


def get_leaching_factor(content_list_of_items: list):
    rooting_depth, clay, sand, rainfall = content_list_of_items
    # test conditions one by one and return the value associated for the first one that passes
    return next(
        (key for key, value in NO3_LEACHING_FACTORS.items() if value(rooting_depth, clay, sand, rainfall)),
        0.12  # default value for "Other"
    )


def _get_value(content_list_of_items: list):
    value = get_leaching_factor(content_list_of_items) * get_atomic_conversion(Units.KG_NO3, Units.TO_N)
    logger.info('term=%s, value=%s', TERM_ID, value)
    return value


def _run(cycle: dict, content_list_of_items: list):
    value = _get_value(content_list_of_items)
    residue = residue_nitrogen(cycle.get('products', []))
    # sums up all nitrogen content from all other "no3ToGroundwater" emissions
    N_total = list_sum(
        get_total_nitrogen(cycle.get('inputs', [])) + [get_animal_product_N_total(cycle)] + [residue])
    return [_emission(value * N_total)]


def run(cycle: dict):
    should_run, content_list_of_items = _should_run(cycle)
    return _run(cycle, content_list_of_items) if should_run else []
