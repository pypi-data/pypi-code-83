from nmigen import Module, Elaboratable, Signal
from nmigen.cli import rtlil


def instr_is_priv(m, is_priv_insn, op):
    """determines if the instruction is privileged or not
    """
    comb = m.d.comb
    with m.Switch(op):
        with m.Case(5, 6):
            comb += is_priv_insn.eq(1)
    return is_priv_insn


class PowerDecode2(Elaboratable):

    def elaborate(self, platform):
        m = Module()
        comb = m.d.comb
        ext_irq = Signal()
        priv = Signal()
        op = Signal(3)
        is_priv_insn = Signal(reset_less=True)

        # external interrupt?
        with m.If(ext_irq):
            comb += priv.eq(0)
            pass
        with m.Elif(instr_is_priv(m, is_priv_insn, op)):
            comb += priv.eq(1)

        return m


if __name__ == '__main__':
    dec2 = PowerDecode2()
    vl = rtlil.convert(dec2)
    with open("dec2.il", "w") as f:
        f.write(vl)
