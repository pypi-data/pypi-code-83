from hestia_earth.models.log import logger
from hestia_earth.models.utils.indicator import _new_indicator
from hestia_earth.models.utils.impact_assessment import impact_value
from . import MODEL

TERM_ID = 'terrestrialAcidificationPotentialIncludingFateAverageEurope'
LOOKUP_COLUMN = 'so2EqTerrestrialAcidificationIncludingFateAverageEuropeCml2001Baseline'


def _indicator(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    indicator = _new_indicator(TERM_ID, MODEL)
    indicator['value'] = value
    return indicator


def run(impact_assessment: dict):
    value = impact_value(impact_assessment, LOOKUP_COLUMN)
    return _indicator(value)
