"""Actions."""

import abc
import re
import logging
import textwrap
from collections import defaultdict
import numpy as np
from tabulate import tabulate

import finesse
from finesse.solutions import ArraySolution
from finesse.parameter import Parameter
from finesse.analysis.runners import run_axes_scan, run_fsig_sweep
from finesse.tree import TreeNode
from finesse.solutions import BaseSolution
from finesse.parameter import GeometricParameter
from finesse.element import ModelElement
from finesse.components import Port, Node, NodeType, DegreeOfFreedom
from finesse.detectors.compute.quantum import QShot0Workspace, QShotNWorkspace

LOGGER = logging.getLogger(__name__)


def convert_str_to_parameter(model, attr: str):
    """Converts names `component.parameter` or `component` to a parameter object. Will
    return default parameter when component name is given.

    Parameters
    ----------
    model : Model
        Model object to look for parameter in
    attr : str
        String value for the name of an element or a parameters full name

    Returns
    -------
    parameter
        The equivalent Parameter object for the attr provided
    """
    obj = model.reduce_get_attr(attr)
    # If this attr string has no period in it, assume it is an element name
    # and try and get it
    if "." in attr:
        return obj
    else:
        if obj.default_parameter_name is None:
            raise ValueError(
                f"{repr(obj)} does not have a default parameter, please specify one to use"
            )
        return getattr(obj, obj.default_parameter_name)


def get_sweep_array(start: float, stop: float, steps: int, mode="lin"):
    start = float(start)
    stop = float(stop)
    steps = int(steps)
    if steps <= 0:
        raise Exception("Steps must be greater than 0")

    if mode == "lin":
        arr = np.linspace(start, stop, steps + 1)
    else:
        arr = np.logspace(np.log10(start), np.log10(stop), steps + 1)

    return arr


def request_dict_reduction(A, B):
    dd = defaultdict(list)
    for d in (A, B):
        for key, value in d.items():
            dd[key].extend(value)
    return dd


class AnalysisState(TreeNode):
    def __init__(self, model, name="AnalysisState", parent=None):
        super().__init__(f"{name} {model}", parent=parent)
        assert isinstance(model, finesse.model.Model)
        self.__model = model
        self.__sim = None
        self.__previous_solution = None
        self.model_finished_with = True

    @property
    def model(self):
        return self.__model

    @property
    def sim(self):
        return self.__sim

    @property
    def previous_solution(self):
        return self.__previous_solution

    def apply(self, action):
        sol = action._do(self)
        if sol:
            self.__previous_solution = sol
        return sol

    def _split(self):
        state = AnalysisState(self.model.deepcopy(), parent=self)
        return state

    def name_to_elec_mech_nodes(self, nodes):
        rtn = []
        for name in nodes:
            obj = self.model.reduce_get_attr(name)
            is_port = isinstance(obj, Port)
            is_node = isinstance(obj, Node)
            is_dof = isinstance(obj, DegreeOfFreedom)

            if is_dof:
                obj = obj.AC
                is_port = True
            elif is_port and len(obj.nodes) != 1:
                raise ValueError(
                    f"Port {repr(obj)} does not have a single node ({obj.nodes}) so you must specify which to use."
                )
            elif not (is_node or is_port):
                raise ValueError(f"Value {repr(obj)} was neither a Port nor a Node")
            elif obj.type == NodeType.OPTICAL:
                raise ValueError(
                    f"Optical nodes/ports {obj} cannot be used for excitations or outputs"
                )

            if is_port:  # select only single node from port
                obj = obj.nodes[0]
            obj.used_in_detector_output.append(self)
            rtn.append(obj)
        return rtn

    def _build_model(self, changing_params, keep_nodes):
        if not self.model_finished_with:
            raise Exception(
                "Trying to build new model whilst current one is in use. Make sure to call `finished()` on this state if the simulation has been completed."
            )

        if self.model.is_built:
            self._finished()

        LOGGER.info(
            f"Building simulation for model {repr(self.model)}"
            f"Changing parameters = {changing_params}"
        )

        # If we do not have a simulation we need to build one
        for p in changing_params:
            p.is_tunable = True

        self.keep_nodes = tuple(self.name_to_elec_mech_nodes(keep_nodes))

        self.__changing_params = changing_params
        self.__sim = self.model._build()
        self.__sim.__enter__()
        self.model_finished_with = False

    def _finished(self):
        if self.__sim:
            LOGGER.info(
                f"Finishing simulation {repr(self.sim)} for model {repr(self.model)}"
            )
            self.model_finished_with = True
            self.__sim.__exit__(None, None, None)
            self.model.unbuild()
            for p in self.__changing_params:
                p.is_tunable = False
            for obj in self.keep_nodes:
                obj.used_in_detector_output.remove(self)
            self.__sim = None

    def __copy__(self):
        raise Exception("Cannot copy state objects")

    def __deepcopy__(self):
        raise Exception("Cannot copy state objects")


class Action(metaclass=abc.ABCMeta):
    def __init__(self, name, analysis_state_manager=False):
        self.__name = name
        self.__analysis_state_manager = analysis_state_manager

    @property
    def name(self):
        return self.__name

    @property
    def analysis_state_manager(self):
        return self.__analysis_state_manager

    def run(self, model, return_state=False):
        """
        Parameters
        ----------
        model : Model
            Model to run this action on
        return_state : boolean
            If True the AnalysisState object is returned along with the solution

        Returns
        -------
        solution : BaseSolution
            Solution object generated by this action
        state : AnalysisState, when return_state = True
            The final state object after pasing through the action. This can be used
            to extract the models generated and tuned at later actions.
        """
        state = AnalysisState(model)
        try:
            if not self.analysis_state_manager:
                action = Series(self)
            else:
                action = self

            result = state.apply(action)

            if type(result) is tuple:
                sol = BaseSolution("root")
                for _ in result:
                    if _ is not None:
                        sol.add(_)
            else:
                sol = result

            if type(sol) is BaseSolution and len(sol.children) == 1:
                sol = sol[0]
        finally:
            state._finished()

        if return_state:
            return sol, state
        else:
            return sol

    @abc.abstractmethod
    def _requests(self, model, memo, first=True):
        """Updates the memo dictionary with details about what this action needs from a
        simulation to run. Parent actions will get requests from all its child actions
        so that it can build a model that suits all of them, to minimise the amount of
        building.

        This method can do initial checks to make sure the model has the
        required features to perform the action too.

        memo['changing_parameters'] - append to this list the full name string
                                      of parameters that this action needs
        memo['keep_nodes'] - append to this list the full name string
                                    of nodes that this action needs to keep.
                                    This should be used where actions are
                                    accessing node outputs without using a
                                    detector element (which registers that
                                    nodes should be kept already).

        Parameters
        ----------
        model : Model
            The Model that the action will be operating on
        memo : defaultdict(list)
            A dictionary that should be filled with requests
        first : boolean
            True if this is the first request being made
        """
        raise NotImplementedError()

    def get_requests(self, model):
        memo = defaultdict(list)
        self._requests(model, memo)
        return memo

    @abc.abstractmethod
    def _do(self, state: AnalysisState) -> BaseSolution:
        pass

    def plan(self, previous=None):
        """Returns an expected plan for the actions that will be run in a tree form.
        This may not be exactly what is ran.

        Returns
        -------
        plan : TreeNode
        """
        if previous is None:
            previous = TreeNode("start")

        me = TreeNode(self.name)
        me.empty = not self.analysis_state_manager
        previous.add(me)

        found_actions = []

        for key, value in self.__dict__.items():
            if isinstance(value, Action):
                found_actions.append(value)
            elif isinstance(value, (tuple, list, set)):
                for _ in value:
                    if isinstance(_, Action):
                        found_actions.append(_)

        for action in found_actions:
            action.plan(me)
        return previous


