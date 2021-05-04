import os

import dropbox

import click

from dropbox_api_team_4.func.check_api_token import check_api_token
from dropbox_api_team_4.func.download_file import download_file_from_internet, upload_file_v2
from dropbox_api_team_4.func.error_processing import error_processing


@click.group()
def main():
    pass


@main.command()
@click.argument("file")
@click.option("--destination_dir", default="/")
@click.option("--api_token", default=None)
@check_api_token
@error_processing
def upload_file(file: str, destination_dir: str, api_token: str) -> None:
    upload_file_v2(file, destination_dir, api_token)


@main.command()
@click.argument("link")
@click.option("--destination_dir", default="/")
@click.option("--api_token", default=None)
@error_processing
@check_api_token
def transfer_file(link: str, destination_dir: str, api_token: str) -> None:
    download_file_from_internet(link, destination_dir)
    file_name = os.path.basename(link)

    print(file_name)

    upload_file_v2(file_name, destination_dir, api_token)


@main.command()
@click.argument("old_path")
@click.argument("new_path")
@click.option("--api_token", default=None)
@error_processing
@check_api_token
def rename_file(old_path: str, new_path: str, api_token: str) -> None:
    dbx = dropbox.Dropbox(api_token)

    dbx.files_move_v2(from_path=old_path, to_path=new_path)


@main.command()
@click.argument("file")
@click.option("--api_token", default=None)
@error_processing
@check_api_token
def delete_file(file: str, api_token: str):
    dbx = dropbox.Dropbox(api_token)

    dbx.files_delete_v2(file)


@main.command()
@click.argument("file")
@click.option("--destination_dir", default="/")
@click.option("--api_token", default=None)
@error_processing
@check_api_token
def download_file(file: str, destination_dir: str, api_token: str) -> None:
    dbx = dropbox.Dropbox(api_token)

    with open(destination_dir, "wb") as f:
        metadata, res = dbx.files_download(file)
        f.write(res.content)


if __name__ == '__main__':
    main()
