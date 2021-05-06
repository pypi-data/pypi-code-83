
''
import asyncio
import weakref

def create_future() -> asyncio.Future:
    """Create a future for the running loop
    
    :returns: new future
    """
    loop = asyncio.get_running_loop()
    return loop.create_future()

class FutureChain():
    'Helper class to chain asyncio futures'

    def on_destination_cancelled(self, source, destination):
        source.cancel()

    def on_source_cancelled(self, source, destination):
        destination.cancel()

    def on_source_exception(self, source, destination):
        destination.set_exception(source.exception())

    def on_source_result(self, source, destination):
        destination.set_result(source.result())

    def __call__(self, source, destination):
        assert isinstance(source, asyncio.Future)
        assert isinstance(destination, asyncio.Future)

        @destination.add_done_callback
        def on_destination_done(destination, source_ref=weakref.ref(source)):
            if ((source := source_ref()) and destination.cancelled()):
                self.on_destination_cancelled(source, destination)

        @source.add_done_callback
        def on_source_done(source, destination_ref=weakref.ref(destination)):
            destination = destination_ref()
            if ((not destination) or destination.cancelled()):
                return
            if source.cancelled():
                self.on_source_cancelled(source, destination)
            elif (source.exception() is not None):
                self.on_source_exception(source, destination)
            else:
                self.on_source_result(source, destination)
chain_future = FutureChain()

class _FutureChainException(FutureChain):

    def on_source_result(self, source, destination):
        return
chain_future_exception = _FutureChainException()

class _FutureChainHandle(FutureChain):

    def on_source_result(self, source, destination):
        destination.set_result(True)
chain_future_handle = _FutureChainHandle()
