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


@googleapps.jsonbase
class ParagraphElement(googleapps.JsonBase):
    json_properties = ['page_break', 'column_break', 'footnote_reference', 'horizontal_rule', 'equation', 'inline_object_element', 'auto_text', 'text_run']

    def set_defaults(self):
        self._text_style = None
        self._inline_object = None

    @property
    def element_type(self):
        if self.text_run:
            return('text')

        for field in ('page_break', 'column_break', 'footnote_reference', 'horizontal_rule', 'equation', 'inline_object_element'):
            if getattr(self, field):
                return(field)

        raise Exception("Failed to determine type")

    @property
    def text(self):
        if self.text_run:
            return(self.text_run['content'])

    @property
    def text_style(self):
        if not self._text_style:
            if self.text_run:
                self._text_style = TextStyle(self.text_run['textStyle'], self)
            else:
                self._text_style = TextStyle({}, self)
        return(self._text_style)

    @property
    def inline_object_element_id(self):
        if self.element_type != 'inline_object_element':
            return
        return (self.inline_object_element['inlineObjectId'])

    @property
    def inline_object(self):
        if not self._inline_object:
            oid = self.inline_object_element_id
            if not oid:
                return
            self._inline_object = self.parent.parent.inline_objects[oid]
        return(self._inline_object)




@googleapps.jsonbase
class TextStyle(googleapps.JsonBase):

    json_properties=['bold', 'italic', 'foreground_color', 'font_size', 'weighted_font_family']

    @property
    def link(self):
        if 'link' in self.json:
            return(self.json['link']['url'])

    @property
    def font_family(self):
        if self.weighted_font_family:
            return(self.weighted_font_family['fontFamily'])


    @property
    def font_weight(self):
        if self.weighted_font_family:
            return(self.weighted_font_family['weight'])
