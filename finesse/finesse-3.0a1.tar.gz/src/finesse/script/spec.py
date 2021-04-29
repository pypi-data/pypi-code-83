"""Kat script specification.

This defines supported kat script syntax and maps it to Finesse Python classes via
adapters.
"""

import abc
from difflib import get_close_matches
import logging
from collections import ChainMap
from .. import components, detectors, locks, symbols
from ..model import Model
from ..components import mechanical, electronics
from ..components.ligo import suspensions as ligo
from ..analysis import actions
from ..analysis import noise
from .adapter import ElementAdapter, CommandAdapter, AnalysisAdapter, GetterProxy


LOGGER = logging.getLogger(__name__)


class _GuassGetterProxy(GetterProxy):
    def __call__(self, gauss):
        # Use the :attr:`.Gauss._specified_params` attribute to dump the `kwargs`
        # signature argument.
        return [], {"name": gauss.name, "node": gauss.node, **gauss._specified_params}


class _FsigGetterProxy(GetterProxy):
    def __call__(self, model):
        if model.fsig.f.value is None:
            return

        return [model.fsig.f], {}


def _set_fsig(model, f):
    """Signal input frequency.

    Parameters
    ----------
    f : float or :class:`.Symbol`
        The frequency.
    """
    model.fsig.f = f


class _LambdaGetterProxy(GetterProxy):
    def __call__(self, model):
        return [model.lambda0], {}


def _set_lambda0(model, lambda0):
    """Reference wavelength.

    Parameters
    ----------
    lambda0 : float
        The reference wavelength.
    """
    model.lambda0 = lambda0


class _ModesGetterProxy(GetterProxy):
    def __call__(self, model):
        modes = model.modes_setting

        # Filter out empty values.
        modes = {key: value for key, value in modes.items() if value is not None}

        if not modes:
            return

        return [], modes


def _set_link(model, *args, **kwargs):
    model.link(*args, **kwargs)


class _IntrixGetterProxy(GetterProxy):
    def __call__(self, model):
        if not model.input_matrix_dc:
            return

        # FIXME: implement proper getter
        raise NotImplementedError("intrix dumping not yet implemented")


def _set_intrix(model, *args, **kwargs):
    """Set input matrix."""
    assert not kwargs

    DOF = args[0]
    factors, readouts = args[1::2], args[2::2]
    if len(factors) != len(readouts):
        raise Exception("must specify 'factor, readout' pairs")
    for factor, readout in zip(factors, readouts):
        model.input_matrix_dc[DOF, readout] = factor


class _TEMGetterProxy(GetterProxy):
    def __call__(self, model):
        """(args, kwargs) tuples for each defined TEM mode."""
        tems = []

        for laser in model.get_elements_of_type(components.Laser):
            for (n, m), (factor, phase) in laser.non_default_power_coeffs.items():
                tems.append(
                    ([laser], {"n": n, "m": m, "factor": factor, "phase": phase})
                )

        if not tems:
            # Don't generate anything.
            return

        return tems


def _set_tem(model, laser, *args, **kwargs):
    """Set laser TEM."""
    laser.tem(*args, **kwargs)


