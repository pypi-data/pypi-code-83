from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calibration:
	"""Calibration commands group definition. 15 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("calibration", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .Calibration_.All import All
			self._all = All(self._core, self._base)
		return self._all

	@property
	def bbin(self):
		"""bbin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bbin'):
			from .Calibration_.Bbin import Bbin
			self._bbin = Bbin(self._core, self._base)
		return self._bbin

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_frequency'):
			from .Calibration_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def iqModulator(self):
		"""iqModulator commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_iqModulator'):
			from .Calibration_.IqModulator import IqModulator
			self._iqModulator = IqModulator(self._core, self._base)
		return self._iqModulator

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_level'):
			from .Calibration_.Level import Level
			self._level = Level(self._core, self._base)
		return self._level

	@property
	def roscillator(self):
		"""roscillator commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_roscillator'):
			from .Calibration_.Roscillator import Roscillator
			self._roscillator = Roscillator(self._core, self._base)
		return self._roscillator

	def clone(self) -> 'Calibration':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Calibration(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
