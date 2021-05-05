from nmigen import Cat, Module, Const, Signal, signed
from nmigen.sim.pysim import Simulator, Settle

def resolve(expr, set_value=None):
    sim = Simulator(Module())
    a = []
    def testbench():
        if set_value is not None:
            (to_set, value) = set_value
            yield to_set.eq(value)
            yield Settle()
        a.append((yield expr))
    sim.add_process(testbench)
    sim.run()
    return a[0]

sig = Const(-153)
print("sig", sig, resolve(sig))
print("abs sig", abs(sig), resolve(abs(sig)))

sig2 = Cat(sig).as_signed()
print("sig2", sig2, resolve(sig2))
print("abs sig2", abs(sig2), resolve(abs(sig2)))

print("bin sig2", bin(resolve(sig2)))
print("bin -sig2", bin(resolve(-sig2)))

value = Signal(signed(5))
sig4 = Cat(value).as_signed()
print("sig4", sig4, bin(resolve(sig4, (value, -2))))
print("abs sig4", abs(sig4), bin(resolve(abs(sig4), (value, -2))))

value = Signal(signed(5))
print("value", value, resolve(value, (value, -2)))
print("abs value", abs(value), resolve(abs(value), (value, -2)))

