"""1st sprint project Turing College Calculator"""
__version__ = "0.0.4"

from sarunasncalculator.calculator import Calculator

callc = Calculator()
callc.add(2)
callc.add(7)

#we can print current running memory , function returns float
print(callc.get_current_result())

#we can print action sequence , function returns str
print(callc.get_action_seq())
