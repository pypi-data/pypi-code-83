import logging

import numpy as np

from finesse.components.modal.lens import LensWorkspace
from finesse.components.general import Connector, InteractionType
from finesse.components.node import NodeDirection, NodeType
from finesse.parameter import float_parameter
from finesse.utilities import refractive_index
from finesse.components.modal.workspace import KnmConnectorWorkspace

        
@float_parameter(
    "fc",
    "Central frequency",
    units="Hz"
)
@float_parameter(
    "bandwidth",
    "Bandpass bandwidth",
    units="Hz"
)
class OpticalBandpassFilter(Connector):
    """An idealised optical bandpass filter that will transmit an optical frequency around
    some central frequency with a 3dB bandwidth.

    Parameters
    ----------
    name : str
        Name of element
    fc : float, symbol
        Central frequency
    bandwidth : float, symbol
        Filter 3dB bandwidth
    """

    def __init__(self, name, fc=0, bandwidth=1000):
        super().__init__(name)

        self.fc = fc
        self.bandwidth = bandwidth

        self._add_port("p1", NodeType.OPTICAL)
        self.p1._add_node("i", NodeDirection.INPUT)
        self.p1._add_node("o", NodeDirection.OUTPUT)

        self._add_port("p2", NodeType.OPTICAL)
        self.p2._add_node("i", NodeDirection.INPUT)
        self.p2._add_node("o", NodeDirection.OUTPUT)

        # optic to optic couplings
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
        
    def _get_workspace(self, sim):
        from finesse.simulations.basematrix import CarrierSignalMatrixSimulation

        if isinstance(sim, CarrierSignalMatrixSimulation):
            _, is_changing = self._eval_parameters()
            refill = (
                sim.is_component_in_mismatch_couplings(self)
                or len(is_changing)
                or sim.carrier.any_frequencies_changing
                or (sim.signal.any_frequencies_changing if sim.signal else False)
        )
            from .modal.optical_bandpass import optical_bandpass_carrier_fill, optical_bandpass_signal_fill, OpticalBandpassWorkspace

            ws = OpticalBandpassWorkspace(self, sim, refill)
            # This assumes that nr1/nr2 cannot change during a simulation
            ws.nr1 = refractive_index(self.p1)
            ws.nr2 = refractive_index(self.p2)
            # TODO ddb refractive index should be equal on
            # both sides of the lens as we are using the thin
            # lens approximation
            assert ws.nr1 == ws.nr2

            ws.carrier.add_fill_function(optical_bandpass_carrier_fill, refill)
            ws.signal.add_fill_function(optical_bandpass_signal_fill, refill)

            if sim.is_modal:
                # Set the coupling matrix information
                # ABCDs are same in each direction
                ws.set_knm_info(
                    "P1i_P2o",
                    nr_from=ws.nr1,
                    nr_to=ws.nr2,
                    is_transmission=True,
                )
                # TODO nr reversed here for now until it's forced to be same on both sides
                ws.set_knm_info(
                    "P2i_P1o",
                    nr_from=ws.nr2,
                    nr_to=ws.nr1,
                    is_transmission=True,
                )

            return ws
        else:
            raise Exception(f"Optical bandpass filter does not handle a simulation of type {sim}")