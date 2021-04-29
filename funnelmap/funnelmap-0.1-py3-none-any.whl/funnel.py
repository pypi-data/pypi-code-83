"""
module for the central FunnelMap class
"""

from __future__ import annotations

from collections import abc

from funnelmap.formats import FunnelFormatter
from funnelmap.saving import FunnelRecorder

def iterable_not_str(obj):
	return isinstance(obj, abc.Iterable) and not isinstance(obj, str)


class FunnelMap(abc.MutableMapping):
	"""
	mapping arbitrary aliases to unique ids
	"""

	def __init__(self, obj = None):
		if isinstance(obj, dict):
			mappings = obj

			for k, viter in mappings.items():
				if iterable_not_str(viter):
					for v in viter:
						if v in mappings:
							raise ValueError(f"{repr(v)} cannot be both an alias and id")

						if v in self.__dict__:
							id_ = repr(self.__dict__[v])
							raise KeyError(f"alias {repr(v)} already references {id_}")

						self.__dict__[v] = k
				else:
					if viter in mappings:
						raise ValueError(f"{repr(viter)} cannot be both an alias and id")

					if viter in self.__dict__:
						id_ = repr(self.__dict__[viter])
						raise KeyError(f"alias {repr(viter)} already references {id_}")

					self.__dict__[viter] = k

		elif isinstance(obj, abc.MutableMapping):
			# when creating from a non-dict mapping, aliases (the keys) are already
			#	guaranteed unique. just need to check for no alias-id collisions
			ids = set()
			for alias, id_ in obj.items():
				print(alias, id_)
				if alias in ids:
					raise ValueError(f"{repr(alias)} cannot be both an alias and id")
				ids.add(id_)
				self.__dict__[alias] = id_

		else:
			self.__dict__ = {}

	@property
	def ids(self):
		"""ids of a FunnelMap in a list"""
		return list(set(self.__dict__.values()))

	@property
	def aliases(self):
		"""aliases of a FunnelMap in a list"""
		return list(self.__dict__.keys())

	def to_json(self, path: str = '', **kwargs):
		"""
		convert FunnelMap object to a JSON string

		Parameters
		----------
		path : str | path-like
			file path. if not provided, the JSON is returned as a string
		kwargs
			optional keywords to pass to the json constructor

		Returns
		-------
		str
		"""
		formatter = FunnelFormatter(self)
		return formatter.to_json(path, **kwargs)

	def to_dataframe(self, ids: str = 'index'):
		"""
		convert FunnelMap object to a pandas DataFrame

		Parameters
		----------
		ids : str ( = 'index' )
			accepted values are 'index' and 'column'. determines the location
			of the unique ids in the dataframe. the aliases are the entries of
			the frame

		Returns
		-------
		pandas DataFrame
		"""
		formatter = FunnelFormatter(self)
		return formatter.to_dataframe(ids)

	def record(self, name: str, project: str = '', replace: bool = False):
		"""
		save the ids and aliases of the FunnelMap in JSON format in the directory
		determined by parameters `name` and `project`, i.e.
			./funnelmap/records/project/name

		Parameters
		----------
		name : str
			the name of the JSON that stores ids and aliases. '.json' suffix optional
		project : str ( = '')
			name of the subdirectory of /funnelmaps/records that will contain the
			JSON. if not provided, the 'name' parameter is used, so the file path
			would be
				./funnelmap/records/name/name(.json)
			'project' can be multiple levels of directories, as in
				./records/project/subproject/name(.json)
			or even
				./records/project/subproject/.../n*[sub]project/name(.json)
		replace : bool ( = False)
			if the JSON file already exists, do we replace? if it does, and
			`replace = False`, a FileExistsError is thrown. if it does not,
			or `replace = True`, the file is overwritten
		"""
		recorder = FunnelRecorder(self)
		recorder.record(name, project, replace)

	@classmethod
	def from_dataframe(
		self,
		df : DataFrame,
		ids: str = 'index',
	):
		"""
		construct a FunnelMap from a pandas DataFrame.

		Parameters
		----------
		df : pandas DataFrame
			DataFrame that holds ids and aliases
		ids : str ( = 'index')
			location of ids in the DataFrame. if 'index' or 'column', those axis
			labels are used as the ids, and the DataFrame entries are the aliases.
		"""
		if ids == 'index':
			dct = df.to_dict(orient='index')
			for k in dct.keys():
				dct[k] = set((el for el in dct[k].values() if el))
			return FunnelMap(dct)

		if ids == 'columns':
			dct = df.to_dict(orient='list')
			for k in dct.keys():
				dct[k] = set((el for el in dct[k] if el))
			return FunnelMap(dct)

		raise NotImplementedError(
			f"cannot construct FunnelMap with ids parameter {ids}"
		)

	def __setitem__(self, alias, id_):
		self.__dict__[alias] = id_

	def __getitem__(self, alias):
		try:
			return self.__dict__[alias]
		except KeyError:
			if alias in self.ids:
				return alias
			else:
				raise KeyError(f"{repr(alias)}") from None

	def __delitem__(self, alias):
		try:
			del self.__dict__[alias]
		except KeyError:
			if alias in self.ids:
				pass
			else:
				raise KeyError(f"{repr(alias)}") from None

	def __iter__(self):
		return iter(self.__dict__)

	def __len__(self):
		return len(self.__dict__)

	def __str__(self):
		na, ni = len(self.aliases), len(self.ids)
		return f"FunnelMap[{na} aliases, {ni} ids]"

	def __eq__(self, obj):
		"""two FunnelMaps are equal if their mappings are the same"""
		if isinstance(obj, FunnelMap):
			return self.__dict__ == obj.__dict__
		return False
