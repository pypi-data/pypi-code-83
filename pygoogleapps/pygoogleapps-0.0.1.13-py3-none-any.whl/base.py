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
import re
import datetime

class JSONProperty():

    def __init__(self, property, readonly=False):
        self.property = property
        self.readonly = readonly
        self.attr = '_' + property

    def __get__(self, obj, cls=None):
        if not hasattr(obj, self.attr):
            return(None)
        return(getattr(obj, self.attr))

    def __set__(self, obj, value):
        return(setattr(obj, self.attr, value))

    def __delete__(self, obj):
       raise Exception("Not supporting json property setting yet")


class JSONObject():

    def __init__(self, property, object_class):
        self.property = property
        self.attr = '_' + property
        self.object_class = object_class

    def __get__(self, obj, cls=None):
        if not hasattr(obj, self.attr):
            return(None)
        return(getattr(obj, self.attr))

    def __set__(self, obj, value):
        # -- actually, this expects the value to be a json object that it passes to the class
        klass = self.object_class
        if type(value) in (list, tuple):
            result = []
            for item in value:
                result.append(klass(item, parent=self))
            return(setattr(obj, self.attr, result))
        else:
            setattr(obj, self.attr, klass(value, parent=self))

    def __delete__(self, obj):
       raise Exception("Not supporting json property setting yet")


def jsonbase(cls):
    # This is just shorthand for a specific interface for the classproperties
    for prop in cls.json_properties:
        setattr(cls, prop, JSONProperty(prop))

    for prop, objclass in cls.json_objects.items():
        setattr(cls, prop, JSONObject(prop, objclass))
    return(cls)

isodate = re.compile(r'(\d\d\d\d)-(\d\d)-(\d\d)')
class JsonBase():
    json_objects = {}
    json_properties = []

    def __init__(self, json, parent=None):
        self._parent = parent
        self.set_defaults()
        if json is None:
            self._json = None
        else:
            self.process_json(json)

    def set_defaults(self):
        return

    @property
    def json(self):
        return(self._json)

    @property
    def parent(self):
        return(self._parent)

    def process_json(self, jresult):
        self._json = jresult
        for param in self.json_properties + list(self.json_objects):
            camelParam = googleapps.toCamel(param)
            if camelParam in jresult:
                val = jresult[camelParam]
                if type(val) is str:
                    datepieces = googleapps.from_rfctime(val)
                    if datepieces:
                        val = datepieces
                    else:
                        dm = isodate.fullmatch(val)
                        if dm:
                            val = datetime.date(int(dm.group(1)), int(dm.group(2)), int(dm.group(3)))

                setattr(self, param, val)