class BaseSpec(metaclass=abc.ABCMeta):
    """Empty language specification."""

    _SUPPORTED_CONSTANTS = {}
    _SUPPORTED_KEYWORDS = set()
    _SUPPORTED_UNARY_OPERATORS = {}
    _SUPPORTED_BINARY_OPERATORS = {}
    _SUPPORTED_EXPRESSION_FUNCTIONS = {}
    _DEFAULT_ELEMENTS = []
    _DEFAULT_COMMANDS = []
    _DEFAULT_ANALYSES = []

    def __init__(self):
        # Modifiable specifications. These are dynamically supported by the parser.
        self.elements = {}
        self.commands = {}
        self.analyses = {}

        # Fixed specifications. These are not modifiable by the user.
        self.constants = self._SUPPORTED_CONSTANTS
        self.keywords = self._SUPPORTED_KEYWORDS
        self.unary_operators = self._SUPPORTED_UNARY_OPERATORS
        self.binary_operators = self._SUPPORTED_BINARY_OPERATORS
        self.expression_functions = self._SUPPORTED_EXPRESSION_FUNCTIONS

        # Add support for the default directives.
        for elementdata in self._DEFAULT_ELEMENTS:
            self.register_element(*elementdata)
        for commanddata in self._DEFAULT_COMMANDS:
            self.register_command(*commanddata)
        for analysisdata in self._DEFAULT_ANALYSES:
            self.register_analysis(*analysisdata)

    @property
    def directives(self):
        """All top level parser directives.

        :getter: Returns a mapping of top level parser directive aliases to
                 :class:`adapters <.BaseAdapter>`.
        :type: :class:`~collections.ChainMap`
        """
        # ChainMap yields in LIFO order so key order becomes elements, then commands,
        # then analyses. This order is relied upon by :func:`.syntax`.
        return ChainMap(self.analyses, self.commands, self.elements)

    @property
    def reserved_names(self):
        """All reserved names.

        This is primarily useful for tests.

        :getter: Returns the names reserved in the parser as special production types.
        :type: :class:`list`
        """
        return list(self.keywords) + list(self.constants)

    def _register_adapter(self, ptype, mapping, aliases, kwargs=None, overwrite=False):
        if kwargs is None:
            kwargs = {}

        adapter = ptype(aliases, **kwargs)

        for alias in adapter.aliases:
            if alias in mapping:
                if overwrite:
                    LOGGER.info(f"Overwriting existing '{alias}' with {adapter}")
                else:
                    raise KeyError(
                        f"'{alias}' from {adapter} already exists (provided by "
                        f"{mapping[alias]}). If you intend to overwrite the existing "
                        f"definition, set overwrite=True."
                    )

            mapping[alias] = adapter

    def register_element(self, *args, **kwargs):
        """Add parser and generator support for a model element such as a component or
        detector.

        Other Parameters
        ----------------
        aliases : str or sequence
            The element alias(es).

        kwargs : mapping, optional
            Keyword arguments to pass to the adapter constructor; defaults to None.

        overwrite : bool, optional
            Overwrite elements with the same aliases, if present. Defaults to False.
        """
        self._register_adapter(ElementAdapter, self.elements, *args, **kwargs)

    def register_command(self, *args, **kwargs):
        """Add parser and generator support for a command.

        Other Parameters
        ----------------
        aliases : str or sequence
            The command alias(es).

        kwargs : mapping, optional
            Keyword arguments to pass to the adapter constructor; defaults to None.

        overwrite : bool, optional
            Overwrite commands with the same aliases, if present. Defaults to False.
        """
        self._register_adapter(CommandAdapter, self.commands, *args, **kwargs)

    def register_analysis(self, *args, **kwargs):
        """Add parser and generator support for an analysis.

        Other Parameters
        ----------------
        aliases : str or sequence
            The analysis alias(es).

        kwargs : mapping, optional
            Keyword arguments to pass to the adapter constructor; defaults to None.

        overwrite : bool, optional
            Overwrite analyses with the same aliases, if present. Defaults to False.
        """
        self._register_adapter(AnalysisAdapter, self.analyses, *args, **kwargs)

    def adapter_by_setter(self, setter):
        """Get adapter given its Python setter.

        Parameters
        ----------
        setter : type
            The setter to look up the adapter for.

        Returns
        -------
        :class:`.BaseAdapter`
            The adapter corresponding to `setter`.

        Raises
        ------
        ValueError
            If no adapter corresponding to `setter` could be found.
        """
        for adapter in self.directives.values():
            if adapter.setter == setter:
                return adapter

        raise ValueError(f"Could not find adapter for '{setter!r}'")

    def match_fuzzy_directive(self, search, limit=3, cutoff=0.5):
        """Get the directives that most closely match the specified string.

        Parameters
        ----------
        search : str
            The directive to search for.

        limit : int, optional
            The maximum number of matches to return.

        cutoff : float, optional
            The cutoff below which to assume no match. This is the ratio as defined in
            the `Python documentation
            <https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.ratio>`__.

        Returns
        -------
        list
            Up to `limit` closest matches.
        """
        return get_close_matches(search, self.directives, n=limit, cutoff=cutoff)


