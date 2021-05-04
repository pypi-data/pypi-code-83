"""
Functions for loading, storing and clearing of Cache Files
This can also be used for backup function in future releases
"""
import pickle
from datetime import datetime
from os import path, remove
from autosync import const, model


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
		f'{const.appcfg.cache_dir}/{str(org.org_id)}-{str(org.name)}.mnet'
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
	cache_file = f'{const.appcfg.cache_dir}/{str(org.org_id)}-{str(org.name)}.mnet'
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