class Folder(Action):
    """A Folder action collects a new solution every time the action is called.

    An example of this is the 'post step' for the `xaxis`. A folder action is made
    called `post_step` and is passed to a function which will `do` it multiple times.
    After each step the specificed action is called and its solution will be added to
    the folder.
    """

    def __init__(self, name, action, solution):
        super().__init__(name)
        self.action = action
        self.folder_solution = BaseSolution(name)
        solution.add(self.folder_solution)

    def _do(self, state):
        sol = state.apply(self.action)
        if sol:
            self.folder_solution.add(sol)

    def _requests(self, model, memo, first=True):
        return self.action._requests(model, memo)


class Parallel(Action):
    def __init__(self, *actions):
        super().__init__("parallel", True)
        self.actions = actions

    def _do(self, state):
        sols = []
        for action in self.actions:
            # Need to loop through all the actions that we want to run
            # And build new states to feed into them.
            newstate = state._split()
            if not action.analysis_state_manager:
                # If the next action is managing the state then it should either
                # be building a simulation or passing the state on to something that
                # does. If the next action isn't, like an Xaxis, we should build it
                # so that it can work with it.
                rq = action.get_requests(newstate.model)
                params = tuple(
                    convert_str_to_parameter(newstate.model, _)
                    for _ in rq["changing_parameters"]
                )
                newstate._build_model(params, rq["keep_nodes"])
            sols.append(newstate.apply(action))

        return tuple(sols)

    def _requests(self, model, memo, first=True):
        # Parallel by it's nature has to deepcopy the model
        # that has been passed into it, otherwise there will
        # be all sort of clashes that will be hard to resolve.
        pass


class Series(Action):
    def __init__(self, *actions, flatten=True):
        super().__init__("series", True)
        self.actions = actions
        self.flatten = flatten

    def _do(self, state):
        LOGGER.info(f"Doing action {self}")
        if state.sim is not None:
            # Split the state and work on a new model
            # which will involve rebuilding the current model
            # state and optimising it for whatever this series
            # will be performing
            state = state._split()

        rq = self.get_requests(state.model)
        params = tuple(
            convert_str_to_parameter(state.model, _) for _ in rq["changing_parameters"]
        )
        state._build_model(params, rq["keep_nodes"])

        if self.flatten:
            first = BaseSolution(self.name)
        else:
            first = None

        curr_sol = None
        for i, action in enumerate(self.actions):
            next_sol = state.apply(action)
            if self.flatten and next_sol is not None:
                first.add(next_sol)
            else:
                if next_sol and not curr_sol:
                    first = next_sol  # need to return the first one
                if next_sol:
                    if curr_sol:
                        curr_sol.add(next_sol)
                    curr_sol = next_sol
        return first

    def _requests(self, model, memo, first=True):
        if not first:
            return

        for action in self.actions:
            action._requests(model, memo, False)


class LogModelAttribute(Action):
    def __init__(self, *attrs):
        super().__init__("print_parmeter")
        self.attrs = attrs

    def _requests(self, model, memo, first=True):
        pass

    def _do(self, state):
        LOGGER.info(*(f"{_}={state.model.reduce_get_attr(str(_))}" for _ in self.attrs))


