"""
Preps function to poccess clone in Async
"""
import asyncio
import logging
import threading

from merakitools import const, lib, model
from .processor import validate_device_config_processor, _config_tags


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
        lib.store_cache(self.org_id, model.meraki_nets[self.org_id], 'autosync')

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
        configs = []
        with lib.MerakiAsyncApi() as sdk:
            logger = logging.getLogger('meraki.aio')
            logger.setLevel(logging.WARNING)
            for device in model.meraki_nets[self.org_id].devices:
                configs.append(validate_device_config_processor(self.org_id, device, sdk))
            for config in configs:
                if config is not None:
                    result = await sdk.organizations.createOrganizationActionBatch(self.org_id, config, confirmed=True)
                    status = await sdk.organizations.getOrganizationActionBatch(self.org_id, result['id'])
                    while not status['status']['completed'] or status['status']['failed']:
                        status = await sdk.organizations.getOrganizationActionBatch(self.org_id, result['id'])
                    print(
                        f"Action Batch ID: {result['id']} status Completed: :{status['status']['completed']} failed: {status['status']['failed']}")
                    if status['status']['failed']:
                        print(f'Failed Config')
                    else:
                        print(f'No Confiugration for Device')

    # validate_device_config_processor(self.org_id,device, sdk)
    # net_compare_task = [
    #		_config_tags(self.org_id,device,sdk)
    #		for device in model.meraki_nets[self.org_id].devices]
    #
    # await asyncio.gather(*net_compare_task)
