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
import dateutil.parser
import pickle
import re
import shutil
import io
import time
import warnings
from pprint import pprint

import googleapps
from googleapps.serviceclient import CommitType
import googleapiclient

def mime_type_class(mime_type):
    default = googleapps.drive.File

    mime_type_classes = {
        # expand this as more classes are defined for the Drive Item Factory
        'application/vnd.google-apps.file': googleapps.drive.File,
        'application/vnd.google-apps.folder': googleapps.drive.Folder,
        #'application/vnd.google-apps.spreadsheet': googleapps.sheets.Spreadsheet,
    }

    if mime_type in mime_type_classes:
        return(mime_type_classes[mime_type])
    return(default)

@googleapps.serviceclient.googleappclient
class DriveItem(googleapps.ServiceClient):
    default_api = 'drive'
    default_api_version = 'v3'
    cache_directory = 'cache'
    services = googleapps.ServiceManager()

    time_fields = ('trashed_time', 'viewed_by_me_time', 'created_time', 'modified_time', 'modified_by_me_time', 'shared_with_me_time')

    # these properties are automatically generated into properties the googleappclient decorators
    api_ro_properties = ('id','md5_checksum', 'size',' quota_bytes_used', 'head_revision_id',)
    api_properties = ('name', 'mime_type', 'description', 'starred', 'trashed', 'explicitly_trashed', 'trashing_user', 'trashed_time',
                      'version', 'web_content_link', 'web_view_link', 'icon_link', 'has_thumbnail', 'thumbnail_link', 'thumbnail_version',
                      'modified_time', 'modified_by_me', 'modified_by_me_time',
                      'owned_by_me', 'shared', 'shared_with_me_time',
                      'viewed_by_me_time', 'viewers_can_copy_content', 'writers_can_share',
                      'original_filename', 'fulll_file_extension', 'file_extension',
                      # TODO: these should be managed more individaully
                      'parents', 'spaces', 'permissions', 'permission_ids',
                      # owners, permissions,
                      'drive_id'
                      )
    absent_google_fields = ('md5_checksum',)

    def __init__(self, *args, **kwargs):
        # can create a drive item as :
        # DriveItem(id)

        # DriveItem(name=TITLE) - create new file

        # TODO: Verify default behavior of DriveItem(single_param) is that single_param is the name. Not the ID.
        if len(args) == 1:
            kwargs['id'] = args[0]
            args = args[1:]
        elif len(args) > 1:
            raise Exception("googleapps.drive does not provide support for more than one ordered argument")

        super().__init__(**kwargs)
        self.last_loaded = None
        self.changes = {}

    def is_folder(self):
        return(self.__class__.__name__ == 'Folder')

    def is_file(self):
        return(self.__class__.__name__ == 'File')

    @property
    def in_shared_drive(self):
        return(self.drive_id is not None)

    def folders(self):
        return([googleapps.drive.Folder(id) for id in self.parents])

    @property
    def folder(self):
        folders = self.folders()
        if len(folders) > 1:
            self._die('folder()', "but it has multiple parents: '" + "','".join(self.parents) + "'")
        return(folders[0])

    def load(self):
        self.make_request('files', 'get', fileId=self.id, supportsAllDrives=True, fields='*', callback=self.process_request_json)

    def refresh(self):
        # at present this is no different than load
        # but we keep it separate in case we want to abstract it further sometime in the future
        self.load()

    def save(self):
        if self.last_loaded:
            # just update, because it already exists remotely
            self.update()
        else:
            # new entity, so gather all the properties and make the create() request
            parameters = {'body': self._create_json_parameters()}
            if 'media_body' in self.changes:
                parameters['media_body'] = self.changes['media_body']
            # any call to create should update the rest of the properties with the result
            if self.debug:
                print("---------------- SAVING NEW OBJECT USING files().create(): -------------")
                pprint(parameters)
                print("------------------------------------------------------------------------")
            result = self.make_request('files', 'create', fields='*', callback=self.process_request_json, **parameters)

        # okay, regardless of the path above, process the result
        self.changes = {}

    def _create_json_parameters(self):
        parameters = {}
        for property in self.api_properties:
            if hasattr(self, property):
                if property == 'parents':
                    # special processing - get the parent ids
                    # we defer fetching IDs until here because it is possible in non-autocommit situations
                    # that the parent may not have been saved() yet
                    parameters['parents']= [parent if type(parent) is str else parent.id for parent in getattr(self, property)]
                else:
                    parameters[googleapps.toCamel(property)] = getattr(self, property)
        return(parameters)


    #-----------------------------
    #
    # Top-level requests
    #
    #-----------------------------

    def delete(self):
        self.add_request('files', 'delete', fileId=self.id )
        # clear all changes
        self.changes = {}
        self.deleted = True
        return(True)

    def copy(self, name=None, to_folder=None):
        body = {}

        if name:
            body['name'] = name

        if to_folder:
            if type(to_folder) is str:
                body['parents'] = [ to_folder ]
            else:
                body['parents'] = [ to_folder.id ]

        new_obj = self.__class__()
        self.add_request('files', 'copy',
            fileId=self.id,
            body=body,
            fields='*',
            callback=new_obj.process_request_json
        )
        return(new_obj)

    def download(self, filepath=None, mime_type=None, convert_document=True, overwrite=False):
        # by default, export to an io.BytesIO handle object
        # filepath can be a directory or a full path
        # if the directory exists, it will save it as a file with self.name
        # if no directory, it will save as the file
        # If it is a document convert, it will append an extension if it is not part of the filename


        # determine the filename (or not) to write data to
        fullpath = None
        if filepath:
            if os.path.exists(filepath) and os.path.isdir(filepath):
                fullpath = os.path.join(directory, self.name)
            else:
                fullpath = filepath

        # determine the request, which can be a straight download or an export, especially an export of a Google Document
        request = None
        googledoc_convert = None
        if not mime_type and fullpath and self.is_google_document() and convert_document:
            fextmatch = re.search('\.(\w+)$', fullpath)
            if not fextmatch:
                raise Exception("Cannot get extension for filename " + fullpath)
            document_mime_type = googleapps.drive.MimeType.extension_mime_type(fextmatch.group(1))
            request = self.services.get_service('drive').files().export_media(fileId=self.id, mimeType=document_mime_type)
        elif mime_type:
            request = self.services.get_service('drive').files().export_media(fileId=self.id, mimeType=mime_type)
        else:
            request = self.services.get_service('drive').files().get_media(fileId=self.id)


        # open the filehandle, possibly adding the extension if necessary
        if fullpath:
            if googledoc_convert:
                doc_extension = googleapps.drive.MimeType.mime_type_extension(googledoc_convert)
                if not re.search(r"\\." + doc_extension + "$", fullpath, re.I):
                    fullpath += '.' + doc_extension

            if os.path.exists(fullpath) and not overwrite:
                raise Exception("Attempting to overwrite " + fullpath + ", but the overwrite parameter in the download() call is set to False.")
            fh = open(fullpath, 'wb')
        else:
            fh = io.BytesIO()

        # process the download
        downloader= googleapiclient.http.MediaIoBaseDownload(fh, request)
        done = False
        iterations = 0
        at_99 = 0
        while done is False:
            #import pdb
            #pdb.set_trace()
            try:
                status, done = downloader.next_chunk()
            except googleapiclient.errors.HttpError as he:
                print("---- caught exception in chunk download.  waiting for a couple seconds -----")
                print(str(he))
                time.sleep(3)
                status, done = downloader.next_chunk()

            iterations += 1
            if self.debug:
                if (iterations % 20) == 0:
                    print('.')
                else:
                    print('.', end="")
            # we ran into a bug in which the download would never end, so we're going to try to investigate more
            if status.progress() > .99:
                at_99 += 1
                if at_99 > 10:
                    raise Exception('Likely download error. Download at 99% for over 10 iterations.  Investigate?')

        if fullpath:
            fh.close()
            os.utime(fullpath, times=(datetime.datetime.now().timestamp(), self.modified_time.timestamp()))
            return(fullpath)
        else:
            return(fh)

    #-----------------------
    #
    # Property Updates
    #
    #-----------------------

    def rename(self, new_name):
        self.name = new_name

    @classmethod
    def _resolve_ids(cls, objects_or_ids):
        return([id if type(id) is str else id.id for id in objects_or_ids])

    def move(self, to_folder):
        # best to copy the remove_from list so that we avoid conflicts of the array passed by reference
        # TODO: have the 'parents' property return a copy to beging with
        self.add_folder_change(add_to=[to_folder], remove_from=self.parents.copy())

    def remove_from_folder(self, *folders):
        self.add_folder_change(remove_from=folders)

    def add_to_folder(self, *folders):
        self.add_folder_change(add_to=folders)

    #-----------------------
    #
    # Internal Functions
    #
    #-----------------------

    def add_folder_change(self, add_to=None, remove_from=None, allow_commit=True):
        # allow_commit is whether or not to consider this at the top level - if a number of actions will be occurring,
        # passing in allow_commit=False can make it seem like an atomic call
        self.changes.setdefault('folder_changes', [])

        if remove_from:
            folder_ids = self._resolve_ids(remove_from)
            for folder_id in folder_ids:
                try:
                    index = self.parents.index(folder_id)
                    del self.parents[index]
                    self.changes['folder_changes'].append(['remove', folder_id])
                except ValueError as e:
                    raise ValueError("Folder '" + index + "' is not a parent of '" + self.id + "', and so it cannot be removed")

        if add_to:
            folder_ids = self._resolve_ids(add_to)
            for folder_id in folder_ids:
                if folder_id not in self.parents:
                    self.changes['folder_changes'].append(['add', folder_id])
                    self.parents.append(folder_id)


        if allow_commit and self.commit_policy >= CommitType.auto_commit:
            self.update()


    def update(self):

        root_properties = ('keep_revision_forever', 'ocr_language', 'supports_all_drives', 'use_content_as_indexable_text', 'media_body')

        root_parameters = {}
        body_parameters = {}

        for property in self.changes:
            if property == 'folder_changes':
                continue
            elif property in root_properties:
                root_parameters[googleapps.toCamel(property)] = getattr(self, property)
            else:
                body_parameters[googleapps.toCamel(property)] = getattr(self, property)

        # allow for the possibility of both adding and removing parents before committing updates
        if 'folder_changes' in self.changes:
            to_add = {}
            to_remove = {}
            for change in self.changes['folder_changes']:
                if change[0] == 'add':
                    if change[1] in to_remove:
                        del to_remove[change[1]]
                    to_add[change[1]]= True
                else:
                    if change[1] in to_add:
                        del to_add[change[1]]
                    to_remove[change[1]]= True
            if to_add:
                root_parameters['addParents'] = ','.join(to_add)
            if to_remove:
                root_parameters['removeParents'] = ','.join(to_remove)

        # all set, make the request
        self.make_request('files', 'update',
                          fileId=self.id,
                          callback=self.process_request_json,
                          fields='*',
                          body=body_parameters,
                          **root_parameters,
                          )


    def record_value_change(self, property, cleared=False):
        if cleared:
            del self.changes[property]
        else:
            # if autocommit *AND* This is already an existing element, make the change
            # if it does not exist on Drive yet, we don't make the change because
            # it may be happening during an atomic transaction (upload, create, ....)
            # We may want to move toward a more atomic-transaction system at some point
            if self.commit_policy == CommitType.auto_commit and self.last_loaded:
                result = self.make_request('files', 'update',
                                  fileId=self.id,
                                  body={googleapps.toCamel(property): getattr(self, property)},
                                  fields='*',
                                  callback = self.process_request_json
                                  )
            else:
                self.changes[property] = True

    def process_request_json(self, raw_json):
        json = googleapps.unCamel(raw_json)
        if self.debug:
            print("--- Received JSON to Process ----")
            pprint(json)
            print("---------------------------------")

        # first, if this is the fist actuall remote call we've made, set the ID
        if not hasattr(self, 'id'):
            self._id = json['id']

        for key in self.api_properties + self.api_ro_properties:
            if key in json:
                if self.debug:
                    print("\tSet " + key)
                    if hasattr(self, key):
                        current = getattr(self, key)
                        if json[key] != current:
                            print("\t\t**** This value ("+str(json[key])+") is different than the current existing value of : " + str(current))
                # special processing, convert for time fields
                if key in self.time_fields:
                    setattr(self, '_' + key, googleapps.from_rfctime(json[key]))
                else:
                    setattr(self, '_' + key, json[key])
            elif key in self.absent_google_fields:
                if self.debug:
                    print("Setting absent field " + key + " to none")
                # Because these properties will die with a Not Loaded error if they are called,
                # and this would signify they were loaded,
                # we set them as none if they don't exist
                setattr(self, '_' + key, None)
            else:
                if self.debug:
                    print("NOT SETTING absent field " + key)


        #TODO: Verify this is an appropriate decision
        #  BEST AND NEED TO DO: - the timestamp right before the request was made, which is probably safest
        # could be:
        #  same as the later of modified/view time, reported by Google
        #  currently, which is the timestamp this function began running, which is just the worst option but easy for now
        self.last_loaded=datetime.datetime.now()




    def _die(self, function, msg):
        identifying_string = str(function) + " called for Google Drive item "
        if hasattr(self, 'id'):
            if hasattr(self, 'name'):
                identifying_string += self.name + " (id='" +str(self.id)+ "')"
            else:
                identifying_string += "'" +str(self.id)+ "'"
        elif hasattr(self, 'name'):
            identifying_string += "'" +str(self.name)+ "'"
        else:
            pass
        raise Exception(identifying_string + msg)


    @classmethod
    def process_queryvalue(cls, value):
        if value is None:
            return
        if type(value) is str:
            value = re.sub("'", "\\'", value)
            return("'" + value + "'")
        elif type(value) in (datetime.datetime, datetime.date, datetime.time):
            return googleapps.to_rfctime(value)
        elif type(value) is bool:
            if value:
                return('true')
            else:
                return('false')
        return(str(value))


    @classmethod
    def generate_query_string(cls, conjunction='and', **fields):

        q = []
        for field,value in fields.items():
            camelfield = googleapps.toCamel(field)
            if field in ['or', 'and']:
                # disjunction instead of conjunction
                q.append('(' + cls.generate_query_string(conjunction=field, **value) + ')')
            elif type(value) is dict:
                if value['op'] in ('in', 'not in'):
                    # 'in' is reversed
                    q.append(cls.process_queryvalue(value['value']) + ' '+value['op']+' ' + camelfield)
                else:
                    q.append(camelfield + ' ' + value['op'] + ' ' + cls.process_queryvalue(value['value']))
            elif type(value) is list:
                value_strings = []
                for val in value:
                    value_strings.append(camelfield + ' = ' + cls.process_queryvalue(val))
                q.append('(' + ' OR '.join(value_strings) + ')')

            elif value is not None:
                # in some cases (like with the trashed parameter, the user can explicitly be
                # set to None to mean that the default should not be passed in - and in fact
                # nothing should be provided, so we leave the elif to only add a parameter
                # if it is not none)
                q.append(camelfield + ' = ' + cls.process_queryvalue(value))

        if cls.debug:
            print("---- Query String Generated -----")
            print(q)
        if len(q) == 1:
            return(q[0])
        else:
            cnj = ' ' + conjunction + ' '
            return(cnj.join(q))


    def is_google_document(self):
        return(self.mime_type in googleapps.drive.MimeType.google_document_types)

    def is_media(self):
        return(self.mime_type in googleapps.drive.MimeType.media_types)

    def cache(self):
        # TODO
        # THIS IS NOT UPDATED


        path = self.cache_directory
        if not os.path.exists(path):
             os.makedirs(path)

        dt = datetime.datetime.now()
        folder_name = 'cache/' + dt.strftime('%Y-%m-%d %H.%M.%S')

        os.makedirs(folder_name)

        for network in self.get_networks():
            os.makedirs(folder_name + '/' + network.dirname)
            print("\nDownload and cache files for " + network.dirname)
            for plan in network.get_school_plans():
                fn = plan.filename
                if not re.search(r'\.xlsx$', fn, re.I):
                    fn += '.xlsx'
                self.download_file(plan.id,
                                   fn,
                                   format='xl',
                                   dir=folder_name + '/' + network.dirname)

        # if we get here, we are done!
        if os.path.exists('cache/current'):
            os.remove('cache/current')
        os.symlink(os.path.realpath(folder_name), 'cache/current', target_is_directory=True)
        # cache updated!

    def change_owner(self, new_owner):
        raise Exception("Not implemented yet.");

    def share(self, role, auth_type='user', share_with=None, domain=None,
            allow_discovery=None, expiration_date=None, with_link=None,
            message=None, notify=True, transfer_owner=False, domain_admin=False):
        """ Control sharing access to the folder.

        role {str} : The permission role: [owner, organizer, fileOrganizer, writer, commente, reader]
        type {str} : The type of grantee. One of: [user, group, domain, anyone]
        share_with {str|list}: The user email address(es) to share with.
        domain {str} (optional): The domain to which this new permission applies
        with_link {bool}: If true, set these permissions to anyone with the link. If with_link is true and domain is not None, it will apply to anyone with the link but in the domain
        """

        #---- General args, but the real action happens in the body (defined below)
        overall_args = {
            'fileId':self.id,
            'useDomainAdminAccess':domain_admin,
            'transferOwnership':transfer_owner,
        }

        # special case ??
        body = { 'role': role, 'type': auth_type }