class Sweep(Action):
    """An action that sweeps N number of parameters through the values in N arrays.

    Parameters
    ----------
    args : [Parameter, str], array, boolean
        Expects 3 arguments per axis. The first is a full name of a Parameter or
        a Parameter object. The second is an array of values to step this
        parameter over, and lastly a boolean value to say whether this is a
        relative step from the parameters initial value.

    pre_step : Action, optional
        An action to perform before the step is computed

    post_step : Action, optional
        An action to perform after the step is computed

    reset_parameter : boolean, optional
        When true this action will reset the all the parameters it changed to
        the values before it ran.

    name : str
        Name of the action, used to find the solution in the final output.
    """

    def __init__(
        self, *args, pre_step=None, post_step=None, reset_parameter=True, name="step"
    ):
        super().__init__(name)
        if len(args) % 3 != 0:
            raise Exception(
                f"Sweep requires triplet of input arguments: parameter, array, relative_change. Not {args}"
            )
        self.args = args
        self.pre_step = pre_step
        self.post_step = post_step
        self.reset_parameter = reset_parameter

        def process_input_parameter(p):
            if isinstance(p, ModelElement):
                if p.default_parameter_name is None:
                    raise ValueError(
                        f"{repr(p)} does not have a default parameter, please specify one to use"
                    )
                p = getattr(p, p.default_parameter_name)

            if isinstance(p, Parameter):
                if not p.changeable_during_simulation:
                    raise Exception(
                        f"Parameter {p.full_name} cannot be changed during a simulation"
                    )
                return p.full_name
            else:
                return p

        self.parameters = tuple(process_input_parameter(p) for p in args[::3])

        self.axes = tuple(np.atleast_1d(_).astype(np.float64) for _ in args[1::3])
        self.offsets = np.array(args[2::3], dtype=np.float64)
        self.out_shape = tuple(np.size(_) for _ in self.axes)

    def _requests(self, model, memo, first=True):
        params = tuple(convert_str_to_parameter(model, _) for _ in self.parameters)
        if self.reset_parameter:
            # Get the actual parameter for this xaxis
            for p in params:
                if p.value is None:
                    raise ValueError(
                        f"Parameters being changed in a simulation must start with a float value not None. Change {repr(p)} to a float value."
                    )

        if any((not p.changeable_during_simulation for p in params)):
            raise Exception(
                f"The property {p.full_name} cannot be changed during a simulation"
            )

        memo["changing_parameters"].extend(self.parameters)
        if self.pre_step:
            self.pre_step._requests(model, memo)
        if self.post_step:
            self.post_step._requests(model, memo)

    def _do(self, state):
        if state.model is None:
            raise Exception("No model was provided")
        if state.sim is None:
            raise Exception("No simulation was provided")

        # Get all the parameters that need to be tuned in this action and
        # any of its pre/post steps
        rq = self.get_requests(state.model)
        all_params = tuple(
            convert_str_to_parameter(state.model, _) for _ in rq["changing_parameters"]
        )
        # Get the actual parameter for this xaxis
        params = tuple(
            convert_str_to_parameter(state.model, _) for _ in self.parameters
        )

        if not all((p.is_tunable for p in all_params)):
            raise Exception(
                f"Not all parameters {params} are tunable in this simulation {state.sim}"
            )

        return self._run(state, *params)

    def _run(self, state, *params):
        # Record intial values of parameters before we go changing
        # anything so we can reset them later
        if self.reset_parameter:
            initial = tuple(
                float(param.value) for param in state.sim.tunable_parameters
            )

        sol = ArraySolution(
            self.name,
            None,
            state.sim.detector_workspaces,
            self.out_shape,
            self.axes,
            params,
        )
        offsets = np.array(params, dtype=np.float64) * self.offsets
        # Make new folder structure in solution if we have any actions
        # that branch off.
        pre_step = Folder("pre_step", self.pre_step, sol) if self.pre_step else None
        post_step = Folder("post_step", self.post_step, sol) if self.post_step else None
        run_axes_scan(
            state, self.axes, params, offsets, self.out_shape, sol, pre_step, post_step,
        )
        if self.reset_parameter:
            # Reset all parameters and if we were changing a geometric parameter
            # reset the beamtrace data to initial state
            for i, param in zip(initial, state.sim.tunable_parameters):
                param.value = i

            # Ensure the __cvalue of each symbolic parameter gets reset accordingly
            for param in state.sim.changing_parameters:
                param._reset_cvalue()

            if any(
                type(p) is GeometricParameter and p.is_symbolic
                for p in state.sim.changing_parameters
            ):
                state.model._update_symbolic_abcds()
            # Need to check all changing parameters incase of symbols
            # if any(type(p) is GeometricParameter for p in state.sim.changing_parameters):
            #    state.model.beam_trace()

        return sol


class Noxaxis(Sweep):
    def __init__(self, pre_step=None, post_step=None, name="noxaxis"):
        super().__init__(name=name, pre_step=None, post_step=None)


class XNaxis(Sweep):
    def __init__(
        self, *args, relative=False, pre_step=None, post_step=None, name="XNaxis"
    ):
        if len(args) % 5 != 0:
            raise Exception(
                f"XNaxis arguments must come in groups of five: parameter, mode, start, stop, steps not {args}"
            )
        self.relative = relative
        self.N = len(args) // 5

        if self.N == 0:
            raise Exception("XNaxis requires at least one axis to be specified")
        # Here we map the XNaxis arguments to the Sweep inputs
        self.__set_args = args
        new_args = []

        for i in range(0, len(args), 5):
            new_args.append(args[i + 0])
            new_args.append(
                get_sweep_array(args[i + 2], args[i + 3], args[i + 4], args[i + 1])
            )
            new_args.append(relative)

        super().__init__(*new_args, pre_step=pre_step, post_step=post_step, name=name)

    def __getattr__(self, key):
        res = re.match("(parameter|mode|start|stop|steps|offset)([0-9]*)", key)
        if res is None:
            super().__getattribute__(key)
        else:
            grp = res.groups()
            N = 1 if grp[1] == "" else int(grp[1])
            if N == 0:
                raise Exception("Specify an axes greater than 0")
            if N > self.N:
                raise Exception(f"This xaxis does not have {N} axes")
            idx = 6 * (N - 1)
            if grp[0] == "parameter":
                return self.__set_args[idx + 0]
            elif grp[0] == "mode":
                return self.__set_args[idx + 1]
            elif grp[0] == "start":
                return self.__set_args[idx + 2]
            elif grp[0] == "stop":
                return self.__set_args[idx + 3]
            elif grp[0] == "steps":
                return self.__set_args[idx + 4]
            elif grp[0] == "offset":
                return self.__set_args[idx + 5]


class Xaxis(XNaxis):
    def __init__(
        self,
        parameter,
        mode,
        start,
        stop,
        steps,
        relative=False,
        pre_step=None,
        post_step=None,
        name="xaxis",
    ):
        super().__init__(
            parameter,
            mode,
            start,
            stop,
            steps,
            relative=relative,
            pre_step=pre_step,
            post_step=post_step,
            name=name,
        )


class X2axis(XNaxis):
    def __init__(
        self,
        parameter1,
        mode1,
        start1,
        stop1,
        steps1,
        parameter2,
        mode2,
        start2,
        stop2,
        steps2,
        relative=False,
        pre_step=None,
        post_step=None,
        name="x2axis",
    ):
        super().__init__(
            parameter1,
            mode1,
            start1,
            stop1,
            steps1,
            parameter2,
            mode2,
            start2,
            stop2,
            steps2,
            relative=relative,
            pre_step=pre_step,
            post_step=post_step,
            name=name,
        )


class X3axis(XNaxis):
    def __init__(
        self,
        parameter1,
        mode1,
        start1,
        stop1,
        steps1,
        parameter2,
        mode2,
        start2,
        stop2,
        steps2,
        parameter3,
        mode3,
        start3,
        stop3,
        steps3,
        relative=False,
        pre_step=None,
        post_step=None,
        name="x3axis",
    ):
        super().__init__(
            parameter1,
            mode1,
            start1,
            stop1,
            steps1,
            parameter2,
            mode2,
            start2,
            stop2,
            steps2,
            parameter3,
            mode3,
            start3,
            stop3,
            steps3,
            relative=relative,
            pre_step=pre_step,
            post_step=post_step,
            name=name,
        )


class RunLocksSolution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.iters = 0
        self.results = None
        self.lock_names = ()


