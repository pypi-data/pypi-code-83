
"""# `concurrent.futures` Executor
"""
import asyncio
import asyncio.futures
import weakref
from concurrent import futures
from .executor import AsyncExecutor
from .futures import chain_future_exception, chain_future_handle, create_future

class ConcurrentFuturesExecutor(AsyncExecutor):

    def __init__(self, executor: futures.Executor):
        self._executor = executor

    def __enter__(self):
        self._executor.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._executor.__exit__(exc_type, exc_val, exc_tb)
        return

    def _apply(self, func, /, *args, **kwargs) -> asyncio.Future:
        aio_cf_future = create_future()
        task = asyncio.create_task(self._apply_async(func, aio_cf_future, *args, **kwargs))
        chain_future_exception(task, aio_cf_future)
        return aio_cf_future

    async def _apply_async(self, func, aio_cf_fut: asyncio.Future, /, *args, **kwargs):
        (args, kwargs) = (await self._process_args(args, kwargs))
        cf_fut = self._executor.submit(func, *args, **kwargs)
        asyncio.futures._chain_future(cf_fut, aio_cf_fut)

    async def _process_args(self, args, kwargs):
        args = [(await self._unwrap_and_wait_maybe(x)) for x in args]
        kwargs = {k: (await self._unwrap_and_wait_maybe(v)) for (k, v) in kwargs.items()}
        return (args, kwargs)

    async def _unwrap_and_wait_maybe(self, obj):
        try:
            self._unwrap_handle(obj)
        except ValueError:
            return obj
        return (await self.retrieve(obj))

    def _register_handle(self, handle, future):
        chain_future_handle(future, handle)
