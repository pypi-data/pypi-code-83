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
import datetime
from .event import *


@googleapps.serviceclient.googleappclient
class Calendar(googleapps.ServiceClient):
    default_api = 'calendar'
    default_api_version = 'v3'
    api_ro_properties = ('id', 'summary', 'description')
    #default_scope = 'https://www.googleapis.com/auth/calendar.readonly'
    default_scope = 'https://www.googleapis.com/auth/calendar'

    def __init__(self, *args, **kwargs):
        self._json = None
        # TODO: Verify default behavior of DriveItem(single_param) is that single_param is the name. Not the ID.
        if len(args) == 1:
            kwargs['id'] = args[0]
        elif len(args) > 1:
            raise Exception("googleapps.drive objects do not provide support for more than one ordered argument")

        super().__init__(**kwargs)
        self._events = None

    @property
    def calendar_id(self):
        return(self.json['id'])

    @property
    def json(self):
        if not self._json:
            self.load()
        return(self._json)

    def load(self):
        self.make_request('calendars', 'get', calendarId=self.id, callback=self.process_json)

    def process_json(self, jresult):
        self._id  = jresult['id']
        self._json = jresult
        for param in self.api_properties:
            setattr(self, '_' + param, jresult[googleapps.toCamel(param)])

    def events(self, min_date=None, max_date=None):
        if not min_date:
            min_date=datetime.datetime.now()
        if not self._events:
            eventjson = self.make_request('events', 'list', calendarId=self.id, timeMin=min_date)
            self._events = EventList(eventjson, self)
        return(self._events)

    def create_event(self, summary, start, end, **kwargs):
        e = Event.create(self, self.id, summary, start, end, **kwargs)
        self._events.append(e)