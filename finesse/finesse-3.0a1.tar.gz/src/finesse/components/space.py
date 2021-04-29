"""
Space-type objects representing physical distances between components.
"""

import logging
import numpy as np
import types
from finesse.parameter import float_parameter
from finesse.components.general import (
    Connector,
    InteractionType,
    borrows_nodes,
    DOFDefinition,
)
from finesse.components.workspace import ConnectionSetting
from finesse.components.node import NodeDirection, NodeType, Port


LOGGER = logging.getLogger(__name__)


@borrows_nodes()
@float_parameter(
    "L",
    "Length",
    validate="_check_L",
    units="m",
    is_geometric=True,
)
@float_parameter(
    "nr",
    "Refractive index",
    validate="_check_nr",
    is_geometric=True,
    changeable_during_simulation=False,
)
@float_parameter("gouy_x", "Gouy phase (x)", units="Degrees")
@float_parameter("gouy_y", "Gouy phase (y)", units="Degrees")
class Space(Connector):
    """Represents a space between two components in the interferometer configuration, with a given \
    length and index of refraction.

    Parameters
    ----------
    name : str, optional
        Name of newly created space.

    portA, portB : :class:`.Port`, optional
        Ports to connect.

    L : float, optional
        Geometric length of newly created :class:`.Space` instance; defaults to 0.

    nr : float, optional
        Index of refraction of newly created :class:`.Space` instance; defaults to 1.0.
    """

    def __init__(self, name=None, portA=None, portB=None, L=0, nr=1.0, gouy_x=0, gouy_y=0):
        if (portA is None) != (portB is None):
            LOGGER.warn(
                "Can't construct a space with only one port connected; ignoring ports."
            )
            portA = None
            portB = None

        if portA is not None and not isinstance(portA, Port):
            raise Exception("PortA is not a Port")
        if portA is not None and not isinstance(portB, Port):
            raise Exception("PortB is not a Port")

        if portA is not None and portA.type != NodeType.OPTICAL:
            raise Exception("PortA is not an optical port")
        if portB is not None and portB.type != NodeType.OPTICAL:
            raise Exception("PortB is not an optical port")

        if portA is not None and portB is not None:
            if portA.component._model is not portB.component._model:
                raise Exception("Port A and B are not part of the same model")

        if name is None:
            if portA is not None and portB is not None:
                compA = portA.component.name
                compB = portB.component.name
                name = f"{compA}_{portA.name}__{compB}_{portB.name}"
            else:
                raise ValueError(
                    "Cannot create an unconnected space without providing a name"
                )

        super().__init__(name)

        self.__portA = portA
        self.__portB = portB
        self._add_to_model_namespace = True
        self._namespace = ".spaces"
        self.L = L
        self.nr = nr
        self.gouy_x.is_tunable = True
        self.gouy_y.is_tunable = True
        self.gouy_x = gouy_x
        self.gouy_y = gouy_y
        
        self._add_port("p1", NodeType.OPTICAL)
        self._add_port("p2", NodeType.OPTICAL)

        # Phase modulation input
        self._add_port("phs", NodeType.ELECTRICAL)
        self.phs._add_node("i", NodeDirection.INPUT)
        # Amplitude modulation input
        self._add_port("amp", NodeType.ELECTRICAL)
        self.amp._add_node("i", NodeDirection.INPUT)
        # strain input
        self._add_port("h", NodeType.ELECTRICAL)
        self.h._add_node("i", NodeDirection.INPUT)

        if portA is not None and portB is not None:
            self.connect(portA, portB)
        self.__changing_check = set((self.L, self.nr))

        # Define typical degrees of freedom for this component
        self.dofs = types.SimpleNamespace()
        # Strain doesn't have a DC term really in Finesse
        # changing a space length won't generate a signal
        self.dofs.h = DOFDefinition(None, self.h.i, 1)

    @property
    def portA(self):
        return self.__portA

    @property
    def portB(self):
        return self.__portB

    def connect(self, portA, portB):
        """
        Sets the ports of this `Space`.

        Parameters
        ----------
        portA : :class:`.Port`, optional
            Port to connect

        portB : :class:`.Port`, optional
            Port to connect
        """
        if portA.is_connected:
            raise Exception(f"Port {portA} has already been connected to")
        if portB.is_connected:
            raise Exception(f"Port {portB} has already been connected to")

        # From the Space's perspective the input and output
        # nodes are swapped around for its ports
        self.p1._add_node("i", None, portA.o)
        self.p1._add_node("o", None, portA.i)
        self.p2._add_node("i", None, portB.o)
        self.p2._add_node("o", None, portB.i)

        self._register_node_coupling(
            "P1i_P2o",
            self.p1.i,
            self.p2.o,
            interaction_type=InteractionType.TRANSMISSION,
        )
        self._register_node_coupling(
            "P2i_P1o",
            self.p2.i,
            self.p1.o,
            interaction_type=InteractionType.TRANSMISSION,
        )
        self._register_node_coupling("SIGPHS_P1o", self.phs.i, self.p1.o)
        self._register_node_coupling("SIGPHS_P2o", self.phs.i, self.p2.o)
        self._register_node_coupling("SIGAMP_P1o", self.amp.i, self.p1.o)
        self._register_node_coupling("SIGAMP_P2o", self.amp.i, self.p2.o)
        self._register_node_coupling("H_P1o", self.h.i, self.p1.o)
        self._register_node_coupling("H_P2o", self.h.i, self.p2.o)

    def _get_workspace(self, sim):
        from finesse.components.modal.space import (
            space_carrier_fill,
            space_signal_fill,
            space_set_gouy,
            SpaceWorkspace,
        )

        _, is_changing = self._eval_parameters()

        carrier_refill = sim.carrier.any_frequencies_changing and (float(self.L.value) > 0 or self.L.is_changing)
        carrier_refill |= len(is_changing)
        carrier_refill |= sim.trace_forest.contains_space(self)

        ws = SpaceWorkspace(self, sim, False)
        ws.set_gouy_function(space_set_gouy)
        # Set the fill function for this simulation
        ws.carrier.add_fill_function(space_carrier_fill, carrier_refill)
        ws.carrier.connection_settings["P1i_P2o"] = ConnectionSetting.DIAGONAL
        ws.carrier.connection_settings["P2i_P1o"] = ConnectionSetting.DIAGONAL

        if sim.signal:
            signal_refill = sim.signal.any_frequencies_changing and (float(self.L.value) > 0 or self.L.is_changing)
            signal_refill |= len(is_changing)
            signal_refill |= sim.trace_forest.contains_space(self)
            
            ws.signal.add_fill_function(space_signal_fill, signal_refill)
            
            ws.signal.connection_settings["P1i_P2o"] = ConnectionSetting.DIAGONAL
            ws.signal.connection_settings["P2i_P1o"] = ConnectionSetting.DIAGONAL
            ws.signal.connection_settings["SIGPHS_P1o"] = ConnectionSetting.DIAGONAL
            ws.signal.connection_settings["SIGPHS_P2o"] = ConnectionSetting.DIAGONAL
            ws.signal.connection_settings["SIGAMP_P1o"] = ConnectionSetting.DIAGONAL
            ws.signal.connection_settings["SIGAMP_P2o"] = ConnectionSetting.DIAGONAL
            ws.signal.connection_settings["H_P1o"] = ConnectionSetting.DIAGONAL
            ws.signal.connection_settings["H_P2o"] = ConnectionSetting.DIAGONAL

        # Initialise the ABCD matrix memory-views
        if sim.is_modal:
            ws.abcd = self.ABCD(self.p1.i, self.p2.o, "x", copy=False)

        return ws

    def _check_L(self, value):
        if value < 0:
            raise ValueError("Length of a space must not be negative.")

        return value

    def _check_nr(self, value):
        if value < 1:
            raise ValueError("Index of refraction must be >= 1")

        return value

    def _resymbolise_ABCDs(self):
        L = self.L.ref
        nr = self.nr.ref

        M_sym = np.array([[1.0, L / nr], [0.0, 1.0]])

        # Matrices same in both propagations and both planes so
        # only need one register call for all couplings here
        self.register_abcd_matrix(
            M_sym, (self.p1.i, self.p2.o), (self.p2.i, self.p1.o),
        )

    @property
    def abcd(self):
        """Numeric ABCD matrix.

        Equivalent to any of ``space.ABCD(1, 2, "x")``, ``space.ABCD(2, 1, "x")``,
        ``space.ABCD(1, 2, "y")``, ``space.ABCD(2, 1, "y")``.

        :getter: Returns a copy of the (numeric) ABCD matrix (read-only).
        """
        return self.ABCD(1, 2, "x")

    def ABCD(
        self,
        from_node,
        to_node,
        direction="x",
        symbolic=False,
        copy=True,
        retboth=False,
    ):
        r"""Returns the ABCD matrix of the space for the specified coupling.

        .. _fig_abcd_space_transmission:
        .. figure:: ../images/abcd_spacet.*
            :align: center

        This is given by,

        .. math::
            M = \begin{pmatrix}
                    1 & \frac{L}{n_r} \\
                    0 & 1
                \end{pmatrix},

        where :math:`L` is the length of the space and :math:`n_r` is
        the index of refraction.

        See :meth:`.Connector.ABCD` for descriptions of parameters, return values and possible
        exceptions.
        """
        return super().ABCD(from_node, to_node, direction, symbolic, copy, retboth)
