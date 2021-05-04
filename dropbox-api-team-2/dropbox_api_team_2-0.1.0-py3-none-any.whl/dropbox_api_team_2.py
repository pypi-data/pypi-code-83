from os import environ
import os.path
import shutil
from pathlib import Path
from typing import Optional
import dropbox
import click
import requests

os.environ['DROPBOX_API_TOKEN'] = 'Iw4qX20FVv8AAAAAAAAAASc9awUiHNciUe4n4Z4lF4kdkAV91No0DhnYHCMtlQoC'
access_token = os.environ['DROPBOX_API_TOKEN']


@click.group()
def main():
    pass


@main.command()
@click.argument('file_name')
@click.option('--destination_dir', default='/')
@click.option('--api_token', default=access_token)
def upload_file(file_name: Optional[str], destination_dir: str, api_token: str):
    dbx = dropbox.Dropbox(api_token)
    with open(file_name, 'rb') as f:
        dbx.files_upload(f.read(), Path(destination_dir) / file_name)


@main.command()
@click.argument('link_to_file')
@click.option('--destination_dir', default='/')
@click.option('--api_token', default=access_token)
def transfer_file(link_to_file: str, destination_dir: Optional[str], api_token: str):
    dbx = dropbox.Dropbox(api_token)
    file_name = link_to_file.split('/')[-1]
    data_to_write = requests.get(link_to_file).content
    dbx.files_upload(data_to_write, Path(destination_dir) / file_name)


@main.command()
@click.argument('cur_name')
@click.argument('new_name')
@click.option('--api_token', default=access_token)
def rename_file(cur_name: str, new_name: str, api_token: str):
    dbx = dropbox.Dropbox(api_token)
    dbx.files_move_v2('/' + cur_name, '/' + new_name)


@main.command()
@click.argument('file_name')
@click.option('--api_token', default=access_token)
def delete_file(file_name: Optional[str], api_token: str):
    dbx = dropbox.Dropbox(api_token)
    if file_name == '':
        raise ValueError('Target file name may not be empty')
    dbx.files_delete('/' + file_name)


@main.command()
@click.argument('file_name')
@click.option('--destination_dir', default='downloaded_files')
@click.option('--api_token', default=access_token)
def download_file(file_name: str, destination_dir: str, api_token: str):
    dbx = dropbox.Dropbox(api_token)
    os.makedirs(destination_dir, exist_ok=True)
    # print(file_name)
    cur_file, res = dbx.files_download(file_name)
    with open(Path(destination_dir) / file_name.split('/')[-1], 'wb') as f:
        f.write(res.content)


if __name__ == '__main__':
    main()
