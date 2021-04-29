import re
import pytest
from finesse.element import ModelElement
from finesse.parameter import float_parameter
from finesse.script.exceptions import KatScriptError
from ....util import dedent_multiline


@float_parameter("fake_param", "Fake parameter")
class FakeElement(ModelElement):
    def __init__(self, name, fake_param=0.0):
        super().__init__(name)
        self.fake_param = fake_param


@pytest.fixture
def compiler(compiler, fake_binop_cls):
    compiler.spec.register_element(
        "fake_element", {"setter": FakeElement, "getter": FakeElement}
    )
    compiler.spec.binary_operators["-"] = lambda a, b: fake_binop_cls("-", a, b)

    return compiler


@pytest.mark.parametrize(
    "script,error",
    (
        pytest.param(
            dedent_multiline(
                """
                fake_element myelement1 &myelement2.fake_param
                fake_element myelement2 &myelement1.fake_param
                """
            ),
            (
                "\nlines 1-2: cyclic parameters\n"
                "-->1: fake_element myelement1 &myelement2.fake_param\n"
                "                              ^^^^^^^^^^^^^^^^^^^^^^\n"
                "-->2: fake_element myelement2 &myelement1.fake_param\n"
                "                              ^^^^^^^^^^^^^^^^^^^^^^"
            ),
            id="cycle between two elements",
        ),
        pytest.param(
            dedent_multiline(
                """
                fake_element myelement1 &myelement2.fake_param
                fake_element myelement2 1-&myelement1.fake_param
                """
            ),
            (
                "\nlines 1-2: cyclic parameters\n"
                "-->1: fake_element myelement1 &myelement2.fake_param\n"
                "                              ^^^^^^^^^^^^^^^^^^^^^^\n"
                "-->2: fake_element myelement2 1-&myelement1.fake_param\n"
                "                                ^^^^^^^^^^^^^^^^^^^^^^"
            ),
            id="cycle between two elements (one inside expression)",
        ),
        pytest.param(
            dedent_multiline(
                """
                fake_element myelement1 &myelement2.fake_param
                fake_element myelement2 -&myelement1.fake_param
                """
            ),
            (
                "\nlines 1-2: cyclic parameters\n"
                "-->1: fake_element myelement1 &myelement2.fake_param\n"
                "                              ^^^^^^^^^^^^^^^^^^^^^^\n"
                "-->2: fake_element myelement2 -&myelement1.fake_param\n"
                "                               ^^^^^^^^^^^^^^^^^^^^^^"
            ),
            id="cycle between two elements (one inside unary function)",
        ),
        pytest.param(
            dedent_multiline(
                """
                fake_element myelement1 &myelement2.fake_param
                fake_element myelement2 &myelement3.fake_param
                fake_element myelement3 &myelement4.fake_param
                fake_element myelement4 &myelement1.fake_param
                """
            ),
            (
                "\nlines 1-4: cyclic parameters\n"
                "-->1: fake_element myelement1 &myelement2.fake_param\n"
                "                              ^^^^^^^^^^^^^^^^^^^^^^\n"
                "-->2: fake_element myelement2 &myelement3.fake_param\n"
                "                              ^^^^^^^^^^^^^^^^^^^^^^\n"
                "-->3: fake_element myelement3 &myelement4.fake_param\n"
                "                              ^^^^^^^^^^^^^^^^^^^^^^\n"
                "-->4: fake_element myelement4 &myelement1.fake_param\n"
                "                              ^^^^^^^^^^^^^^^^^^^^^^"
            ),
            id="cycle between four elements",
        ),
    ),
)
def test_cycles_invalid(compiler, script, error):
    with pytest.raises(KatScriptError, match=re.escape(error)):
        compiler.compile(script)