class RunLocks(Action):
    def __init__(
        self, *locks, exception_on_fail=True, max_iterations=10000, name="run locks"
    ):
        super().__init__(name)
        self.locks = tuple((l if isinstance(l, str) else l.name) for l in locks)
        self.max_iterations = max_iterations
        self.exception_on_fail = exception_on_fail

    def _do(self, state):
        if state.sim is None:
            raise Exception("Simulation has not been built")
        if not isinstance(state.sim, finesse.simulations.CarrierSignalMatrixSimulation):
            raise NotImplementedError()

        recompute = True

        if len(self.locks) == 0:
            locks = state.model.locks
        else:
            locks = tuple(state.model.elements[name] for name in self.locks)

        out_wss = set(  # workspaces can be in both lists
            (*state.sim.readout_workspaces, *state.sim.detector_workspaces)
        )

        dws = tuple(
            next(
                filter(lambda x: x.oinfo.name == lock.error_signal.name, out_wss,),
                None,
            )
            for lock in locks
        )

        N = len(locks)
        # Store initial parameters incase of failure so we can reset the model
        initial_parameters = tuple(float(lock.feedback) for lock in locks)

        sol = RunLocksSolution(self.name)
        sol.iters = -1
        sol.results = np.zeros((len(locks), 2, self.max_iterations + 1))
        sol.lock_names = tuple(lock.name for lock in locks)

        while recompute and sol.iters < self.max_iterations:
            sol.iters += 1
            state.sim.run_carrier()
            recompute = False
            for i in range(N):
                if not locks[i].disabled:
                    acc = locks[i].accuracy
                    res = dws[i].get_output() - locks[i].offset
                    sol.results[i, 0, sol.iters] = res
                    if not (-acc <= res <= acc):
                        # We'll need to recompute the carrier sim
                        recompute = True
                        feedback = locks[i].gain * res
                        locks[i].feedback.value += feedback
                        sol.results[i, 1, sol.iters] = feedback

        if recompute is True:
            if self.exception_on_fail:
                raise Exception("Locks failed: max iterations reached")
            else:
                LOGGER.warn("Locks failed")
                for lock, value in zip(locks, initial_parameters):
                    lock.feedback.value = value
        return sol

    def _requests(self, model, memo, first=True):
        if len(self.locks) == 0:
            # If none given lock everything
            for lock in model.locks:
                memo["changing_parameters"].append(lock.feedback.full_name)
        else:
            for name in self.locks:
                if name not in model.elements:
                    raise Exception(f"Model {model} does not have a lock called {name}")
                memo["changing_parameters"].append(
                    model.elements[name].feedback.full_name
                )


class Scale(Action):
    """Action for scaling simulation outputs by some fixed amount. Included for
    compatibility with legacy Finesse code. New users should apply any desired scalings
    manually from Python.

    Parameters
    ----------
    detectors : dict
        A dictionary of `detector name: scaling factor` mappings.
    """

    def __init__(self, scales: dict, **kwargs):
        super().__init__(None)
        self.kwargs = kwargs
        self.scales = scales

    def _requests(self, model, memo, first=True):
        pass

    def _do(self, state):
        sol = state.previous_solution
        for det, fac in self.scales.items():
            sol._outputs[det][()] *= fac


class Debug(Action):
    def __init__(self, name="Debug"):
        super().__init__(name)
        self.cancel = False

    def _requests(self, model, memo, first=True):
        pass

    def do(self, state):
        if not self.cancel:
            from IPython.terminal.embed import InteractiveShellEmbed

            banner = textwrap.dedent(
                f"""
            ---- Finesse Debugging
            Instance          : {self.name}
            Previous solution : s_prev
            Current model     : model
            Current carrier   : carrier
            Current signal    : signal

            To stop future debug calls set : self.cancel = True
            To continue analyis            : exit
            """
            )
            self.shell = InteractiveShellEmbed(banner1=banner)
            self.shell()


### Beam tracing related actions ###


class ABCD(Action):
    """Computation of an ABCD matrix over a path.

    See :func:`.compute_abcd` for details.
    """

    def __init__(self, name="abcd", **kwargs):
        super().__init__(name)
        self.kwargs = kwargs

    def _requests(self, model, memo, first=True):
        pass

    def _do(self, state):
        return state.model.ABCD(solution_name=self.name, **self.kwargs)


class BeamTrace(Action):
    """Full beam tracing on a complete model.

    See :meth:`.Model.beam_trace` for details.
    """

    def __init__(self, name="beam_trace", **kwargs):
        super().__init__(name)
        self.kwargs = kwargs

    def _requests(self, model, memo, first=True):
        pass

    def _do(self, state):
        return state.model.beam_trace(solution_name=self.name, **self.kwargs)


class PropagateBeam(Action):
    """Propagation of a beam, in a single plane, through a given path.

    See :meth:`.Model.propagate_beam` for details.
    """

    def __init__(self, name="propagation", **kwargs):
        super().__init__(name)
        self.kwargs = kwargs

    def _requests(self, model, memo, first=True):
        pass

    def _do(self, state):
        return state.model.propagate_beam(solution_name=self.name, **self.kwargs)


class PropagateAstigmaticBeam(Action):
    """Propagation of a beam, in both planes, through a given path.

    See :meth:`.Model.propagate_beam_astig` for details.
    """

    def __init__(self, name="astig_propagation", **kwargs):
        super().__init__(name)
        self.kwargs = kwargs

    def _requests(self, model, memo, first=True):
        pass

    def _do(self, state):
        return state.model.propagate_beam_astig(solution_name=self.name, **self.kwargs)


class Plot(Action):
    def __init__(self, name="abcd"):
        super().__init__(name)

    def _requests(self, model, memo, first=True):
        pass

    def _do(self, state):
        raise NotImplementedError()


class Printer(Action):
    def __init__(self, name="printer"):
        super().__init__(name)

    def _requests(self, model, memo, first=True):
        pass

    def _do(self, state):
        raise NotImplementedError()


class PrintModel(Action):
    def __init__(self, name="print_model"):
        super().__init__(name)

    def _requests(self, model, memo, first=True):
        pass

    def _do(self, state):
        print(state.model)


class PrintModelAttr(Action):
    def __init__(self, *args):
        super().__init__(self.__class__.__name__)
        self.args = tuple(a.full_name for a in args)

    def _requests(self, model, memo, first=True):
        pass

    def _do(self, state):
        print(*(f"{_}={state.model.reduce_get_attr(_)}" for _ in self.args))


