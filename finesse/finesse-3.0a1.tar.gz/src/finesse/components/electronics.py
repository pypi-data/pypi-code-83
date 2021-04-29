import numpy as np

from finesse.components.general import Connector
from finesse.components.workspace import ConnectorWorkspace
from finesse.components.node import NodeDirection, NodeType
from finesse.parameter import float_parameter


class FilterWorkspace(ConnectorWorkspace):
    pass


@float_parameter("gain", "Gain")
class ZPKNodeActuator(Connector):
    def __init__(self, name, mechanical_node, gain=1, z=[], p=[], k=1):
        super().__init__(name)

        if mechanical_node.type is not NodeType.MECHANICAL:
            raise Exception("Actuation must be on a mechanical node.")

        self.gain = gain
        self.z = z
        self.p = p
        self.k = k

        self.__node = mechanical_node

        self._add_port("p1", NodeType.ELECTRICAL)
        self.p1._add_node("i", NodeDirection.INPUT)

        self._add_port("mech", NodeType.MECHANICAL)
        self.mech._add_node("actuation", None, mechanical_node)

        self._register_node_coupling("P1_ACT", self.p1.i, mechanical_node)

    def _get_workspace(self, sim):
        if sim.signal:
            refill = sim.model.fsig.f.is_changing or any(
                p.is_changing for p in self.parameters
            )
            ws = FilterWorkspace(self, sim, refill, refill)
            ws.signal.add_fill_function(self.fill, refill)
            ws.frequencies = sim.electrical_frequencies[self.p1.i].frequencies
            return ws
        else:
            return None

    def fill(self, ws):
        if ws.signal.connections.P1_ACT_idx > -1:
            for _ in ws.frequencies:
                # Assumes only couples to first mech frequency
                with ws.sim.signal.component_edge_fill3(
                    ws.owner_id, ws.signal.connections.P1_ACT_idx, _.index, 0,
                ) as mat:
                    mat[:] = ws.values.gain


@float_parameter("gain", "Gain")
class Amplifier(Connector):
    def __init__(self, name, gain=1):
        super().__init__(name)
        self.gain = gain

        self._add_port("p1", NodeType.ELECTRICAL)
        self.p1._add_node("i", NodeDirection.INPUT)

        self._add_port("p2", NodeType.ELECTRICAL)
        self.p2._add_node("o", NodeDirection.OUTPUT)

        self._register_node_coupling("P1_P2", self.p1.i, self.p2.o)

    def _get_workspace(self, sim):
        if sim.signal:
            if self.p1.i.full_name not in sim.signal.nodes:
                return
            refill = sim.model.fsig.f.is_changing or any(
                p.is_changing for p in self.parameters
            )
            ws = FilterWorkspace(self, sim, refill, refill)
            ws.signal.add_fill_function(self.fill, refill)
            ws.frequencies = sim.signal.electrical_frequencies[self.p1.i].frequencies
            return ws
        else:
            return None

    def fill(self, ws):
        if ws.signal.connections.P1_P2_idx > -1:
            for _ in ws.frequencies:
                with ws.sim.signal.component_edge_fill3(
                    ws.owner_id, ws.signal.connections.P1_P2_idx, 0, 0,
                ) as mat:
                    mat[:] = ws.values.gain

    def eval(self, f):
        return float(self.gain)


