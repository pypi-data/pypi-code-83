"""Laser-type optical components for producing beams."""
import logging
import math
import types
import numpy as np

from finesse.cymath.complex import crotate
from finesse.parameter import float_parameter

from finesse.components.general import (
    Connector,
    FrequencyGenerator,
    NoiseType,
    DOFDefinition,
)
from finesse.components.node import NodeType, NodeDirection

LOGGER = logging.getLogger(__name__)


@float_parameter("P", "Power", units="W")
@float_parameter("phase", "Phase", units="degrees")
@float_parameter("f", "Frequency", units="Hz")
class Laser(Connector, FrequencyGenerator):
    """Represents a laser producing a beam with associated properties such as power and
    frequency.

    Parameters
    ----------
    name : str
        Name of the newly created laser.

    P : float, optional
        Power of the laser (in Watts), defaults to 1 W.

    f : float or :class:`.Frequency`, optional
        Frequency-offset of the laser from the default (in Hz) or
        :class:`.Frequency` object. Defaults to 0 Hz offset.

    phase : float, optional
        Phase-offset of the laser from the default, defaults to zero.
    """

    _DEFAULT_POWER_COEFFS = {(0, 0): (1.0, 0.0)}

    def __init__(self, name, P=1, f=0, phase=0):
        Connector.__init__(self, name)
        FrequencyGenerator.__init__(self)

        self._add_port("p1", NodeType.OPTICAL)
        self.p1._add_node("i", NodeDirection.INPUT)
        self.p1._add_node("o", NodeDirection.OUTPUT)

        # Modulation inputs
        self._add_port("amp", NodeType.ELECTRICAL)
        self.amp._add_node("i", NodeDirection.INPUT)
        self._add_port("phs", NodeType.ELECTRICAL)
        self.phs._add_node("i", NodeDirection.INPUT)
        self._add_port("frq", NodeType.ELECTRICAL)
        self.frq._add_node("i", NodeDirection.INPUT)

        self._register_node_coupling("SIGAMP_P1o", self.amp.i, self.p1.o)
        self._register_node_coupling("SIGPHS_P1o", self.phs.i, self.p1.o)
        self._register_node_coupling("SIGFRQ_P1o", self.frq.i, self.p1.o)

        self.f = f
        self.P = P
        self.phase = phase
        self.__power_coeffs = self._DEFAULT_POWER_COEFFS.copy()

        # Define typical degrees of freedom for this component
        self.dofs = types.SimpleNamespace()
        self.dofs.amp = DOFDefinition(self.P, self.amp.i, 1)
        self.dofs.phs = DOFDefinition(self.phase, self.phs.i, 1)
        self.dofs.frq = DOFDefinition(self.f, self.frq.i, 1)

    def _source_frequencies(self):
        return [self.f.ref]

    @property
    def power_coeffs(self):
        """The relative power factors and phase offsets for each HGnm mode.

        :getter: Returns the mode factors and phase offsets as a dict with
                 the mode indices as keys. Read-only.
        """
        return self.__power_coeffs.copy()

    @property
    def non_default_power_coeffs(self):
        """The power factors and phase offsets excluding the default.

        :getter: Returns the non-default mode factors and phase offsets as a
                 dict with the mode indices as keys. Read-only.
        """
        coeffs = self.power_coeffs
        default_coeffs = self._DEFAULT_POWER_COEFFS
        if default_coeffs.items() <= coeffs.items():
            # The current coefficients contain the defaults, so remove them.
            for key in default_coeffs:
                coeffs.pop(key)
        return coeffs

    def tem(self, n, m, factor, phase=0.0):
        """Distributes power into the mode HGnm.

        .. note::
            This does not change the total power of the laser, rather, it
            re-distributes this power into / out of the specified mode.

        Parameters
        ----------
        n, m : int
            Mode indices.

        factor : number
            Relative power factor, modes with equal `factor` will
            have equivalent power distributed to them.

        phase : number, optional; default = 0
            Phase offset for the field, in degrees.
        """
        self.__power_coeffs[(n, m)] = factor, phase

    def __find_src_freq(self, sim):
        # if it's tunable we want to look for the symbol that is just this
        # lasers frequency, as it will be changing
        for f in sim.optical_frequencies.frequencies:
            if not self.f.is_changing:
                # Don't match changing frequency bins if ours won't match
                if not f.symbol.is_changing and (
                    f.f == self.f.value  # match potential param refs
                    or f.f == float(self.f.value)  # match numeric values
                ):
                    # If nothing is changing then we can just match freq values
                    return f
            else:
                # If our frequency is changing then we have to have a frequency bin that
                # matches our symbol
                if f.symbol == self.f.ref:
                    return f  # Simple case
        return None

    def _get_workspace(self, sim):
        from finesse.components.modal.laser import (
            laser_carrier_fill_rhs,
            laser_fill_signal,
            laser_fill_qnoise,
            LaserWorkspace,
            laser_set_gouy,
        )

        ws = LaserWorkspace(self, sim, True)
        ws.node_car_id = sim.carrier.node_id(self.p1.o)
        ws.fsrc_car_idx = -1

        ws.set_gouy_function(laser_set_gouy)
        # Carrier just fills RHS
        ws.carrier.set_fill_rhs_fn(laser_carrier_fill_rhs)

        fsrc = self.__find_src_freq(sim.carrier)
        # Didn't find a Frequency bin for this laser in carrier simulation
        if fsrc is None:
            raise Exception(f"Could not find a frequency bin at {self.f} for {self}")
        ws.fsrc_car_idx = fsrc.index

        if sim.is_modal:
            scaling = 0
            ws.power_coeffs = np.zeros(sim.model_data.num_HOMs, dtype=np.complex128)
            coeffs = self.power_coeffs
            for i in range(sim.model_data.num_HOMs):
                n = sim.model_data.homs_view[i][0]
                m = sim.model_data.homs_view[i][1]

                try:
                    factor, phase = coeffs.pop((n, m))
                except KeyError:
                    factor = phase = 0

                ws.power_coeffs[i] = crotate(
                    complex(math.sqrt(factor), 0), math.radians(phase)
                )
                scaling += abs(ws.power_coeffs[i]) ** 2

            if not scaling:
                raise RuntimeError(
                    f"No power in any modes of {self.name}! At least one mode "
                    "must have a non-zero power factor applied to it."
                )

            for i in range(sim.model_data.num_HOMs):
                ws.power_coeffs[i] /= np.sqrt(scaling)

            if coeffs:
                LOGGER.warning(
                    "The following modes, included in the coeffs of %s, are not being "
                    "modelled and will be ignored: %s",
                    self.name,
                    list(coeffs.keys()),
                )

        if sim.signal:
            ws.node_sig_id = sim.signal.node_id(self.p1.o)
            # Audio sim requies matrix filling
            # for signal couplings
            ws.signal.add_fill_function(laser_fill_signal, True) # TODO sort out refill flag here
            ws.signal.set_fill_noise_function(NoiseType.QUANTUM, laser_fill_qnoise)
            # Find the sideband frequencies
            sb = tuple(
                (
                    f
                    for f in sim.signal.optical_frequencies.frequencies
                    if f.audio_carrier_index == fsrc.index
                )
            )
            if len(sb) != 2:
                raise Exception(
                    f"Only something other than two audio sidebands {sb} for carrier {fsrc}"
                )
            ws.fcar_sig_sb_idx = (sb[0].index, sb[1].index)

        # if sim.is_modal: self._update_tem_gouy_phases(sim)
        return ws

    def _couples_frequency(self, ws, connection, frequency_in, frequency_out):
        # The only connections we have are signal inputs to optical output
        # And all the inputs should generate any output.
        return True
