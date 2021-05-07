from calc.calculator import Calculator
import py.test
import itertools
from hypothesis import given, assume, strategies as st
import cmath

def test_calculator():
	x = Calculator()
	assert x.add(3) == format(3, '.2f')
	assert x.sub(1) == format(2, '.2f')
	assert x.mul(8) == format(16, '.2f')
	assert x.div(4) == format(4, '.2f')
	assert x.nrt(2) == format(2, '.2f')
	x.reset()
	assert x.add(1) == format(1, '.2f')

def test_calculator_types():
	with py.test.raises(TypeError):
		calculator = Calculator()
		calculator.add(3, 'hello')
	with py.test.raises(TypeError):
		calculator.add(3,5,8,5)

#def test_torture_test():
#	calculator = Calculator()
#	args = [10, 0, 1, 18, -5, -1, 0.5, -1.5]
#	for t in itertools.permutations(args,2):
#		calculator.add(*t)
#		calculator.sub(*t)
#		calculator.mul(*t)
#		calculator.div(*t)
#		calculator.nrt(*t)

@given(
	st.floats(min_value=-100, max_value=100),
	st.floats(min_value=-100, max_value=100)
)
def test_calculator_hypo(a,b):
	assume(abs(a) > 0.001)
	assume(abs(b) > 0.001)
	calculator = Calculator()
	assert calculator.add(a,b) == format(a+b, '.2f')
	assert calculator.sub(a,b) == format(a-b, '.2f')
	assert calculator.mul(a,b) == format(a*b, '.2f')
	assert calculator.div(a,b) == format(a/b, '.2f')
	assert calculator.nrt(a,b) == format(pow(a,1/b), '.2f')