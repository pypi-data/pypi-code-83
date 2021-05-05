"""
    Main Module of autosync Application
"""
import asyncio
import datetime
import sys
import time

import pandas as pd
from tabulate import tabulate

from merakitools import const, lib, model, utils
from merakitools.model import golden_nets, meraki_nets


def completioninfo():
	"""
    Prints table of infomration after all tasks are complete
    Args:
    Returns:

    """
	orgcount = 0
	network_count = 0
	output_table = []
	for org in meraki_nets:
		orgcount = orgcount + 1
		network_count = network_count + int(len(meraki_nets[org].networks))
		output_table.append({
				'Orginization Name': meraki_nets[org].name,
				'Total Network'    : len(meraki_nets[org].networks),
				'Sync Runtime'     : meraki_nets[org].syncruntime,
				'Last Sync'        : meraki_nets[org].lastsync
		})
	print(f'Total Orgs Synced: {orgcount} '
	      f'Total Network Synced: {network_count}')
	table = pd.DataFrame.from_dict(output_table)
	print(tabulate(table, headers='keys', tablefmt='psql'))


def setup_app(cfg_file=None):
	const.appcfg = model.APPCONFIG(cfg_file)
	temp_sdk = lib.MerakiApi()
	const.meraki_sdk = temp_sdk.api


async def run(cfg_file=None):
	"""
    Main Module Start of Application
    Args:
    Returns:

    """
	setup_app(cfg_file)
	start_time = time.perf_counter()
	print(f'Start time: {start_time:0.5f}')
	golden_nets.update({
			const.appcfg.tag_golden:
				model.ORGDB(const.appcfg.tag_golden,
				            const.appcfg.tag_golden)
	})
	golden_nets[const.appcfg.tag_golden].networks.update(
			{const.appcfg.tag_golden: const.appcfg.tag_golden})
	if const.appcfg.use_cache:
		lib.load_cache(const.appcfg.tag_golden,True)
	if const.appcfg.all_orgs:
		orgs = utils.getOrginizationsAll()
		utils.set_orginization_by_id(orgs)
	elif len(const.appcfg.allow_org_list) != 0:
		orgdb_tasks = [
				utils.getOrginization(org)
				for org in const.appcfg.allow_org_list
		]
		await asyncio.gather(*orgdb_tasks)
	elif len(const.appcfg.allow_org_list_names) != 0:
		orgs = utils.getOrginizationsAll()
		utils.set_orginizations_by_name(orgs)
	else:
		print("Error No Orginizations List Exiting")
		sys.exit()
	org_threads = []
	validate_thread = []
	for org_id in meraki_nets:
		org_threads.append(utils.Orgsyncprocessor(org_id))
	for orgthread in org_threads:
		orgthread.start()
	for orgthread in org_threads:
		orgthread.join()
	
	for org in meraki_nets:
		validate_thread.append(utils.Validateorginization(org))
	for thread in validate_thread:
		thread.start()
	for thread in validate_thread:
		thread.join()
	
	if const.appcfg.use_cache:
		golden_nets[
			const.appcfg.tag_golden].lastsync = datetime.datetime.utcnow()
		lib.store_cache(const.appcfg.tag_golden,True)
	
	print(f'Total Job Runtime: '
	      f'{(time.perf_counter() - start_time):0.5f} secounds')
	completioninfo()


if __name__ == '__main__':
	config_file = 'testing/config.json'
	asyncio.run(run(config_file))
	print('Done')
