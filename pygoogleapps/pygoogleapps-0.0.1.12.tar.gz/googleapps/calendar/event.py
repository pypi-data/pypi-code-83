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
import datetime

@googleapps.jsonbase
class EventTime(googleapps.JsonBase):
    json_properties = ['date', 'date_time', 'time_zone']

@googleapps.jsonbase
class Event(googleapps.JsonBase):
    json_properties = ['id', 'status', 'html_link', 'created', 'updated', 'summary', 'description', 'location', 'creator', 'organizer', 'start', 'end', 'end_time_unspecified', 'recurrence', 'attendees']

    json_objects = {
        'start': EventTime,
        'end': EventTime,
        'originalStartTime': EventTime,
    }

    @classmethod
    def create(cls, service, calendar_id, summary, start, end, **kwargs):
        if type(start) is datetime.date:
            start = {
                'date': start.isoformat(),
            }
            end = {
                'date': end.isoformat(),
            }
        else:
            start = {
                'date_time': googleapps.to_rfctime(start),
                'time_zone': 'America/New_York'
            }
            end = {
                'date_time': googleapps.to_rfctime(end),
                'time_zone': 'America/New_York'
            }

        eventjson = service.make_request('events', 'insert', calendarId=calendar_id,
            body={
                'start':start,
                'end':end,
                'summary': summary,
                **kwargs,
        })
        return(Event(eventjson))


@googleapps.jsonbase
class EventList(googleapps.JsonBase):
    json_properties = ['etag', 'summary', 'description', 'updated', 'time_zone', 'access_role', 'default_reminders']
    json_objects = {
        'items': Event
    }

    def __getitem__(self, i):
        """ This meta-method allows the EventList object to be treated like an indexed array of Events.

        Example:
            import usl
            u = usl.USL()
            school_0 = u[0]
            """
        return(self.items[i])

    def __len__(self):
        """ This meta-method allows len() to work correctly """
        return(len(self.items))

