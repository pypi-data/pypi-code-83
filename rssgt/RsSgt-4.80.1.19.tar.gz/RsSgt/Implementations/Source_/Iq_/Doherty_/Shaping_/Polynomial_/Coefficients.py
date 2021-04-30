from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coefficients:
	"""Coefficients commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("coefficients", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:POLYnomial:COEFficients:CATalog \n
		Snippet: value: List[str] = driver.source.iq.doherty.shaping.polynomial.coefficients.get_catalog() \n
		No command help available \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:SHAPing:POLYnomial:COEFficients:CATalog?')
		return Conversions.str_to_str_list(response)

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:POLYnomial:COEFficients:LOAD \n
		Snippet: driver.source.iq.doherty.shaping.polynomial.coefficients.load(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:SHAPing:POLYnomial:COEFficients:LOAD {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:POLYnomial:COEFficients:STORe \n
		Snippet: driver.source.iq.doherty.shaping.polynomial.coefficients.set_store(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:SHAPing:POLYnomial:COEFficients:STORe {param}')

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Ipart_0: List[float]: No parameter help available
			- J_0: float: No parameter help available
			- I_1: float: No parameter help available
			- J_1: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Ipart_0', DataType.FloatList, None, False, True, 1),
			ArgStruct.scalar_float('J_0'),
			ArgStruct.scalar_float('I_1'),
			ArgStruct.scalar_float('J_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ipart_0: List[float] = None
			self.J_0: float = None
			self.I_1: float = None
			self.J_1: float = None

	def get_value(self) -> ValueStruct:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:POLYnomial:COEFficients \n
		Snippet: value: ValueStruct = driver.source.iq.doherty.shaping.polynomial.coefficients.get_value() \n
		No command help available \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce<HwInstance>:IQ:DOHerty:SHAPing:POLYnomial:COEFficients?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:POLYnomial:COEFficients \n
		Snippet: driver.source.iq.doherty.shaping.polynomial.coefficients.set_value(value = ValueStruct()) \n
		No command help available \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce<HwInstance>:IQ:DOHerty:SHAPing:POLYnomial:COEFficients', value)
