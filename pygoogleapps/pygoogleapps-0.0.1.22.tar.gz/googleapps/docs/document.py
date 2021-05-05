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


from pprint import pprint
import googleapps
from googleapps.serviceclient import CommitType
from .bodyelement import BodyElement
from .listelement import ListElement


@googleapps.serviceclient.googleappclient
class Document(googleapps.ServiceClient):
    default_api = 'docs'
    default_api_version = 'v1'
    api_ro_properties = ('document_id', 'revision_id', 'suggestions_view_mode', 'inline_objects')
    api_properties = ('title', )
    commit_policy=CommitType.defer_commit

    def __init__(self, *args, **kwargs):
        self._json = None
        self._body = None
        self._lists = None
        # can create a drive item as :
        # Document(id)

        # Document(name=TITLE) - create new file

        # TODO: Verify default behavior of DriveItem(single_param) is that single_param is the name. Not the ID.
        if len(args) == 1:
            kwargs['document_id'] = args[0]
        elif len(args) > 1:
            raise Exception("googleapps.drive objects do not provide support for more than one ordered argument")

        super().__init__(**kwargs)

    @property
    def id(self):
        return(self.document_id)

    def load(self):
        self.make_request('documents', 'get', documentId=self.id, callback=self.process_json)

    def refresh(self):
        # at present this is no different than load
        # but we keep it separate in case we want to abstract it further sometime in the future
        self.load()

    def process_json(self, djson):
        self._document_id  = djson['documentId']
        self._json = djson
        for param in self.api_properties:
            setattr(self, '_' + param, djson[googleapps.toCamel(param)])

    @property
    def json(self):
        if not self._json:
            self.load()
        return(self._json)

    @property
    def body(self):
        if not self._body:
            self._body = [BodyElement.factory(x, self) for x in self.json['body']['content']]
        return(self._body)

    @property
    def lists(self):
        if not self._lists:
            self._lists = {key:ListElement(key, val, self) for key, val in self.json['lists'].items()}
        return(self._lists)