class FrequencyResponseSolution(BaseSolution):
    def __getitem__(self, key):
        try:
            key = np.atleast_1d(key).tolist()
            inp_key = slice(None, None, None)
            out_key = slice(None, None, None)

            for k in key:
                _k = np.atleast_1d(k)
                if all(_ in self.inputs for _ in _k):
                    inp_key = tuple(self.inputs.index(_) for _ in _k)
                if all(_ in self.outputs for _ in _k):
                    out_key = tuple(self.outputs.index(_) for _ in _k)

            slices = (slice(None, None, None), inp_key, out_key)
            return self.out[slices].squeeze()
        except (ValueError, IndexError, TypeError):
            return super().__getitem__(key)

    def plot_dofs(self, *dofs, axs=None, max_width=12, show_unity=False, **kwargs):
        import matplotlib.pyplot as plt
        import numpy as np

        if len(dofs) == 0:
            dofs = self.inputs

        if axs is None:
            # if no axes are given then grab the figure
            # and any axes that are in it
            fig = plt.gcf()
            axs = np.atleast_2d(fig.axes)
        else:
            axs = np.atleast_2d(axs)
            fig = axs[0, 0].get_figure()

        dofs = np.atleast_1d(dofs)
        N = len(dofs)
        W = min(5, max_width / N)
        if np.prod(axs.shape) != N:
            fig, axs = plt.subplots(
                1, N, figsize=(W * N, 3.5), squeeze=False, sharey=True
            )

        for i, dof in enumerate(dofs):
            axs[0, i].loglog(self.f, abs(self[dof]), **kwargs)
            axs[0, i].legend(self.outputs)
            axs[0, i].set_xlabel("Frequency [Hz]")
            axs[0, i].set_title(dof)
            if show_unity:
                axs[0, i].hlines(
                    1, min(self.f), max(self.f), color="k", ls=":", zorder=-10
                )

        axs[0, 0].set_ylabel("OUTPUT/DOF")
        plt.tight_layout()

        return fig, axs

    plot = plot_dofs  # Default plot option

    def plot_readouts(self, *readouts, axs=None, ls=None, max_width=12):
        import matplotlib.pyplot as plt

        if len(readouts) == 0:
            readouts = self.outputs

        readouts = np.atleast_1d(readouts)
        if axs is None:
            N = len(readouts)
            W = min(5, max_width / N)
            fig, axs = plt.subplots(
                1, N, figsize=(W * N, 3.5), squeeze=False, sharey=True
            )
        else:
            fig = plt.gcf()

        for i, rd in enumerate(readouts):
            axs[0, i].loglog(self.f, abs(self[rd]), ls=ls)
            axs[0, i].legend(self.inputs)
            axs[0, i].set_xlabel("Frequency [Hz]")
            axs[0, i].set_title(rd)

        axs[0, 0].set_ylabel("OUTPUT/DOF")
        plt.tight_layout()

        return fig, axs


class FrequencyResponse(Action):
    """Computes the frequency response of a signal injceted at various nodes to compute
    transfer functions to multiple output nodes. Inputs and outputs should be electrical
    or mechanical nodes. It does this in an efficient way by using the same model and
    solving for multiple RHS input vectors.

    This action does not alter the model state.

    Parameters
    ----------
    f : array, double
        Frequencies to compute the transfer functions over
    inputs : iterable[str or Element]
        Mechanical or electrical node to inject signal at
    outputs : iterable[str or Element]
        Mechanical or electrical nodes to measure output at
    open_loop : bool, optional
        Computes open loop transfer functions if the system has closed
    name : str, optional
        Solution name

    Examples
    --------
    Here we measure a set of transfer functions from DARM and CARM
    to four readouts for a particular `model`,

    >>> sol = FrequencyResponse(np.geomspace(0.1, 50000, 100),
    ...         ('DARM', 'CARM'),
    ...         ('AS.DC', 'AS45.I', 'AS45.Q', 'REFL9.I'),
    ... ).run(model)

    Single inputs and outputs can also be specified

    >>> FrequencyResponse(np.geomspace(0.1, 50000, 100), 'DARM', AS.DC').run(model)

    The transfer functions can then be accessed like a 2D array by name,
    the ordering of inputs to outputs does not matter.

    >>> sol['DARM'] # DARM to all outputs
    >>> sol['DARM', 'AS.DC'] # DARM to AS.DC
    >>> sol['DARM', ('AS.DC', 'AS45.I')]
    >>> sol['AS.DC'] # All inputs to AS.DC readout
    """

    def __init__(self, f, inputs, outputs, *, open_loop=False, name="inject"):
        super().__init__(name)
        inputs = np.atleast_1d(inputs)
        outputs = np.atleast_1d(outputs)

        try:
            self.f = np.array(f, dtype=np.float64, copy=True)
        except Exception:
            # If the f is a symbol...
            self.f = np.array(f.eval(), dtype=np.float64, copy=True)

        def process(x):
            if not isinstance(x, (str, np.str_)):
                return x.full_name
            return x

        self.inputs = list(process(i) for i in inputs)
        self.outputs = list(process(o) for o in outputs)
        self.open_loop = open_loop

    def _do(self, state, fsig_independant_outputs=None, fsig_dependant_outputs=None):
        input_rhs_indices = np.zeros(len(self.inputs), dtype=int)
        output_rhs_indices = np.zeros(len(self.outputs), dtype=int)

        for i, node in enumerate(state.name_to_elec_mech_nodes(self.inputs)):
            input_rhs_indices[i] = state.sim.signal.field(node, 0, 0)
        for i, node in enumerate(state.name_to_elec_mech_nodes(self.outputs)):
            output_rhs_indices[i] = state.sim.signal.field(node, 0, 0)

        sol = FrequencyResponseSolution(self.name)
        sol.f = self.f
        sol.inputs = self.inputs
        sol.outputs = self.outputs
        state.sim.carrier.run()
        rtn = run_fsig_sweep(
            state.sim,
            self.f,
            input_rhs_indices,
            output_rhs_indices,
            None,
            self.open_loop,
            tuple(fsig_independant_outputs)
            if fsig_independant_outputs is not None
            else None,
            tuple(fsig_dependant_outputs)
            if fsig_dependant_outputs is not None
            else None,
        )
        if len(rtn) == 2:
            sol.out = rtn[0]
            sol.extra_outputs = rtn[1]
        else:
            sol.out = rtn

        return sol

    def _requests(self, model, memo, first=True):
        memo["changing_parameters"].append("fsig.f")
        memo["keep_nodes"].extend(self.inputs)
        memo["keep_nodes"].extend(self.outputs)


class OptimiseRFReadoutPhaseDCSolution(BaseSolution):
    pass


