from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("output", core, parent)

	# noinspection PyTypeChecker
	def get_polarity(self) -> enums.NormInv:
		"""SCPI: [SOURce<HW>]:SWEep:MARKer:OUTPut:POLarity \n
		Snippet: value: enums.NormInv = driver.source.sweep.marker.output.get_polarity() \n
		Selects the polarity of the marker signal. \n
			:return: polarity: NORMal| INVerted NORMal Marker level is high when after reaching the mark. INVerted Marker level is low after reaching the mark.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:MARKer:OUTPut:POLarity?')
		return Conversions.str_to_scalar_enum(response, enums.NormInv)

	def set_polarity(self, polarity: enums.NormInv) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:MARKer:OUTPut:POLarity \n
		Snippet: driver.source.sweep.marker.output.set_polarity(polarity = enums.NormInv.INVerted) \n
		Selects the polarity of the marker signal. \n
			:param polarity: NORMal| INVerted NORMal Marker level is high when after reaching the mark. INVerted Marker level is low after reaching the mark.
		"""
		param = Conversions.enum_scalar_to_str(polarity, enums.NormInv)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:MARKer:OUTPut:POLarity {param}')
