
"""# Executor
"""
import asyncio
from typing import List
from .futures import create_future

class Executor():

    def _apply(self, func, /, *args, **kwargs):
        raise NotImplementedError

    def _register_handle(self, handle: asyncio.Future, future):
        raise NotImplementedError

    def _unwrap_handle(self, handle: asyncio.Future):
        try:
            return handle.__resource
        except AttributeError as err:
            raise ValueError('object is not a handle') from err

    def _wrap_resource(self, resource) -> asyncio.Future:
        handle = create_future()
        handle.__resource = resource
        self._register_handle(handle, resource)
        return handle

    def map(self, func, /, *iterables) -> List[asyncio.Future]:
        return [self.submit(func, *args) for args in zip(*iterables)]

    async def retrieve(self, handle: asyncio.Future):
        raise NotImplementedError

    def submit(self, func, /, *args, **kwargs) -> asyncio.Future:
        return self._wrap_resource(self._apply(func, *args, **kwargs))

class AsyncExecutor(Executor):

    async def retrieve(self, handle: asyncio.Future):
        return (await self._unwrap_handle(handle))
