from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lower:
	"""Lower commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("lower", core, parent)

	def set(self, new_value_for_current: float) -> None:
		"""SCPI: [SOURce]:CURRent[:LEVel][:IMMediate]:ALIMit:LOWer \n
		Snippet: driver.source.current.level.immediate.alimit.lower.set(new_value_for_current = 1.0) \n
		Sets or queries the lower safety limit for current. \n
			:param new_value_for_current: No help available
		"""
		param = Conversions.decimal_value_to_str(new_value_for_current)
		self._core.io.write(f'SOURce:CURRent:LEVel:IMMediate:ALIMit:LOWer {param}')

	def get(self) -> float:
		"""SCPI: [SOURce]:CURRent[:LEVel][:IMMediate]:ALIMit:LOWer \n
		Snippet: value: float = driver.source.current.level.immediate.alimit.lower.get() \n
		Sets or queries the lower safety limit for current. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'SOURce:CURRent:LEVel:IMMediate:ALIMit:LOWer?')
		return Conversions.str_to_float(response)
