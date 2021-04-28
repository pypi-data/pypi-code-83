from numpy.testing import assert_equal
from threedigrid_builder.base import Lines
from threedigrid_builder.base import Nodes

import numpy as np
import pygeos
import pytest


@pytest.fixture
def nodes():
    return Nodes(id=[1, 2, 3], coordinates=[(1, 1), (2, 2), (3, 3)])


@pytest.fixture
def lines():
    return Lines(
        id=[0, 1, 2],
        line=[(1, 2), (2, 3), (1, 3)],
        line_geometries=[None, pygeos.linestrings([(5, 5), (6, 6)]), None],
    )


def test_set_line_coords(nodes, lines):
    lines.set_line_coords(nodes)

    assert_equal(lines.line_coords, [[1, 1, 2, 2], [2, 2, 3, 3], [1, 1, 3, 3]])


def test_fix_line_geometries(nodes, lines):
    lines.line_coords = np.array(
        [[1, 1, 2, 2], [np.nan, np.nan, np.nan, np.nan], [1, 1, 3, 3]]
    )

    lines.fix_line_geometries()

    assert pygeos.equals(lines.line_geometries[0], pygeos.linestrings([(1, 1), (2, 2)]))
    assert pygeos.equals(lines.line_geometries[1], pygeos.linestrings([(5, 5), (6, 6)]))
    assert pygeos.equals(lines.line_geometries[2], pygeos.linestrings([(1, 1), (3, 3)]))


def test_set_discharge_coefficients(lines):
    lines.discharge_coefficient_positive[:] = 2.0
    lines.discharge_coefficient_negative[0] = 3.0
    lines.set_discharge_coefficients()

    assert_equal(lines.discharge_coefficient_positive, [2.0, 2.0, 2.0])
    assert_equal(lines.discharge_coefficient_negative, [3.0, 1.0, 1.0])


@pytest.mark.parametrize(
    "nodes_dmax,expected",
    [
        ([1.0, 2.0, 3.0], [2.0, 3.0, 3.0]),
        ([1.0, 2.0, np.nan], [2.0, np.nan, np.nan]),  # nan propagates
    ],
)
def test_set_bottom_levels(nodes, lines, nodes_dmax, expected):
    nodes.dmax[:] = nodes_dmax
    lines.set_bottom_levels(nodes, allow_nan=True)

    assert_equal(lines.dpumax, expected)


def test_set_bottom_levels_nan_check(nodes, lines):
    nodes.dmax[:] = [1.0, 2.0, np.nan]

    with pytest.raises(ValueError):
        lines.set_bottom_levels(nodes)
