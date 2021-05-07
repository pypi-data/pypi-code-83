from hestia_earth.schema import EmissionMethodTier
import numpy as np
from hestia_earth.utils.lookup import download_lookup, get_table_value
from hestia_earth.utils.model import find_primary_product
from hestia_earth.utils.tools import list_average, list_sum

from hestia_earth.models.log import logger
from hestia_earth.models.utils.constant import Units, get_atomic_conversion
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.measurement import _most_relevant_measurement_value
from hestia_earth.models.utils.input import get_total_nitrogen
from . import MODEL

TERM_ID = 'n2OToAirAllOrigins'
N2O_FACTORS_BY_CLIMATE_ZONE = {
    '1': 0.6117,
    '2': 0.6117,
    '3': 0.0226,
    '4': 0.0,
    '5': 0.0226,
    '6': 0.0,
    '7': 0.0226,
    '8': 0.0,
    '9': -0.3022,
    '10': -0.3022,
    '11': -0.3022,
    '12': -0.3022,
    '13': -0.3022
}
N2O_FACTORS_BY_CROP = {
    'Cereals': 0,
    'Grass': -0.3502,
    'Legume': 0.3783,
    'Other': 0.4420,
    'W-Rice': -0.8850,
    'None': 0.5870
}


def _get_crop_crouping(product: dict):
    term_id = product.get('term', {}).get('@id') if product else None
    lookup = download_lookup('crop.csv', True)
    return get_table_value(lookup, 'termid', term_id, 'cropgroupingstehfestbouwman')


def _should_run(cycle: dict):
    end_date = cycle.get('endDate')
    site = cycle.get('site', {})
    measurements = site.get('measurements', [])
    clay = _most_relevant_measurement_value(measurements, 'clayContent', end_date)
    logger.debug('clay, value=%s', clay)

    sand = _most_relevant_measurement_value(measurements, 'sandContent', end_date)
    logger.debug('sand, value=%s', sand)

    organicCarbonContent = _most_relevant_measurement_value(measurements, 'soilOrganicCarbonContent', end_date)
    logger.debug('organicCarbonContent, value=%s', organicCarbonContent)

    soilPh = _most_relevant_measurement_value(measurements, 'soilPh', end_date)
    logger.debug('soilPh, value=%s', soilPh)

    ecoClimateZone = _most_relevant_measurement_value(measurements, 'ecoClimateZone', end_date)
    ecoClimateZone = str(ecoClimateZone[0]) if len(ecoClimateZone) > 0 else None
    logger.debug('ecoClimateZone, value=%s', ecoClimateZone)

    product = find_primary_product(cycle)
    crop_grouping = _get_crop_crouping(product) if product else None
    logger.debug('crop_grouping, value=%s', crop_grouping)

    N_total = list_sum(get_total_nitrogen(cycle.get('inputs', [])))
    logger.debug('N_total, value=%s', N_total)

    content_list_of_items = [clay, sand, organicCarbonContent, soilPh, ecoClimateZone, crop_grouping]
    should_run = all(content_list_of_items) and N_total > 0 and crop_grouping in N2O_FACTORS_BY_CROP
    logger.info('term=%s, should_run=%s', TERM_ID, should_run)

    return should_run, N_total, content_list_of_items


def _organic_carbon_factor(organicCarbonContent: float):
    return 0 if organicCarbonContent/100 < 0.01 else (0.0526 if organicCarbonContent/100 <= 0.03 else 0.6334)


def _soilph_factor(soilPh: float):
    return 0 if soilPh < 5.5 else (-0.4836 if soilPh > 7.3 else -0.0693)


def _sand_factor(sand: float, clay: float):
    return 0 if sand/100 > 0.65 and clay/100 < 0.18 else (-0.1528 if sand/100 < 0.65 and clay/100 < 0.35 else 0.4312)


def _get_value(content_list_of_items: list, N_total: float):
    clay, sand, organicCarbonContent, soilPh, ecoClimateZone, crop_grouping = content_list_of_items

    carbon_factr = _organic_carbon_factor(list_average(organicCarbonContent))
    soil_factr = _soilph_factor(list_average(soilPh))
    sand_factr = _sand_factor(list_average(sand), list_average(clay))
    eco_factor = N2O_FACTORS_BY_CLIMATE_ZONE[ecoClimateZone]
    crop_grp_factor = N2O_FACTORS_BY_CROP[crop_grouping]
    factors_sum = sum([carbon_factr, soil_factr, sand_factr, eco_factor, crop_grp_factor])

    value = np.amin(((
        0.072 * N_total,
        np.exp(0.475 + 0.0038 * N_total + factors_sum) - np.exp(0.475 + factors_sum))
    )) * get_atomic_conversion(Units.KG_N2O, Units.TO_N)
    logger.info('term=%s, value=%s', TERM_ID, value)

    return value


def _emission(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_2.value
    return emission


def _run(content_list_of_items: list, N_total: float):
    value = _get_value(content_list_of_items, N_total)
    return [_emission(value)]


def run(cycle: dict):
    should_run, N_total, content_list_of_items = _should_run(cycle)
    return _run(content_list_of_items, N_total) if should_run else []
