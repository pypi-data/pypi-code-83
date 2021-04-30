from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gate:
	"""Gate commands group definition. 6 total commands, 6 Sub-groups, 0 group commands
	Repeated Capability: Gate, default value after init: Gate.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("gate", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_gate_get', 'repcap_gate_set', repcap.Gate.Nr1)

	def repcap_gate_set(self, enum_value: repcap.Gate) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Gate.Default
		Default value after init: Gate.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_gate_get(self) -> repcap.Gate:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_average'):
			from .Gate_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def feed(self):
		"""feed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_feed'):
			from .Gate_.Feed import Feed
			self._feed = Feed(self._core, self._base)
		return self._feed

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Gate_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def start(self):
		"""start commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_start'):
			from .Gate_.Start import Start
			self._start = Start(self._core, self._base)
		return self._start

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Gate_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def stop(self):
		"""stop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stop'):
			from .Gate_.Stop import Stop
			self._stop = Stop(self._core, self._base)
		return self._stop

	def clone(self) -> 'Gate':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gate(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
