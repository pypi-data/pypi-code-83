"""
Proccess functions to loop through networks with in an orginizaion and
send that o
"""
import asyncio

import random
import time
from autosync import mnetutils, model, lib, const
from datetime import datetime


async def validate_network_processor(org_id: str, net_id: str,
                                     sdk: object):
	"""
    ASYNC Function to synclye through configuration dict for network and
    call the clone functions based on netork net_id 
    Args: 
        org_id:Orginization Id 
        net_id: Network Id 
        sdk: Meraki SDK Object

    Returns:

    """
	org_name = model.meraki_nets[org_id].name
	net_name = model.meraki_nets[org_id].networks[net_id].name
	print(
			f'{lib.bc.OKBLUE}{org_name} - {net_name} {lib.bc.OKGREEN}Starting configuration validation...{lib.bc.ENDC}'
	)
	for product in model.meraki_nets[org_id].networks[net_id].dashboard:
		await mnetutils.clone(org_id, net_id, sdk, product)


async def proccess_network(org_id: str, net_id: str, sdk: object,
                           tags: list):
	"""
    Function checkts Tag of network for Master tag then loops through
    configuration in network and saves items into the Class objects
	Args:
        org_id:Orginization Id 
        net_id: Network Id 
        sdk: Meraki SDK Objectt

	Returns:

	"""
	t1 = time.perf_counter()
	
	is_golden = await check_is_golden(tags, net_id)
	if is_golden:
		net = model.golden_nets[const.appcfg.tag_golden].networks[
			const.appcfg.tag_golden]
		net_name = const.appcfg.tag_golden
		last_change_ts = await lib.last_change(
			model.golden_nets[const.appcfg.tag_golden].change_log,
			net_id)
		is_changed = await check_last_change(net.change_log_ts,
		                                     last_change_ts)
		if model.golden_nets[
			const.appcfg.tag_golden].cached and is_changed:
			print(
				f'{lib.bc.WARNING} Golden Network Tag: {const.appcfg.tag_golden} Starting Configuration Sync at {t1:0.5f} secound {lib.bc.OKBLUE} - Cached Change TS: '
				f'{model.golden_nets[const.appcfg.tag_golden].networks[const.appcfg.tag_golden].change_log_ts} '
				f'Current TS: {str(last_change_ts)} {lib.bc.ENDC}')
			sync = True
		elif model.golden_nets[
			const.appcfg.tag_golden].cached and not is_changed:
			print(
				f'{lib.bc.OKGREEN} Golden Network Tag: {const.appcfg.tag_golden} is CACHED and has not changed  {lib.bc.ENDC}')
			sync = False
		else:
			print(
					f'{lib.bc.OKGREEN}Started Configuration Sync at {t1:0.5f} secound'
					f' Golden Network Tag: {const.appcfg.tag_golden} is not Cached ')
			sync = True
	else:
		last_change_ts = await lib.last_change(
			model.meraki_nets[org_id].change_log, net_id)
		net = model.meraki_nets[org_id].networks[net_id]
		net_name = model.meraki_nets[org_id].networks[net_id].name
		is_changed = await check_last_change(net.change_log_ts,
		                                     last_change_ts)
		
		if model.meraki_nets[org_id].cached and is_changed:
			print(
					f'{lib.bc.WARNING} Network: {net_name} HAS CHANGED  {lib.bc.OKBLUE} Starting Configuration Sync at {t1:0.5f} secound {lib.bc.OKBLUE} - Cached Change TS: '
					f'{model.meraki_nets[org_id].networks[net_id].change_log_ts} '
					f'Current TS: {str(last_change_ts)} {lib.bc.ENDC}')
			sync = True
		elif model.meraki_nets[org_id].cached and not is_changed:
			print(
					f'{lib.bc.OKGREEN} Network: {net_name} is CACHED and has not changed  {lib.bc.ENDC}')
			sync = False
		else:
			print(
					f'{lib.bc.OKGREEN}Started Configuration Sync at {t1:0.5f} secound'
					f' Network: {net_name} is not Cached ')
			sync = True
	if 'networks' not in net.products:
		net.products.append('networks')
	approvedList = net.supported
	if sync:
		if const.appcfg.tag_target in net.tags or const.appcfg.tag_override:
			for product in net.products:
				if product in approvedList:
					waiting = random.randrange(0, 5)
					await asyncio.sleep(waiting)
					if is_golden:
						await mnetutils.sync(sdk, const.appcfg.tag_golden,
						                     const.appcfg.tag_golden,
						                     product, is_golden)
					else:
						try:
							await mnetutils.sync(sdk, net.org_id,
							                     net.net_id, product,
							                     is_golden)
					
						except Exception as error:
							if const.appcfg.debug:
								print(f'Error: {error}')
					print(
						f'{lib.bc.OKBLUE}{net_name} Finished syncing - {lib.bc.WARNING}{product}{lib.bc.ENDC}')
				else:
					if const.appcfg.debug:
						print(f"No Sync Module for {product}")
			if is_golden:
				model.golden_nets[net_name].networks[
					net_name].lastsync = datetime.utcnow()
				model.golden_nets[net_name].networks[
					net_name].syncruntime = time.perf_counter() - t1
			else:
				
				model.meraki_nets[org_id].networks[
					net_id].lastsync = datetime.utcnow()
				model.meraki_nets[org_id].networks[
					net_id].syncruntime = time.perf_counter() - t1
		if is_golden:
			model.golden_nets[const.appcfg.tag_golden].networks[
				const.appcfg.tag_golden].change_log_ts = await lib.get_network_last_change_ts(
				sdk, org_id, net_id)
		
		print(f'{lib.bc.OKGREEN}Built Config From Network: {net_name} '
		      f'Process took: {net.syncruntime:0.5f} secounds{lib.bc.Default}')
	
	else:
		if const.appcfg.enable_status:
			t = time.perf_counter() - t1
			print(f'Network: {net_name} '
			      f'Skiped Syncing Process took: {t:0.5f} secounds')





async def check_last_change(change, dashboard_change):
	if change != dashboard_change:
		return True
	else:
		return False


async def check_is_golden(tags, net_id):
	if const.appcfg.tag_golden in tags or net_id == 'L_575334852396597314Z':
		return True
	else:
		return False
