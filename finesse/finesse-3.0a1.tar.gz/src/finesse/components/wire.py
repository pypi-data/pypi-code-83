"""
Wire-type objects representing electrical connections between components.
"""

import logging
import numpy as np

from finesse.components.general import Connector, borrows_nodes

LOGGER = logging.getLogger(__name__)

from finesse.components.workspace import ConnectorWorkspace
from finesse.components.node import NodeType, NodeDirection
from finesse.parameter import float_parameter


class WireWorkspace(ConnectorWorkspace):
    pass


@float_parameter("delay", "Delay", validate="_check_delay", units="s")
@borrows_nodes()
class Wire(Connector):
    """Represents a wire between two electrical components in the interferometer configuration.

    Parameters
    ----------
    name : str, optional
        Name of newly created wire.

    portA, portB : :class:`.Port`, optional
        Ports to connect.
    """

    def __init__(self, name=None, portA=None, portB=None, delay=0):
        if (portA is None) != (portB is None):
            LOGGER.warn(
                "Can't construct a wire with only one port "
                "connected, ignoring ports."
            )
            portA = None
            portB = None

        if portA is not None and portA.type != NodeType.ELECTRICAL:
            raise Exception("PortA argument is not an electrical port")
        if portB is not None and portB.type != NodeType.ELECTRICAL:
            raise Exception("PortB argument is not an electrical port")

        if name is None:
            if portA is not None and portB is not None:
                compA = portA.component.name
                compB = portB.component.name
                name = f"{compA}_{portA.name}__{compB}_{portB.name}"
            else:
                raise ValueError(
                    "Cannot create an unconnected wire without " "providing a name"
                )

        super().__init__(name)
        self.delay = delay
        self._add_to_model_namespace = False

        self.__portA = portA
        self.__portB = portB

        self._add_port("p1", NodeType.ELECTRICAL)
        self._add_port("p2", NodeType.ELECTRICAL)

        if portA is not None and portB is not None:
            self.connect(portA, portB)

    @property
    def portA(self):
        return self.__portA

    @property
    def portB(self):
        return self.__portB

    def _check_delay(self, value):
        if value < 0:
            raise ValueError("Delay of a wire must not be negative.")

        return value

    def connect(self, portA, portB):
        """
        Sets the ports of this `Wire`.

        Parameters
        ----------
        portA : :class:`.Port`, optional
            Port to connect

        portB : :class:`.Port`, optional
            Port to connect
        """
        if portA.nodes[0].direction == portB.nodes[0].direction:
            raise Exception(
                f"Can not connect two {portA.nodes[0].direction} nodes, {portA.nodes[0]} to {portB.nodes[0]}."
            )

        # From the Wire's perspective the input and output
        # nodes are swapped around for its ports
        if portA.nodes[0].direction == NodeDirection.INPUT:
            self.p1._add_node("i", None, portB.o)
            self.p2._add_node("o", None, portA.i)
        else:
            self.p1._add_node("i", None, portA.o)
            self.p2._add_node("o", None, portB.i)

        self._register_node_coupling("P1i_P2o", self.p1.i, self.p2.o)

    def _get_workspace(self, sim):
        if sim.signal:
            _, is_changing = self._eval_parameters()
            # Most wires are zero delay, so don't bother refilling them all the time
            refill = (
                (sim.model.fsig.f.is_changing or sim.signal.any_frequencies_changing)
                and self.delay.is_changing
                and self.delay != 0
            )

            ws = WireWorkspace(self, sim, refill, refill)
            ws.frequencies = sim.signal.electrical_frequencies[self.p1.i].frequencies
            # Set the fill function for this simulation
            ws.signal.add_fill_function(self.fill, refill)
            return ws
        else:
            return None

    def fill(self, ws):
        for _ in ws.frequencies:
            if ws.signal.connections.P1i_P2o_idx > -1:
                with ws.sim.signal.component_edge_fill3(
                    ws.owner_id, ws.signal.connections.P1i_P2o_idx, _.index, _.index,
                ) as mat:
                    mat[:] = np.exp(1j * ws.values.delay * _.f)
