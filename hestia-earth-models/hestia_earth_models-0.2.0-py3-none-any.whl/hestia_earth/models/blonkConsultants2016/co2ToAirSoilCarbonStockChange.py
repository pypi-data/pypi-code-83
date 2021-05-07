from hestia_earth.schema import EmissionMethodTier
from hestia_earth.utils.model import find_primary_product
from hestia_earth.utils.tools import list_average

from hestia_earth.models.log import logger
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.measurement import _most_relevant_measurement_value
from hestia_earth.models.utils.crop import get_crop_grouping, get_emission_factor, TONNE_TO_KG, HECTAR_TO_M2
from . import MODEL

TERM_ID = 'co2ToAirSoilCarbonStockChange'


def _emission(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_1.value
    return emission


def _run(landOccupation: float, factors: list):
    value = landOccupation * sum(factors) * TONNE_TO_KG / HECTAR_TO_M2
    return [_emission(value)]


def _should_run(cycle: dict):
    end_date = cycle.get('endDate')
    site = cycle.get('site', {})
    country_id = site.get('country', {}).get('@id')
    measurements = site.get('measurements', [])
    landOccupation = _most_relevant_measurement_value(measurements, 'landOccupation', end_date)

    primary_product = find_primary_product(cycle)
    crop_grouping = get_crop_grouping(primary_product.get('term', {}).get('@id')) if primary_product else None

    co2landuse = get_emission_factor(
        factor='co2landuse',
        term_id=country_id,
        lookup_col=crop_grouping) if country_id and crop_grouping else None

    factors = [co2landuse]

    should_run = len(landOccupation) > 0 and all([factor is not None for factor in factors])
    logger.info('term=%s, should_run=%s', TERM_ID, should_run)
    return should_run, list_average(landOccupation), factors


def run(cycle: dict):
    should_run, landOccupation, factors = _should_run(cycle)
    return _run(landOccupation, factors) if should_run else []
