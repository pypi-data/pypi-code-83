import pytest
from finesse.model import Model
from finesse.components.general import Connector
from finesse.components.node import NodeDirection, NodeType
from finesse.detectors.general import Detector
from finesse.analysis.actions import Action
from finesse.parameter import float_parameter
from finesse.script.spec import BaseSpec


@pytest.fixture
def spec():
    """Kat spec with no registered elements, commands, etc.

    The spec is shared by builder and generator tests.
    """

    class EmptyTestSpec(BaseSpec):
        """Empty specification class, used by tests."""

    return EmptyTestSpec()


@pytest.fixture
def model():
    class FakeModel(Model):
        """A fake model."""

    return FakeModel()


@pytest.fixture
def fake_element_cls():
    @float_parameter("a", "Fake Parameter A")
    @float_parameter("b", "Fake Parameter B")
    class FakeElement(Connector):
        """A fake 2-port element."""

        def __init__(self, name, a=None, b=None):
            super().__init__(name)
            self.a = a
            self.b = b

            # Add some ports.
            self._add_port("p1", NodeType.OPTICAL)
            self.p1._add_node("i", NodeDirection.INPUT)
            self.p1._add_node("o", NodeDirection.OUTPUT)

            self._add_port("p2", NodeType.OPTICAL)
            self.p2._add_node("i", NodeDirection.INPUT)
            self.p2._add_node("o", NodeDirection.OUTPUT)

    return FakeElement


@pytest.fixture
def fake_element_noparam_cls():
    class FakeNoParamElement(Connector):
        """A fake element with no model parameters."""

        def __init__(self, name, a=None, b=None):
            super().__init__(name)
            self.a = a
            self.b = b

            # Add some ports.
            self._add_port("p1", NodeType.OPTICAL)
            self.p1._add_node("i", NodeDirection.INPUT)
            self.p1._add_node("o", NodeDirection.OUTPUT)

            self._add_port("p2", NodeType.OPTICAL)
            self.p2._add_node("i", NodeDirection.INPUT)
            self.p2._add_node("o", NodeDirection.OUTPUT)

    return FakeNoParamElement


@pytest.fixture
def fake_binop_cls():
    class FakeBinaryOperation:
        """A fake binary operation."""

        def __init__(self, operator, lhs, rhs):
            self.operator = operator
            self.lhs = lhs
            self.rhs = rhs

        def eval(self):
            return eval(f"{self.lhs}{self.operator}{self.rhs}")

    return FakeBinaryOperation


@pytest.fixture
def fake_unop_cls():
    class FakeUnaryOperation:
        """A fake unary operation."""

        def __init__(self, operator, argument):
            self.operator = operator
            self.argument = argument

        def eval(self):
            return eval(f"{self.operator}{self.argument}")

    return FakeUnaryOperation


@pytest.fixture
def fake_detector_cls():
    class FakeDetector(Detector):
        """A fake detector element."""

        def __init__(self, name, target):
            super().__init__(name)
            self.target = target

    return FakeDetector


@pytest.fixture
def fake_analysis_cls():
    class FakeAnalysis(Action):
        """A fake action."""

        def __init__(self, a=None, b=None):
            self.a = a
            self.b = b

        def _do(self, state):
            raise NotImplementedError

        def _requests(self, model, memo, first=True):
            raise NotImplementedError

    return FakeAnalysis
