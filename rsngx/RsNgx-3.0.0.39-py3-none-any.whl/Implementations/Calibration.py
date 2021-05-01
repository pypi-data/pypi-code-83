from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from ..Internal.Utilities import trim_str_response
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calibration:
	"""Calibration commands group definition. 9 total commands, 2 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("calibration", core, parent)

	@property
	def point(self):
		"""point commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_point'):
			from .Calibration_.Point import Point
			self._point = Point(self._core, self._base)
		return self._point

	@property
	def self(self):
		"""self commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_self'):
			from .Calibration_.Self import Self
			self._self = Self(self._core, self._base)
		return self._self

	# noinspection PyTypeChecker
	class DateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Arg_0: float: No parameter help available
			- Arg_1: float: No parameter help available
			- Arg_2: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Arg_0'),
			ArgStruct.scalar_float('Arg_1'),
			ArgStruct.scalar_float('Arg_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Arg_0: float = None
			self.Arg_1: float = None
			self.Arg_2: float = None

	def get_date(self) -> DateStruct:
		"""SCPI: CALibration:DATE \n
		Snippet: value: DateStruct = driver.calibration.get_date() \n
		No command help available \n
			:return: structure: for return value, see the help for DateStruct structure arguments.
		"""
		return self._core.io.query_struct('CALibration:DATE?', self.__class__.DateStruct())

	def save(self) -> None:
		"""SCPI: CALibration:SAVE \n
		Snippet: driver.calibration.save() \n
		No command help available \n
		"""
		self._core.io.write(f'CALibration:SAVE')

	def save_with_opc(self) -> None:
		"""SCPI: CALibration:SAVE \n
		Snippet: driver.calibration.save_with_opc() \n
		No command help available \n
		Same as save, but waits for the operation to complete before continuing further. Use the RsNgx.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CALibration:SAVE')

	def get_temperature(self) -> float:
		"""SCPI: CALibration:TEMPerature \n
		Snippet: value: float = driver.calibration.get_temperature() \n
		No command help available \n
			:return: result: No help available
		"""
		response = self._core.io.query_str('CALibration:TEMPerature?')
		return Conversions.str_to_float(response)

	def get_type_py(self) -> str:
		"""SCPI: CALibration:TYPE \n
		Snippet: value: str = driver.calibration.get_type_py() \n
		No command help available \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('CALibration:TYPE?')
		return trim_str_response(response)

	def set_type_py(self, arg_0: str) -> None:
		"""SCPI: CALibration:TYPE \n
		Snippet: driver.calibration.set_type_py(arg_0 = '1') \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.value_to_quoted_str(arg_0)
		self._core.io.write(f'CALibration:TYPE {param}')

	def get_value(self) -> float:
		"""SCPI: CALibration:VALue \n
		Snippet: value: float = driver.calibration.get_value() \n
		No command help available \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('CALibration:VALue?')
		return Conversions.str_to_float(response)

	def set_value(self, arg_0: float) -> None:
		"""SCPI: CALibration:VALue \n
		Snippet: driver.calibration.set_value(arg_0 = 1.0) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'CALibration:VALue {param}')

	def get_count(self) -> float:
		"""SCPI: CALibration:COUNt \n
		Snippet: value: float = driver.calibration.get_count() \n
		No command help available \n
			:return: result: No help available
		"""
		response = self._core.io.query_str('CALibration:COUNt?')
		return Conversions.str_to_float(response)

	def get_user(self) -> bool:
		"""SCPI: CALibration:USER \n
		Snippet: value: bool = driver.calibration.get_user() \n
		No command help available \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('CALibration:USER?')
		return Conversions.str_to_bool(response)

	def set_user(self, arg_0: bool) -> None:
		"""SCPI: CALibration:USER \n
		Snippet: driver.calibration.set_user(arg_0 = False) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'CALibration:USER {param}')
