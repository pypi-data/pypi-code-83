
"""# `dask.distributed` Executor
"""
import asyncio
import enum
import weakref
from dask import distributed
from .executor import AsyncExecutor

class DaskStatus(str, enum.Enum):
    FINISHED = 'finished'
    CANCELLED = 'cancelled'
    LOST = 'lost'
    PENDING = 'pending'
    ERROR = 'error'

class DaskExecutor(AsyncExecutor):

    def __init__(self, client: distributed.Client):
        assert client.asynchronous
        self._client = client

    def _apply(self, func, /, *args, **kwargs) -> asyncio.Future:
        (args, kwargs) = self._process_args(args, kwargs)
        return self._client.submit(func, *args, **kwargs)

    def _process_args(self, args, kwargs):
        args = [self._unwrap_maybe(x) for x in args]
        kwargs = {k: self._unwrap_maybe(v) for (k, v) in kwargs.items()}
        return (args, kwargs)

    def _unwrap_maybe(self, obj):
        try:
            return self._unwrap_handle(obj)
        except ValueError:
            return obj

    def _register_handle(self, handle: asyncio.Future, dask_fut: distributed.Future):

        @handle.add_done_callback
        def on_fut_done(fut, dask_fut_ref=weakref.ref(dask_fut)):
            if ((dask_fut := dask_fut_ref()) and fut.cancelled()):
                asyncio.create_task(dask_fut.cancel(force=True))

        @dask_fut.add_done_callback
        def on_dask_fut_done(dask_fut, fut_ref=weakref.ref(handle)):
            fut = fut_ref()
            if ((not fut) or fut.cancelled()):
                return
            if (dask_fut.status == DaskStatus.FINISHED):
                fut.set_result(True)
            elif (dask_fut.status == DaskStatus.CANCELLED):
                fut.cancel()
            else:
                try:
                    (typ, exc, tb) = dask_fut.result()
                    raise exc.with_traceback(tb)
                except BaseException as err:
                    fut.set_exception(err)
