"""1st sprint project Turing College Calculator"""
__version__ = "0.0.3"

from sarunasncalculator.calculator import Calculator

callc = Calculator()
callc.add(2)
callc.add(3)

print(callc.get_action_seq())
