from hestia_earth.schema import SchemaType
from hestia_earth.utils.api import download_hestia, find_related


def related_cycles(site_id: str):
    """
    Get the list of `Cycle` related to the `Site`.

    In Hestia, a `Cycle` must have a link to a `Site`, therefore a `Site` can be related to many `Cycle`s.

    Parameters
    ----------
    site_id : str
        The `@id` of the `Site`.

    Returns
    -------
    list[dict]
        The related `Cycle`s as `dict`.
    """
    nodes = find_related(SchemaType.SITE, site_id, SchemaType.CYCLE)
    return [] if nodes is None else list(map(lambda node: download_hestia(node.get('@id'), SchemaType.CYCLE), nodes))
