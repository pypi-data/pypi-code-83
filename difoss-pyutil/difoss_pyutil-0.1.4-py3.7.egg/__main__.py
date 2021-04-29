#!env python3
# -*- coding:utf-8 -*-
# author: difosschan
#
__all__ = ('dir_diff', 'main')

from . import *

from os.path import join as path_join
import os
import click
from typing import *
import time
import tarfile
import shutil

CWD=os.getcwd()
EXCLUDE_DIRS=['.git', '.idea', '__pycache__', 'build', 'eggs', '.eggs', 'wheels', 'vendor', 'phpmyadmin']
EXCLUDE_FILES: List[str]=[]
EXCLUDE_EXTENSIONS: List[str]=[]
INCLUDE_EXTENSIONS: List[str]=['.php']

def G(key: str, default=None) -> Any:
    '''
    get globals by <key>
    :param key: key of globals, usually in uppercase
    '''
    return globals().get(key, default)


def dir_diff(old_dir: str, new_dir: str):

    diff_rel_files = []

    _, old_rel_files = walk(old_dir, without_root_path=True, exclude_dirs=G('EXCLUDE_DIRS'),
                        exclude_files=G('EXCLUDE_FILES'), include_extensions=G('INCLUDE_EXTENSIONS'))
    _, new_rel_files = walk(new_dir,  without_root_path=True, exclude_dirs=G('EXCLUDE_DIRS'),
                        exclude_files=G('EXCLUDE_FILES'), include_extensions=G('INCLUDE_EXTENSIONS'))

    addeds = list(set(new_rel_files).difference(set(old_rel_files)))
    deleteds = list(set(old_rel_files).difference(set(new_rel_files)))

    P('Directory compare result:', addeds=addeds, deleteds=deleteds, _indent=2)

    for x in new_rel_files:
        if is_different(x, old_dir, new_dir):
            diff_rel_files.append(x)
            P("Detect difference", file=x, _level='info')

    return diff_rel_files


def is_different(f, d1, d2) -> bool:
    f1 = path_join(d1, f)
    f2 = path_join(d2, f)
    st1 = dump(f1)
    st2 = dump(f2)
    if st1.get('size', 0) != st2.get('size', 0):
        return True

    with open(f1, 'r') as file1:
        with open(f2, 'r') as file2:
            diff = set(file1).difference(file2)
    return True if diff else False

def dump(f: str) -> Dict:
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = os.stat(f)
    return dict(mode=mode, ino=ino, dev=dev, nlink=nlink, uid=uid, gid=gid, size=size,
                atime=atime, mtime=mtime, ctime=ctime)

# --------------------------------------------------------------------------------
def set_global(ctx, param, value):
    name=param.human_readable_name
    globalVarName = str(name).upper()
    globals()[globalVarName]=value
    return value

def set_debug(ctx, param, value):
    set_printable(value)
    set_global(ctx, param, value)
    return value

@click.command()
@click.option('-d', '--debug', help='print debug info', is_flag=True, callback=set_debug)
@click.argument('old_dir')
@click.argument('new_dir')
def cmd_diff(debug: bool,
             old_dir: str,
             new_dir: str):
    diff_rel_files = dir_diff(old_dir, new_dir)
    P(f'Compared with the old directory <{old_dir}>,'
      f' the new directory <{new_dir}> changes files as follows.',
      files=diff_rel_files,
      _must=True, _indent=2, _level='info')


@click.command()
@click.option('-d', '--debug', help='print debug info', is_flag=True, callback=set_debug)
@click.option('-t', '--time-style',
              type=click.Choice(['local', 'utc']),
              default='local',
              help='choose which style of time in archive filename')
@click.option('-k', '--keep-dir', type=click.STRING,
              help='directory which includes the files wanna keep')
@click.option('-w', '--who', help='author name')
@click.argument('old_dir')
@click.argument('new_dir')
def cmd_tar(debug: bool,
            time_style: str,
            keep_dir: str,
            who: str,
            old_dir: str,
            new_dir: str):
    '''Compare two directory, and tar. (keep files in <--keep-dir> if you want)'''
    files = dir_diff(old_dir, new_dir)

    keep_suffix = '.keep'
    keep_suffix_len = len(keep_suffix)

    keep_files = []
    if keep_dir:
        _, keep_files = walk(keep_dir, without_root_path=True, include_extensions=[keep_suffix,])

    for kf in keep_files:
        keep_origin_fn = kf[:-keep_suffix_len]
        file2keep = path_join(new_dir, keep_origin_fn)
        if os.path.exists(file2keep):
            # backup modified file.
            shutil.move(file2keep, path_join(keep_dir, keep_origin_fn))
            # copy file from keep-dir into new-dir, also rename it.
            shutil.copy(path_join(keep_dir, kf), path_join(new_dir, keep_origin_fn))

    # Create archive filename
    archive_info = [new_dir, ]
    if time_style == 'local':
        archive_info.append(time.strftime('%Y-%m-%d-%H%M%S', time.localtime()))
    elif  time_style == 'utc':
        archive_info.append(time.strftime('%Y-%m-%d-%H%M%S', time.gmtime()))
    if who:
        archive_info.append(f'by{who}')
    archive_fn = '_'.join(archive_info) + '.tar.gz'

    with tarfile.open(archive_fn, 'w:gz') as tar:
        # Add files into archive
        for x in files:
            tar.add(path_join(new_dir, x), arcname=x)
        tar.close()
    P('archive file done.', filename=archive_fn, _level='info', _must=True)

    # move back from keep-dir
    revert_files = []
    for kf in keep_files:
        keep_origin_fn = kf[:-keep_suffix_len]
        file2keep = path_join(keep_dir, keep_origin_fn)
        if os.path.exists(file2keep):
            shutil.move(file2keep, path_join(new_dir, keep_origin_fn))
            revert_files.append(keep_origin_fn)
    if revert_files:
        P('Revert files in keep-dir back to new-dir', file=revert_files, _level='info', _indent=2, _must=True)

@click.group()
def main():
    pass

main.add_command(cmd_diff, name='diff')
main.add_command(cmd_tar, name='tar')

if __name__ == '__main__':
    main()