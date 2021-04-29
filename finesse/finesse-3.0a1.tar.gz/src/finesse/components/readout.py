"""
A components sub-module containing classes for detecting power at
a physical point in a configuration.
"""

import numpy as np
import types
import finesse
import finesse.detectors._pdtypes as pdtypes
from finesse.components.general import Connector, borrows_nodes
from finesse.components.node import NodeDirection, NodeType, Port
from finesse.components.workspace import ConnectorWorkspace
from finesse.parameter import float_parameter
from finesse.detectors.compute.power import PD0Workspace, PD1Workspace, PD2Workspace
from finesse.element import ModelElement

from finesse.detectors.compute.quantum import (
    QShot0Workspace,
    QShotNWorkspace,
)

class ReadoutWorkspace(ConnectorWorkspace):
    pass


class ReadoutOutput(ModelElement):
    def __init__(self, name, readout):
        super().__init__(name)
        self.__readout = readout

    @property
    def readout(self):
        return self.__readout


class Readout(Connector): 
    def __init__(self, name, optical_node, output_detectors=False):
        super().__init__(name)
        self.__output_detectors = output_detectors
        self._add_port("p1", NodeType.OPTICAL)

        if optical_node is not None:
            port = optical_node if isinstance(optical_node, Port) else optical_node.port
            other_node = tuple(o for o in port.nodes if o is not optical_node)[0]

            self.p1._add_node("i", None, optical_node)
            self.p1._add_node("o", None, other_node)
        else:
            self.p1._add_node("i", NodeDirection.INPUT)
            self.p1._add_node("o", NodeDirection.OUTPUT)

    def _get_output_workspaces(self, model):
        return None

    @property
    def optical_node(self):
        if self.p1.i.component != self:
            return self.p1.i

    @property
    def has_mask(self):
        return False

    @property
    def output_detectors(self):
        return self.__output_detectors

    @output_detectors.setter
    def output_detectors(self, value):
        self.__output_detectors = value


@borrows_nodes()
class ReadoutDC(Readout):
    def __init__(self, name, optical_node=None, output_detectors=False):
        super().__init__(name, optical_node, output_detectors=output_detectors)
        
        self._add_port("DC", NodeType.ELECTRICAL)
        self.DC._add_node("o", NodeDirection.OUTPUT)

        self._register_node_coupling("P1i_DC", self.p1.i, self.DC.o)

        self.outputs = types.SimpleNamespace()
        self.outputs.DC = f'{self.name}_DC'

    def _on_add(self, model):
        model.add(ReadoutOutput(self.name+"_DC", self))

    def _get_workspace(self, sim):
        if sim.signal:
            has_DC_node = self.DC.o.full_name in sim.signal.nodes
            
            if not has_DC_node:
                return None # Don't do anything if no nodes included

            ws = ReadoutWorkspace(self, sim, True, True)
            ws.I = np.eye(sim.model_data.num_HOMs, dtype=np.complex128)
            ws.signal.add_fill_function(self._fill_matrix, True)
            ws.frequencies = sim.signal.electrical_frequencies[self.DC.o].frequencies
            return ws
        else:
            return None

    def _get_output_workspaces(self, sim):
        from finesse.detectors.workspace import OutputInformation
        from finesse.detectors.compute.power import pd0_DC_output, PD0Workspace
        wss = []
        for quadrature in ('DC',):
            # Setup a single demodulation photodiode detector for
            # using for outputs
            oinfo = OutputInformation(
                self.name + "_" + quadrature,
                (self.p1.i, ),
                np.float64,
                "W",
                None,
                "W",
                True,
                False
            )
            ws = PD0Workspace(self, sim, oinfo=oinfo)
            ni = sim.carrier.get_node_info(oinfo.nodes[0])
            ws.rhs_index = ni["rhs_index"]
            ws.size = ni["nfreqs"] * ni["nhoms"]
            ws.dc_node_id = sim.carrier.node_id(oinfo.nodes[0])
            ws.set_output_fn(pd0_DC_output)
            wss.append(ws)

        if sim.signal:
            oinfo = OutputInformation(
                self.name + "_shot_noise",
                (self.p1.i, ),
                np.float64,
                "W/rtHz",
                None,
                "ASD",
                True,
                False
            )
            wss.append(
                QShot0Workspace(self, sim, False, output_info=oinfo)
            )

        return wss

    def _fill_matrix(self, ws):
        """
        Computing E.conj() * upper + E * lower.conj()
        """
        for freq in ws.sim.signal.optical_frequencies.frequencies:
            # Get the carrier HOMs for this frequency
            E = ws.sim.carrier.get_out(self.p1.i, freq.audio_carrier_index)
            # is_lower_sb = freq.audio_order < 0
            for efreq in ws.frequencies:
                with ws.sim.signal.component_edge_fill3(
                    ws.owner_id, ws.signal.connections.P1i_DC_idx, freq.index, efreq.index,
                ) as mat:
                    mat[:] = E.conjugate() 


