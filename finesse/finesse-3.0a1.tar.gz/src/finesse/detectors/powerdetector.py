"""
Computes the laser power in an interferometer output or the power from an electrical signal.
"""

import logging
import numbers

import numpy as np
import finesse.detectors._pdtypes as pdtypes
from finesse.detectors.compute import (
    pd0_DC_output,
    pd0_DC_output_segmented,
    pd0_DC_output_masked,
    pd1_DC_output,
    pd1_AC_output,
    pd2_DC_output,
    pd2_AC_output,
)
from finesse.detectors.compute.power import PD0Workspace, PD1Workspace, PD2Workspace
from finesse.detectors.general import MaskedDetector
from finesse.parameter import float_parameter, ParameterState, Parameter


LOGGER = logging.getLogger(__name__)


def check_is_audio(ws, f: Parameter):
    if ws.sim.signal is None:
        return False
    elif f.state == ParameterState.Symbolic:
        return f.value.owner is ws.sim.model.fsig
    else:
        return f.value is ws.sim.model.fsig.f.value


@float_parameter("f", "Frequency")
@float_parameter("phase", "Phase")
class PowerDetectorDemod1(MaskedDetector):
    """Represents a power detector with one RF demodulation.
    It calculates the RF beat power at a node in Watts of optical power.

    If no demodulation phase is specified then this detector outputs a
    complex value `I+1j*Q`.

    Parameters
    ----------
    name : str
        Name of newly created power detector.

    node : :class:`.Node`
        Node to read output from.

    f : float
        Demodulation frequency in Hz

    phase : float, optional
        Demodulation phase in degrees
    """

    def __init__(self, name, node, f, phase=None):
        if f is None:
            raise ValueError("A demodulation frequency must be provided")

        if phase is not None:
            self.__mode = "mixer_real"
            dtype = np.float64
        else:
            self.__mode = "mixer_complex"
            dtype = np.complex128

        self._beats = None

        MaskedDetector.__init__(self, name, node, dtype=dtype, unit="W", label="Power")
        self.f = f
        self.phase = phase

    def _get_workspace(self, sim):
        ws = PD1Workspace(self, sim)

        ws.is_f_changing = self.f.is_changing
        ws.is_phase_changing = self.phase.is_changing

        if ws.is_phase_changing or self.phase.value is not None:
            # We might change from None to some actual value
            ws.output_real = True
            self._set_dtype(np.float64)
        else:
            # If no phase defined output complex power
            ws.output_real = False
            self._set_dtype(np.complex128)

        ws.dc_node_id = sim.carrier.node_id(self.node)
        if sim.signal:
            ws.ac_node_id = sim.signal.node_id(self.node)
            ws.is_audio_mixing = check_is_audio(ws, self.f)

        # Would there be any weird situation where AC and DC homs are different?
        ws.homs = ws.sim.model_data.homs_view

        if ws.is_audio_mixing:
            ws.set_output_fn(pd1_AC_output)
        else:
            ws.set_output_fn(pd1_DC_output)

        if not ws.is_f_changing and not ws.is_audio_mixing:
            # Sidebands beating together are known apriori if frequency bins are not
            # changing, or if this is just an audio mixer.
            ws.update_parameter_values()
            # If frequency is fixed then we just precompute the beats
            ws.update_beats()

        return ws


