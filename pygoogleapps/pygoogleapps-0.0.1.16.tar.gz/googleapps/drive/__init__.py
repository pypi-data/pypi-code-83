import googleapps
from .driveitem import DriveItem
from .file import File
from .folder import Folder

from googleapps.serviceclient import CommitType
import googleapiclient

import os, os.path
import datetime
import pickle
import re
import shutil
import enum

import warnings
from pprint import pprint

def item_class(mime_type=None):
    if mime_type == MimeType.folder_mime_type():
        return(Folder)
    else:
        return(File)

def item_from_json(json):
    #
    # This can be expanded as we have more classes
    #


    #print("******* Item from json ******")
    #pprint(json)
    #print("*****************************")
    ItemType = item_class(json['mimeType'])
    item = ItemType(id=json['id'])
    item.process_request_json(json)
    return(item)



def create_folder(*args, **kwargs):
    kwargs['mime_type'] = MimeType.folder_mime_type()
    return(create(*args, **kwargs))


def create(name=None, in_folder=None, path=None, **body):

    if 'mime_type' in body:
        ItemClass = item_class(body['mime_type'])
    else:
        ItemClass = item_class()

    if name:
        body['name'] = name

    if in_folder:
        body['parents'] = [in_folder]

    if path:
        raise Exception("Haven't implemented path logic yet")

    item = ItemClass(**body)

    # only save if autocommit is on
    if item.commit_policy >= CommitType.auto_commit:
        item.save()

    return(item)


def upload(filepath, mime_type=None, convert=None, **parameters):
    obj = File(**parameters, mime_type=mime_type)
    obj.upload(filepath, convert=convert)
    return(obj)

def get(id, retry_count=3, search_all_drives=True, **extra_args):
    if extra_args:
        extra_args = {googleapps.toCamel(key): extra_args[key] for key in extra_args}
    else:
        extra_args = {}

    request = googleapps.serviceclient.ServiceRequest(api=DriveItem.default_api,
                                                      api_version=DriveItem.default_api_version,
                                                      resource='files',
                                                      function='get',
                                                      parameters={'fileId':id, 'fields':'*', 'supportsAllDrives':search_all_drives, **extra_args},
                                                      callback=None
                                                      )
    try:
        response = DriveItem.make_class_request( request, attempt_recover=False )
        return(item_from_json(response))
    except googleapiclient.errors.HttpError as e:
        if re.search('File not found', str(e)):
            # if the file is not found, we just return null
            return
        elif re.search('Resource not avail|Try again later', str(e)):

            if retry_count:
                # if we suspect this is a network or resource busy error, we just call get again
                return(get(id, retry_count-1))
            else:
                # other errors, pass along
                raise(e)
        else:
            print("Not sure what to do with this HttpError")
            raise(e)

def open(id):
    return(get(id))

def open_folder(id):
    folder = get(id)
    if folder is None:
        return

    if folder.mime_type != MimeType.folder_mime_type():
        raise Exception("Attempted to open folder '" + str(id) + "', but it is not a Folder! It is a " + folder.mime_type)

    return(folder)


def open_path(path, in_folder=None):
    raise Exception("Not implemented yet")

def exists(path, in_folder=None):
    raise Exception("Not implemented yet")


def find(*args, **kwargs):
    # shortcut to find exactly one item
    result = find_all(*args, **kwargs)
    if not result:
        return
    if len(result) == 1:
        return result[0]
    raise Exception("Parameters sent to find_file() matched multiple files: " + "; ".join(f.name + '( ' + f.id + ' )' for f in result))



def find_all(filename=None, file_type=None, in_folder=None, domains=None, spaces=None, order=None, all_drives=None, **queryfields):

    params = { }
    if domains:
        params['corpora'] = domains

    if all_drives is not None:
        #params['include_items_from_all_drives'] = all_drives
        params['supportsAllDrives'] = all_drives
        params['includeItemsFromAllDrives'] = all_drives

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
        queryfields['mime_type'] = MimeType.mime_type(file_type)

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

    query = DriveItem.generate_query_string(**queryfields)

    #print("------------------------------ FIND ALL -------------------------------------------")
    #print(query)
    #print("------------------------------ END FIND ALL -------------------------------------------")
    response = DriveItem.services.load_service('drive').files().list(
        fields='*',
        q=query,
        **params
    ).execute()

    result = []
    #--- if there are more files, loop over them !
    another_page = True
    while another_page:
        for f in response['files']:
            result.append(item_from_json(f))

        another_page = response.get('nextPageToken', None)
        if another_page:
            if googleapps.ServiceClient.debug:
                print("-- Fetching another page worth of files because it appears there are more to download")
            response = DriveItem.services.load_service('drive').files().list(
                fields='*',
                q=query,
                pageToken=another_page,
                **params
            ).execute()


    return(result)


