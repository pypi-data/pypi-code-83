# Copyright (c) 2019-2021 Kevin Crouse
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @license: http://www.apache.org/licenses/LICENSE-2.0
# @author: Kevin Crouse (krcrouse@gmail.com)

import os, os.path
import datetime
import pickle
import re
import shutil

import warnings
from pprint import pprint

import googleapps
from googleapps.serviceclient import CommitType
from .driveitem import DriveItem
from .file import File

class Folder (DriveItem):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self._children = None

    @property
    def mime_type(self):
        return(googleapps.drive.MimeType.folder_mime_type())

    def process_request_json(self, json):
        if 'mimeType' in json and json['mimeType'] != self.mime_type:
            raise Exception("Processing Google Drive remote response for (alleged) folder " + str(json['id']) + ", Drive item is not reported as a folder but as type '" + json['mimeType']+ "'")
        del json['mimeType']
        return(super().process_request_json(json))

    @property
    def children(self):
        if self._children is None:
            self._children = googleapps.drive.find_all(in_folder=self, all_drives=self.in_shared_drive)
        return(self._children)

    def get_children(self, name=None, use_regexp=False, mime_type=None):
        files = []
        for child in self.children:
            if mime_type and child.mime_type != mime_type:
                continue
            if name:
                if use_regexp:
                    if re.search(name, child.name, re.I):
                        files.append(child)
                elif name == child.name:
                    files.append(child)
            else:
                files.append(child)
        return(files)

    def get_folder(self, *args, **kwargs):
        folders = self.get_folders(*args, **kwargs)
        if len(folders) == 0:
            return
        if len(folders) == 1:
            return(folders[0])

        raise Exception("Multiple folders match the following criteria: " + str(kwargs))

    def get_file(self, *args, **kwargs):
        files = self.get_files(*args, **kwargs)
        if len(files) == 0:
            return
        if len(files) == 1:
            return(files[0])

        raise Exception("Multiple files match criteria: " + str(kwargs))


    def get_files(self, *args, **kwargs):
        children= self.get_children(*args, **kwargs)
        files = []
        folder_mimetype = googleapps.drive.MimeType.folder_mime_type()
        for child in children:
            if child.mime_type == folder_mimetype:
                continue
            files.append(child)
        return(files)

    def get_folders(self, *args, **kwargs):
        return(self.get_children(*args, mime_type=googleapps.drive.MimeType.folder_mime_type(), **kwargs))


    def create_folder(self, name=None, **body):
        if 'mime_type' in body:
            raise Exception("Parameter mime_type not valid for create_folder()")

        if name:
            body['name'] = name

        body['parents'] = [self.id]

        item = Folder(**body)
        # only save if autocommit is on
        if item.commit_policy >= CommitType.auto_commit:
            item.save()
        # add it
        self.children.append(item)

        return(item)


    def upload_file(self, filepath, mime_type=None, convert=None, **parameters):
        if 'parents' in parameters:
            parameters['parents'].append(self.id)
        else:
            parameters['parents'] = [self.id]
        obj = File(**parameters)
        obj.upload(filepath, mime_type=mime_type, convert=convert)
        self.children.append(obj)
        return(obj)

    def upload(self, folderpath):
        # create the folder
        raise Exception ("Upload folder not implemented")

        # iterate
        #for root, dirs, files in os.scandir(folderpath):

            #for file in files:


    #-------- OLD -------------
    @classmethod
    def remove_by_id(self, id):
        raise Exception("Not implemented yet")

    @classmethod
    def remove_by_id(self, id):
        raise Exception("Not implemented yet")

    def make_path(self, path):
        raise Exception("Not implemented yet")

    def remove(self, if_empty=False):
        raise Exception("Not implemented yet")
#    def rmtree(self):
#        raise Exception("Not implemented yet")

    def copy(self):
        raise Exception("Not implemented yet")

    def download(self):
        raise Exception("Not implemented yet")

    def make_archive(self, output_name, format='zip'):
        # formats: tar gztar bztar xztar
        raise Exception("Not implemented yet")

    def scan(self, files_only=None, folders_only=None):
        if files_only:
            is_folder = False
        elif folders_only:
            is_folder = True
        else:
            is_folder = None
        return(googleapps.drive.find(self.service, in_folder=self.id, is_folder=is_folder, all_drives=self.in_shared_drive,))

    def list(self, *args, result_type='name', **kwargs):
        # just shorthand to call scanfolder
        # returns a list of folder names
        folders = self.scanfolder(*args, **kwargs)
        result = []
        for item in folders:
            if result_type == 'name':
                result.append(item.name)
            elif result_type == 'id':
                result.append(item.id)
            else:
                raise Exception("google.drive.listfolder called with unknown result type " + str(result_type))
        return(result)

    def walk(self):
        raise Exception("Not thoroughly investigated.")

        q = "'" + str(self.id) + "' in parents"
        if not include_trash:
            q += " and trashed=false"

        if filters:
            if type(filters) is not list:
                filters = [ filters ]

            for ftr in filters:
                if ftr == 'folders':
                    q += " and mimeType='application/vnd.google-apps.folder'"
                elif ftr == 'files':
                    q += " and mimeType='application/vnd.google-apps.folder'"
                elif ftr == 'spreadsheets':
                    q += " and mimeType='application/vnd.google-apps.spreadsheet'"
                else:
                    raise Exception("Unknown filter requested, type" + str(ftr))

        result = []
        for item in self.get_service('drive').files().list(
                    q=q,
                    fields="nextPageToken, files(id, name, parents, trashed)",
            ).execute().get('files'):

            result.append(DriveItem(item['id'], name=item['name']))

        return(result)
