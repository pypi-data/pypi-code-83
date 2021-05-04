from dropbox_api_team_3.box import box
from typing import Optional
import click
from functools import wraps
import os


@click.group()
def main():
    pass


def change_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'api_token' in kwargs.keys():
            api_token = kwargs['api_token']
            box.change_token(api_token=api_token)

        elif args[-1] is not None:
            api_token = args[-1]
            box.change_token(api_token=api_token)

        elif os.getenv('token') is not None:
            api_token = os.getenv('token')
            box.change_token(api_token=api_token)

        return func(*args, **kwargs)

    return wrapper


@main.command()
@click.argument('path_to_files')
@click.option('--destination_dir', default=None)
@click.option('--api_token', default=None)
@change_token
def upload_file(path_to_files: str, destination_dir: Optional[str] = None, api_token: Optional[str] = None) -> None:
    box.upload_files(path_to_files=path_to_files,
                     path_in_dropbox=destination_dir)


@main.command()
@click.argument('link_to_files')
@click.option('--destination_dir', default=None)
@click.option('--api_token', default=None)
@change_token
def transfer_file(link_to_files: str, destination_dir: Optional[str] = None, api_token: Optional[str] = None) -> None:
    box.transfer_file(link_to_file=link_to_files,
                      path_in_dropbox=destination_dir)


@main.command()
@click.argument('drop_box_old_file_path')
@click.argument('drop_box_new_file_path')
@click.option('--api_token', default=None)
@change_token
def rename_file(drop_box_old_file_path: str, drop_box_new_file_path: str, api_token: Optional[str] = None) -> None:
    box.rename_file(drop_box_old_file_path=drop_box_old_file_path,
                    new_name=drop_box_new_file_path)


@main.command()
@click.argument('file_path')
@click.option('--api_token', default=None)
@change_token
def delete_file(file_path: str, api_token: Optional[str] = None) -> None:
    box.delete_file(path_in_dropbox=file_path)


@main.command()
@click.argument('file_path')
@click.option('--destination_dir', default=None)
@click.option('--api_token', default=None)
@change_token
def download_file(file_path: str, destination_dir: Optional[str] = None, api_token: Optional[str] = None) -> None:
    box.download_default(path_in_dropbox=file_path,
                         dir_to_save=destination_dir)
