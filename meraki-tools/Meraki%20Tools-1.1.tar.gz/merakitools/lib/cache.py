"""
Functions for loading, storing and clearing of Cache Files
This can also be used for backup function in future releases
"""
import pickle
import jsonpickle
import json
from datetime import datetime
from os import path, remove,mkdir
from merakitools import const, model


def cache_age(item):
	"""
	Determins age of Cache file
	Args:
		item: Data Model item that has the last_sync value

	Returns: time delta from time utc now to the value stored in last+sync

	"""
	return datetime.utcnow() - item.last_sync


# returns the cached object if exists otherwise returns the locally synced
def load_cache(org_id: str, is_golden: bool):
	"""
	Lods Cache into Memory from stored pickle files
	Args:
		is_golden: If Master True Load org from Master Dict
		org_id: Org ID of meraki Org to load

	Returns:

	"""
	if is_golden:
		org = model.golden_nets[org_id]
	else:
		org = model.meraki_nets[org_id]
	cache_file_str = \
		f'{const.appcfg.cache_dir}/{const.appcfg.tag_golden}/{str(org.org_id)}-{str(org.name)}.mnet'
	if path.exists(cache_file_str) and const.appcfg.use_cache:
		with open(cache_file_str, "rb") as cache_file:
			org_cached = pickle.load(cache_file)
		if org_cached.lastsync is None:
			print('Has Cache! But it is stale, re-syncing')
			clear_cache(org_id, is_golden)
			org.cached = False
		elif datetime.utcnow() - datetime.fromisoformat(str(org_cached.lastsync)):
			org.__dict__ = org_cached.__dict__.copy()
		else:
			print('Cache File Error! But it is stale, re-syncing')
			clear_cache(org_id, is_golden)
			org.cached = False
	else:
		print('No Cache Found')
		org.cached = False


# writes it to disk for faster load times
def store_cache(org_id: str, is_golden: bool):
	"""
	Stores Cache to file system as pickle files
	Args:
		org_id: Orginixation ID
		is_golden (object): Golden Network

	Returns:

	"""
	if not const.appcfg.use_cache:
		return
	if is_golden:
		org = model.golden_nets[org_id]
		model.golden_nets[org_id].change_log = []
	else:
		org = model.meraki_nets[org_id]
		model.meraki_nets[org_id].change_log = []
	org.cached = True
	
	clear_cache(org_id, is_golden)
	if path.exists(f'{const.appcfg.cache_dir}/{const.appcfg.tag_golden}'):
		cache_file = f'{const.appcfg.cache_dir}/{const.appcfg.tag_golden}/{str(org.org_id)}-{str(org.name)}.mnet'
		pickle.dump(org, open(cache_file, "wb"))
	else:
		mkdir(path.abspath(f'{const.appcfg.cache_dir}/{const.appcfg.tag_golden}'))
		cache_file = f'{const.appcfg.cache_dir}/{const.appcfg.tag_golden}/{str(org.org_id)}-{str(org.name)}.mnet'
		pickle.dump(org, open(cache_file, "wb"))
		


# clears cache and kills disk backup
def clear_cache(org_id: str, is_golden: bool):
	"""
	Clears Cache ( Delets Pickle file from File System
	Args:
		org_id: Orginixation ID
		is_golden: Golden Network

	Returns:

	"""
	if is_golden:
		org = model.golden_nets[org_id]
	else:
		org = model.meraki_nets[org_id]
	cache_file_str = \
		f'{const.appcfg.cache_dir}/{str(org.org_id)}-{str(org.name)}.mnet'
	if path.exists(cache_file_str):
		remove(cache_file_str)
def _chk_dir_name(file: str):
	"""
	Checks DIE name for home folder
	Args:
		file:

	Returns:ABS Path for fiolder

	"""
	if file.startswith('~/'):
		return path.expanduser(file)
	else:
		return path.abspath(file)
def dump_cache_file_to_json(cache_file: str, output_dir: str):
	"""
	Dumps Pickle Cache File to a JSON file for Troubleshooting and validation
	Args:
		cache_file(STR): Cache Full Path and Name with extension
		

	Returns:

	"""
	fpath, name = path.split(cache_file)
	output_file_name = f'{name.split(".")[0]}.json'
	cache_file = _chk_dir_name(cache_file)
	output_full_path = _chk_dir_name(f'{output_dir}/{output_file_name}')
	output_dir = _chk_dir_name(output_dir)
	print(f'Staring export of cache to JSON')
	if path.exists(cache_file):
		with open(cache_file, "rb") as cache_file:
			org_cached = pickle.load(cache_file)
		orgJSON = jsonpickle.encode(org_cached,unpicklable=False)
		output_json = json.loads(orgJSON)
		if not path.exists(output_dir):
			mkdir(output_dir)
		with open(output_full_path, 'w', encoding='utf-8') as dump_file:
			json.dump(output_json, dump_file, ensure_ascii=False, indent=4)
		print(
			f'Cache File {cache_file.name} exported to JSON file {output_full_path}')
	else:
		print('Input cache file does not exisit')
	
	
	
if __name__ == '__main__':
	dump_cache_file_to_json('~/mnetCache/622059698530550345-CiscoLab-Manhattan1.mnet','~/apps/testSync/output')