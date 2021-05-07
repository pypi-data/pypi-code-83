import numpy as np
from hestia_earth.schema import EmissionMethodTier
from hestia_earth.utils.tools import list_average, list_sum

from hestia_earth.models.log import logger
from hestia_earth.models.utils.constant import Units, get_atomic_conversion
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.input import get_total_nitrogen
from hestia_earth.models.utils.product import residue_nitrogen
from hestia_earth.models.utils.measurement import _most_relevant_measurement_value
from . import MODEL

TERM_ID = 'noxToAirAllOrigins'
NOX_FACTORS_BY_CLIMATE_ZONE = {
    '1': 0.5189,
    '2': 0.5189,
    '3': 0.3511,
    '4': 0.0,
    '5': 0.3511,
    '6': 0.0,
    '7': 0.3511,
    '8': 0.0,
    '9': 1.1167,
    '10': 1.1167,
    '11': 1.1167,
    '12': 1.1167,
    '13': 1.1167
}


def _should_run(cycle: dict):
    end_date = cycle.get('endDate')
    site = cycle.get('site', {})
    measurements = site.get('measurements', [])
    ecoClimateZone = _most_relevant_measurement_value(measurements, 'ecoClimateZone', end_date)
    ecoClimateZone = str(ecoClimateZone[0]) if len(ecoClimateZone) > 0 else None
    nitrogenContent = list_average(_most_relevant_measurement_value(measurements, 'soilTotalNitrogenContent', end_date))

    residue = residue_nitrogen(cycle.get('products', []))
    logger.debug('residue, value=%s', residue)

    N_total = list_sum(get_total_nitrogen(cycle.get('inputs', [])) + [residue])
    logger.debug('N_total, value=%s', N_total)

    should_run = ecoClimateZone is not None and nitrogenContent is not None and N_total > 0
    logger.info('term=%s, should_run=%s', TERM_ID, should_run)
    return should_run, ecoClimateZone, nitrogenContent, N_total, residue


def _get_value(ecoClimateZone: str, nitrogenContent: float, N_total: float):
    eco_factor = NOX_FACTORS_BY_CLIMATE_ZONE[ecoClimateZone]
    n_factor = 0 if nitrogenContent / 1000000 < 0.0005 else -1.0211 if nitrogenContent / 1000000 <= 0.002 else 0.7892
    value = min(
        0.025 * N_total,
        np.exp(-0.451 + 0.0061 * N_total + n_factor + eco_factor) -
        np.exp(-0.451 + n_factor + eco_factor)
    ) * get_atomic_conversion(Units.KG_NOX, Units.TO_N)
    logger.info('term=%s, value=%s', TERM_ID, value)
    return value


def _emission(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_2.value
    return emission


def _run(eecoClimateZone: str, nitrogenContent: float, N_total: float):
    value = _get_value(eecoClimateZone, nitrogenContent, N_total)
    return [_emission(value)]


def run(cycle: dict):
    should_run, ecoClimateZone, nitrogenContent, N_total, *args = _should_run(cycle)
    return _run(ecoClimateZone, nitrogenContent, N_total) if should_run else []
