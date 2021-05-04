import os
from os import listdir
from os.path import isfile, join
import dropbox
import requests
import pathlib
from dotenv import load_dotenv
from dropbox.dropbox_client import BadInputException


def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except BadInputException:
            return

        except Exception as e:
            print(e)
    return wrapper


class Box:

    def __init__(self, api_key):
        self.dbx = dropbox.Dropbox(api_key)

    @error_handler
    def rename_file(self, drop_box_old_file_path, new_name):
        new_path = drop_box_old_file_path.split('/')
        new_path = new_path[:-1]
        new_path = '/'.join([str(n) for n in new_path])
        self.dbx.files_move_v2(drop_box_old_file_path, f'{new_path}/{new_name}')

    @error_handler
    def create_folder(self, folder_path):
        response = self.dbx.files_list_folder(path='')
        for i in response.entries:
            if type(i) == dropbox.files.FolderMetadata:
                if i.path_display == folder_path:
                    return
        self.dbx.files_create_folder(folder_path)

    @error_handler
    def __one_file_upload(self, path, path_in_dropbox):
        with open(path, 'rb') as file:
            file = file.read()
            self.dbx.files_upload(file, f'{path_in_dropbox}/{os.path.basename(path)}')

    @error_handler
    def upload_files(self, path_to_files, path_in_dropbox):

        if not path_in_dropbox:
            path_in_dropbox = '/standard_folder'

        self.create_folder(path_in_dropbox)

        if os.path.isfile(path_to_files):
            self.__one_file_upload(path_to_files, path_in_dropbox)
        else:
            files = [f for f in listdir(path_to_files) if isfile(join(path_to_files, f))]
            for i in files:
                self.__one_file_upload(f'{path_to_files}/{i}', path_in_dropbox)

    @error_handler
    def transfer_file(self, link_to_file, path_in_dropbox):

        if not path_in_dropbox:
            path_in_dropbox = '/standard_folder'

        file = requests.get(link_to_file)
        filename = os.path.basename(link_to_file)

        with open(filename, mode='wb+') as f:
            f.write(file.content)

        abs_path = pathlib.Path().absolute() / filename
        self.upload_files(abs_path, path_in_dropbox)

        os.remove(abs_path)

    @error_handler
    def delete_file(self, path_in_dropbox):
        self.dbx.files_delete_v2(path_in_dropbox)

    @error_handler
    def download_default(self, path_in_dropbox, dir_to_save):
        if not dir_to_save:
            dir_to_save = './'
        try:
            os.mkdir(dir_to_save)
        except FileExistsError:
            pass

        name_of_file = os.path.basename(path_in_dropbox)
        path_to_save = os.path.join(dir_to_save, name_of_file)

        with open(path_to_save, "wb") as f:
            metadata, res = self.dbx.files_download(path=f'{path_in_dropbox}')
            f.write(res.content)

    @error_handler
    def change_token(self, api_token):
        self.__init__(api_token)


dotenv_path = './.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

token = str(os.getenv('token'))
box = Box(token)
