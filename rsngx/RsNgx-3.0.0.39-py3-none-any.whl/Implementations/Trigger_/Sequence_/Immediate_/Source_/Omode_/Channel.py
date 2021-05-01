from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Channel:
	"""Channel commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("channel", core, parent)

	def set(self, arg_0: int) -> None:
		"""SCPI: TRIGger[:SEQuence][:IMMediate]:SOURce:OMODe:CHANnel \n
		Snippet: driver.trigger.sequence.immediate.source.omode.channel.set(arg_0 = 1) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'TRIGger:SEQuence:IMMediate:SOURce:OMODe:CHANnel {param}')

	def get(self, arg_0: int) -> int:
		"""SCPI: TRIGger[:SEQuence][:IMMediate]:SOURce:OMODe:CHANnel \n
		Snippet: value: int = driver.trigger.sequence.immediate.source.omode.channel.get(arg_0 = 1) \n
		No command help available \n
			:param arg_0: No help available
			:return: arg_0: No help available"""
		param = Conversions.decimal_value_to_str(arg_0)
		response = self._core.io.query_str(f'TRIGger:SEQuence:IMMediate:SOURce:OMODe:CHANnel? {param}')
		return Conversions.str_to_int(response)
