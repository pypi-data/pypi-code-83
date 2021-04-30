from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Threshold:
	"""Threshold commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("threshold", core, parent)

	@property
	def base(self):
		"""base commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_base'):
			from .Threshold_.Base import Base
			self._base = Base(self._core, self._base)
		return self._base

	@property
	def power(self):
		"""power commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Threshold_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	def clone(self) -> 'Threshold':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Threshold(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
