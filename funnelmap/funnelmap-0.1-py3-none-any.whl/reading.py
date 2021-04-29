"""
module for reading ids and aliases in from files of various types
"""

from __future__ import annotations

import json
import csv

from funnelmap.funnel import FunnelMap
from funnelmap.saving import retrieve_from_registry


def read_csv(
	path: str,
	id_index: int = 0,
	**fmtparams
):
	"""
	construct a FunnelMap from a .csv file. the location of the id is determined
	by the `id_index` parameter, and aliases for that id are the remaining
	elements in the same row.

	Parameters
	----------
	path : str | path-like
		location of the .csv file holding ids and aliases
	id_index : int ( = 0 )
		column index of the id's
	fmtparams : keyword arguments
		formatting parameters that are passed to csv.reader

	Returns
	-------
	FunnelMap

	Raises
	------
	KeyError
		if an id is the same as one already provided
	"""

	try:
		idx = int(id_index)
	except:
		raise TypeError("id_index must be an int")

	maps = {}
	with open(path, newline='') as csvfile:
		map_reader = csv.reader(csvfile, **fmtparams)
		for i, id_and_aliases in enumerate(map_reader):
			id_ = id_and_aliases.pop(idx)
			if id_ in maps:
				raise KeyError(f"id {repr(id_)} in row {i} is already defined")

			maps[id_] = set((al.strip() for al in id_and_aliases if al != ''))

	return FunnelMap(maps)


def read_json(path: str):
	"""
	construct a FunnelMap from a .json file. the JSON structure is assumed to
	be a list of dictionary elements structured like
		{
			'id' : id_0,
			'aliases' : [
				al_00, al_01, ..., al_0k
			]
		}

	Parameters
	----------
	path : str | path-like
		location of the .json file holding ids and aliases

	Returns
	-------
	FunnelMap
	"""
	maps = {}
	with open(path, 'r') as json_file:
		json_list = json.load(json_file)
		for dct in json_list:

			if set(dct.keys()) != {'id', 'aliases'}:
				raise OSError("JSON dicts must only have 'id' and 'aliases' keys")

			id_ = dct['id']
			if id_ in maps:
				raise KeyError(f"id {repr(id_)} is defined more than once")

			maps[id_] = set((al for al in dct['aliases']))

	return FunnelMap(maps)


def read_record(name: str, project: str = ''):
	"""
	retrieve the recorded json path from the stored registry by name of the json.

	Parameters
	----------
	name : str
		the name of the requested JSON
	projects : str ( = '' )
		the project name corresponding to the requested JSON. if there is only
		JSON with filename {name}.json, this parameter is irrelevant. if there
		are multiple and `project` is not provided, a ValueError is thrown. if
		project is provided, the JSON with filename `name` in that project is
		returned
	"""
	json_file = retrieve_from_registry(name, project)
	return read_json(json_file)
