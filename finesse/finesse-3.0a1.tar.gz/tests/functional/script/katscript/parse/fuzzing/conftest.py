import pytest
from finesse.components.general import Connector
from finesse.script.spec import KatSpec
from finesse.script.compiler import KatCompiler


def resolve(value):
    if isinstance(value, list):
        for index, item in enumerate(value):
            value[index] = resolve(item)
    else:
        try:
            value = value.eval()
        except AttributeError:
            pass

    return value


@pytest.fixture(scope="package")
def fuzz_value_parse_compare():
    """Special package-scoped parser for fuzzing values."""

    class FakeNoParamElement(Connector):
        """A fake element with no model parameters."""

        def __init__(self, name, a=None):
            super().__init__(name)
            self.a = a

    # Register special fuzz component.
    spec = KatSpec()
    spec.register_element(("fuzz",), {"setter": FakeNoParamElement})
    compiler = KatCompiler(spec=spec)

    def _(value, expected, exact=True):
        model = compiler.compile(f"fuzz fuzzer {value}")
        value = resolve(model.fuzzer.a)
        expected = resolve(expected)

        if exact:
            assert value == expected
        else:
            assert value == pytest.approx(expected)

    return _