#        if role == 'commenter':
#            body = { 'role': role, 'type': auth_type, 'additionalRoles': [ 'commenter' ] }
#        else:
#            body = { 'role': role, 'type': auth_type }

        if domain:
            body['domain'] = domain
        if expiration_date:
            # this should be in RFC 3339 date-time
            body['expirationDate'] = expiration_date
        if with_link is not None:
            body['withLink'] = with_link
        if allow_discovery is not None:
            body['allowFileDiscovery'] = allow_discovery

        if share_with:
            overall_args['sendNotificationEmail'] = notify
            overall_args['emailMessage'] = message

            if type(share_with) not in (list,tuple):
                share_with = [ share_with ]

            for email in share_with:
                single_body = body.copy()
                single_body['emailAddress'] = email
                self.add_request('permissions', 'create', body=single_body, **overall_args)
        else:
            self.add_request('permissions', 'create', body=body, **overall_args)



    def metadata(self, metadata=None, refresh=False):
        if self.deleted:
            raise FileNotFoundError("Attempt to use drive object after deletion")

        if self._metadata and not refresh:
            return(self._metadata)

        if not metadata:
            # https://developers.google.com/resources/api-libraries/documentation/drive/v3/python/latest/drive_v3.files.html#get
            try:
                metadata = self.services.load_service('drive').files().get(fileId=self.id, fields='*').execute()
            except Exception as e:
                errmsg = e._get_reason()
                if re.search('File not found:', errmsg):
                    raise FileNotFoundError(errmsg)
                # anything else, raise like normal
                raise(e)

        self._metadata = metadata

        # -- create the current instance variable set based on the response.
        #    At the moment this is minimal. See the api-libraries for the full scope
        #    of information.

        # -- determine the type
        self._mime_type = metadata['mimeType']

        ## DETERIME
        # is_file
        # is_folder
        # ...
        self.type_isa = googleapps.drive.mime_type_isa(metadata['mimeType'])

        # Whether the file has been explicitly trashed, as opposed to recursively trashed from a parent folder.
        self._name = metadata["name"] # The name of the file. This is not necessarily unique within a folder. Note that for immutable items such as the top level folders of Team Drives, My Drive root folder, and Application Data folder the name is constant.
        if 'description' in metadata:
            self._description = metadata['description'] # A short description of the file.
        else:
            self._description = None
        # Whether the file has been trashed, either explicitly or from a trashed parent folder. Only the owner may trash a file, and other users cannot see files in the owner's trash.
        self._trashed = metadata['trashed']
        if 'size' in metadata:
            self._size = metadata['size']
        else:
            self._size = None
        if 'parents' in metadata:
            self._parent_folder_ids = metadata['parents']

        # this gets turned into an object on first call to obj.parents
        self._parents = None

        self._user_is_owner = metadata['ownedByMe']
        self._is_shared = metadata['shared']
        self._writers_can_share = metadata['writersCanShare']

        self._modified_user = metadata['lastModifyingUser']['permissionId']
        self._last_modified_user_email = metadata['lastModifyingUser']['emailAddress']
        #'is_me': metadata['lastModifyingUser']['me'],


        self._created_time = dateutil.parser.parse(metadata["createdTime"]) # The time at which the file was created (RFC 3339 date-time).
        self._modified_time = dateutil.parser.parse(metadata["modifiedTime"]) # The last time the file was modified by anyone (RFC 3339 date-time).

        self._ever_accessed_by_me = metadata["viewedByMe"] # Whether the file has been viewed by this user.
        self._ever_modified_by_me = metadata["modifiedByMe"] # Whether the file has been modified by this user.
        if "viewedByMeTime" in metadata:
            self._access_time_by_me = dateutil.parser.parse( metadata["viewedByMeTime"] )
        else:
            self._access_time_by_me = None

        if "modifiedByMeTime" in metadata:
            self._modified_time_by_me = dateutil.parser.parse( metadata["modifiedByMeTime"] )
        else:
            self._modified_time_by_me = None

        ###### DOES THIS WORK ON FILES AND NOT FOLDERS?
        if "folderColorRgb" in metadata:
            # only in folders
            self._folder_color = metadata["folderColorRgb"] # The color for a folder as an RGB hex string. The supported colors are published in the folderColorPalette field of the About resource.
            # If an unsupported color is specified, the closest color in the palette will be used instead.

        self._capabilities = {
         # Capabilities the current user has on this file. Each capability corresponds to a fine-grained action that a user may take.
          'can_read_revisions': metadata['capabilities']["canReadRevisions"], # Whether the current user can read the revisions resource of this file. For a Team Drive item, whether revisions of non-folder descendants of this item, or this item itself if it is not a folder, can be read.
          'can_trash': metadata['capabilities']["canTrash"], # Whether the current user can move this file to trash.
          'can_copy': metadata['capabilities']["canCopy"], # Whether the current user can copy this file. For a Team Drive item, whether the current user can copy non-folder descendants of this item, or this item itself if it is not a folder.
          'can_share': metadata['capabilities']["canShare"], # Whether the current user can modify the sharing settings for this file.
          'can_delete': metadata['capabilities']["canDelete"], # Whether the current user can delete this file.
          'can_rename': metadata['capabilities']["canRename"], # Whether the current user can rename this file.
          'can_list_children': metadata['capabilities']["canListChildren"], # Whether the current user can list the children of this folder. This is always false when the item is not a folder.
          'can_download': metadata['capabilities']["canDownload"], # Whether the current user can download this file.
          'can_comment': metadata['capabilities']["canComment"], # Whether the current user can comment on this file.
          'can_edit': metadata['capabilities']["canEdit"], # Whether the current user can edit this file.
          'can_remove_children': metadata['capabilities']["canRemoveChildren"], # Whether the current user can remove children from this folder. This is always false when the item is not a folder.
          'can_add_children': metadata['capabilities']["canAddChildren"], # Whether the current user can add children to this folder. This is always false when the item is not a folder.
          'can_change_viewers_can_copy_content': metadata['capabilities']["canChangeViewersCanCopyContent"], # Whether the current user can change whether viewers can copy the contents of this file.
          'can_untrash': metadata['capabilities']["canUntrash"], # Whether the current user can restore this file from trash.

            # --- not enabled because of teamdrive reference (and may generate keyerror
#          'can_move_into_teamdrive': metadata['capabilities']["canMoveItemIntoTeamDrive"], # Whether the current user can move this item into a Team Drive. If the item is in a Team Drive, this field is equivalent to canMoveTeamDriveItem.
#          'can_move_teamdrive': metadata['capabilities']["canMoveTeamDriveItem"], # Whether the current user can move this Team Drive item by changing its parent. Note that a request to change the parent for this item may still fail depending on the new parent that is being added. Only populated for Team Drive files.
            # 'can_read_teamdrvie': metadata['capabilities']["canReadTeamDrive"], # Whether the current user can read the Team Drive to which this file belongs. Only populated for Team Drive files.

        }


        # The owners of the file. Currently, only certain legacy files may have more than one owner. Not populated for Team Drive files.
        if len(metadata['owners']):
            self._owners = [
                {'is_me' : owner["me"], # Whether this user is the requesting user.
                'user_display_name': owner["displayName"],  # A plain text displayable name for this user.
                'user_id': owner["permissionId"], # The user's ID as visible in Permission resources.
                'user_email': owner["emailAddress"]} # The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.
                for owner in metadata['owners']]
        else:
            self._owner = None

        if 'md5Checksum' in metadata:
            self._md5 = metadata["md5Checksum"] # The MD5 checksum for the content of the file. This is only applicable to files with binary content in Drive.
        else:
            self._md5 = None

        if "webContentLink" in metadata:
            self._download_link = metadata["webContentLink"] # A link for downloading the content of the file in a browser. This is only available for files with binary content in Drive.
        else:
            self._download_link = None
        self._users_with_access = metadata["permissionIds"]

        # The final component of fullFileExtension. This is only available for files with binary content in Drive.
        # The full file extension extracted from the name field. May contain multiple concatenated extensions, such as "tar.gz". This is only available for files with binary content in Drive.
        if 'fullFileExtension' in metadata:
            self._full_file_extension = metadata['fullFileExtension']
        else:
            self._full_file_extension = None
        # This is automatically updated when the name field changes, however it is not cleared if the new name does not contain a valid extension.
        if 'fileExtension' in metadata:
            self._file_extension = metadata["fileExtension"]
        else:
            self._full_file_extension = None

        return(self._metadata)
