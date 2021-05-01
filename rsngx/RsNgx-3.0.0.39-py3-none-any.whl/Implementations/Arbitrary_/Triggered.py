from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Triggered:
	"""Triggered commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("triggered", core, parent)

	def get_state(self) -> bool:
		"""SCPI: ARBitrary:TRIGgered[:STATe] \n
		Snippet: value: bool = driver.arbitrary.triggered.get_state() \n
		Sets or queries the arbitrary trigger mode. \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('ARBitrary:TRIGgered:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, arg_0: bool) -> None:
		"""SCPI: ARBitrary:TRIGgered[:STATe] \n
		Snippet: driver.arbitrary.triggered.set_state(arg_0 = False) \n
		Sets or queries the arbitrary trigger mode. \n
			:param arg_0: 0 OFF - Trigger input is deactivated. 1 ON - Trigger input is activated.
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'ARBitrary:TRIGgered:STATe {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ArbTrigMode:
		"""SCPI: ARBitrary:TRIGgered:MODE \n
		Snippet: value: enums.ArbTrigMode = driver.arbitrary.triggered.get_mode() \n
		Sets or queries the arbitrary trigger mode of the previous selected channel. \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('ARBitrary:TRIGgered:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ArbTrigMode)

	def set_mode(self, arg_0: enums.ArbTrigMode) -> None:
		"""SCPI: ARBitrary:TRIGgered:MODE \n
		Snippet: driver.arbitrary.triggered.set_mode(arg_0 = enums.ArbTrigMode.RUN) \n
		Sets or queries the arbitrary trigger mode of the previous selected channel. \n
			:param arg_0: SINGle | RUN SINGle A trigger event starts only with one arbitrary sequence. RUN A trigger event starts the whole arbitrary sequences (with all repetitions) .
		"""
		param = Conversions.enum_scalar_to_str(arg_0, enums.ArbTrigMode)
		self._core.io.write(f'ARBitrary:TRIGgered:MODE {param}')