class MimeType():

    core_mime_types = [
        ('file', 'application/vnd.google-apps.file'),
        ('folder', 'application/vnd.google-apps.folder'),
        ('unknown', 'application/vnd.google-apps.unknown'),
        ('bmp', 'image/bmp'),
        ('gif', 'image/gif'),
        ('jpeg', 'image/jpeg'),
        ('png', 'image/png'),
        ('svg', 'image/svg+xml'),
        ('pdf', 'application/pdf'),
        ('css', 'text/css'),
        ('csv', 'text/csv'),
        ('html', 'text/html'),
        ('javascript', 'application/javascript'),
        ('plain_text', 'text/plain'),
        ('rtf', 'application/rtf'),
        ('zip', 'application/zip'),
        ('google_app_script', 'application/vnd.google-apps.script'),
        ('google_drawing', 'application/vnd.google-apps.drawing'),
        ('google_docs', 'application/vnd.google-apps.document'),
        ('google_forms', 'application/vnd.google-apps.form'),
        ('google_sheets', 'application/vnd.google-apps.spreadsheet'),
        ('google_slides', 'application/vnd.google-apps.presentation'),
        ('opendocument_graphics', 'application/vnd.oasis.opendocument.graphics'),
        ('opendocument_presentation', 'application/vnd.oasis.opendocument.presentation'),
        ('opendocument_spreadsheet', 'application/vnd.oasis.opendocument.spreadsheet'),
        ('opendocument_text', 'application/vnd.oasis.opendocument.text'),
        ('microsoft_excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
        ('microsoft_excel_legacy', 'application/vnd.ms-excel'),
        ('microsoft_powerpoint', 'application/vnd.openxmlformats-officedocument.presentationml.presentation'),
        ('microsoft_powerpoint_legacy', 'application/vnd.ms-powerpoint'),
        ('microsoft_word', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'),
        ('microsoft_word_legacy', 'application/msword'),
    ]

    #
    extensions = [
        ('odg', 'application/vnd.oasis.opendocument.graphics'),
        ('odp', 'application/vnd.oasis.opendocument.presentation'),
        ('ods', 'application/vnd.oasis.opendocument.spreadsheet'),
        ('odt', 'application/vnd.oasis.opendocument.text'),
        ('xlsx', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
        ('xls', 'application/vnd.ms-excel'),
        ('pptx', 'application/vnd.openxmlformats-officedocument.presentationml.presentation'),
        ('ppt', 'application/vnd.ms-powerpoint'),
        ('docx', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'),
        ('doc', 'application/msword'),
        ('jpg', 'image/jpeg'),
        ('js', 'application/javascript'),
        ('txt', 'text/plain'),
        ('csv', 'text/csv'),
    ]

    # Some aliases for simplicity
    aliases = [
        ('google_document', 'google_docs'),
        ('google_spreadsheet', 'google_sheets'),
        ('google_presentation', 'google_slides'),
        ('libreoffice_graphics', 'opendocument_graphics'),
        ('libreoffice_document', 'opendocument_text'),
        ('libreoffice_presentation', 'opendocument_presentation'),
        ('libreoffice_spreadsheet', 'opendocument_spreadsheet'),
        ('openoffice_graphics', 'opendocument_graphics'),
        ('openoffice_document', 'opendocument_text'),
        ('openoffice_presentation', 'opendocument_presentation'),
        ('openoffice_spreadsheet', 'opendocument_spreadsheet'),
        ('ms_excel', 'microsoft_excel'),
        ('ms_excel_legacy', 'microsoft_excel_legacy'),
        ('ms_powerpoint', 'microsoft_powerpoint'),
        ('ms_powerpoint_legacy', 'microsoft_powerpoint_legacy'),
        ('ms_word', 'microsoft_word'),
        ('ms_word_legacy', 'microsoft_word_legacy'),
    ]

    # mime_types that can be translated to Google Apps Office Formats
    office_mime_types = {
        'application/rtf': 'application/vnd.google-apps.document',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'application/vnd.google-apps.document',
        'application/vnd.oasis.opendocument.text': 'application/vnd.google-apps.document',
        'application/vnd.google-apps.document': 'application/vnd.google-apps.document',

        'application/vnd.google-apps.spreadsheet': 'application/vnd.google-apps.spreadsheet',
        'text/csv': 'application/vnd.google-apps.spreadsheet',
        'text/tab-separated-values': 'application/vnd.google-apps.spreadsheet',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'application/vnd.google-apps.spreadsheet',
        'application/x-vnd.oasis.opendocument.spreadsheet': 'application/vnd.google-apps.spreadsheet',

        'application/vnd.google-apps.presentation': 'application/vnd.google-apps.presentation',
        'application/vnd.oasis.opendocument.presentation': 'application/vnd.google-apps.presentation',
        'application/vnd.openxmlformats-officedocument.presentationml.presentation': 'application/vnd.google-apps.presentation',
    }

    google_document_types = {
        'application/vnd.google-apps.document',
        'application/vnd.google-apps.drawing',
        'application/vnd.google-apps.form',
        'application/vnd.google-apps.presentation',
        'application/vnd.google-apps.spreadsheet',
    }

    office_conversion_types = {
        'document': 'application/vnd.google-apps.document',
        'spreadsheet': 'application/vnd.google-apps.spreadsheet',
        'presentation': 'application/vnd.google-apps.presentation',
    }

    office_types = {
        'application/rtf': 'document',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'document',
        'application/vnd.oasis.opendocument.text': 'document',
        'application/vnd.google-apps.document': 'document',

        'application/vnd.google-apps.spreadsheet': 'spreadsheet',
        'text/csv': 'spreadsheet',
        'text/tab-separated-values': 'spreadsheet',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'spreadsheet',
        'application/x-vnd.oasis.opendocument.spreadsheet': 'spreadsheet', #libreoffice/ods
        'application/vnd.oasis.opendocument.spreadsheet': 'spreadsheet', #libreoffice/ods
        'application/vnd.ms-excel': 'spreadsheet', # legacy msexcel

        'application/vnd.google-apps.presentation': 'presentation',
        'application/vnd.oasis.opendocument.presentation': 'presentation',
        'application/vnd.openxmlformats-officedocument.presentationml.presentation': 'presentation',
    }

    media_types = ( 'application/vnd.google-apps.audio',
                    'application/vnd.google-apps.video',
                    'application/vnd.google-apps.photo')


    _mime_types = {}
    _reverse_mime_types = {}
    _aliases = {}
    _reverse_aliases= {}
    _extensions = {}
    _reverse_extensions = {}

    for mt in core_mime_types:
        _mime_types[mt[0]] = mt[1]
        _reverse_mime_types[mt[1]] = mt[0]

    for al in aliases:
        _aliases[al[0]] = al[1]
        _reverse_aliases[al[1]] = al[0]

    for ext in extensions:
        _extensions[ext[0]] = ext[1]
        _reverse_extensions[ext[1]] = ext[0]

    @classmethod
    def folder_mime_type(cls):
        return(cls._mime_types['folder'])

    @classmethod
    def mime_type_from_filename(cls, filename):
        ext = re.search(r'\.([^\.]+)$')
        if ext:
            return(cls.extension_mime_type(ext.group(1)))
        return

    @classmethod
    def extension_mime_type(cls, ext):
        if ext.lower() in cls._extensions:
            return(cls._extensions[ext.lower()])
        return

    @classmethod
    def mime_type_extension(cls, mime_type):
        if mime_type.lower() in cls._reverse_extensions:
            return(cls._reverse_extensions[mime_type.lower()])
        return

    @classmethod
    def mime_type(cls, file_type):
        # see if the type provided is a direct link
        if file_type.lower() in cls._mime_types:
            return(cls._mime_types[file_type.lower()])
        # otherwise, see what the alias is
        if file_type.lower() in cls._aliases:
            return(cls._mime_types[cls._aliases[file_type.lower()]])

        # default is to just return the mime_type for "file"
        return(cls._mime_types['file'])

    @classmethod
    def file_type(cls, mime_type):
        # see if the type provided is a direct link
        if mime_type.lower() in cls._reverse_mime_types:
            return(cls._reverse_mime_types[mime_type.lower()])

        # default is just to return 'file'
        return('file')

    @classmethod
    def document_type(cls, mime_type=None, file_type=None, extension=None):
        if mime_type:
            mime_type = mime_type.lower()
        elif file_type:
            mime_type = cls.mime_type(file_type)
        elif extension:
            mime_type = cls.extension_mime_type(extension)
        if mime_type in cls.office_types:
            return(cls.office_types[mime_type])
        return

    @classmethod
    def google_document_type(cls, mime_type=None, file_type=None, extension=None):
        if mime_type:
            mime_type = mime_type.lower()
        elif file_type:
            mime_type = cls.mime_type(file_type)
        elif extension:
            mime_type = cls.extension_mime_type(extension)

        if re.search('google-apps', mime_type) and mime_type in cls.office_types:
            return(cls.office_types[mime_type])
        return


    @classmethod
    def convert_document_mime_type(cls, **kwargs):
        office_type = cls.document_type(**kwargs)
        if not office_type:
            return
        return(cls.office_conversion_types[office_type])

for mt in MimeType.core_mime_types:
    setattr(MimeType, mt[0], mt[1])

for alias in MimeType.aliases:
    setattr(MimeType, alias[0], getattr(MimeType,alias[1]))
