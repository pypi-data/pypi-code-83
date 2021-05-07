from hestia_earth.schema import EmissionMethodTier, TermTermType
from hestia_earth.utils.lookup import column_name, download_lookup, get_table_value, extract_grouped_data
from hestia_earth.utils.model import find_term_match
from hestia_earth.utils.tools import list_average, list_sum, safe_parse_float

from hestia_earth.models.log import logger
from hestia_earth.models.utils import _filter_list_term_type, _filter_list_term_unit
from hestia_earth.models.utils.constant import Units
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.measurement import _most_relevant_measurement_value
from . import MODEL

TERM_ID = 'nh3ToAirInorganicFertilizer'


def _emission(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_2.value
    return emission


def _get_temperature_lookup_key(temperature: float):
    return 'cool' if temperature <= 14 else ('temperate' if temperature <= 25 else 'warm')


def _get_soilPh_lookup_key(soilPh: float):
    return 'acidic' if soilPh < 7 else 'basic'


def _get_input_factor(term_id: str, soilPh_key: str, temperature_key: str):
    lookup = download_lookup('inorganicFertilizer.csv', True)
    data = get_table_value(lookup, 'termid', term_id, column_name(f"NH3_emissions_factor_{soilPh_key}"))
    return safe_parse_float(extract_grouped_data(data, temperature_key), 1)


def _get_input_value(soilPh_key: str, temperature_key: str):
    def get_value(input: dict):
        term_id = input.get('term', {}).get('@id')
        factor = _get_input_factor(term_id, soilPh_key, temperature_key)
        logger.debug('factor for Term: %s = %s', term_id, factor)
        return list_sum(input.get('value')) * factor
    return get_value


def _run(temperature: float, soilPh: float, inputs: float):
    soilPh_key = _get_soilPh_lookup_key(soilPh)
    temperature_key = _get_temperature_lookup_key(temperature)
    value = list_sum(list(map(_get_input_value(soilPh_key, temperature_key), inputs)))
    return [_emission(value)]


def _should_run(cycle: dict):
    end_date = cycle.get('endDate')
    site = cycle.get('site', {})
    measurements = site.get('measurements', [])
    soilPh = _most_relevant_measurement_value(measurements, 'soilPh', end_date)
    temperature = _most_relevant_measurement_value(measurements, 'temperatureAnnual', end_date)
    temperature = _most_relevant_measurement_value(
        measurements, 'temperatureLongTermAnnualMean', end_date) if len(temperature) == 0 else temperature

    inputs = _filter_list_term_type(cycle.get('inputs', []), TermTermType.INORGANICFERTILIZER)
    has_unspecified_as_n = find_term_match(inputs, 'inorganicNitrogenFertilizerUnspecifiedAsN', None)

    kg_N_inputs = _filter_list_term_unit(inputs, Units.KG_N)

    should_run = len(temperature) > 0 \
        and len(soilPh) > 0 \
        and not has_unspecified_as_n \
        and len(kg_N_inputs) > 0
    logger.info('term=%s, should_run=%s', TERM_ID, should_run)

    return should_run, list_average(temperature), list_average(soilPh), kg_N_inputs


def run(cycle: dict):
    should_run, temperature, soilPh, inputs = _should_run(cycle)
    return _run(temperature, soilPh, inputs) if should_run else []