class OptimiseRFReadoutPhaseDC(Action):
    """This optimises the demodulation phase of ReadoutRF elements relative to some
    DegreeOfFreedom. This optimises the phases so that the ReadoutRF in-phase signal
    will optimally sense the provided DegreeOfFreedom.

    The phases are optimised by calculating the DC response of the readouts.

    This Action changes the state of the model.

    Parameters
    ----------
    args
        Pairs of DegreesOfFreedom and ReadoutRF elements, or pairs of their names.
    d_dof : float, optional
        The small offset applied to the DOFs to compute the gradients of the error
        signals.

    Examples
    --------
    Here we optimise REFL9 I and AS45 I to sense CARM and DARM optimially:
    >>> sol = OptimiseRFReadoutPhaseDC("CARM", "REFL9", "DARM", "AS45").run(aligo)
    """

    def __init__(self, *args, d_dof=1e-9, name="optimise_demod_phases_dc"):
        super().__init__(name)
        self.args = args
        self.dofs = args[::2]
        self.readouts = args[1::2]
        self.d_dof = d_dof

        if len(self.dofs) != len(self.readouts):
            raise ValueError(
                "Pairs of Degrees of freedoms and readouts must be provided"
            )

    def _do(self, state):
        Idws = tuple(
            next(
                filter(
                    lambda x: x.oinfo.name == rd + "_I", state.sim.readout_workspaces
                ),
                None,
            )
            for rd in self.readouts
        )
        Qdws = tuple(
            next(
                filter(
                    lambda x: x.oinfo.name == rd + "_Q", state.sim.readout_workspaces
                ),
                None,
            )
            for rd in self.readouts
        )
        dcs = tuple(state.model.reduce_get_attr(f"{dof}.DC") for dof in self.dofs)

        N = len(self.dofs)
        sol = OptimiseRFReadoutPhaseDCSolution(self.name)
        sol.Ivals = np.zeros((N, 2), dtype=complex)
        sol.Qvals = np.zeros((N, 2), dtype=complex)
        # Here we compute the gradient of the error signals
        # with respect to some DOF change
        for i in range(N):
            dcs[i].value -= self.d_dof
            state.sim.run_carrier()
            sol.Ivals[i, 0] = Idws[i].get_output()
            sol.Qvals[i, 0] = Qdws[i].get_output()
            dcs[i].value += 2 * self.d_dof
            state.sim.run_carrier()
            sol.Ivals[i, 1] = Idws[i].get_output()
            sol.Qvals[i, 1] = Qdws[i].get_output()
            # reset value
            dcs[i].value -= self.d_dof
        # Compute the gradients in both I and Q
        sol.Igradients = (sol.Ivals[:, 1] - sol.Ivals[:, 0]) / 2e-6
        sol.Qgradients = (sol.Qvals[:, 1] - sol.Qvals[:, 0]) / 2e-6
        # We can use the complex angle to compute how much to change the
        # demod phase by to optimise it
        sol.add_degrees = np.angle(sol.Igradients + 1j * sol.Qgradients, deg=True)
        sol.phases = {}
        for i in range(N):
            param = state.model.reduce_get_attr(f"{self.readouts[i]}.phase")
            param.value += sol.add_degrees[i]
            sol.phases[self.readouts[i]] = float(param.value)

        return sol

    def _requests(self, model, memo, first=True):
        memo["changing_parameters"].extend((f"{_}.DC" for _ in self.dofs))
        memo["changing_parameters"].extend((f"{_}.phase" for _ in self.readouts))
        return memo


class SensingMatrixDCSolution(BaseSolution):
    """Sensing matrix DC solution.

    The raw sensing matrix information can be accessed using the
    `SensingMatrixDCSolution.out` member. This is a complex-valued array with dimensions
    (DOFs, Readouts), which are accessible via `SensingMatrixDCSolution.dofs` and
    `SensingMatrixDCSolution.readouts`.

    A table can be printed using :meth:`.SensingMatrixDCSolution.display`.

    Polar plot can be generated using :meth:`.SensingMatrixDCSolution.plot`

    Printing :class:`.SensingMatrixDCSolution` will show an ASCII table of the data.
    """

    def display(self, dofs=None, readouts=None, tablefmt="html", floatfmt=".2G"):
        """Displays a HTML table of the sensing matrix.

        Notes
        -----
        Only works when called from an IPython environmeny with the `display`
        method available.

        Parameters
        ----------
        dofs : iterable[str], optional
            Names of degrees of freedom to show, defaults to all if None
        readouts : iterable[str], optional
            Names of readouts to show, defaults to all if None
        """
        from IPython import display

        B, dofs, readouts = self.matrix_data(dofs, readouts)
        if tablefmt == "html":
            display(
                tabulate(
                    B,
                    headers=readouts,
                    showindex=dofs,
                    tablefmt=tablefmt,
                    floatfmt=floatfmt,
                )
            )
        else:
            print(
                tabulate(
                    B,
                    headers=readouts,
                    showindex=dofs,
                    tablefmt=tablefmt,
                    floatfmt=floatfmt,
                )
            )

    def __str__(self):
        B, dofs, readouts = self.matrix_data()
        return tabulate(
            B, headers=readouts, showindex=dofs, tablefmt="fancy_grid", floatfmt=".2G"
        )

    def matrix_data(self, dofs=None, readouts=None):
        """Generates a sensing matrix table.

        Parameters
        ----------
        dofs : iterable[str], optional
            Names of degrees of freedom to show, defaults to all if None
        readouts : iterable[str], optional
            Names of readouts to show, defaults to all if None

        Returns
        -------
        matrix : 2D numpy array, complex
        dofs : list of :class:`str`
        readouts: list of :class:`str`
        """
        dofs = dofs or self.dofs
        readouts = readouts or self.readouts
        dofs = np.atleast_1d(dofs)
        readouts = np.atleast_1d(readouts)
        hdrs = tuple(rd + iq for rd in readouts for iq in ("_I", "_Q"))
        sl1 = tuple(dofs.index(_) for _ in dofs)
        sl2 = tuple(readouts.index(_) for _ in readouts)
        # Reshaping so that we have extra columns with I and Q signals
        A = self.out[sl1, :][:, sl2]
        Nr, Nc = A.shape
        B = np.zeros(2 * Nr * Nc)
        B[0::2] = A.real.flat
        B[1::2] = A.imag.flat
        B = B.reshape(Nr, 2 * Nc)
        return B, dofs.tolist(), hdrs

    def plot(self, Nrows, Ncols, figsize=(6, 5), *, dofs=None, readouts=None):
        import matplotlib.pyplot as plt

        dofs = np.atleast_1d(dofs or self.dofs)
        readouts = np.atleast_1d(readouts or self.readouts)

        fig, axs = plt.subplots(
            Nrows,
            Ncols,
            figsize=figsize,
            subplot_kw={"projection": "polar"},
            squeeze=False,
        )
        axs = axs.flatten()
        for idx in range(len(readouts)):
            dof_idxs = tuple(self.dofs.index(_) for _ in dofs)
            _ax = axs[idx]
            A = self.out[dof_idxs, idx]

            _ax.set_theta_zero_location("E")
            r_lim = (np.log10(np.abs(A)).min() - 1, np.log10(np.abs(A)).max())
            _ax.set_ylim(r_lim[0], r_lim[1] + 1)
            _ax.set_yticklabels([])

            theta = np.angle(A)
            r = np.log10(np.abs(A))
            _ax.plot(
                (theta, theta),
                (r_lim[0] * np.ones_like(r), r),
                marker="D",
                markersize=5,
            )
            _ax.set_title(self.readouts[idx])
        _ax.legend(self.dofs, loc="best", bbox_to_anchor=(0.5, -0.3), fontsize=8)
        plt.tight_layout(pad=1.2)
        return fig, axs