@float_parameter("gain", "Gain")
class Filter(Connector):
    def __init__(self, name, gain=1):
        super().__init__(name)
        self.gain = gain

        self._add_port("p1", NodeType.ELECTRICAL)
        self.p1._add_node("i", NodeDirection.INPUT)

        self._add_port("p2", NodeType.ELECTRICAL)
        self.p2._add_node("o", NodeDirection.OUTPUT)

        self._register_node_coupling("P1_P2", self.p1.i, self.p2.o)

    def _get_workspace(self, sim):
        if sim.signal:
            refill = sim.model.fsig.f.is_changing or any(
                p.is_changing for p in self.parameters
            )
            ws = FilterWorkspace(self, sim, refill, refill)
            ws.signal.add_fill_function(self.fill, refill)
            ws.frequencies = sim.signal.electrical_frequencies[self.p1.i].frequencies
            return ws
        else:
            return None

    def fill(self, ws):
        Hz = self.eval(ws.sim.model_data.fsig)
        if ws.signal.connections.P1_P2_idx > -1:
            for _ in ws.frequencies:
                with ws.sim.signal.component_edge_fill3(
                    ws.owner_id, ws.signal.connections.P1_P2_idx, 0, 0,
                ) as mat:
                    mat[:] = Hz

    def bode_plot(self, f=None, n=None, return_axes=False):
        """
        Plots Bode for this filter.

        Parameters
        ----------
        f : optional
            Frequencies to plot for in Hz (Not radians)
        n : int, optional
            number of points to plot
        Returns
        -------
        axis : Matplotlib axis for plot if return_axes=True
        """
        import matplotlib.pyplot as plt
        import scipy
        import scipy.signal

        if f is not None:
            w = 2 * np.pi * f
        else:
            w = None

        w, mag, phase = scipy.signal.bode(self.sys, n=n)

        fig, axs = plt.subplots(2, 1, sharex=True)
        axs[0].semilogx(w / 2 / np.pi, mag)
        axs[0].set_ylabel("Amplitude [dB]")

        axs[1].semilogx(w / 2 / np.pi, phase)
        axs[1].set_xlabel("Frequency [Hz]")
        axs[1].set_ylabel("Phase [Deg]")

        fig.suptitle(f"Bode plot for {self.name}")

        if return_axes:
            return axs


@float_parameter("gain", "Gain")
class ZPKFilter(Filter):
    def __init__(self, name, z, p, k, *, fQ=False, gain=1):
        super().__init__(name, gain)
        import cmath
        root = lambda f, Q: -2*np.pi*f/(2*Q) + cmath.sqrt((2*np.pi*f/(2*Q))**2 - (2*np.pi*f)**2)

        if fQ:
            self.z = []
            for f,Q in z:
                r = root(f,Q)
                self.z.append(r)
                self.z.append(r.conjugate())
            
            self.p = []
            for f,Q in p:
                r = root(f,Q)
                self.p.append(r)
                self.p.append(r.conjugate())
        else:
            self.z = z
            self.p = p
        self.k = k

    @property
    def sys(self):
        return (self.z, self.p, self.k)

    def eval(self, f):
        import scipy.signal as signal
        return (
            float(self.gain)
            * signal.freqs_zpk(self.z, self.p, float(self.k), 2 * np.pi * f)[1]
        )


@float_parameter("gain", "Gain")
class ButterFilter(ZPKFilter):
    def __init__(self, name, order, btype, frequency, *, gain=1, analog=True):
        super().__init__(name, [],[],[], gain=gain)
        self.__order = order
        self.__btype = btype
        self.__analog = analog
        self.__frequency = frequency
        self.set_zpk()

    def set_zpk(self):
        import scipy.signal as signal
        z,p,k = signal.butter(
            self.order,
            2 * np.pi * np.array(self.frequency),
            btype=self.btype,
            analog=self.analog,
            output="zpk",
        )
        self.z = z
        self.p = p
        self.k = k

    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, value):
        self.__frequency = value
        self.set_zpk()

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value
        self.set_zpk()

    @property
    def btype(self):
        return self.__btype

    @btype.setter
    def btype(self, value):
        self.__btype = value
        self.set_zpk()

    @property
    def analog(self):
        return self.__analog

    @analog.setter
    def analog(self, value):
        self.__analog = value
        self.set_zpk()



@float_parameter("gain", "Gain")
class Cheby1Filter(ZPKFilter):
    def __init__(self, name, order, rp, btype, frequency, *, gain=1, analog=True):
        import scipy.signal as signal

        zpk = signal.cheby1(
            order,
            rp,
            2 * np.pi * np.array(frequency),
            btype=btype,
            analog=analog,
            output="zpk",
        )
        super().__init__(name, *zpk, gain=gain)
