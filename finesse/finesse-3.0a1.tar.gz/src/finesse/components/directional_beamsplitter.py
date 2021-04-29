"""
Optical components performing directional redirection of beams.
"""

import logging
import numpy as np

from finesse.components.general import Connector, InteractionType
from finesse.components.node import NodeDirection, NodeType
from finesse.components.workspace import Connections
from finesse.components.modal.workspace import KnmConnectorWorkspace
from finesse.utilities import refractive_index

LOGGER = logging.getLogger(__name__)


class DBSWorkspace(KnmConnectorWorkspace):
    def __init__(self, owner, sim, refill):
        super().__init__(owner, sim, refill, refill)


class DirectionalBeamsplitter(Connector):
    """
    Represents a directional beamsplitter optical component.

    Parameters
    ----------
    name : str
        Name of newly created directional beamsplitter.
    """

    def __init__(self, name):
        super().__init__(name)

        self._add_port("p1", NodeType.OPTICAL)
        self.p1._add_node("i", NodeDirection.INPUT)
        self.p1._add_node("o", NodeDirection.OUTPUT)

        self._add_port("p2", NodeType.OPTICAL)
        self.p2._add_node("i", NodeDirection.INPUT)
        self.p2._add_node("o", NodeDirection.OUTPUT)

        self._add_port("p3", NodeType.OPTICAL)
        self.p3._add_node("i", NodeDirection.INPUT)
        self.p3._add_node("o", NodeDirection.OUTPUT)

        self._add_port("p4", NodeType.OPTICAL)
        self.p4._add_node("i", NodeDirection.INPUT)
        self.p4._add_node("o", NodeDirection.OUTPUT)

        # optic to optic couplings
        self._register_node_coupling(
            "P1i_P3o",
            self.p1.i,
            self.p3.o,
            interaction_type=InteractionType.TRANSMISSION,
        )
        self._register_node_coupling(
            "P3i_P4o",
            self.p3.i,
            self.p4.o,
            interaction_type=InteractionType.TRANSMISSION,
        )
        self._register_node_coupling(
            "P4i_P2o",
            self.p4.i,
            self.p2.o,
            interaction_type=InteractionType.TRANSMISSION,
        )
        self._register_node_coupling(
            "P2i_P1o",
            self.p2.i,
            self.p1.o,
            interaction_type=InteractionType.TRANSMISSION,
        )

    def _get_workspace(self, sim):
        ws = DBSWorkspace(self, sim, False)
        ws.I = np.eye(sim.model_data.num_HOMs, dtype=np.complex128)
        ws.carrier.add_fill_function(self._fill_carrier, False)
        if sim.signal:
            ws.signal.add_fill_function(self._fill_signal, False)

        ws.nr1 = refractive_index(self.p1)
        ws.nr2 = refractive_index(self.p2)
        ws.nr3 = refractive_index(self.p3)
        ws.nr4 = refractive_index(self.p4)

        if sim.is_modal:
            ws.set_knm_info(
                "P1i_P3o", nr_from=ws.nr1, nr_to=ws.nr3, is_transmission=True
            )
            ws.set_knm_info(
                "P3i_P4o", nr_from=ws.nr3, nr_to=ws.nr4, is_transmission=True
            )
            ws.set_knm_info(
                "P4i_P2o", nr_from=ws.nr4, nr_to=ws.nr2, is_transmission=True
            )
            ws.set_knm_info(
                "P2i_P1o", nr_from=ws.nr2, nr_to=ws.nr1, is_transmission=True
            )
        return ws

    def _fill_carrier(self, ws):
        self._fill_matrix(ws.owner_id, ws.sim.carrier, ws.carrier.connections, ws.I)

    def _fill_signal(self, ws):
        self._fill_matrix(ws.owner_id, ws.sim.signal, ws.signal.connections, ws.I)

    def _fill_matrix(self, owner_id, mtx, connections, I):
        for freq in mtx.optical_frequencies.frequencies:
            for idx in (
                connections.P1i_P3o_idx,
                connections.P3i_P4o_idx,
                connections.P4i_P2o_idx,
                connections.P2i_P1o_idx,
            ):
                with mtx.component_edge_fill3(
                    owner_id, idx, freq.index, freq.index,
                ) as mat:
                    mat[:] = I
