from hestia_earth.schema import SchemaType, TermTermType
from hestia_earth.utils.api import find_node, search


def get_emission_inputs_production_terms():
    """
    Find all "Inputs Production" `emission` terms from the Glossary:
    https://hestia.earth/glossary?termType=emission&query=Inputs Production

    Returns
    -------
    list
        List of matching term `@id` as `str`.
    """
    terms = find_node(SchemaType.TERM, {
        'termType': TermTermType.EMISSION.value,
        'name': 'Inputs Production'
    })
    return list(map(lambda n: n['@id'], terms))


def get_liquid_fuel_terms() -> list:
    """
    Find all "liquid" `fuel` terms from the Glossary:
    - https://hestia.earth/glossary?termType=fuel&query=gasoline
    - https://hestia.earth/glossary?termType=fuel&query=diesel

    Returns
    -------
    list
        List of matching term `@id` as `str`.
    """
    terms = search({
        "bool": {
            "must": [
                {
                    "match": {
                        "@type": SchemaType.TERM.value
                    }
                },
                {
                    "match": {
                        "termType": TermTermType.FUEL.value
                    }
                }
            ],
            "should": [
                {
                    "regexp": {
                        "name": "gasoline*"
                    }
                },
                {
                    "regexp": {
                        "name": "diesel*"
                    }
                }
            ],
            "minimum_should_match": 1
        }
    })
    return list(map(lambda n: n['@id'], terms))


def get_irrigation_terms() -> list:
    """
    Find all `water` terms from the Glossary:
    https://hestia.earth/glossary?termType=water

    Returns
    -------
    list
        List of matching term `@id` as `str`.
    """
    terms = find_node(SchemaType.TERM, {
        'termType': TermTermType.WATER.value
    })
    return list(map(lambda n: n['@id'], terms))


def get_urea_terms():
    """
    Find all `inorganicFertilizer` urea terms from the Glossary:
    https://hestia.earth/glossary?termType=inorganicFertilizer&query=urea

    Returns
    -------
    list
        List of matching term `@id` as `str`.
    """
    terms = find_node(SchemaType.TERM, {
        'termType': TermTermType.INORGANICFERTILIZER.value,
        'name': 'urea'
    })
    return list(map(lambda n: n['@id'], terms))