@borrows_nodes()
class ReadoutDCQPD(Readout):
    def __init__(self, name, optical_node=None, output_detectors=False):
        super().__init__(name, optical_node, output_detectors=output_detectors)

        self._add_port("x", NodeType.ELECTRICAL)
        self.x._add_node("o", NodeDirection.OUTPUT)

        self._add_port("y", NodeType.ELECTRICAL)
        self.y._add_node("o", NodeDirection.OUTPUT)

        self._register_node_coupling("P1i_x", self.p1.i, self.x.o)
        self._register_node_coupling("P1i_y", self.p1.i, self.y.o)

        self.outputs = types.SimpleNamespace()
        self.outputs.x = f'{self.name}_X'
        self.outputs.y = f'{self.name}_Y'

    def _on_add(self, model):
        model.add(ReadoutOutput(self.name + "_X", self))
        model.add(ReadoutOutput(self.name + "_Y", self))

    def _get_workspace(self, sim):
        if sim.signal:
            has_x_node = self.x.o.full_name in sim.signal.nodes
            has_y_node = self.y.o.full_name in sim.signal.nodes
            
            if not (has_x_node or has_y_node):
                return None # Don't do anything if no nodes included

            ws = ReadoutWorkspace(self, sim, True, True)
            ws.signal.add_fill_function(self._fill_matrix, True)
            ws.frequencies = sim.signal.electrical_frequencies[self.y.o].frequencies
            ws.Kx = pdtypes.construct_segment_beat_matrix(
                sim.model.mode_index_map,
                pdtypes.XSPLIT
            )
            ws.Ky = pdtypes.construct_segment_beat_matrix(
                sim.model.mode_index_map,
                pdtypes.YSPLIT
            )
            ws.node_car_id = sim.carrier.node_id(self.p1.i)
            return ws
        else:
            return None

    def _get_output_workspaces(self, sim):
        from finesse.detectors.workspace import OutputInformation
        from finesse.detectors.compute.power import pd0_DC_output_segmented, PD0Workspace
        wss = []
        for dof, split in (('X', pdtypes.XSPLIT), ('Y', pdtypes.YSPLIT)):
            # Setup a single demodulation photodiode detector for
            # using for outputs
            oinfo = OutputInformation(
                self.name + "_" + dof,
                (self.p1.i, ),
                np.float64,
                "W",
                None,
                "W",
                True,
                False
            )
            ws = PD0Workspace(self, sim, oinfo=oinfo)
            ws.dc_node_id = sim.carrier.node_id(oinfo.nodes[0])
            ws.tmp = np.zeros(ws.size, dtype=complex)
            ws.K = pdtypes.construct_segment_beat_matrix(
                sim.model.mode_index_map, split
            )
            ws.set_output_fn(pd0_DC_output_segmented)
            wss.append(ws)

        return wss

    def _fill_matrix(self, ws):
        for freq in ws.sim.signal.optical_frequencies.frequencies:
            # Get the carrier HOMs for this frequency
            cidx = freq.audio_carrier_index
            rhs_idx = ws.sim.carrier.field(self.p1.i, cidx, 0)
            Ec = np.conjugate(ws.sim.carrier.out_view[rhs_idx:(rhs_idx + ws.sim.model_data.num_HOMs)])
            # is_lower_sb = freq.audio_order < 0
            for efreq in ws.frequencies:
                if ws.signal.connections.P1i_x_idx > -1:
                    with ws.sim.signal.component_edge_fill3(
                        ws.owner_id, ws.signal.connections.P1i_x_idx, freq.index, efreq.index,
                    ) as mat:
                        mat[:] = np.dot(ws.Kx, Ec)

                if ws.signal.connections.P1i_y_idx > -1:
                    with ws.sim.signal.component_edge_fill3(
                        ws.owner_id, ws.signal.connections.P1i_y_idx, freq.index, efreq.index,
                    ) as mat:
                        mat[:] = np.dot(ws.Ky, Ec)


