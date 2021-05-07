from hestia_earth.schema import EmissionMethodTier, TermTermType

from hestia_earth.models.log import logger
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.product import abg_residue_nitrogen, abg_total_residue_nitrogen
from hestia_earth.models.utils.cycle import _is_term_type_complete
from . import MODEL

TERM_ID = 'nh3ToAirCropResidueDecomposition'


def _emission(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_1.value
    return emission


def _run(residue_nitrogen: float, nitrogenContent: float):
    a = a = min([
        max([(0.38 * 1000 * nitrogenContent/100 - 5.44) / 100, 0]),
        17 / 100
    ])
    value = a * residue_nitrogen * 1.21589
    return [_emission(value)]


def _should_run(cycle: dict):
    products = cycle.get('products', [])
    residue_nitrogen = abg_residue_nitrogen(products)
    nitrogenContent = abg_total_residue_nitrogen(products)

    should_run = (residue_nitrogen > 0 or _is_term_type_complete(cycle, {'termType': TermTermType.CROPRESIDUE.value})) \
        and nitrogenContent > 5
    logger.info('term=%s, should_run=%s', TERM_ID, should_run)
    return should_run, residue_nitrogen, nitrogenContent


def run(cycle: dict):
    should_run, residue_nitrogen, nitrogenContent = _should_run(cycle)
    return _run(residue_nitrogen, nitrogenContent) if should_run else []
