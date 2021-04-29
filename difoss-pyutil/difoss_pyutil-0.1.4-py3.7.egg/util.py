#!python3
# -*- coding:utf-8 -*-
# author: difosschan
#
__all__ = (
    'run_shell',
    'get_file_info',
    'using'
)

import os
from typing import *

## Improved from <https://github.com/difosschan/difoss-pybase.git>
from subprocess import Popen, PIPE
import platform
# @return return_code, stdout, stderr
def run_shell(cmd, cwd=None, callback_after_run: Callable[[str, str, int, str, str], Any]=None) -> Tuple[int, str, str]:
    close_fds = not (platform.system() == 'Windows') # WTF: close_fds=True NOT supported on windows.

    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, close_fds=close_fds, cwd=cwd)

    p.wait()
    stdout, stderr = p.communicate()

    stdout = str(stdout, 'utf-8').rstrip('\n')
    stderr = str(stderr, 'utf-8').rstrip('\n')

    code = p.returncode

    if callback_after_run:
        callback_after_run(cmd, cwd, code, stdout, stderr)

    return (code, stdout, stderr)

def get_file_info(fullname):
    (file_path, temp_filename) = os.path.split(fullname)
    (short_name, extension) = os.path.splitext(temp_filename)
    return {'short_name': short_name, 'extension': extension, 'path': file_path}


try:
    import resource
    def using():
        usage = resource.getrusage(resource.RUSAGE_SELF)
        return {
            'user_time': usage[0],
            'sys_time': usage[1],
            'mem(mb)': usage[2] / 1024.0,
        }
except:
    def using():
        return {}

