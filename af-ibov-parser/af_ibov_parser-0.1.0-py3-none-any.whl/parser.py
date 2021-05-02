'''
This module contains all parser utilities responsible for
parsing ibov archives.
'''


import os
import errno
from typing import Dict, List, Optional

from .record import Record
from .errors import AFError


def parse_archive(src: str, dest: str,
                  results: Optional[Dict[str, int]]) -> None:
    '''
    Parses records of an archive and stores it in the filesystem
    in a json string format.
    '''
    archive_name = src.split('/')[-1]
    if results is not None and archive_name not in results:
        results[archive_name] = 0
    try:
        os.makedirs(f'{dest}/{archive_name}', exist_ok=True)
    except OSError as e:
        raise AFError(e.strerror, code=e.errno)
    if not os.path.exists(src):
        raise AFError('File not found: {src}', code=errno.ENOENT)
    with open(src, 'r') as f:
        f.readline()
        while True:
            line = f.readline()
            if not line:
                break
            if line.startswith('99COTA'):
                continue
            record = Record.from_str(line.rstrip('\n'))
            record_path = f'{dest}/{archive_name}/{record.as_hash()}.json'
            if os.path.exists(record_path):
                continue
            try:
                with open(record_path, 'w+') as f1:
                    f1.write(record.as_json())
            except OSError as e:
                raise AFError(e.strerror, code=e.errno)
            if results is not None:
                results[archive_name] += 1
                # results[archive_name].append(f'{record_path}')
