# this fails (not possible)

from nmigen import Elaboratable, Signal, Array, Module


class ARRAY(Elaboratable):

    def elaborate(self, platform):
        m = Module()
        comb, sync = m.d.comb, m.d.sync

        tree = Array(Signal(2) for i in range(8))
        tree2 = Array(Signal(2) for i in range(8))
        target = Signal(16)

        comb += tree.eq(tree2)
        #comb += target.eq(tree)

        return m


from nmigen.cli import rtlil

def test_array():
    dut = ARRAY()
    vl = rtlil.convert(dut, ports=[])
    with open("test_array.il", "w") as f:
        f.write(vl)

if __name__ == '__main__':
    test_array()

