from hestia_earth.schema import EmissionMethodTier

from hestia_earth.models.log import logger
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.product import residue_nitrogen
from .n2OToAirAllOrigins import _should_run
from . import MODEL

TERM_ID = 'n2OToAirCropResidueDecompositionDirect'
EF_CRES_N_N2O = 0.015711073034911115


def _emission(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_2.value
    return emission


def _run(cycle: dict):
    residue = residue_nitrogen(cycle.get('products', []))
    logger.debug('residue, value=%s', residue)
    value = residue * EF_CRES_N_N2O
    return [_emission(value)]


def run(cycle: dict):
    should_run = _should_run(cycle)
    return _run(cycle) if should_run else []
