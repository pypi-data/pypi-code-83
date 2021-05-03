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
from .paragraphelement import ParagraphElement
import re
heading_re = re.compile(r'HEADING_(\d+)')


@googleapps.jsonbase
class BodyElement(googleapps.JsonBase):
    json_properties = ['start_index', 'end_index']

    @classmethod
    def factory(cls, json, parent):
        if 'paragraph' in json:
            return(ParagraphBody(json, parent))
        elif 'sectionBreak' in json:
            return(SectionBreakBody(json, parent))
        elif 'table' in json:
            return(TableBody(json, parent))
        elif 'tableOfContents' in json:
            return(TableOfContentsBody(json, parent))
        else:
            raise Exception("Cannot identify body element type")

class SectionBreakBody(BodyElement):
    body_type = 'section break'
    json_properties = BodyElement.json_properties + ['section_break']


class TableBody(BodyElement):
    body_type = 'table'
    json_properties = BodyElement.json_properties + ['table']

class TableOfContentsBody(BodyElement):
    body_type = 'table of contents'
    json_properties = BodyElement.json_properties + ['table_of_contents']

class ParagraphBody(BodyElement):
    body_type = 'paragraph'
    json_properties = BodyElement.json_properties + ['paragraph']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._elements = None
        self._style = None

    @property
    def bullet(self):
        if 'bullet' in self.paragraph:
            return(self.paragraph['bullet'])

    @property
    def list(self):
        if not self.bullet:
            return
        l = self.parent.lists[self.bullet['listId']]
        if 'nestingLevel' in self.bullet:
            return(l.get_level(self.bullet['nestingLevel']))
        else:
            return(l.get_level(0))

    @property
    def list_type(self):
        l = self.list
        if not l:
            return
        return(l.list_type)

    @property
    def style(self):
        if not self._style:
            self._style = ParagraphStyle(self.paragraph['paragraphStyle'])
        return(self._style)

    @property
    def paragraph_type(self):
        if self.style.name == 'NORMAL_TEXT':
            return('text')
        elif heading_re.match(self.style.name):
            return('heading')
        elif self.style.name == 'TITLE':
            return('title')
        elif self.style.name == 'SUBTITLE':
            return('subtitle')

    @property
    def heading_level(self):
        m = heading_re.match(self.style.name)
        if not m:
            return
        return(int(m.group(1)))


    @property
    def elements(self):
        if not self._elements:
            self._elements = [ParagraphElement(elem, self) for elem in self.paragraph['elements']]
        return(self._elements)


class ParagraphStyle(googleapps.JsonBase):

    @property
    def name(self):
        return(self.json['namedStyleType'])
