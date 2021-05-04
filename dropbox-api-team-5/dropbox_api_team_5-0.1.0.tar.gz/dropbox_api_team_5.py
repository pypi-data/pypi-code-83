import os.path
import shutil
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import click
import requests


@click.group()
def main():
    pass


@main.command()
@click.argument('link')
@click.option('--target_dir_path', default='downloaded_files')
@click.option('--target_file_name', default=None)
def download_file(link: str, target_dir_path: str, target_file_name: Optional[str] = None) -> None:
    """
    This function downloads a file from internet

    :param link: web link where file is stored
    :param target_dir_path: local path where a file from web will be downloaded.
                             If not provided, relative './downloaded_files' will be used.
    :param target_file_name: name of the file under which it will be saved locally.
                             If not provided, file name from link will be used.
    :return: None
    """

    target_file_name = target_file_name if target_file_name is not None else os.path.basename(urlparse(link).path)
    if target_file_name == '':
        raise ValueError('Target file name may not be empty')

    response = requests.get(link, stream=True)
    if response.status_code == 200:
        os.makedirs(target_dir_path, exist_ok=True)
        with open(Path(target_dir_path) / target_file_name, 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)
    else:
        raise IOError(f'Wrong status code {response.status_code}')


@main.command()
@click.argument('link')
def print_response(link: str):
    """
    This function prints content from provided link

    :param link: a link from which content will be printed
    :return: None
    """
    print(requests.get(link).text)


if __name__ == '__main__':
    main()
