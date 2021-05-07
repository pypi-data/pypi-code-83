from hestia_earth.schema import SchemaType, TermTermType
from hestia_earth.utils.api import download_hestia
from hestia_earth.utils.model import linked_node
from hestia_earth.utils.tools import list_sum, safe_parse_float
from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name

from . import _term_id, _include_methodModel, _filter_list_term_type, _filter_list_term_unit
from .constant import Units
from .cycle import _is_term_type_complete
from .property import get_node_property


def _new_input(term, model=None):
    node = {'@type': SchemaType.INPUT.value}
    node['term'] = linked_node(term if isinstance(term, dict) else download_hestia(_term_id(term)))
    return _include_methodModel(node, model)


def _input_value(input: dict): return list_sum(input.get('value', []))


def _input_value_as(term_id: str):
    def get_value(input: dict):
        property = get_node_property(input, term_id)
        percent = safe_parse_float(property.get('value')) if property else 100
        # need to multiply value by the nitrogenContent percentage to get final value
        return list_sum(input.get('value', [])) * percent / 100
    return get_value


def get_total_value(inputs: list):
    """
    Get the total `value` of a list of `Input`s.
    This method does not take into account the `units` and possible conversions.

    Parameters
    ----------
    inputs : list
        A list of `Input`.

    Returns
    -------
    list
        The total `value` as a list of numbers.
    """
    return list(map(_input_value, inputs))


def get_total_value_converted(inputs: list, conversion_property: str):
    """
    Get the total `value` of a list of `Input`s converted using a property of the `Input`.

    Parameters
    ----------
    inputs : list
        A list of `Input`.
    conversion_property : str
        Property used for the conversion. Example: `nitrogenContent`.
        See https://hestia.earth/glossary?termType=property for a list of `Property`.

    Returns
    -------
    list
        The total `value` as a list of numbers.
    """
    return list(map(_input_value_as(conversion_property), inputs))


def get_total_nitrogen(inputs: list) -> list:
    """
    Get the total nitrogen content of a list of `Input`s.

    The result contains the values of the following `Input`s:
    1. Every organic fertilizer specified in `kg N` will be used.
    2. Every organic fertilizer specified in `kg` will be multiplied by the `nitrogenContent` of that `Input`.

    Parameters
    ----------
    inputs : list
        A list of `Input`.

    Returns
    -------
    list
        The nitrogen values as a list of numbers.
    """
    kg_N_inputs = _filter_list_term_unit(inputs, Units.KG_N)
    kg_inputs = _filter_list_term_unit(inputs, Units.KG)
    return get_total_value(kg_N_inputs) + get_total_value_converted(kg_inputs, 'nitrogenContent')


def get_total_phosphate(inputs: list) -> list:
    """
    Get the total phosphate content of a list of `Input`s.

    The result contains the values of the following `Input`s:
    1. Every organic fertilizer specified in `kg P2O5` will be used.
    1. Every organic fertilizer specified in `kg N` will be multiplied by the `phosphateContentAsP2O5` of that `Input`.
    2. Every organic fertilizer specified in `kg` will be multiplied by the `phosphateContentAsP2O5` of that `Input`.

    Parameters
    ----------
    inputs : list
        A list of `Input`.

    Returns
    -------
    list
        The nitrogen values as a list of numbers.
    """
    kg_P_inputs = _filter_list_term_unit(inputs, Units.KG_P2O5)
    kg_N_inputs = _filter_list_term_unit(inputs, Units.KG_N)
    kg_inputs = _filter_list_term_unit(inputs, Units.KG)
    return get_total_value(kg_P_inputs) + get_total_value_converted(kg_N_inputs + kg_inputs, 'phosphateContentAsP2O5')


