from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ueid:
	"""Ueid commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueid", core, parent)

	def set(self, ueid: int, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:ITEM<CH0>:UEID \n
		Snippet: driver.source.bb.eutra.dl.subf.encc.pdcch.extc.item.ueid.set(ueid = 1, subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the n_RNTI for the selected PDCCH. \n
			:param ueid: integer Range: 0 to 100000
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')"""
		param = Conversions.decimal_value_to_str(ueid)
		subframeNull_cmd_val = self._base.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._base.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:ITEM{itemNull_cmd_val}:UEID {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:ITEM<CH0>:UEID \n
		Snippet: value: int = driver.source.bb.eutra.dl.subf.encc.pdcch.extc.item.ueid.get(subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the n_RNTI for the selected PDCCH. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
			:return: ueid: integer Range: 0 to 100000"""
		subframeNull_cmd_val = self._base.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._base.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:ITEM{itemNull_cmd_val}:UEID?')
		return Conversions.str_to_int(response)
