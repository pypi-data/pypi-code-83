'''
This module contains the handle functions used by the CLI subcommands.
'''


import os
import json
import asyncio
from typing import Dict, Optional, List

from .version import VERSION
from .parser import parse_archive
from .task import TaskManager


def version(output: str = 'text') -> str:
    '''
    Handler for the `version` subcommand.

    It jus shows the CLI version.
    '''
    if output == 'text':
        return VERSION

    return json.dumps({'version': VERSION}, indent=4)


def parse(src: str = '', dest: str = '',
          workers: Optional[int] = None,
          output: str = 'text') -> str:
    '''
    Parses archives stored in `src` and write
    parsed records in `dest`.

    It will create a folder per archive in `dest`.
    '''
    results: Dict[str, int] = {}
    loop = asyncio.get_event_loop()
    manager = TaskManager()

    data = []
    if os.path.isdir(src):
        for fname in os.listdir(src):
            data.append(f'{src}/{fname}')
    if os.path.isfile(src):
        data.append(src)
    loop.run_until_complete(manager(data,
                            parse_archive,
                            dest,
                            results,
                            workers=workers))

    if output == 'json':
        return json.dumps({
            'files': results
        }, indent=4)

    parts: List[str] = []
    for k, v in results.items():
        parts.append(f'{k}:{v}')
        parts.append('\n')

    return ''.join(parts)
