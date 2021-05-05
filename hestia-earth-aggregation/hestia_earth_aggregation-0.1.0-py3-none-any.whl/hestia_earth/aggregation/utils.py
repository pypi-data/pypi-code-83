from functools import reduce
from hestia_earth.utils.tools import safe_parse_float

from .version import VERSION


def _flatten(values: list): return list(reduce(lambda x, y: x + (y if isinstance(y, list) else [y]), values, []))


def _aggregated_version(node: dict, *keys):
    node['aggregated'] = node.get('aggregated', [])
    node['aggregatedVersion'] = node.get('aggregatedVersion', [])
    all_keys = ['value'] if len(keys) == 0 else keys
    for key in all_keys:
        if key in node['aggregated']:
            node.get('aggregatedVersion')[node['aggregated'].index(key)] = VERSION
        else:
            node['aggregated'].append(key)
            node['aggregatedVersion'].append(VERSION)
    return node


def _extract_lookup_closest_date(data: str, year: int):
    # example data: 2000:-;2001:0;2002:0;2003:0;2004:0;2005:0
    data_by_date = reduce(
        lambda prev, curr: {
            **prev,
            **{curr.split(':')[0]: curr.split(':')[1]}
        } if len(curr) > 0 and curr.split(':')[1] != '-' else prev,
        data.split(';'),
        {}
    ) if data is not None and len(data) > 1 else None
    closest_year = None if data_by_date is None else min(list(data_by_date.keys()), key=lambda x: abs(int(x) - year))
    return None if closest_year is None else safe_parse_float(data_by_date[closest_year], None)
