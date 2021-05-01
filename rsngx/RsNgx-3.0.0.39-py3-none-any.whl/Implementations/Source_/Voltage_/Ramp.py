from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ramp:
	"""Ramp commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ramp", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:VOLTage:RAMP[:STATe] \n
		Snippet: value: bool = driver.source.voltage.ramp.get_state() \n
		Sets or queries the state of ramp function for the previous selected channel. \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('SOURce:VOLTage:RAMP:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, arg_0: bool) -> None:
		"""SCPI: [SOURce]:VOLTage:RAMP[:STATe] \n
		Snippet: driver.source.voltage.ramp.set_state(arg_0 = False) \n
		Sets or queries the state of ramp function for the previous selected channel. \n
			:param arg_0: No help available
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'SOURce:VOLTage:RAMP:STATe {param}')

	def get_duration(self) -> float:
		"""SCPI: [SOURce]:VOLTage:RAMP:DURation \n
		Snippet: value: float = driver.source.voltage.ramp.get_duration() \n
		Sets or queries the duration of the voltage ramp. \n
			:return: new_value_for_voltage: No help available
		"""
		response = self._core.io.query_str('SOURce:VOLTage:RAMP:DURation?')
		return Conversions.str_to_float(response)

	def set_duration(self, new_value_for_voltage: float) -> None:
		"""SCPI: [SOURce]:VOLTage:RAMP:DURation \n
		Snippet: driver.source.voltage.ramp.set_duration(new_value_for_voltage = 1.0) \n
		Sets or queries the duration of the voltage ramp. \n
			:param new_value_for_voltage: No help available
		"""
		param = Conversions.decimal_value_to_str(new_value_for_voltage)
		self._core.io.write(f'SOURce:VOLTage:RAMP:DURation {param}')
