import aiohttp
import asyncio
from enum import Enum

from aiohttp import BasicAuth

from .lock import GlueHomeLock

_base_url = 'https://user-api.gluehome.com/v1'
_user_agent = 'pygluehome/0.0.1'


class GlueHomeLockOperationStatus(Enum):
    pending = 'pending'
    completed = 'completed'
    timeout = 'timeout'
    failed = 'failed'


class GlueHomeLockOperation(Enum):
    lock = 'lock'
    unlock = 'unlock'


class GlueHomeApi:
    def __init__(self, session, api_key):
        """
        :type session: aiohttp.ClientSession
        """
        self.session = session
        self._headers = {'User-Agent': _user_agent, 'Authorization': f"Api-Key {api_key}"}

    async def all_locks(self):
        async with self.session.get(f'{_base_url}/locks', headers=self._headers) as r:
            r.raise_for_status()
            for lock_data in await r.json():
                yield GlueHomeLock(self, lock_data['id'], lock_data)

    async def lock(self, lock_id):
        lock_data = await self._lock_data(lock_id)
        return GlueHomeLock(self, lock_data['id'], lock_data)

    async def _lock_data(self, lock_id):
        async with self.session.get(f'{_base_url}/locks/{lock_id}', headers=self._headers) as r:
            r.raise_for_status()
            return await r.json()

    async def _perform_operation(self, lock_id, operation):
        """
        :type operation: GlueHomeLockOperation
        """
        async with self.session.post(f'{_base_url}/locks/{lock_id}/operations', headers=self._headers, json={
            'type': operation.value
        }) as r:
            r.raise_for_status()
            operation_id = (await r.json())['id']

            status = GlueHomeLockOperationStatus.pending
            tries = 0
            while status == GlueHomeLockOperationStatus.pending:
                await asyncio.sleep(1)
                status = await self._check_operation(lock_id, operation_id)
                tries = tries + 1
                if (tries >= 20 and status == GlueHomeLockOperationStatus.pending):
                    status = GlueHomeLockOperationStatus.timeout

            return status

    async def _lock_lock(self, lock_id):
        status = await self._perform_operation(lock_id, GlueHomeLockOperation.lock)

        if status == GlueHomeLockOperationStatus.failed:
            raise Exception("Locking failed")

        if status == GlueHomeLockOperationStatus.timeout:
            raise Exception("Locking timed out")

        return

    async def _unlock_lock(self, lock_id):
        status = await self._perform_operation(lock_id, GlueHomeLockOperation.unlock)

        if status == GlueHomeLockOperationStatus.failed:
            raise Exception("Unlocking failed")

        if status == GlueHomeLockOperationStatus.timeout:
            raise Exception("Unlocking timed out")

        return

    async def _check_operation(self, lock_id, operation_id):
        async with self.session.get(f'{_base_url}/locks/{lock_id}/operations/{operation_id}', headers=self._headers) as r:
            r.raise_for_status()
            return GlueHomeLockOperationStatus((await r.json())['status'])


async def issue_api_key(session, username, password):
    """
    :type session: aiohttp.ClientSession
    """
    headers = {'User-Agent': _user_agent, 'Content-Type': 'application/json'}
    async with session.post(f'{_base_url}/api-keys', auth=BasicAuth(username, password), headers=headers, json={
        'name': 'pygluelock',
        'scopes': ['locks.write', 'locks.read', 'events.read'],
    }) as r:
        return (await r.json())['apiKey']