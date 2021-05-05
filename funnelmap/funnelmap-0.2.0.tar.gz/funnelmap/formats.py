"""
module for converting ids and aliases of a FunnelMap into other objects
"""
from __future__ import annotations

import json


class FunnelFormatter(object):

	def __init__(self, funnel: Funnel):
		self.funnel = funnel

		# for writing FunnelMap, it's convenient to get the aliases and ids into
		#	a dict like {id: [alias, ... alias], ...}
		self.mappings = dict()
		for alias in self.funnel.aliases:
			id_ = self.funnel[alias]
			if id_ in self.mappings:
				self.mappings[id_].append(alias)
			else:
				self.mappings[id_] = [alias]

	def to_json(
		self,
		path: str,
		**kwargs
	):
		"""
		convert a funnel into a JSON string of the form
			[
				{
					'id' : id_0,
					'aliases' : [
						al_00, al_01, ..., al_0k
					]
				},
				{
					'id' : id_1,
					'aliases' : [
						al_10, al_11, ..., al_1j
					]
				},
				...
			]

		Parameters
		----------
		path : str | path-like
			file path. if not provided, the JSON is returned as a string
		kwargs
			optional keywords to pass to the json module's `dump` or `dumps`
			method
		"""

		json_list = [{'id':i, 'aliases':a} for i, a in self.mappings.items()]

		if path:
			with open(path, 'w') as json_file:
				json.dump(json_list, json_file, **kwargs)
		else:
			return json.dumps(json_list, **kwargs)

	def to_dataframe(
		self,
		ids: str = 'index'
	):
		"""
		convert a funnel to a pandas DataFrame

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
		try:
			import pandas
		except ModuleNotFoundError as err:
			msg = "`pandas` package needed to convert FunnelMap to DataFrame"
			raise ModuleNotFoundError(msg) from err

		# .from_dict(..., orient='columns') can raise the error
		#	ValueError: arrays must all be same length
		df = pandas.DataFrame.from_dict(self.mappings, orient='index')
		if ids == 'index':
			return df
		elif ids == 'columns':
			return df.transpose()

		raise ValueError(f"unrecognized value for `ids`: {repr(ids)}")
