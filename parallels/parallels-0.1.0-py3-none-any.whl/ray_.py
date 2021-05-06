
"""# `ray` Executor
"""
import asyncio
import weakref
import ray
import ray.exceptions
from .executor import AsyncExecutor

class RayExecutor(AsyncExecutor):
    pass

    def _apply(self, func, /, *args, **kwargs) -> asyncio.Future:
        (args, kwargs) = self._process_args(args, kwargs)
        return _ray_call.remote(func, *args, **kwargs)

    def _process_args(self, args, kwargs):
        args = [self._unwrap_maybe(x) for x in args]
        kwargs = {k: self._unwrap_maybe(v) for (k, v) in kwargs.items()}
        return (args, kwargs)

    def _unwrap_maybe(self, obj):
        try:
            return self._unwrap_handle(obj)
        except ValueError:
            return obj

    def _register_handle(self, handle: asyncio.Future, ref: ray.ObjectRef):

        def on_ref_completed_threadsafe(result, handle_ref=weakref.ref(handle)):
            if (not (handle := handle_ref())):
                return
            if handle.cancelled():
                return
            if isinstance(result, ray.exceptions.RayTaskError):
                handle.set_exception(result.as_instanceof_cause())
            elif isinstance(result, ray.exceptions.RayError):
                handle.set_exception(result)
            else:
                handle.set_result(True)
        loop = asyncio.get_running_loop()

        @ref._on_completed
        def on_ref_completed(result):
            loop.call_soon_threadsafe(on_ref_completed_threadsafe, result)

        @handle.add_done_callback
        def on_fut_done(fut):
            if fut.cancelled():
                ray.cancel(ref)

    async def retrieve(self, handle: asyncio.Future):
        return (await self._unwrap_handle(handle))

@ray.remote
def _ray_call(func, *args, **kwargs):
    return func(*args, **kwargs)
