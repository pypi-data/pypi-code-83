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
import googleapiclient

import warnings
from pprint import pprint


import googleapps
from .driveitem import DriveItem


class File (DriveItem):

    def get_spreadsheet(self):
        if googleapps.drive.MimeType.google_document_type(mime_type=self.mime_type) == 'spreadsheet':
            return(googleapps.sheets.get(self.id))
        raise Exception("File " + self.name + " (id="+self.id+") is not a Google Apps spreadsheet. Mime Type is " + self.mime_type)
        return

    @property
    def file_type(self):
        return(googleapps.drive.MimeType.file_type(self.mime_type))

    @file_type.setter
    def file_type(self, value):
        self.mime_type = googleapps.drive.MimeType.mime_type(value)

    def is_google_document(self):
        if re.search('google', self.file_type):
            return(True)
        return(False)

    def is_spreadsheet(self):
        return (self.document_type == 'spreadsheet')


    @property
    def document_type(self):
        return(googleapps.drive.MimeType.document_type(mime_type=self.mime_type))

    @property
    def document_mime_type(self):
        return(googleapps.drive.MimeType.convert_document_mime_type(mime_type=self.document_type))

    @property
    def mime_type_extension(self):
        return(googleapps.drive.MimeType.mime_type_extension(self.mime_type))

    def _prepare_upload(self, filepath, mime_type=None, convert=None):

        if not os.path.exists(filepath):
            raise FileNotFoundError("Source file to upload does not exist at path " + str(filepath))

        result = {}

        #now get/load the source file
        if mime_type:
            result['mime_type'] = mime_type
        else:
            match = re.search(r'\.([^\.]+)$', filepath)
            result['mime_type'] = googleapps.drive.MimeType.extension_mime_type(match.group(1))

        # get file times
        stat = os.stat(filepath)
        result['modified_time'] = datetime.datetime.fromtimestamp(stat.st_mtime)
        result['created_time'] = datetime.datetime.fromtimestamp(stat.st_ctime)

        # and the media
        result['media'] = googleapiclient.http.MediaFileUpload(filepath, mimetype=result['mime_type'], resumable=True)

        # Find out if it is eligible to convert to google doc
        if result['mime_type'] and (convert or convert is None):
            doctype = googleapps.drive.MimeType.convert_document_mime_type(mime_type=result['mime_type'])
            if doctype:
                # BY DEFUALT, (convert is None) we convert.
                # We need to do it in this order because we want the orgiinal mime_type set for the
                # MediaFileUpload, but the converted mime_type on the file object
                result['mime_type'] = doctype

        return(result)


    def replace(self, filepath, mime_type=None, convert=None):
        # this is a bit of shorthand as it calls update() at the end to enact the replacement
        # the programmer could do this on their own terms merely by setting media_body as a change variable

        if not self.last_loaded and not self.id:
            raise Exception("replace() called on object, but this is not existing in the Drive yet")

        media_data = self._prepare_upload(filepath, mime_type, convert)

        # error checking if we have available information
        # It's possible we have not actually loaded the file information, in which case
        # we cannot do this error checking
        if self.last_loaded and media_data['mime_type'] != self.mime_type:
            # is this right? What about for convent/unconvert?
            raise Exception("Mime Type " + mime_type + " is derived by the file replace() call, but differs than "+self.mime_type+", which is manually set on the object ")

        # we also update the time variables based on the media data
        for file_time_field in 'modified_time', 'created_time':
            setattr(self, file_time_field, media_data[file_time_field])

        self.changes['media_body'] = media_data['media']

        return(self.update())


    def upload(self, filepath, mime_type=None, convert=None):
        if self.last_loaded:
            raise Exception("upload() is designed for an object that is not in the google drive yet")

        # automatically set the name from the filepath if it doesn't already exist
        if not 'name' in self.changes:
            #TODO: test this
            match = re.search(r'([^\/\\]+)$', filepath)
            if not match or not match.group(1):
                raise Exception("Cannot determine filename from " + filepath)
            self.name = match.group(1)

        # get metadata parameters
        media_data = self._prepare_upload(filepath, mime_type, convert)
        if 'mime_type' not in self.changes:
            self.mime_type = media_data['mime_type']
        elif media_data['mime_type'] != self.mime_type:
            # Is this necessary?
            raise Exception("Mime Type " + mime_type + " is derived by the file upload() call, but differs from "+self.mime_type+", which is manually set on the object ")

        # to determine the correct parameters, we follow this protocol:
        # 1. If the properties were manually set on the object by the programmer prior to the upload() call, that takes precedence over the file properties
        # 2. By default, the file time properties (create, access, modified) are set for the upload

        # this diverges from the replace() method because when upload() is called, it is assumed not to be in the drive yet, and so if the programmer
        # set the times prior to the call to upload(), they should want those to be override times.

        for file_time_field in 'modified_time', 'created_time':
            if file_time_field not in self.changes:
                setattr(self, file_time_field, media_data[file_time_field])

        self.changes['media_body'] = media_data['media']
        return(self.save())
