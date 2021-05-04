import os
import shutil
from urllib.parse import urlparse
import dropbox

import requests


def download_file_from_internet(link: str, destination_dir: str):
    destination_dir = destination_dir \
        if destination_dir is not None \
        else os.path.basename(urlparse(link).path)
    if destination_dir == '':
        raise ValueError('Target file name may not be empty')

    response = requests.get(link, stream=True)
    if response.status_code == 200:
        file_name = os.path.basename(link)

        full_path = os.path.join('.', file_name)

        with open(full_path, 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)
    else:
        raise IOError(f'Wrong status code {response.status_code}')


def upload_file_v2(file: str, destination_dir: str, api_token: str) -> None:
    dbx = dropbox.Dropbox(api_token)

    full_path = destination_dir + os.path.basename(file)

    with open(file, "rb") as f:
        dbx.files_upload(f.read(), full_path) # mode=dropbox.files.WriteMode.overwrite
    return