@borrows_nodes()
@float_parameter("f", "Frequency")
@float_parameter("phase", "Phase")
class ReadoutRF(Readout):
    def __init__(self, name, optical_node=None, *, f=None, phase=0, output_detectors=False):
        super().__init__(name, optical_node, output_detectors=output_detectors)

        self.f = f
        self.phase = phase

        self._add_port("I", NodeType.ELECTRICAL)
        self.I._add_node("o", NodeDirection.OUTPUT)
        self._add_port("Q", NodeType.ELECTRICAL)
        self.Q._add_node("o", NodeDirection.OUTPUT)

        self._register_node_coupling("P1i_I", self.p1.i, self.I.o)
        self._register_node_coupling("P1i_Q", self.p1.i, self.Q.o)

        self.outputs = types.SimpleNamespace()
        self.outputs.I = f'{self.name}_I'
        self.outputs.Q = f'{self.name}_Q'

    @property
    def optical_node(self):
        if self.p1.i.component != self:
            return self.p1.i

    def _on_add(self, model):
        model.add(ReadoutOutput(self.name+"_I", self))
        model.add(ReadoutOutput(self.name+"_Q", self))

    def _get_workspace(self, sim):
        if sim.signal:
            has_I_node = self.I.o.full_name in sim.signal.nodes
            has_Q_node = self.Q.o.full_name in sim.signal.nodes

            if not (has_I_node or has_Q_node):
                return None # Don't do anything if no nodes included

            ws = ReadoutWorkspace(self, sim, True, True)
            ws.signal.add_fill_function(self._fill_matrix, True)
            ws.frequencies = sim.signal.electrical_frequencies[self.I.o if has_I_node else self.Q.o].frequencies
            ws.dc_node_id = sim.carrier.node_id(self.p1.i)
            return ws
        else:
            return None

    def _get_output_workspaces(self, sim):
        from finesse.detectors.workspace import OutputInformation
        from finesse.detectors.compute.power import pd1_DC_output
        wss = []
        for quadrature in ('I', 'Q'):
            # Setup a single demodulation photodiode detector for
            # using for outputs
            oinfo = OutputInformation(
                self.name + "_" + quadrature,
                (self.p1.i, ),
                np.float64,
                "W",
                None,
                "W",
                True,
                False
            )
            poff = 90 if quadrature == 'Q' else 0
            ws = PD1Workspace(self, sim, phase_offset=poff, oinfo=oinfo)
            ws.is_f_changing = self.f.is_changing
            ws.is_phase_changing = self.phase.is_changing
            ws.output_real = True
            ws.dc_node_id = sim.carrier.node_id(oinfo.nodes[0])
            ws.homs = ws.sim.model_data.homs_view
            ws.set_output_fn(pd1_DC_output)

            if not ws.is_f_changing:
                # precompute these things if nothing is changing
                ws.update_parameter_values()
                ws.update_beats()

            wss.append(ws)

        if sim.signal:
            oinfo = OutputInformation(
                self.name + "_shot_noise",
                (self.p1.i, ),
                np.float64,
                "W/rtHz",
                None,
                "ASD",
                True,
                False
            )
            wss.append(
                QShotNWorkspace(self, sim, 1, False, output_info=oinfo)
            )
        return wss

    def _fill_matrix(self, ws):
        # 1/2 from demod gain
        factorI = (
            -1 # ddb - can't see why we need this minus sign.
            # Makes us match up with pd2 in v2 and v3 though
            * ws.sim.model_data.EPSILON0_C
            * np.exp(-1j * ws.values.phase * finesse.constants.DEG2RAD)
        )
        cfactorI = factorI.conjugate()
        factorQ = 1j * factorI
        cfactorQ = factorQ.conjugate()

        # Need to zero everything first
        for f1 in ws.sim.carrier.optical_frequencies.frequencies:
            for f2 in ws.sim.carrier.optical_frequencies.frequencies:
                df = f1.f - f2.f
                if df == ws.values.f or df == -ws.values.f:
                    if ws.signal.connections.P1i_I_idx >= 0:
                        with ws.sim.signal.component_edge_fill3(
                            ws.owner_id,
                            ws.signal.connections.P1i_I_idx,
                            ws.sim.carrier.optical_frequencies.get_info(f2.index)["audio_lower_index"],
                            0,
                        ) as mat:
                            mat[:] = 0
                        with ws.sim.signal.component_edge_fill3(
                            ws.owner_id,
                            ws.signal.connections.P1i_I_idx,
                            ws.sim.carrier.optical_frequencies.get_info(f1.index)["audio_upper_index"],
                            0,
                        ) as mat:
                            mat[:] = 0

                    if ws.signal.connections.P1i_Q_idx >= 0:
                        with ws.sim.signal.component_edge_fill3(
                            ws.owner_id,
                            ws.signal.connections.P1i_Q_idx,
                            ws.sim.carrier.optical_frequencies.get_info(f2.index)["audio_lower_index"],
                            0,
                        ) as mat:
                            mat[:] = 0

                        with ws.sim.signal.component_edge_fill3(
                            ws.owner_id,
                            ws.signal.connections.P1i_Q_idx,
                            ws.sim.carrier.optical_frequencies.get_info(f1.index)["audio_upper_index"],
                            0,
                        ) as mat:
                            mat[:] = 0

        for f1 in ws.sim.carrier.optical_frequencies.frequencies:
            for f2 in ws.sim.carrier.optical_frequencies.frequencies:
                df = f1.f - f2.f
                # Get the carrier HOMs for this frequency
                rhs_idx = ws.sim.carrier.field(self.p1.i, f1.index, 0)
                E1 = ws.sim.carrier.out_view[rhs_idx:(rhs_idx + ws.sim.model_data.num_HOMs)]
                rhs_idx = ws.sim.carrier.field(self.p1.i, f2.index, 0)
                E2c = np.conjugate(ws.sim.carrier.out_view[rhs_idx:(rhs_idx + ws.sim.model_data.num_HOMs)])
                
                if df == -ws.values.f:
                    if ws.signal.connections.P1i_I_idx >= 0:
                        with ws.sim.signal.component_edge_fill3(
                            ws.owner_id,
                            ws.signal.connections.P1i_I_idx,
                            ws.sim.carrier.optical_frequencies.get_info(f2.index)["audio_lower_index"],
                            0,
                        ) as mat:
                            # This will apply a conjugation internally as it's
                            # a lower SB connection
                            mat[:] += factorI.conjugate() * E1

                        with ws.sim.signal.component_edge_fill3(
                            ws.owner_id,
                            ws.signal.connections.P1i_I_idx,
                            ws.sim.carrier.optical_frequencies.get_info(f1.index)["audio_upper_index"],
                            0,
                        ) as mat:
                            mat[:] += factorI.conjugate() * E2c

                    if ws.signal.connections.P1i_Q_idx >= 0:
                        with ws.sim.signal.component_edge_fill3(
                            ws.owner_id,
                            ws.signal.connections.P1i_Q_idx,
                            ws.sim.carrier.optical_frequencies.get_info(f2.index)["audio_lower_index"],
                            0,
                        ) as mat:
                            # This will apply a conjugation internally as it's 
                            # a lower SB connection
                            mat[:] += factorQ.conjugate() * E1

                        with ws.sim.signal.component_edge_fill3(
                            ws.owner_id,
                            ws.signal.connections.P1i_Q_idx,
                            ws.sim.carrier.optical_frequencies.get_info(f1.index)["audio_upper_index"],
                            0,
                        ) as mat:
                            mat[:] += factorQ.conjugate() * E2c

                if df == ws.values.f:
                    if ws.signal.connections.P1i_I_idx >= 0:
                        with ws.sim.signal.component_edge_fill3(
                            ws.owner_id,
                            ws.signal.connections.P1i_I_idx,
                            ws.sim.carrier.optical_frequencies.get_info(f2.index)["audio_lower_index"],
                            0,
                        ) as mat:
                            mat[:] += factorI * E1

                        with ws.sim.signal.component_edge_fill3(
                            ws.owner_id,
                            ws.signal.connections.P1i_I_idx,
                            ws.sim.carrier.optical_frequencies.get_info(f1.index)["audio_upper_index"],
                            0,
                        ) as mat:
                            mat[:] += factorI * E2c

                    if ws.signal.connections.P1i_Q_idx >= 0:
                        with ws.sim.signal.component_edge_fill3(
                            ws.owner_id,
                            ws.signal.connections.P1i_Q_idx,
                            ws.sim.carrier.optical_frequencies.get_info(f2.index)["audio_lower_index"],
                            0,
                        ) as mat:
                            mat[:] += factorQ * E1

                        with ws.sim.signal.component_edge_fill3(
                            ws.owner_id,
                            ws.signal.connections.P1i_Q_idx,
                            ws.sim.carrier.optical_frequencies.get_info(f1.index)["audio_upper_index"],
                            0,
                        ) as mat:
                            mat[:] += factorQ * E2c
