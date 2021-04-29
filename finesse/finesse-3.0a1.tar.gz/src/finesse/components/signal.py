"""
Signal-type electrical component for producing signal inputs.
"""
from finesse.components.node import NodeType, Node, Port
from finesse.components.general import Connector
from finesse.parameter import float_parameter, info_parameter
from finesse.components.modal.signal import siggen_fill_rhs, SignalGeneratorWorkspace
from finesse.components.dof import DegreeOfFreedom

@float_parameter("amplitude", "Amplitude", units="arb")
@float_parameter("phase", "Phase", units="degrees")
@info_parameter("f", "Frequency", units="Hz")
class SignalGenerator(Connector):
    """Represents a signal generator which produces a signal with a given amplitude and phase.

    Parameters
    ----------
    name : str
        Name of newly created signal generator.

    node : .class:`finesse.components.node.Node`
        A node to inject a signal into.

    amplitude : float, optional
        Amplitude of the signal in volts.

    phase : float, optional
        Phase-offset of the signal from the default in degrees, defaults to zero.
    """

    def __init__(self, name, node, amplitude=1, phase=0):
        Connector.__init__(self, name)

        if isinstance(node, DegreeOfFreedom):
            node = node.AC.i
        elif isinstance(node, Port):
            if len(node.nodes) == 1:
                node = node.nodes[0]
            else:
                raise Exception(
                    f"Signal generator ({name}) input `{node}` should be a Node not a Port"
                )
        elif not isinstance(node, Node):
            raise Exception(
                f"Signal generator ({name}) input `{node}` should be a Node"
            )

        self._add_port("port", node.type)
        self.port._add_node("o", None, node)
        node.has_signal_injection = True

        self.amplitude = amplitude
        self.phase = phase

    @property
    def node(self):
        """The node the signal generator injects into.

        :getter: Returns the node the signal generator injects into.
        """
        return self.port.o

    @property
    def f(self):
        return self._model.fsig.f

    def _get_workspace(self, sim):
        if sim.signal:
            ws = SignalGeneratorWorkspace(self, sim, True)
            ws.rhs_idx = ws.sim.signal.field(self.port.o, 0, 0)
            ws.signal.set_fill_rhs_fn(siggen_fill_rhs)

            if self.port.o.type is NodeType.MECHANICAL:
                ws.scaling = 1 / sim.model_data.x_scale
            else:
                ws.scaling = 1

            return ws
        else:
            return None
