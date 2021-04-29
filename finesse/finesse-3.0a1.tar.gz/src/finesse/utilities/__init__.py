"""Useful common utility functions and classes used throughout the Finesse package.

Listed below are all the sub-modules of the ``utilities`` module with a brief
description of the contents of each.
"""

# TODO: sort out which things get imported at the module level here
from .components import refractive_index
from .homs import make_modes, insert_modes
from .text import (
    ngettext,
    option_list,
    format_section,
    format_bullet_list,
    add_linenos,
    stringify,
    stringify_graph_gml,
)
from finesse.utilities.misc import (
    check_name,
    pairwise,
    valid_name,
    is_iterable,
    changed_params,
    opened_file,
    logs,
    graph_layouts,
    networkx_layouts,
    graphviz_layouts,
)
from finesse.utilities.units import SI, SI_LABEL, SI_VALUE

__all__ = (
    "refractive_index",
    "make_modes",
    "insert_modes",
    "ngettext",
    "option_list",
    "format_section",
    "format_bullet_list",
    "add_linenos",
    "stringify",
    "stringify_graph_gml",
    "check_name",
    "pairwise",
    "valid_name",
    "is_iterable",
    "changed_params",
    "opened_file",
    "logs",
    "graph_layouts",
    "networkx_layouts",
    "graphviz_layouts",
    "SI",
    "SI_LABEL",
    "SI_VALUE",
)