class KatSpec(BaseSpec):
    """Kat language specification.

    This defines the available instructions for the parser and the adapters that convert
    them to and from Python models. The default instructions, actions and keywords are
    built into public properties which may be modified by users (e.g. to add support for
    custom commands). As such, the internal defaults (fields with names beginning
    `_DEFAULT_`) should not be modified after import.
    """

    # List of default elements in (aliases, type, kwargs) form.
    # :class:`.InstructionAdapter` objects are created for each element and the aliases
    # are each mapped to their corresponding adapter. Order here does not matter.
    _DEFAULT_ELEMENTS = [
        # Components.
        (
            ("amplifier", "amp"),
            {"setter": electronics.Amplifier, "getter": electronics.Amplifier},
        ),
        (
            ("beamsplitter", "bs"),
            {"setter": components.Beamsplitter, "getter": components.Beamsplitter},
        ),
        # Cavity's `build_last` flag is set because it implicitly depends on any nodes
        # that appear in the path from its start port back to itself, so its
        # dependencies cannot be determined by the time the first set of elements are
        # built into the model. It is therefore moved to the second build pass by this
        # flag.
        (
            ("cavity", "cav"),
            {
                "setter": components.Cavity,
                "getter": components.Cavity,
                "build_last": True,
            },
        ),
        (
            ("degree_of_freedom", "dof"),
            {
                "setter": components.DegreeOfFreedom,
                "getter": components.DegreeOfFreedom,
            },
        ),
        (
            ("directional_beamsplitter", "dbs"),
            {
                "setter": components.DirectionalBeamsplitter,
                "getter": components.DirectionalBeamsplitter,
            },
        ),
        (
            ("filter_zpk", "zpk"),
            {"setter": electronics.ZPKFilter, "getter": electronics.ZPKFilter},
        ),
        (
            ("filter_butter", "butter"),
            {"setter": electronics.ButterFilter, "getter": electronics.ButterFilter},
        ),
        (
            ("filter_cheby1", "cheby1"),
            {"setter": electronics.Cheby1Filter, "getter": electronics.Cheby1Filter},
        ),
        (
            ("isolator", "isol"),
            {"setter": components.Isolator, "getter": components.Isolator},
        ),
        (("laser", "l"), {"setter": components.Laser, "getter": components.Laser}),
        ("lens", {"setter": components.Lens, "getter": components.Lens}),
        (("mirror", "m"), {"setter": components.Mirror, "getter": components.Mirror}),
        (
            ("modulator", "mod"),
            {"setter": components.Modulator, "getter": components.Modulator},
        ),
        (
            ("optical_bandpass", "obp"),
            {
                "setter": components.optical_bandpass.OpticalBandpassFilter,
                "getter": components.optical_bandpass.OpticalBandpassFilter,
            },
        ),
        (
            ("squeezer", "sq"),
            {"setter": components.Squeezer, "getter": components.Squeezer},
        ),
        (
            "readout_dc",
            {"setter": components.ReadoutDC, "getter": components.ReadoutDC},
        ),
        (
            "readout_dc_qpd",
            {"setter": components.ReadoutDCQPD, "getter": components.ReadoutDCQPD},
        ),
        (
            "readout_rf",
            {"setter": components.ReadoutRF, "getter": components.ReadoutRF},
        ),
        (
            ("variable", "var"),
            {"setter": components.Variable, "getter": components.Variable},
        ),
        # Detectors.
        (
            ("amplitude_detector", "ad"),
            {
                "setter": detectors.AmplitudeDetector,
                "getter": detectors.AmplitudeDetector,
            },
        ),
        (
            "astigd",
            {
                "setter": detectors.AstigmatismDetector,
                "getter": detectors.AstigmatismDetector,
            },
        ),
        (
            ("beam_property_detector", "bp"),
            {
                "setter": detectors.BeamPropertyDetector,
                "getter": detectors.BeamPropertyDetector,
            },
        ),
        ("ccd", {"setter": detectors.CCD, "getter": detectors.CCD}),
        ("ccdline", {"setter": detectors.CCDScanLine, "getter": detectors.CCDScanLine}),
        ("ccdpx", {"setter": detectors.CCDPixel, "getter": detectors.CCDPixel}),
        (
            "cp",
            {
                "setter": detectors.CavityPropertyDetector,
                "getter": detectors.CavityPropertyDetector,
            },
        ),
        ("fcam", {"setter": detectors.FieldCamera, "getter": detectors.FieldCamera}),
        (
            "fline",
            {"setter": detectors.FieldScanLine, "getter": detectors.FieldScanLine},
        ),
        ("fpx", {"setter": detectors.FieldPixel, "getter": detectors.FieldPixel}),
        # Gouy's `build_last` flag is set because it implicitly depends on any nodes
        # that appear in the path from its start port back to itself, so its
        # dependencies cannot be determined by the time the first set of elements are
        # built into the model. It is therefore moved to the second build pass by this
        # flag.
        (
            "gouy",
            {"setter": detectors.Gouy, "getter": detectors.Gouy, "build_last": True},
        ),
        ("knmd", {"setter": detectors.KnmDetector, "getter": detectors.KnmDetector}),
        (
            "mmd",
            {
                "setter": detectors.ModeMismatchDetector,
                "getter": detectors.ModeMismatchDetector,
            },
        ),
        (
            ("motion_detector", "xd"),
            {"setter": detectors.MotionDetector, "getter": detectors.MotionDetector},
        ),
        (
            ("power_detector_dc", "pd"),
            {"setter": detectors.PowerDetector, "getter": detectors.PowerDetector},
        ),
        (
            ("power_detector_demod_1", "pd1"),
            {
                "setter": detectors.PowerDetectorDemod1,
                "getter": detectors.PowerDetectorDemod1,
            },
        ),
        (
            ("power_detector_demod_2", "pd2"),
            {
                "setter": detectors.PowerDetectorDemod2,
                "getter": detectors.PowerDetectorDemod2,
            },
        ),
        (
            ("quantum_noise_detector", "qnoised"),
            {
                "setter": detectors.QuantumNoiseDetector,
                "getter": detectors.QuantumNoiseDetector,
            },
        ),
        (
            ("quantum_noise_detector_demod_1", "qnoised1"),
            {
                "setter": detectors.QuantumNoiseDetectorDemod1,
                "getter": detectors.QuantumNoiseDetectorDemod1,
            },
        ),
        (
            ("quantum_noise_detector_demod_2", "qnoised2"),
            {
                "setter": detectors.QuantumNoiseDetectorDemod2,
                "getter": detectors.QuantumNoiseDetectorDemod2,
            },
        ),
        (
            ("quantum_shot_noise_detector", "qshot"),
            {
                "setter": detectors.QuantumShotNoiseDetector,
                "getter": detectors.QuantumShotNoiseDetector,
            },
        ),
        (
            ("quantum_shot_noise_detector_demod_1", "qshot1"),
            {
                "setter": detectors.QuantumShotNoiseDetectorDemod1,
                "getter": detectors.QuantumShotNoiseDetectorDemod1,
            },
        ),
        (
            ("quantum_shot_noise_detector_demod_2", "qshot2"),
            {
                "setter": detectors.QuantumShotNoiseDetectorDemod2,
                "getter": detectors.QuantumShotNoiseDetectorDemod2,
            },
        ),
        (
            ("signal_generator", "sgen"),
            {
                "setter": components.SignalGenerator,
                "getter": components.SignalGenerator,
            },
        ),
        ("splitpd", {"setter": detectors.SplitPD, "getter": detectors.SplitPD}),
        (
            ("zpk_actuator", "actuator"),
            {
                "setter": electronics.ZPKNodeActuator,
                "getter": electronics.ZPKNodeActuator,
            },
        ),
        # Connectors.
        (("space", "s"), {"setter": components.Space, "getter": components.Space}),
        ("nothing", {"setter": components.Nothing, "getter": components.Nothing}),
        # Mechanics.
        ("free_mass", {"setter": mechanical.FreeMass, "getter": mechanical.FreeMass}),
        ("pendulum", {"setter": mechanical.Pendulum, "getter": mechanical.Pendulum}),
        (
            "ligo_triple",
            {"setter": ligo.LIGOTripleSuspension, "getter": ligo.LIGOTripleSuspension},
        ),
        (
            "ligo_quad",
            {"setter": ligo.LIGOQuadSuspension, "getter": ligo.LIGOQuadSuspension},
        ),
        # Lock.
        ("lock", {"setter": locks.Lock, "getter": locks.Lock}),
        # Noises.
        ("noise", {"setter": noise.ClassicalNoise, "getter": noise.ClassicalNoise}),
        # Gauss.
        ("gauss", {"setter": components.Gauss, "getter": _GuassGetterProxy()},),
    ]

    # List of default function adapters.
    _DEFAULT_COMMANDS = [
        (
            # Fsig.
            # This technically sets a component (:class:`.finesse.frequency.Fsig`), but
            # it's always present in models so this is instead implemented as a command.
            "fsig",
            {"setter": _set_fsig, "getter": _FsigGetterProxy(), "singular": True},
        ),
        (
            "lambda",
            {"setter": _set_lambda0, "getter": _LambdaGetterProxy(), "singular": True},
        ),
        (
            "modes",
            {
                "setter": Model.select_modes,
                "getter": _ModesGetterProxy(),
                "singular": True,
            },
        ),
        ("link", {"setter": _set_link, "singular": False},),
        (
            "intrix",
            {"setter": _set_intrix, "getter": _IntrixGetterProxy(), "singular": False},
        ),
        ("tem", {"setter": _set_tem, "getter": _TEMGetterProxy(), "singular": False},),
    ]

    _DEFAULT_ANALYSES = [
        # Group actions.
        ("parallel", {"setter": actions.Parallel, "getter": actions.Parallel}),
        ("series", {"setter": actions.Series, "getter": actions.Series}),
        # Axes.
        ("noxaxis", {"setter": actions.Noxaxis, "getter": actions.Noxaxis}),
        ("xaxis", {"setter": actions.Xaxis, "getter": actions.Xaxis}),
        ("x2axis", {"setter": actions.X2axis, "getter": actions.X2axis}),
        ("x3axis", {"setter": actions.X3axis, "getter": actions.X3axis}),
        ("sweep", {"setter": actions.Sweep, "getter": actions.Sweep}),
        ("change", {"setter": actions.Change, "getter": actions.Change}),
        (
            ("freqresp", "frequency_response"),
            {"setter": actions.FrequencyResponse, "getter": actions.FrequencyResponse},
        ),
        (
            "opt_rf_readout_phase",
            {
                "setter": actions.OptimiseRFReadoutPhaseDC,
                "getter": actions.OptimiseRFReadoutPhaseDC,
            },
        ),
        (
            "sensing_matrix_dc",
            {"setter": actions.SensingMatrixDC, "getter": actions.SensingMatrixDC},
        ),
        # Model physics.
        (
            "noise_analysis",
            {"setter": noise.NoiseAnalysis, "getter": noise.NoiseAnalysis},
        ),
        ("abcd", {"setter": actions.ABCD, "getter": actions.ABCD}),
        ("beam_trace", {"setter": actions.BeamTrace, "getter": actions.BeamTrace}),
        (
            "propagate_beam",
            {"setter": actions.PropagateBeam, "getter": actions.PropagateBeam},
        ),
        (
            "propagate_beam_astig",
            {
                "setter": actions.PropagateAstigmaticBeam,
                "getter": actions.PropagateAstigmaticBeam,
            },
        ),
        # Utilities.
        ("debug", {"setter": actions.Debug, "getter": actions.Debug}),
        ("plot", {"setter": actions.Plot, "getter": actions.Plot}),
        ("print", {"setter": actions.Printer, "getter": actions.Printer}),
        ("run_locks", {"setter": actions.RunLocks, "getter": actions.RunLocks}),
        (
            "noise_projection",
            {"setter": actions.NoiseProjection, "getter": actions.NoiseProjection},
        ),
        ("print_model", {"setter": actions.PrintModel, "getter": actions.PrintModel}),
        (
            "print_model_attr",
            {"setter": actions.PrintModelAttr, "getter": actions.PrintModelAttr},
        ),
    ]

    _SUPPORTED_KEYWORDS = {
        # None.
        "none",
        # HOM collections.
        "even",
        "odd",
        "x",
        "y",
        "off",
        # Axis scales.
        "lin",
        "log",
        # Modulator types.
        "am",
        "pm",
        # Filter types.
        "lowpass",
        "highpass",
        "bandpass",
        "bandstop",
        "xsplit",
        "ysplit",
        # Beam properties (see :class:`finesse.detectors.compute.gaussian.BeamProperty`).
        *detectors.bpdetector.BP_KEYWORDS.keys(),
        # Cavity properties (see :class:`finesse.detectors.compute.gaussian.CavityProperty`).
        *detectors.cavity_detector.CP_KEYWORDS.keys(),
    }

    _SUPPORTED_CONSTANTS = symbols.CONSTANTS

    _SUPPORTED_UNARY_OPERATORS = {
        "+": symbols.FUNCTIONS["pos"],
        "-": symbols.FUNCTIONS["neg"],
    }

    _SUPPORTED_BINARY_OPERATORS = {
        "+": symbols.OPERATORS["__add__"],
        "-": symbols.OPERATORS["__sub__"],
        "*": symbols.OPERATORS["__mul__"],
        "**": symbols.OPERATORS["__pow__"],
        "/": symbols.OPERATORS["__truediv__"],
        "//": symbols.OPERATORS["__floordiv__"],
    }

    # Built-in functions.
    _SUPPORTED_EXPRESSION_FUNCTIONS = symbols.FUNCTIONS
