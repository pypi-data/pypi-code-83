from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("immediate", core, parent)

	def get_amplitude(self) -> float:
		"""SCPI: SOURce:VOLTage:NEGative[:LEVel][:IMMediate][:AMPLitude] \n
		Snippet: value: float = driver.source.voltage.negative.level.immediate.get_amplitude() \n
		Sets or queries the negative voltage value. Applicable only with NGU401 model. \n
			:return: new_value_for_voltage: No help available
		"""
		response = self._core.io.query_str('SOURce:VOLTage:NEGative:LEVel:IMMediate:AMPLitude?')
		return Conversions.str_to_float(response)

	def set_amplitude(self, new_value_for_voltage: float) -> None:
		"""SCPI: SOURce:VOLTage:NEGative[:LEVel][:IMMediate][:AMPLitude] \n
		Snippet: driver.source.voltage.negative.level.immediate.set_amplitude(new_value_for_voltage = 1.0) \n
		Sets or queries the negative voltage value. Applicable only with NGU401 model. \n
			:param new_value_for_voltage: No help available
		"""
		param = Conversions.decimal_value_to_str(new_value_for_voltage)
		self._core.io.write(f'SOURce:VOLTage:NEGative:LEVel:IMMediate:AMPLitude {param}')
