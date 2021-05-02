'''
This module contains classes and functions to deal
with tasks in a ThreadPoolExecutor.
'''

import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, Optional, List


class TaskManager:
    '''
    Task manager class.

    This class produces a callable instance to run
    functions in a ThreadPoolExecutor.
    '''

    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

    def __init__(self,
                 loop: Optional[asyncio.AbstractEventLoop] = None) -> None:
        '''
        Creates a new TaskManage instance.

        It will use `asyncio.get_event_loop()` if no loop is provided.
        '''
        if loop is not None:
            self.loop = loop

    async def __call__(self,
                       data: List[Any],
                       cb: Callable[..., None],
                       *args: Any,
                       workers: Optional[int] = None) -> None:
        '''
        Async call runs `cb` per `data` (List of whatever) item
        in a poll in a pool.

        It will spawn a worker per item in the dataset
        if `workers` is not provided.

        `*args` will be forwarded as `cb` parameters.
        '''
        if workers is None:
            workers = len(data)
        with ThreadPoolExecutor(max_workers=workers) as executor:
            for item in data:
                self.loop.run_in_executor(
                    executor,
                    cb,
                    item,
                    *args
                )
