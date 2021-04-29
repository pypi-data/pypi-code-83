import pytest
from finesse.script import unparse
from finesse.components.laser import Laser


@pytest.fixture
def laser_model(model):
    model.add(Laser("l1"))
    return model


def test_tem_default(laser_model):
    """No tem() command printed when only default is set."""
    script = unparse(laser_model)
    temlines = filter(lambda line: line.startswith("tem("), script.splitlines())
    assert not list(temlines)


@pytest.mark.parametrize(
    "tems",
    (
        # n,m,factor,phase
        ((0, 0, 0, 0),),
        ((0, 0, 0, 0), (1, 0, 1, 0)),
        ((1, 0, 0.5, 45), (0, 1, 0.5, 90)),
    ),
)
def test_tem(laser_model, tems):
    expected_script = []
    for n, m, factor, phase in tems:
        laser_model.l1.tem(n, m, factor, phase)
        expected_script.append(f"tem(l1, n={n}, m={m}, factor={factor}, phase={phase})")

    script = unparse(laser_model)
    temlines = filter(lambda line: line.startswith("tem("), script.splitlines())

    assert set(temlines) == set(expected_script)
