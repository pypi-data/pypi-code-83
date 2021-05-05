"""
module for saving ids and aliases in the funnelmap/records directory
"""
from __future__ import annotations

import pathlib
import json

from rich import print

# create records directory
records_dir = pathlib.Path(__file__).parent / 'records'
if not records_dir.exists():
	records_dir.mkdir()

# registry of recorded FunnelMaps
registry_name = '.registry.json'
registry_file = records_dir / registry_name
if not registry_file.exists():
	registry_file.touch()

# read in the existing registry file
try:
	with open(registry_file, 'r') as json_file:
		_REGISTRY = json.load(json_file)
except ValueError:
	# 'registry_file' is blank
	_REGISTRY = {}





#----------------------------
# functions for changing the registry of saved json

def add_to_registry(name: str, rpath: Union[str, Path]):
	"""
	add the relative (to ./funnelmap/records) path to a FunnelMap record to the
	registry JSON
	"""
	try:
		_old_path_list = _REGISTRY[name]
		rpath_string = str(rpath)
		if rpath_string not in _old_path_list:
			_old_path_list.append(str(rpath))

	except KeyError:
		_REGISTRY[name] = [str(rpath)]

	with open(registry_file, 'w') as json_file:
		json.dump(_REGISTRY, json_file, indent=4)

def delete_from_registry(name: str, rpath: Union[str, Path]):
	"""
	remove a relative path to a FunnelMap record from the registry JSON
	"""
	name_no_suffix = name.split('.')[0]
	path_list = _REGISTRY[name_no_suffix]
	path_list.remove(rpath)

	if not path_list:
		# if no paths corresponding to `name`, delete `name`
		del _REGISTRY[name]

	with open(registry_file, 'w') as json_file:
		json.dump(_REGISTRY, json_file, indent=4)


def _retrieve_paths_from_registry(name: str):
	"""
	retrieve the (sometimes length-one) list of relative paths to JSONs with
	name `name`
	"""
	name_no_suffix = name.split('.')[0]
	try:
		path_list = _REGISTRY[name_no_suffix]
		return path_list.copy()

	except KeyError:
		raise FileNotFoundError(f"there is no stored JSON with name {name}") from None


def retrieve_from_registry(name: str, project: str = ''):
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
		project is provided, the path to the JSON with filename `name` in that
		project is returned
	"""
	path_list = _retrieve_paths_from_registry(name)

	if len(path_list) == 1:
		json_path = records_dir / path_list[0]
		return json_path

	else:
		if not project:
			raise ValueError(
				f"there are multiple projects with JSONs named '{name}'. "
				"please provide a project name via the `project` parameter."
			)

		paths_no_names = ['/'.join(p.split('/')[:-1]) for p in path_list]
		if project not in paths_no_names:
			raise FileNotFoundError(
				f"there is no project containing a JSON with name '{name}'"
			)

		idx = paths_no_names.index(project)
		project_path_with_name = path_list[idx]
		json_path = records_dir / project_path_with_name
		return json_path





#----------------------------
# objects for adding and removing saved jsons

def _delete_parents(path: str):
	"""recursively deleting empty directories"""
	parent = path.parent
	try:
		parent.rmdir()
		_delete_parents(parent)
	except OSError:
		# other JSONs in that directory
		pass

def _delete_json_and_dir(json_name: str, path: str):
	"""remove a recorded JSON, its dir (if empty), and all empty parent dirs"""
	json_path = records_dir / path
	json_path.unlink()

	delete_from_registry(json_name, path)
	_delete_parents(json_path)

def delete_from_records(name: str, project: str = ''):
	"""
	remove JSON with filename `name` from the set of saved FunnelMap JSONs.

	Parameters
	----------
	name : str
		the name of JSON(s) to remove
	project : str ( = '' )
		if not provided, remove all JSONs of with filename `name` from ALL
		projects. if provided, only that project's JSON of name `name` is
		deleted
	"""
	path_list = _retrieve_paths_from_registry(name)

	if project:
		paths_no_names = ['/'.join(p.split('/')[:-1]) for p in path_list]
		if project not in paths_no_names:
			raise FileNotFoundError(
				f"there is no project containing a JSON with name '{name}'"
			)

		idx = paths_no_names.index(project)
		project_path_with_name = path_list[idx]
		_delete_json_and_dir(name, project_path_with_name)

	else:
		for path in path_list:
			_delete_json_and_dir(name, path)


class FunnelRecorder(object):
	"""
	class for saving FunnelMap information
	"""

	records_dir = records_dir

	def __init__(self, funnel: FunnelMap):
		self.funnel = funnel

	def _verify_file_name(self, name: str, fmt: str = 'json'):
		"""making sure file name has '.type' suffix"""
		name = name.split('.')[0]
		return '.'.join([name, fmt])

	def record(
		self,
		name: str,
		project: str = '',
		replace: bool = False
	):
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

		# use 'name' if project name is not provided
		name_no_suffix = name.split('.')[0]
		if not project:
			project = name_no_suffix

		# create project directory if it doesn't exist, making parent directories
		#	if needed
		rec_path = self.records_dir / project
		if not rec_path.exists():
			rec_path.mkdir(parents=True)

		# save funnel data to record JSON
		name_with_suffix = self._verify_file_name(name)
		funnel_path = rec_path / name_with_suffix
		if funnel_path.exists() and not replace:
			raise FileExistsError(
				f"record '{name_with_suffix}' already exists in "
				f"project '{str(project)}'"
			)
		self.funnel.to_json(funnel_path, indent=4)

		# save relative path to registry for faster access later
		rpath = pathlib.Path(project) / name_with_suffix
		add_to_registry(name_no_suffix, rpath)