def get_organic_fertilizer_N_total(cycle: dict) -> float:
    """
    Get the total nitrogen content of organic fertilizers used in the Cycle.

    The result contains the values of the following `Input`s:
    1. Every organic fertilizer specified in `kg N` will be used.
    2. Every organic fertilizer specified in `kg` will be multiplied by the `nitrogenContent` of that fertilizer.

    Note: in the event where `dataCompleteness.fertilizer` is set to `True` and there are no organic fertilizers used,
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
    inputs = _filter_list_term_type(cycle.get('inputs', []), TermTermType.ORGANICFERTILIZER)
    values = get_total_nitrogen(inputs)
    return 0 if len(values) == 0 and _is_term_type_complete(cycle, {'termType': 'fertilizer'}) else list_sum(values)


def get_organic_fertilizer_P_total(cycle: dict) -> float:
    """
    Get the total phosphate content of organic fertilizers used in the Cycle.

    The result contains the values of the following `Input`s:
    1. Every organic fertilizer specified in `kg P2O5` will be used.
    2. Every organic fertilizer specified in `kg` will be multiplied by the `nitrogenContent` of that fertilizer.

    Note: in the event where `dataCompleteness.fertilizer` is set to `True` and there are no organic fertilizers used,
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
    inputs = _filter_list_term_type(cycle.get('inputs', []), TermTermType.ORGANICFERTILIZER)
    values = get_total_phosphate(inputs)
    return 0 if len(values) == 0 and _is_term_type_complete(cycle, {'termType': 'fertilizer'}) else list_sum(values)


def get_inorganic_fertilizer_N_total(cycle: dict) -> float:
    """
    Get the total nitrogen content of inorganic fertilizers used in the Cycle.

    The result is the sum of every inorganic fertilizer specified in `kg N` as an `Input`.

    Note: in the event where `dataCompleteness.fertilizer` is set to `True` and there are no inorganic fertilizers used,
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
    inputs = _filter_list_term_type(cycle.get('inputs', []), TermTermType.INORGANICFERTILIZER)
    values = get_total_nitrogen(inputs)
    return 0 if len(values) == 0 and _is_term_type_complete(cycle, {'termType': 'fertilizer'}) else list_sum(values)


def get_inorganic_fertilizer_P_total(cycle: dict) -> float:
    """
    Get the total Phosphate content of inorganic fertilizers used in the Cycle.

    The result is the sum of every inorganic fertilizer specified in `kg P2O5` as an `Input`.

    Note: in the event where `dataCompleteness.fertilizer` is set to `True` and there are no inorganic fertilizers used,
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
    inputs = _filter_list_term_type(cycle.get('inputs', []), TermTermType.INORGANICFERTILIZER)
    values = get_total_phosphate(inputs)
    return 0 if len(values) == 0 and _is_term_type_complete(cycle, {'termType': 'fertilizer'}) else list_sum(values)


def get_animal_product_N_total(cycle: dict) -> float:
    """
    Get the total nitrogen content of animal products used in the Cycle.

    The result is the sum of every animal product specified in `kg N` as an `Input`.

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
    inputs = _filter_list_term_type(cycle.get('inputs', []), TermTermType.ANIMALPRODUCT)
    values = get_total_nitrogen(inputs)
    return 0 if len(values) == 0 and _is_term_type_complete(cycle, {'termType': 'products'}) else list_sum(values)


def get_animal_product_P_total(cycle: dict) -> float:
    """
    Get the total phosphate content of animal products used in the Cycle.

    The result is the sum of every animal product specified in `kg P2O5` as an `Input`.

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
    inputs = _filter_list_term_type(cycle.get('inputs', []), TermTermType.ANIMALPRODUCT)
    values = get_total_phosphate(inputs)
    return 0 if len(values) == 0 and _is_term_type_complete(cycle, {'termType': 'products'}) else list_sum(values)


def filter_by_term_type_and_lookup(inputs: list, term_type: TermTermType, col_name: str, col_value):
    """
    Filter the list of inputs by `termType` and only those matching a lookup table value.

    Parameters
    ----------
    inputs : list
        A list of `Input`.
    term_type : TermTermType
        A termType as described in https://hestia.earth/schema/Term#termType
    col_name : str
        The name of the column in the lookup table.
    col_value : Any
        The cell value matching the row/column in the lookup table.

    Returns
    -------
    list
        A list of `Input`.
    """
    lookup = download_lookup(f"{term_type.value}.csv", True)
    inputs = _filter_list_term_type(inputs, term_type)

    def filter_input(input: dict):
        term_id = input.get('term', {}).get('@id')
        return get_table_value(lookup, 'termid', term_id, column_name(col_name)) == col_value

    return list(filter(filter_input, inputs))
