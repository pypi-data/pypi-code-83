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

import googleapps
from .driveitem import DriveItem
from .file import File
from .folder import Folder

import googleapiclient

import os, os.path
import datetime
import pickle
import re
import shutil

import warnings
from pprint import pprint


file_type_mimetype = {
    'file': 'application/vnd.google-apps.file',
    'folder': 'application/vnd.google-apps.folder',

    'document': 'application/vnd.google-apps.document',
    'drawing': 'application/vnd.google-apps.drawing',
    'form': 'application/vnd.google-apps.form',
    'presentation': 'application/vnd.google-apps.presentation',
    'spreadsheet': 'application/vnd.google-apps.spreadsheet',

    'audio': 'application/vnd.google-apps.audio',
    'video': 'application/vnd.google-apps.video',
    'photo': 'application/vnd.google-apps.photo',
    
    'map': 'application/vnd.google-apps.map',
    'script': 'application/vnd.google-apps.script',
    'site': 'application/vnd.google-apps.site',
    'fusiontable': 'application/vnd.google-apps.fusiontable',

    #'application/vnd.google-apps.drive-sdk': ['file', ],
    #    'application/vnd.google-apps.unknown': ['file', ],


    'zip':'application/zip',
    
    'pdf':'application/pdf',
    'epub':'application/epub+zip',
    'svg':'image/svg+xml',
    'png':'image/png',
    
    'html':'text/html',
    'txt':'text/plain',
    'text':'text/plain',
    'csv':'text/csv',
    'tsv':'text/tab-separated-values',

    'rtf':'application/rtf',
    
    'docx':'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'xlsx':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'pptx':'application/vnd.openxmlformats-officedocument.presentationml.presentation',

    'odt':'application/vnd.oasis.opendocument.text',
    'ods':'application/x-vnd.oasis.opendocument.spreadsheet',
    'odg':'image/jpeg',
    'odp':'application/vnd.oasis.opendocument.presentation',
    'script':'application/vnd.google-apps.script+json',
}

doctype_search = (
    [('doc','docx','odt','rtf'), 'document'],
    [('xls','xlsx','ods','csv','tsv'),'spreadsheet'],
    [('pptx','ppt','odp'), 'presentation'],
    [('odg'),'drawing'],
)

def is_document(extension):
    for doctype in doctype_search:
        if extension in doctype[0]:
            return(doctype[1])
    return

def translate_filetype(file_type):
    if file_type in file_type_mimetype:
        return(file_type_mimetype[file_type])
    return

_mimetype_isa = {}
def mimetype_isa(mime_type):
    if not _mimetype_isa:
        for drivetype, mimetype in file_type_mimetype.items():
            if drivetype in ('file', 'folder'):
                _mimetype_isa[mimetype] = [drivetype]        
            else:
                _mimetype_isa[mimetype] = [drivetype, 'file']        

    if mime_type in _mimetype_isa:
        return(_mimetype_isa[mime_type])
    # default is just file
    return(['file'])


def create(name, in_folder=None, path=None, **body):

    body['name'] = name

    if in_folder:
        if type(in_folder) == 'str':
            body['parents'] = [ in_folder ]
        else:
            body['parents'] = [ in_folder.id ]

    if path:
        raise Exception("Not implemented yet")

    # create the directory
    cls = DriveItem
    response = cls.services.load_service('drive').files().create(
        body=body,
        fields='*',
    ).execute()

    #-- create the self object
    # -- now we reclassify the type because DriveItem is kinda an abstract class
    subclass = cls.translate_mimetype(response['mimeType'])
    if subclass:
        self = subclass(response['id'], metadata=response)
    else:
        # default: just treat it like a file
        self = File(response['id'], metadata=response)

    # return!
    return(self)


def upload(filepath, source_mime_type=None, name=None, in_folder=None, path=None, mime_type=None, convert=True, resumable=True, **parameters):

    metadata = {}
    for field, value in parameters.items():
        metadata[ googleapps.toCamel(field) ] = value

    # get the filename
    match = re.search(r'([^\/\\]+)$', filepath)
    filename = match.group(1)

    if name:
        metadata['name'] = name
    else:
        metadata['name'] = filename

    if in_folder:
        if type(in_folder) == 'str':
            metadata['parents'] = [ in_folder ]
        else:
            metadata['parents'] = [ in_folder.id ]

    if path:
        raise Exception("Not implemented yet")

    match = re.search(r'\.([^\.]+)$', filename)
    if match:
        extension = match.group(1).lower()

    #now get/load the source file
    if not os.path.exists(filepath):
        raise FileNotFoundError("Source file to upload does not exist at path " + str(filepath))

    media = googleapiclient.http.MediaFileUpload(filepath, mimetype=source_mime_type, resumable=resumable)

    if convert:
        # turn it into a google document (if it is an elgible type)            
        doctype = is_document(extension)
        if doctype:
            metadata['mimeType'] = translate_filetype(doctype)

    cls = DriveItem
    response = cls.services.load_service('drive').files().create(
        body=metadata,
        media_body=media,
        fields='*',
    ).execute()

    subclass = cls.translate_mimetype(response['mimeType'])
    if subclass:
        self = subclass(response['id'], metadata=response)
    else:
        self = File(response['id'], metadata=response)
    return(self)



def find_item(*args, **kwargs):
    # shortcut to find exactly one item
    result = find(*args, **kwargs)
    if not result:
        return
    if len(result) == 1:
        return result[0]
    raise Exception("Parameters sent to find_file() matched multiple files: " + "; ".join(f.name + '( ' + f.id + ' )' for f in result))



def find(filename=None, file_type=None, in_folder=None, domains=None, spaces=None, order=None, **queryfields):

    params = {}
    if domains:
        params['corpora'] = domains

    if order:
        if 'order_by' in queryfields:
            raise Exception('Cannot specify both order_by and order')
        params['order_by'] = order

    if spaces:
        params['spaces'] = spaces

    if filename:
        if 'name' in queryfields:
            raise Exception("Cannot specify both name and filename. These are the same")
        queryfields['name'] = filename

    if file_type:
        if 'mime_type' in queryfields:
            raise Exception('Cannot specify both file_type and mime_type')
        queryfields['mime_type'] = translate_filetype(file_type)
        
    if in_folder:
        if 'parents' in queryfields:
            raise Exception("Cannot specify in_folder and parents")
        if type(in_folder) is str:
            queryfields['parents'] = {'op': 'in', 'value': in_folder}
        else:
            queryfields['parents'] = {'op': 'in', 'value': in_folder.id}

    # by default, we do not serch in the trash
    if 'trashed' not in queryfields:
        queryfields['trashed'] = False


    cls = DriveItem
    q = cls.generate_query_string(**queryfields)

    params['q'] = q
    print("QUERY is " + q)
    response = cls.services.load_service('drive').files().list(
        fields='*',
        **params
    ).execute()

    if not len(response['files']):
        return

    result = []
    for f in response['files']:
        result.append(cls(f['id'], metadata=f))
    return(result)



