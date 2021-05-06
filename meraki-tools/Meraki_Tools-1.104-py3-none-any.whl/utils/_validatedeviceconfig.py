"""
Preps function to poccess clone in Async
"""
import asyncio
import logging
import threading

from merakitools import const, lib, model
from .processor import validate_device_config_processor

class Validatedevice(threading.Thread):
	"""
    Setups the orginization objet to run through clone and validate proccess
    """
	
	def __init__(self, org_id):
		"""
        Init Function or Validateorginization
        Args:
            org_id(string): Orginization ID from Meraki
        """
		threading.Thread.__init__(self)
		self.org_id = org_id
		self.name = model.meraki_nets[org_id].name
		self.change_log = []
	
	def run(self):
		"""
        Start the ASYNC fun fuctions and waits for completions to restore
        Cache
        Returns:

        """
		asyncio.run(self._async_run())
		lib.store_cache(self.org_id, model.meraki_nets[self.org_id],'autosync')
	
	async def _async_run(self):
		"""
        Async version of the run function loops through all networks
        then sends the network to the valate proccessor
        Returns:

        """
		print(
				f'\tOrgName: {self.name}Thread PID:{threading.currentThread().native_id}'
		)
		threading.currentThread().setName(self.name)
		print(f'\tThread Name:{threading.currentThread().name}')
		with lib.MerakiAsyncApi() as sdk:
			logger = logging.getLogger('meraki.aio')
			logger.setLevel(logging.WARNING)
			net_compare_task = [
					validate_device_config_processor(self.org_id,device, sdk)
					for device in model.meraki_nets[self.org_id].devices]
			
			await asyncio.gather(*net_compare_task)