class SensingMatrixDC(Action):
    """Computes the sensing matrix elements for various degrees of freedom and readouts
    that should be present in the model. The solution object for this action then
    contains all the information on the sensing matrix. This can be plotted in polar
    coordinates, displayed in a table, or directly accessed.

    The sensing gain is computed by calculating the gradient of each readout
    signal, which means it is a DC measurement. This will not include any
    suspension or radiation pressure effects.

    This action does not modify the states model.

    Parameters
    ----------
    dofs : iterable[str]
        String names of degrees of freedom
    readouts : iterable[str]
        String names of readouts
    d_dof : float, optional
        Small step used to compute derivative
    """

    def __init__(self, dofs, readouts, d_dof=1e-9, name="sensing_matrix_dc"):
        super().__init__(name)
        self.dofs = dofs
        self.readouts = readouts
        self.d_dof = d_dof

    def _do(self, state):
        Idws = tuple(
            next(
                filter(
                    lambda x: x.oinfo.name == rd + "_I", state.sim.readout_workspaces
                ),
                None,
            )
            for rd in self.readouts
        )
        Qdws = tuple(
            next(
                filter(
                    lambda x: x.oinfo.name == rd + "_Q", state.sim.readout_workspaces
                ),
                None,
            )
            for rd in self.readouts
        )
        dcs = tuple(state.model.reduce_get_attr(f"{dof}.DC") for dof in self.dofs)

        Nd = len(self.dofs)
        Nr = len(self.readouts)

        sol = SensingMatrixDCSolution(self.name)
        sol.dofs = self.dofs
        sol.readouts = self.readouts
        sol.Ivals = np.zeros((Nd, Nr, 2), dtype=float)
        sol.Qvals = np.zeros((Nd, Nr, 2), dtype=float)
        # Here we compute the gradient of the error signals
        # with respect to some DOF change
        for i in range(Nd):
            dcs[i].value -= self.d_dof
            state.sim.run_carrier()
            for j in range(Nr):
                sol.Ivals[i, j, 0] = Idws[j].get_output()
                sol.Qvals[i, j, 0] = Qdws[j].get_output()
            dcs[i].value += 2 * self.d_dof
            state.sim.run_carrier()
            for j in range(Nr):
                sol.Ivals[i, j, 1] = Idws[j].get_output()
                sol.Qvals[i, j, 1] = Qdws[j].get_output()
            # reset value
            dcs[i].value -= self.d_dof
        # Compute the gradients in both I and Q
        sol.Igradients = (sol.Ivals[:, :, 1] - sol.Ivals[:, :, 0]) / 2e-6
        sol.Qgradients = (sol.Qvals[:, :, 1] - sol.Qvals[:, :, 0]) / 2e-6
        sol.out = sol.Igradients + 1j * sol.Qgradients
        return sol

    def _requests(self, model, memo, first=True):
        memo["changing_parameters"].extend((f"{_}.DC" for _ in self.dofs))
        return memo


class Change(Action):
    """Changes a model Parameter to some value during an analysis."""

    def __init__(self, change_dict=None, *, relative=False, **kwargs):
        super().__init__(None)
        self.kwargs = kwargs or {}
        if change_dict:
            self.kwargs.update(change_dict)
        self.relative = relative

    def _requests(self, model, memo, first=True):
        from finesse import Parameter

        for el in self.kwargs.keys():
            p = convert_str_to_parameter(model, el)
            if isinstance(p, Parameter):
                memo["changing_parameters"].append(el)
            else:
                raise TypeError(
                    f"{el} is not a name of a Parameter or Component in the model"
                )

    def _do(self, state):
        for el, val in self.kwargs.items():
            p = convert_str_to_parameter(state.model, el)
            if self.relative:
                p.value += val
            else:
                p.value = val


class NoiseProjectionSolution(BaseSolution):
    def plot(self, output_node=None, lower=0.1, upper=3, *, ax=None, **kwargs):
        import matplotlib.pyplot as plt

        if output_node is None:
            output_node = self.output_nodes[0]

        if ax is None:
            fig = plt.gcf()
            if len(fig.axes) == 0:
                fig.subplots(1, 1)
            ax = fig.axes[0]

        total = np.sqrt((self.out[output_node] ** 2).sum(1))
        rng = lower * total.min(), upper * total.max()
        noises_to_plot = np.any(self.out[output_node] > rng[0], 0)
        ax.loglog(self.f, self.out[output_node][:, noises_to_plot])
        ax.loglog(self.f, total, c="k", ls="-.", lw=2)
        ax.legend((*np.array(self.noises)[noises_to_plot], "Total"))
        ax.set_ylim(*rng)
        ax.set_ylabel(
            f"ASD [{output_node if not self.scaling else self.scaling}/$\\sqrt{{\\mathrm{{Hz}}}}$]"
        )
        ax.set_xlabel("Frequency [Hz]")