@float_parameter("f1", "Frequency 1")
@float_parameter("phase1", "Phase 1")
@float_parameter("f2", "Frequency 2")
@float_parameter("phase2", "Phase 2")
class PowerDetectorDemod2(MaskedDetector):
    """Represents a power detector with two RF demodulation.
    It calculates the RF beat power at a node in Watts of optical power.

    If no demodulation phase is specified for the final demodulation
    this detector outputs a complex value `I+1j*Q` where I and Q are
    the in-phase and quadrature parts of the signal.

    Parameters
    ----------
    name : str
        Name of newly created power detector.

    node : :class:`.Node`
        Node to read output from.

    f1 : float
        First demodulation frequency in Hz

    phase1 : float
        First demodulation phase in degrees

    f2 : float
        Second demodulation frequency in Hz

    phase2 : float, optional
        Second demodulation phase in degrees
    """

    def __init__(self, name, node, f1, phase1, f2, phase2=None):
        if phase2 is not None:
            self.__mode = "mixer_real"
            dtype = np.float64
        else:
            self.__mode = "mixer_complex"
            dtype = np.complex128

        self._beats = None

        MaskedDetector.__init__(self, name, node, dtype=dtype, unit="W", label="Power")
        self.f1 = f1
        self.phase1 = phase1
        self.f2 = f2
        self.phase2 = phase2

    def _get_workspace(self, sim):
        ws = PD2Workspace(self, sim)

        ws.is_f1_changing = self.f1.is_changing
        ws.is_phase1_changing = self.phase1.is_changing
        ws.is_f2_changing = self.f2.is_changing
        ws.is_phase2_changing = self.phase2.is_changing

        if ws.is_phase2_changing or self.phase2.value is not None:
            # We might change from None to some actual value
            ws.output_real = True
            self._set_dtype(np.float64)
        else:
            # If no phase defined output complex power
            ws.output_real = False
            self._set_dtype(np.complex128)

        ws.dc_node_id = sim.carrier.node_id(self.node)

        if sim.signal:
            ws.ac_node_id = sim.signal.node_id(self.node)
            if check_is_audio(ws, self.f1):
                raise Exception(
                    f"pd2 {self.name} f1 cannot be an audio frequency, use f2 for audio demodulation"
                )
            ws.is_audio_mixing = check_is_audio(ws, self.f2)

        # Would there be any weird situation where AC and DC homs are different?
        ws.homs = ws.sim.model_data.homs_view

        if ws.is_audio_mixing:
            ws.set_output_fn(pd2_AC_output)
        else:
            ws.set_output_fn(pd2_DC_output)

        # if not ws.is_f1_changing and not (ws.is_f2_changing and ws.is_audio_mixing):
        #     # Sidebands beating together are known apriori if frequency bins are not
        #     # changing, or if this is just an audio mixer.
        #     ws.update_parameter_values()
        #     # If frequency is fixed then we just precompute the beats
        #     ws.update_beats()

        return ws


class PowerDetector(MaskedDetector):
    """Represents a power detector with no RF demodulations.
    It calculates the DC laser power at a node in Watts of optical power.

    Parameters
    ----------
    name : str
        Name of newly created power detector.

    node : :class:`.Node`
        Node to read output from.
    """

    def __init__(self, name, node, *, pdtype=None):
        MaskedDetector.__init__(
            self, name, node, dtype=np.float64, unit="W", label="Power"
        )
        self.pdtype = getattr(pdtypes, pdtype.upper()) if isinstance(pdtype, str) else pdtype

    def _get_workspace(self, sim):
        ws = PD0Workspace(self, sim)

        ni = sim.carrier.get_node_info(self.node)
        ws.rhs_index = ni["rhs_index"]
        ws.size = ni["nfreqs"] * ni["nhoms"]
        ws.dc_node_id = sim.carrier.node_id(self.node)

        if ws.has_mask:
            if self.pdtype: # not supported yet
                raise NotImplementedError()
            ws.set_output_fn(pd0_DC_output_masked)
        else:
            if self.pdtype:
                import finesse.detectors._pdtypes as pdtype
                ws.tmp = np.zeros(ws.size, dtype=complex)
                ws.K = pdtype.construct_segment_beat_matrix(sim.model.mode_index_map, self.pdtype)
                ws.set_output_fn(pd0_DC_output_segmented)
            else:
                ws.set_output_fn(pd0_DC_output)
        return ws


