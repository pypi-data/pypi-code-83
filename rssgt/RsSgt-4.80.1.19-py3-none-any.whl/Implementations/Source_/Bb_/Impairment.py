from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Impairment:
	"""Impairment commands group definition. 17 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("impairment", core, parent)

	@property
	def bbmm(self):
		"""bbmm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bbmm'):
			from .Impairment_.Bbmm import Bbmm
			self._bbmm = Bbmm(self._core, self._base)
		return self._bbmm

	@property
	def iqOutput(self):
		"""iqOutput commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOutput'):
			from .Impairment_.IqOutput import IqOutput
			self._iqOutput = IqOutput(self._core, self._base)
		return self._iqOutput

	@property
	def optimization(self):
		"""optimization commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_optimization'):
			from .Impairment_.Optimization import Optimization
			self._optimization = Optimization(self._core, self._base)
		return self._optimization

	@property
	def rf(self):
		"""rf commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_rf'):
			from .Impairment_.Rf import Rf
			self._rf = Rf(self._core, self._base)
		return self._rf

	def clone(self) -> 'Impairment':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Impairment(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
