from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WarningPy:
	"""WarningPy commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("warningPy", core, parent)

	@property
	def immediate(self):
		"""immediate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_immediate'):
			from .WarningPy_.Immediate import Immediate
			self._immediate = Immediate(self._core, self._base)
		return self._immediate

	def get_state(self) -> bool:
		"""SCPI: SYSTem:BEEPer:WARNing:STATe \n
		Snippet: value: bool = driver.system.beeper.warningPy.get_state() \n
		No command help available \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('SYSTem:BEEPer:WARNing:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, arg_0: bool) -> None:
		"""SCPI: SYSTem:BEEPer:WARNing:STATe \n
		Snippet: driver.system.beeper.warningPy.set_state(arg_0 = False) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'SYSTem:BEEPer:WARNing:STATe {param}')