@float_parameter("f1", "Frequency 1")
@float_parameter("f2", "Frequency 2")
@float_parameter("f3", "Frequency 3")
@float_parameter("f4", "Frequency 4")
@float_parameter("f5", "Frequency 5")
@float_parameter("f6", "Frequency 6")
@float_parameter("f7", "Frequency 7")
@float_parameter("f8", "Frequency 8")
@float_parameter("f9", "Frequency 9")
@float_parameter("phase1", "Phase 1")
@float_parameter("phase2", "Phase 2")
@float_parameter("phase3", "Phase 3")
@float_parameter("phase4", "Phase 4")
@float_parameter("phase5", "Phase 5")
@float_parameter("phase6", "Phase 6")
@float_parameter("phase7", "Phase 7")
@float_parameter("phase8", "Phase 8")
@float_parameter("phase9", "Phase 9")
class CustomPD(PowerDetector):
    """A custom power detector with beat coefficients describing the coupling of modes."""

    def __init__(self, name, node, beats, **kwargs):
        PowerDetector.__init__(self, name, node, **kwargs)

        if isinstance(beats, np.ndarray):
            self._beats = beats
            self._beats_dict = None
        elif isinstance(beats, dict):
            # the field _beats will be replaced by a np array once
            # construct beats is called (this happens automatically
            # when adding a CustomPD object to a model and / or
            # changing the maxtem value of the model)
            self._beats = None
            self._beats_dict = beats

    def construct_beats(self, maxtem=None):
        """Constructs, or re-constructs, the beat coefficients matrix
        based on the value of `maxtem`.

        The underlying generic beats dictionary passed during construction
        is used to generate the beat factor matrix. If a beats matrix was
        passed directly during construction of the CustomPD, then this
        method has no effect.

        Parameters
        ----------
        maxtem : int, optional
            The maximum TEM order to generate the beat coefficients up
            to. Defaults to `None` such that this value is taken from
            the model associated with this detector.
        """
        if self._beats_dict is None:
            return

        if maxtem is None:
            maxtem = self._model.modes_setting["maxtem"]

            if maxtem is None:
                return

        self._beats = np.zeros((1 + maxtem, 1 + maxtem, 1 + maxtem, 1 + maxtem))

        for (n1, m1, n2, m2), factor in self._beats_dict.items():
            if all(isinstance(k, numbers.Number) for k in (n1, m1, n2, m2)):
                self._beats[int(n1)][int(m1)][int(n2)][int(m2)] = factor
            else:
                if all(k == "x" for k in (m1, m2)) and all(
                    isinstance(k, numbers.Number) for k in (n1, n2)
                ):
                    n1 = int(n1)
                    n2 = int(n2)
                    if n1 > maxtem or n2 > maxtem:
                        continue

                    for i in range(maxtem):
                        self._beats[n1][i][n2][i] = factor
                        self._beats[n2][i][n1][i] = factor
                elif all(k == "x" for k in (n1, n2)) and all(
                    isinstance(k, numbers.Number) for k in (m1, m2)
                ):
                    m1 = int(m1)
                    m2 = int(m2)
                    if m1 > maxtem or m2 > maxtem:
                        continue

                    for i in range(maxtem):
                        self._beats[i][m1][i][m2] = factor
                        self._beats[i][m2][i][m1] = factor


@float_parameter("f1", "Frequency 1")
@float_parameter("f2", "Frequency 2")
@float_parameter("f3", "Frequency 3")
@float_parameter("f4", "Frequency 4")
@float_parameter("f5", "Frequency 5")
@float_parameter("f6", "Frequency 6")
@float_parameter("f7", "Frequency 7")
@float_parameter("f8", "Frequency 8")
@float_parameter("f9", "Frequency 9")
@float_parameter("phase1", "Phase 1")
@float_parameter("phase2", "Phase 2")
@float_parameter("phase3", "Phase 3")
@float_parameter("phase4", "Phase 4")
@float_parameter("phase5", "Phase 5")
@float_parameter("phase6", "Phase 6")
@float_parameter("phase7", "Phase 7")
@float_parameter("phase8", "Phase 8")
@float_parameter("phase9", "Phase 9")
class SplitPD(CustomPD):
    def __init__(self, name, node, direction, **kwargs):
        if direction == "x":
            beats = pdtypes.XSPLIT
        else:
            beats = pdtypes.YSPLIT

        CustomPD.__init__(self, name, node, beats, **kwargs)

        self.__direction = direction
