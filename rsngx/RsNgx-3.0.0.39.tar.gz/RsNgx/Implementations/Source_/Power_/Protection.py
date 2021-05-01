from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Protection:
	"""Protection commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("protection", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:POWer:PROTection[:STATe] \n
		Snippet: value: bool = driver.source.power.protection.get_state() \n
		Sets or queries the OPP state of the previous selected channel. \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('SOURce:POWer:PROTection:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, arg_0: bool) -> None:
		"""SCPI: [SOURce]:POWer:PROTection[:STATe] \n
		Snippet: driver.source.power.protection.set_state(arg_0 = False) \n
		Sets or queries the OPP state of the previous selected channel. \n
			:param arg_0: No help available
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'SOURce:POWer:PROTection:STATe {param}')

	def get_level(self) -> float:
		"""SCPI: [SOURce]:POWer:PROTection:LEVel \n
		Snippet: value: float = driver.source.power.protection.get_level() \n
		Sets or queries the overvoltage protection value of the selected channel. \n
			:return: new_value_for_voltage_protection: No help available
		"""
		response = self._core.io.query_str('SOURce:POWer:PROTection:LEVel?')
		return Conversions.str_to_float(response)

	def set_level(self, new_value_for_voltage_protection: float) -> None:
		"""SCPI: [SOURce]:POWer:PROTection:LEVel \n
		Snippet: driver.source.power.protection.set_level(new_value_for_voltage_protection = 1.0) \n
		Sets or queries the overvoltage protection value of the selected channel. \n
			:param new_value_for_voltage_protection: No help available
		"""
		param = Conversions.decimal_value_to_str(new_value_for_voltage_protection)
		self._core.io.write(f'SOURce:POWer:PROTection:LEVel {param}')

	def get_tripped(self) -> bool:
		"""SCPI: [SOURce]:POWer:PROTection:TRIPped \n
		Snippet: value: bool = driver.source.power.protection.get_tripped() \n
		Queries the OPP state of the selected channel. \n
			:return: result: No help available
		"""
		response = self._core.io.query_str('SOURce:POWer:PROTection:TRIPped?')
		return Conversions.str_to_bool(response)

	def clear(self) -> None:
		"""SCPI: [SOURce]:POWer:PROTection:CLEar \n
		Snippet: driver.source.power.protection.clear() \n
		Resets the OPP state of the selected channel. If an OPP event has occurred before, the reset also erases the message on
		the display. \n
		"""
		self._core.io.write(f'SOURce:POWer:PROTection:CLEar')

	def clear_with_opc(self) -> None:
		"""SCPI: [SOURce]:POWer:PROTection:CLEar \n
		Snippet: driver.source.power.protection.clear_with_opc() \n
		Resets the OPP state of the selected channel. If an OPP event has occurred before, the reset also erases the message on
		the display. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsNgx.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce:POWer:PROTection:CLEar')
