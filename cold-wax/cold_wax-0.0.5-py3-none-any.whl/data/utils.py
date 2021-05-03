import requests
from os import path, makedirs, unlink


def download_from_google_drive(gdrive_file_id, dest_path, overwrite=False) -> bool:
    URL = "https://drive.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params={'id':gdrive_file_id}, stream=True)
    token = get_confirm_token(response)
    if token:
        params = {'id':gdrive_file_id, 'confirm':token}
        response = session.get(URL, params=params, stream=True)
    else:
        return False
    return save_response_content(response, dest_path, overwrite)    


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None


def save_response_content(response, dest_path, overwrite=False):
    if path.isdir(dest_path):
        return False
    if path.exists(dest_path) and not overwrite:
        return False

    if path.exists(dest_path):
        unlink(dest_path)
    else:
        if not path.exists(path.dirname(dest_path)):
            makedirs(path.dirname(dest_path))

    chunks = 32768
    with open(dest_path, "wb") as f:
        for chunk in response.iter_content(chunks):
            if chunk:
                f.write(chunk)
    return True

