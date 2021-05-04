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
class ListElement(googleapps.JsonBase):

    def __init__(self, list_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = list_id
        self._levels = None

    @property
    def levels(self):
        if not self._levels:
            self._levels = [ListLevel(j, self) for j in self._json['listProperties']['nestingLevels']]
        return(self._levels)

    def get_level(self, level):
        return(self.levels[level])

class ListLevel(googleapps.JsonBase):

    @property
    def list_type(self):
        if self.glyph_symbol:
            return('unordered')
        elif self.glyph_type == 'NONE':
            return('none')
        else:
            return('ordered')

    @property
    def item_type(self):
        list_type = self.list_type
        if list_type == 'unordered':
            return(self.glyph_symbol)
        elif list_type == 'none':
            return(None)

        ordered_type = self.glyph_type
        if ordered_type in ('DECIMAL', 'ZERO_DECIMAL'):
            return('numeric')
        if ordered_type in ('ALPHA', 'UPPER_ALPHA'):
            return('alpha')
        if ordered_type in ('ROMAN', 'UPPER_ROMAN'):
            return('roman')
        raise Exception(f"Unkonwn ordered type {ordered_type}")

    @property
    def glyph_type(self):
        if 'glyphType' in self.json:
            return(self.json['glyphType'])
        return(None)

    @property
    def glyph_symbol(self):
        if 'glyphSymbol' in self.json:
            return(self.json['glyphSymbol'])
        return(None)
