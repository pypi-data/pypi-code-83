from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fmt:
	"""Fmt commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fmt", core, parent)

	def set(self, format_py: enums.EutraNbIoTdCiFormat, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:FMT \n
		Snippet: driver.source.bb.eutra.dl.niot.dci.alloc.fmt.set(format_py = enums.EutraNbIoTdCiFormat.N0, allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI format for the selected allocation. \n
			:param format_py: N0| N1| N2
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')"""
		param = Conversions.enum_scalar_to_str(format_py, enums.EutraNbIoTdCiFormat)
		allocationNull_cmd_val = self._base.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:FMT {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.EutraNbIoTdCiFormat:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:FMT \n
		Snippet: value: enums.EutraNbIoTdCiFormat = driver.source.bb.eutra.dl.niot.dci.alloc.fmt.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI format for the selected allocation. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: format_py: N0| N1| N2"""
		allocationNull_cmd_val = self._base.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:FMT?')
		return Conversions.str_to_scalar_enum(response, enums.EutraNbIoTdCiFormat)
