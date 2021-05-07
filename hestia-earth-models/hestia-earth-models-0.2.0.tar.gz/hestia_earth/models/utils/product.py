from hestia_earth.schema import SchemaType, TermTermType
from hestia_earth.utils.api import download_hestia
from hestia_earth.utils.model import find_term_match, linked_node
from hestia_earth.utils.tools import list_average, list_sum, safe_parse_float

from . import _term_id, _include_methodModel, _filter_list_term_type, _filter_list_term_unit
from .constant import Units
from .cycle import _is_term_type_complete
from .property import get_node_property


def _new_product(term, model=None):
    node = {'@type': SchemaType.PRODUCT.value}
    node['term'] = linked_node(term if isinstance(term, dict) else download_hestia(_term_id(term)))
    return _include_methodModel(node, model)


def _get_nitrogen_content(product: dict):
    return safe_parse_float(find_term_match(product.get('properties', []), 'nitrogenContent').get('value', '0'))


def abg_total_residue_nitrogen(products: list):
    """
    Get the total above ground nitrogen content from the `aboveGroundCropResidueTotal` product.

    Parameters
    ----------
    products : list
        List of `Product`s.

    Returns
    -------
    float
        The total value as a number.
    """
    total = find_term_match(products, 'aboveGroundCropResidueTotal')
    return _get_nitrogen_content(total)


def abg_residue_nitrogen(products: list):
    """
    Get the total nitrogen content from all the `aboveGroundCropResidue` products.

    Parameters
    ----------
    products : list
        List of `Product`s.

    Returns
    -------
    float
        The total value as a number.
    """
    left_on_field = find_term_match(products, 'aboveGroundCropResidueLeftOnField').get('value', [0])
    incorporated = find_term_match(products, 'aboveGroundCropResidueIncorporated').get('value', [0])
    return list_sum(left_on_field + incorporated) * abg_total_residue_nitrogen(products) / 100


def blg_residue_nitrogen(products: list):
    """
    Get the total nitrogen content from the `belowGroundCropResidue` product.

    Parameters
    ----------
    products : list
        List of `Product`s.

    Returns
    -------
    float
        The total value as a number.
    """
    residue = find_term_match(products, 'belowGroundCropResidue')
    return list_sum(residue.get('value', [0])) * _get_nitrogen_content(residue) / 100


def residue_nitrogen(products: list) -> float:
    """
    Get the total nitrogen content from the `cropResidue` products.

    Parameters
    ----------
    products : list
        List of `Product`s.

    Returns
    -------
    float
        The total value as a number.
    """
    return abg_residue_nitrogen(products) + blg_residue_nitrogen(products)


def get_animal_product_N_total(cycle: dict) -> float:
    """
    Get the total nitrogen content of animal products used in the Cycle.

    The result is the sum of every animal product specified in `kg N` as a `Product`.

    Note: in the event where `dataCompleteness.products` is set to `True` and there are no animal products used,
    `0` will be returned.

    Parameters
    ----------
    cycle : dict
        The `Cycle` as defined in the Hestia Schema.

    Returns
    -------
    float
        The total value as a number.
    """
    products = _filter_list_term_unit(cycle.get('products', []), Units.KG_N)
    products = _filter_list_term_type(products, TermTermType.ANIMALPRODUCT)
    values = [list_sum(i.get('value'), 0) for i in products if len(i.get('value', [])) > 0]
    return 0 if len(values) == 0 and _is_term_type_complete(cycle, {'termType': 'products'}) else list_sum(values)


def get_average_rooting_depth(cycle: dict) -> float:
    properties = list(map(lambda p: get_node_property(p, 'rootingDepth'), cycle.get('products', [])))
    return list_average([
        safe_parse_float(p.get('value', [])) for p in properties if p is not None
    ])
