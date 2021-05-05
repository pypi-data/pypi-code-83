from nmigen import Module, Elaboratable, Signal
from nmigen.cli import rtlil

class MiniMask(Elaboratable):
    def __init__(self):
        self.shift = Signal(6)
        self.y = Signal(16)

    def elaborate(self, platform):
        m = Module()
        #m.d.comb += self.y.eq((1<<self.shift) - 1)
        for i in range(16):
            with m.If(self.shift > i):
                m.d.comb += self.y[i].eq(1)
        return m

if __name__ == '__main__':
    dut = MiniMask()
    vl = rtlil.convert(dut, ports=[dut.shift, dut.y])
    with open("mini_mask.il", "w") as f:
        f.write(vl)

