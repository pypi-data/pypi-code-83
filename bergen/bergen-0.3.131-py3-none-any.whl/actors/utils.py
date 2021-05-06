import asyncio
from bergen.debugging import DebugLevel
from bergen.handlers import AssignHandler, ReserveHandler, ProvideHandler
import contextvars

loop_context = contextvars.ContextVar("loop_context", default=None)
assign_handler_context  = contextvars.ContextVar('assign_handler', default=None)
reserve_handler_context = contextvars.ContextVar("reserve_handler", default=None)
provide_handler_context = contextvars.ContextVar("provide_handler", default=None)


async def log_async(message, level: DebugLevel = DebugLevel.INFO):
    handler: AssignHandler = assign_handler_context.get()
    await handler.log(message, level)



def log(message, level: DebugLevel = DebugLevel.INFO):
    try:
        event_loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = loop_context.get()
        loop.create_task(log_async(message, level))
    else:
        if event_loop.is_running():
            return log_async(message, level=level)