"""Test cases for selecting modes to include in a model."""

import pytest
import numpy as np


def test_maxtem_off(model):
    """Test HOMs when maxtem set to off."""
    model.switch_off_homs()
    assert np.all(model.homs == [[0, 0]])


def test_maxtem_zero(model):
    """Test HOMs when maxtem set to 0."""
    model.select_modes(maxtem=0)
    assert np.all(model.homs == [[0, 0]])


def test_maxtem_on(model):
    """Test HOMs when maxtem set to 2."""
    model.select_modes(maxtem=2)
    assert np.all(model.homs == [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [2, 0]])


def test_maxtem_on_increased(model):
    """Test HOMs when maxtem set higher."""
    model.select_modes(maxtem=1)
    assert np.all(model.homs == [[0, 0], [0, 1], [1, 0]])

    model.select_modes(maxtem=2)
    assert np.all(model.homs == [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [2, 0]])


def test_maxtem_on_decreased(model):
    """Test HOMs when maxtem set lower."""
    model.select_modes(maxtem=2)
    assert np.all(model.homs == [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [2, 0]])

    model.select_modes(maxtem=1)
    assert np.all(model.homs == [[0, 0], [0, 1], [1, 0]])


def test_maxtem_on_to_off(model):
    """Test HOMs when maxtem set to 1 then off."""
    model.select_modes(maxtem=1)
    assert np.all(model.homs == [[0, 0], [0, 1], [1, 0]])

    model.select_modes("off")
    assert np.all(model.homs == [[0, 0]])


def test_even_modes_specify_maxtem(model):
    """Test HOMs when modes set to even."""
    model.select_modes("even", 4)

    assert np.all(model.homs == [[0, 0], [0, 2], [0, 4], [2, 0], [2, 2], [4, 0]])


def test_odd_modes_specify_maxtem(model):
    """Test HOMs when modes set to odd."""
    model.select_modes("odd", 3)

    assert np.all(model.homs == [[0, 0], [0, 1], [0, 3], [1, 0], [1, 1], [3, 0]])


def test_tangential_modes_specify_maxtem(model):
    """Test HOMs when modes set to 5 for x-direction."""
    model.select_modes("x", 5)

    assert np.all(model.homs == [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]])


def test_sagittal_modes_specify_maxtem(model):
    """Test HOMs when modes set to 4 for y-direction."""
    model.select_modes("y", 4)

    assert np.all(model.homs == [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]])


def test_insert_single_mode(model):
    """Test HOMs when maxtem set to 3 and modes set to x-direction, with extra mode included."""
    model.select_modes(maxtem=3)
    model.select_modes("x", 3)
    model.include_modes("11")

    assert np.all(model.homs == [[0, 0], [1, 0], [1, 1], [2, 0], [3, 0]])


def test_insert_multiple_modes(model):
    """Test HOMs when maxtem set to even 4 modes, with extra mode included."""
    model.select_modes("even", 4)
    model.include_modes(["11", "32", "50"])

    assert np.all(
        model.homs
        == [[0, 0], [0, 2], [0, 4], [1, 1], [2, 0], [2, 2], [3, 2], [4, 0], [5, 0]]
    )


def test_negative_maxtem_is_invalid(model):
    """Test that maxtem cannot be negative."""
    with pytest.raises(ValueError):
        model.select_modes(maxtem=-1)
    with pytest.raises(ValueError):
        model.select_modes(maxtem=-314)

    assert np.all(model.homs == [[0, 0]])


def test_non_integer_maxtem_is_invalid(model):
    """Test that maxtem cannot be floats."""
    with pytest.raises(ValueError):
        model.select_modes(maxtem=3.4)
    with pytest.raises(ValueError):
        model.select_modes(maxtem=-3.4)

    assert np.all(model.homs == [[0, 0]])


def test_unique_mode_indices(model):
    """Test HOMs when manually selected modes."""
    model.select_modes(["00", "11", "22", "11", "00"])

    assert np.all(model.homs == [[0, 0], [1, 1], [2, 2]])


@pytest.mark.xfail(reason="See NOTE in Model.select_modes")
def test_warns_when_enabling(caplog):
    """ Test that a warning is emitted when maxtem = 0

    Test that a warning is emitted when
    the model is automatically swicthed
    to modal, but no higher order modes
    are set.

    Also checks that the message is only
    displayed once.
    """
    import finesse
    from finesse.enums import SpatialType
    import logging

    ifo = finesse.Model()
    ifo.parse(
        f"""

    l LaserIn P=1

    s s0 LaserIn.p1 ITM.p1 L=1

    m ITM R=0.99 T=0.01 Rc=-1
    s sCAV ITM.p2 ETM.p1 L=1.5
    m ETM R=0.99 T=0.01 Rc=1
    """
    )

    assert ifo.spatial_type == SpatialType.PLANE
    assert not ifo.is_modal
    with caplog.at_level(logging.WARNING):
        ifo.parse(
            f"""
        cavity fab1 ITM.p2 via=ETM.p1.i
        """
        )
        assert "enabled with only HG00" in caplog.text

    assert ifo.spatial_type == SpatialType.MODAL
    assert ifo.is_modal

    # Check that this is only displayed once
    caplog.clear()
    with caplog.at_level(logging.WARNING):
        ifo.parse(
            f"""
        s s02 ETM.p2 ITM2.p1 L=1
        m ITM2 R=0.99 T=0.01 Rc=-1
        s sCAV2 ITM2.p2 ETM2.p1 L=1.5
        m ETM2 R=0.99 T=0.01 Rc=1
        cavity fab2 ITM2.p2 via=ETM2.p1.i
        """
        )
        assert "enabled with only HG00" not in caplog.text
