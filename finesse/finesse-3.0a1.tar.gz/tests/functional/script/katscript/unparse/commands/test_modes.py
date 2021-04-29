import pytest
from finesse.script import unparse


@pytest.mark.parametrize(
    "args,kwargs,expected",
    (
        ([], {"maxtem": 0}, "maxtem=0"),
        ([], {"maxtem": 2}, "maxtem=2"),
        (["off"], {}, None),
        (["even"], {"maxtem": 4}, "modes=even, maxtem=4"),
    ),
)
def test_modes(model, args, kwargs, expected):
    model.select_modes(*args, **kwargs)
    script = unparse(model)
    modelines = filter(lambda line: line.startswith("modes("), script.splitlines())

    if expected is not None:
        modeline = next(modelines)
        assert modeline == f"modes({expected})"
    else:
        assert not any(modelines)