class NoiseProjection(Action):
    def __init__(self, f, *output_nodes, scaling=None, name="loop"):
        if len(output_nodes) == 0:
            raise ValueError(
                "At least one output node must be specified to compute noise projection to"
            )
        super().__init__(name)
        process = lambda x: x.full_name if type(x) is not str else x

        self.f = f
        self.scaling = process(scaling) if scaling is not None else None
        self.output_nodes = tuple(process(o) for o in output_nodes)

        if len(self.output_nodes) > len(set(self.output_nodes)):
            raise ValueError(
                f"The same output node has been requested multiple times {self.output_nodes}"
            )

    def _do(self, state):
        sol = NoiseProjectionSolution(self.name)
        sol.f = self.f
        sol.output_nodes = self.output_nodes
        sol.scaling = self.scaling
        # create a list of callables func(fsig) to get the ASD noises
        noise_ASDs = {
            name: el.ASD.lambdify(state.model.fsig.f)
            for name, el in state.model.noises.items()
        }
        # labels for noises
        sol.noises = list(el.name for _, el in state.model.noises.items())
        # Keep track of which nodes have what noise injected into them
        noise_node_map = defaultdict(list)
        for name, el in state.model.noises.items():
            noise_node_map[el.node.full_name].append(el.name)
        # Collect any extra outputs that should be calculated during the fsig sweep. This
        # is to make efficient use of the filling and solving that this is already doing
        # to extract quantum noise, or others, as needed. Some of these outputs will be
        # signal frequency independant, such as standard shot-noise calculations, so just
        # compute them once.
        # TODO eventually handle qnoised detectors, which are frequency dependant
        fsig_indep_output = []
        for dws in state.sim.readout_workspaces:
            if isinstance(dws, (QShot0Workspace, QShotNWorkspace)):
                added = 0  # don't calculate anything if we aren't modelling the nodes
                # The quantum shot noise detectors will be on the optiical
                # input node, which we can't inject a signal into for computing
                # the noise propagation. Here we need to get the electrical outputs
                # of the readout and just put the noise in there
                for n in dws.owner.electrical_nodes:
                    if n.full_name in state.sim.signal.nodes:
                        noise_node_map[n.full_name].append(dws.oinfo.name)
                        added += 1
                if added:
                    fsig_indep_output.append(dws)
        # Compute all the required transfer functions for noise propagation
        # NOTE: We use _do directly here because we just want to call the action
        # on this state, rather than `run` which will try and create a new state.
        # This is fine, as long as we have requested all the options it needs in
        # _requests. We can't make this frequency response in the init as we do
        # not have the model to grab all the various noise and shot-noise nodes
        self.input_nodes = tuple(noise_node_map.keys())
        sol.freqresp = FrequencyResponse(
            self.f, self.input_nodes, self.output_nodes
        )._do(state, fsig_indep_output)
        # Get any shot noise outputs from the solution
        for dws in fsig_indep_output:
            # Make a simple callable to work wiht the noise ASD functions
            noise_ASDs[dws.oinfo.name] = lambda f: sol.freqresp.extra_outputs[
                dws.oinfo.name
            ]
            sol.noises.append(dws.oinfo.name)
        # get a map from nodes->noise, for noise->node index in output
        inv_noise_node_map = {}
        for k, v in noise_node_map.items():
            for n in v:
                inv_noise_node_map[n] = self.input_nodes.index(k)
        # Convert all the ASDs into PSDs
        sol.PSDs = np.array(
            tuple(np.ones_like(self.f) * fn(self.f) ** 2 for fn in noise_ASDs.values())
        ).T
        # Use this to broadcast from the frequency response output to get the right
        # transfer function for each noise source
        out_indices = tuple(inv_noise_node_map[name] for name in noise_ASDs.keys())
        # Here we can compute some projection for calculating equivalent noise budgets
        if self.scaling:
            sol.scaling_solution = FrequencyResponse(
                self.f, self.scaling, self.output_nodes, open_loop=True
            )._do(state)
        sol.out = {}
        # compute abs(H)**2 for noise projection of PSDS
        HH = np.zeros(
            (len(self.f), len(out_indices), len(self.output_nodes)), dtype=float
        )
        np.abs(sol.freqresp.out[:, out_indices, :], out=HH)
        np.multiply(HH, HH, out=HH)
        # The final index of HH is the output node index, so we can quickly iterate over
        # them here to project the noises
        for i, output_node in enumerate(self.output_nodes):
            # sqrt(output**2/node**2 * node**2/Hz) => output/rtHz
            sol.out[output_node] = np.sqrt(HH[:, :, i] * sol.PSDs)
            if self.scaling:
                # output / scaling
                # sqrt(output**2/node**2 * node**2/Hz) => scaling/rtHz
                sol.out[output_node] /= np.abs(sol.scaling_solution.out[:, :, 0])
        return sol

    def _requests(self, model, memo, first=True):
        memo["changing_parameters"].append("fsig.f")
        memo["keep_nodes"].extend(self.output_nodes)
        if self.scaling:
            memo["keep_nodes"].append(self.scaling)
        memo["keep_nodes"].extend((el.node.full_name for n, el in model.noises.items()))


##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################

# class BeamTrace(Action):
#     """Action for tracing the beam throughout an entire model."""

#     def __init__(self, name, **kwargs):
#         super().__init__(name)
#         self.kwargs = kwargs
#         self._info.makes_solution = True

#     def do(self, ws):
#         ws.s_prev.add(ws.model.beam_trace(solution_name=self.name, **self.kwargs))


# class ABCD(Action):
#     """Action to compute a composite ABCD matrix over a given path of a model."""

#     def __init__(self, name, **kwargs):
#         super().__init__(name)
#         self.kwargs = kwargs
#         self._info.makes_solution = True

#     def do(self, ws):
#         ws.s_prev.add(ws.model.ABCD(solution_name=self.name, **self.kwargs))


# class Plot(Action):
#     def __init__(self, *args, **kwargs):
#         super().__init__(self.__class__.__name__)
#         self.args = args
#         self.kwargs = kwargs

#     def do(self, s_prev, model):
#         while type(s_prev) is BaseSolution:
#             s_prev = s_prev.parent

#         if s_prev is not None and hasattr(s_prev, "plot"):
#             s_prev.plot()
#         else:
#             print(f"No plot method found in {s_prev}")


# class Printer(Action):
#     def __init__(self):
#         super().__init__(self.__class__.__name__,)

#     def do(self, ws):
#         s_prev, model = ws.s_prev, ws.model
#         print(s_prev, model)


# class PrintModel(Action):
#     def __init__(self):
#         super().__init__(self.__class__.__name__)

#     def do(self, ws):
#         print(ws.model)


# class PrintSolution(Action):
#     def __init__(self):
#         super().__init__(self.__class__.__name__)

#     def do(self, ws):
#         print(ws.s_prev)


# class PrintAttr(Action):
#     def __init__(self, *args):
#         super().__init__(self.__class__.__name__)
#         self.args = args

#     def do(self, ws):
#         print(*(f"{_}={ws.model.reduce_get_attr(_)}" for _ in self.args))


# class ReprAttr(Action):
#     def __init__(self, *args):
#         super().__init__(self.__class__.__name__)
#         self.args = args

#     def do(self, ws):
#         print(*(f"{_}={repr(ws.model.reduce_get_attr(_))}" for _ in self.args))
