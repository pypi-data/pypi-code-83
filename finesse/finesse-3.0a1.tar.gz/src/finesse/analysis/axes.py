import logging

from finesse.parameter import Parameter
import finesse.analysis.actions as ac

LOGGER = logging.getLogger(__name__)


def noxaxis(model):
    analysis = ac.Noxaxis()
    return analysis.run(model)


def xaxis(
    param: Parameter,
    mode: str,
    start: float,
    stop: float,
    steps: int,
    relative: bool = False,
):
    """Runs a model to scan a parameter between two points for a number of steps.

    The model that is run is retrieved from the parameter reference.

    This should provide an equivalent to the xaxis command in Finesse v2.

    Parameters
    ----------
    param : :class:`.Parameter`
        Parameter of component to scan.
    mode : str
        'lin' or 'log' for linear or logarithmic step sizes.
    start, stop : float
        Start and end values of the scan.
    steps : int
        Number of steps between start and end.
    relative : float, optional
        Changes relative to parameter initial value
    """
    analysis = ac.Xaxis(
        param.full_name, mode, start, stop, steps, relative=relative
    )
    sol = analysis.run(param.owner._model)
    return sol


def x2axis(
    param1,
    mode1,
    start1,
    stop1,
    steps1,
    param2,
    mode2,
    start2,
    stop2,
    steps2,
    relative=0,
    **kwargs,
):
    """Runs a model to scan a parameter between two points for a number of steps.
    The model that is run is retrieved from the parameter reference.

    This should provide an equivalent to the x2axis command in Finesse v2.

    Parameters
    ----------
    param1, param2 : :class:`.Parameter`
        Parameter of component to scan.
    mode1, mode2 : str
        'lin' or 'log' for linear or logarithmic step sizes for axis 1 and 2.
    start1, stop1, start2, stop2 : float
        Start and end values of the scan.
    steps1, steps2 : int
        Number of steps between start and end.
    relative : float, optional
        Changes relative to parameter initial value

    Notes
    -----
    `param2` is in the inner loop and `param1` in the outer loop.
    """
    if param1.owner._model is not param2.owner._model:
        raise ValueError(
            f"Parameters {param1} and {param2}, are from different models."
        )

    analysis = ac.X2axis(
        f"{param1.owner.name}.{param1.name}",
        mode1,
        start1,
        stop1,
        steps1,
        f"{param2.owner.name}.{param2.name}",
        mode2,
        start2,
        stop2,
        steps2,
        relative=relative
    )

    return analysis.run(param1.owner._model)


def x3axis(
    param1,
    mode1,
    start1,
    stop1,
    steps1,
    param2,
    mode2,
    start2,
    stop2,
    steps2,
    param3,
    mode3,
    start3,
    stop3,
    steps3,
    relative=False,
    **kwargs,
):
    """Runs a model to scan a parameter between two points for a number of steps.
    The model that is run is retrieved from the parameter reference.

    This should provide an equivalent to the x3axis command in Finesse v2.

    Parameters
    ----------
    param1, param2, param3 : :class:`.Parameter`
        Parameter of component to scan.
    mode1, mode2, mode3 : str
        'lin' or 'log' for linear or logarithmic step sizes for each axis.
    start1, stop1, start2, stop2, start3, stop3 : float
        Start and end values of the scan.
    steps1, steps2, steps3 : int
        Number of steps between start and end.
    relative : float, optional
        Changes relative to parameter initial value

    Notes
    -----
    `param3` is in the inner loop and `param1` in the outer loop.
    """
    model = param1.owner._model
    if any(param.owner._model is not model for param in (param1, param2, param3)):
        raise ValueError(
            f"Parameters {param1}, {param2}, and {param3}, are not from the same models."
        )
    analysis = ac.X3axis(
        param1.full_name,
        mode1,
        start1,
        stop1,
        steps1,
        param2.full_name,
        mode2,
        start2,
        stop2,
        steps2,
        param3.full_name,
        mode3,
        start3,
        stop3,
        steps3,
        relative=relative
    )

    return analysis.run(param1.owner._model)
