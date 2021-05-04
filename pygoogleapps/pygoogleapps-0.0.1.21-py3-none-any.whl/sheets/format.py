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

import re
import warnings
from pprint import pprint

import googleapps
#from docx.enum import style

class Border(object):

    border_styles = ('STYLE_UNSPECIFIED','DOTTED','DASHED','SOLID','SOLID_MEDIUM','SOLID_THICK','NONE','DOUBLE')

    def __init__(self, style=None, color=None):
        self.style = style
        self.color = color

    @property
    def style(self): return(self._style)

    @style.setter
    def style(self, style):
        if style and style.upper() not in self.border_styles:
            raise Exception("Unrecognized border style " + style)
        self._style = style

    @property
    def color(self): return(self._color)

    @color.setter
    def color(self, color): self._color = color

    def to_json(self):
        ref = {}
        if self.style:
            ref['style'] = self.style.upper()
        if self.color:
            ref['color'] = Format.color_to_google_color(self.color)
        return ref

class CellBorder(object):

    def __init__(self, style=None, color=None):
        self._top = Border(style, color)
        self._bottom = Border(style, color)
        self._left = Border(style, color)
        self._right = Border(style, color)

    @property
    def top(self):return(self._top)
    @property
    def bottom(self):return(self._bottom)
    @property
    def left(self):return(self._left)
    @property
    def right(self):return(self._right)

    @property
    def sides(self):
        return('top', 'bottom', 'left', 'right')

    def _propogate_to_sides(self, attrib, value):
        for side in self.sides:
            setattr(getattr(self, side), attrib, value)

    @property
    def colors(self):
        return([getattr(getattr(self, side), 'color') for side in self.sides])

    @colors.setter
    def colors(self, value):
        self._propogate_to_sides('color', value)

    @property
    def styles(self):
        return([getattr(getattr(self, side), 'style') for side in self.sides])

    @styles.setter
    def styles(self, value):
        self._propogate_to_sides('style', value)

    def to_json(self):
        ref = {}
        for prop in self.sides:
            v = getattr(self, prop).to_json()
            if v:
                ref[prop] = v
        return(ref)

class Format(object):
    _number_format_type = None
    _number_format_pattern = None
    _background = None
    _foreground = None
    _padding = None
    _alignment = None
    _vertical_alignment = None
    _text_wrap = None
    _text_direction = None
    _text_format = None
    _text_rotation = None
    _hyperlink = None
    _border = None
    _align = None
    _vertical_align = None
    _text_wrap = None
    _rotation = None
    _font_name = None
    _fond_size = None
    _bold = None
    _italic = None
    _strikethrough = None
    _underline = None
    _font_size = None



    number_format_types = ('NUMBER_FORMAT_TYPE_UNSPECIFIED', 'TEXT', 'NUMBER', 'PERCENT', 'CURRENCY', 'DATE', 'TIME', 'DATE_TIME', 'SCIENTIFIC')
    color_re = re.compile(r'#?([a-fA-F0-9]{2})([a-fA-F0-9]{2})([a-fA-F0-9]{2})', re.I)

    def __init__(self, **kwargs):
        for arg in kwargs:
            if not hasattr(self, arg):
                raise Exception(type(self).__module__ + " has no property for " + str(arg))
            setattr(self, arg, kwargs[arg])

    @classmethod
    def color_json(cls, r, g, b, alpha=None):
        return ({ 'red':r, 'green': g, 'blue': b, 'alpha': alpha })

    @classmethod
    def color_8bit_to_google(cls, r, g, b, alpha=None):
        return ({ 'red':r/255, 'green': g/255, 'blue': b/255, 'alpha': alpha })

    @classmethod
    def color_to_google_color(cls, color):
        # { 'red':r, 'green': g, 'blue': b, 'alpha': alpha }
        # [ r, g, b ]
        # 0x02
        # 'red', 'yellow'
        # #ff1144
        # FF33FA
        if color is None:
            return(None)

        # if dict, assume it's already done
        if type(color) is dict:
            return(color)

        # if list, assume a list of numbers. But is it 8 bit RGB, or Google RGB? Find out!
        if type(color) is list:
            if (color[0] > 1 or color[1] > 1 or color[0] > 1) or (color[0] == color[1] == color[2] == 0):
                return(cls.color_8bit_to_google(*color))
            else:
                # google colors! in the range of 0-1
                return(cls.color_json(*color))

        # so, it's a scalar
        if type(color) is int:
                raise Exception("Have not implemented Excel's numerically indexed color format yet")

        # html color or color name?
        m = cls.color_re.match(color)
        if not m:
            # Not a hex value, hopefully it is an actual color. Maybe we should restrict by enumeration?
            return(color)

        return( cls.color_8bit_to_google(int(m.group(1), 16), int(m.group(2), 16), int(m.group(3), 16) ))


    horizontal_alignments = ('CENTER', 'RIGHT', 'LEFT')
    vertical_alignments = ('TOP', 'MIDDLE', 'BOTTOM')

    def fieldmask_fields(self, json=None):
        fields = []
        if not json:
            json = self.cellformat_json()

        for field in json:
            if type(json[field]) is dict:
                subfields = self.fieldmask_fields(json[field])
                fields.extend([ '.'.join([field, sf]) for sf in subfields ])
            else:
                fields.append(field)
        return(fields)

    def cellformat_json(self):
        json = {}

        #--------------------------------------------------------
        # numberFormat
        if self.number_format_type:
            if type(self.number_format_type) is int: # this is a hex value
                raise Exception("Have not implemented Excel's default formats yet")
                #json['numberFormat'] = {'format': self.number_format}
            else:
                json['numberFormat'] = {'type': self.number_format_type}
            if self.number_format_pattern:
                json['numberFormat']['pattern']= self.number_format_pattern

        elif self.number_format_pattern:
                json['numberFormat'] = {'pattern': self.number_format_pattern}

        #--------------------------------------------------------
        # backgroundColor
        if self.background:
            json['backgroundColor'] = self.color_to_google_color(self.background)

        #--------------------------------------------------------
        # border

        if self.border:
            border = self.border.to_json()
            if border:
                json['borders'] = border

        #--------------------------------------------------------
        # padding
        # TODO

       #--------------------------------------------------------
        # Alignment

        if self.align:
            value = self.align.upper()
            if value not in self.horizontal_alignments:
                raise Exception("Unknown alignment format '" + value + "'")
            json["horizontalAlignment"] = value

        if self.vertical_align:
            value = self.vertical_align.upper()
            if value not in self.vertical_alignments:
                raise Exception("Unknown vertical alignment format '" + value + "'")
            json["verticalAlignment"] = value

        if self.text_wrap is not None:
            if type(self.text_wrap) is bool:
                if self.text_wrap:
                    json["wrapStrategy"] = 'WRAP'
                else:
                    json["wrapStrategy"] = 'OVERFLOW_CELL'
            else:
                # allows full support of the google lexicon
                json["wrapStrategy"] = self.text_wrap

        if self.rotation:
            json["textRotation"] = { 'angle': self.rotation }
            # also available is 'vertical': Boolean

        text_format = {}
        if self.foreground is not None:
            text_format['foregroundColor'] = self.color_to_google_color(self.foreground)

        if self.font_name:
            text_format["fontFamily"] = self.font_name

        if self.font_size:
            text_format["fontSize"] = self.font_size

        if self.bold is not None:
            text_format["bold"] = self.bold

        if self.italic is not None:
            text_format["italic"] = self.italic

        if self.strikethrough is not None:
            text_format["strikethrough"] = self.strikethrough

        if self.underline is not None:
            text_format["underline"] = self.underline

        if text_format:
            json["textFormat"] = text_format

        return( json )


        #--------------------------------------------------------

    wrap_strategies = ('OVERFLOW_CELL', 'LEGACY_WRAP', 'WRAP', 'CLIP')

        #--------------------------------------------------------

    @property
    def font_name(self):
        return(self._font_name)

    @font_name.setter
    def font_name(self, value):
        self._font_name = value


    @property
    def font_size(self):
        return(self._font_size)

    @font_size.setter
    def font_size(self, value):
        self._font_size = value


    @property
    def font_color(self):
        return(self._font_color)

    @font_color.setter
    def font_color(self, value):
        self._font_color = value



    @property
    def bold(self):
        return(self._bold)

    @bold.setter
    def bold(self, value):
        self._bold = value


    @property
    def italic(self):
        return(self._italic)

    @italic.setter
    def italic(self, value):
        self._italic = value



    @property
    def underline(self):
        return(self._underline)

    @underline.setter
    def underline(self, value):
        self._underline = value


    @property
    def strikethrough(self):
        return(self._strikethrough)

    @strikethrough.setter
    def strikethrough(self, value):
        self._strikethrough = value


    @property
    def font_script(self):
        return(self._font_script)

    @font_script.setter
    def font_script(self, value):
        self._font_script = value


    @property
    def num_format(self):
        return(self._num_format)

    @num_format.setter
    def num_format(self, value):
        self._num_format = value


    @property
    def locked(self):
        return(self._locked)

    @locked.setter
    def locked(self, value):
        self._locked = value


    @property
    def hidden(self):
        return(self._hidden)

    @hidden.setter
    def hidden(self, value):
        self._hidden = value


    @property
    def align(self):
        return(self._align)

    @align.setter
    def align(self, value):
        self._align = value


    @property
    def vertical_align(self):
        return(self._vertical_align)

    @vertical_align.setter
    def vertical_align(self, value):
        self._vertical_align = value


    @property
    def rotation(self):
        return(self._rotation)

    @rotation.setter
    def rotation(self, value):
        self._rotation = value


    @property
    def text_wrap(self):
        return(self._text_wrap)

    @text_wrap.setter
    def text_wrap(self, value):
        self._text_wrap = value



    @property
    def bg_color(self):
        return(self._bg_color)

    @bg_color.setter
    def bg_color(self, value):
        self._bg_color = value


    @property
    def fg_color(self):
        return(self._fg_color)

    @fg_color.setter
    def fg_color(self, value):
        self._fg_color = value


    def _set_border_attribs(self, border, *args, **kwargs):
        if args:
            if len(args) == 1:
                border.style = args[0]
            else:
                raise Exception("Setting border can only take one arg for the border style")
        for arg, value in kwargs.items():
            setattr(border, arg, value)


    @property
    def bottom_border(self):
        return(self.border.bottom)

    @bottom_border.setter
    def bottom_border(self, *args, **kwargs):
        self._set_border_attribs(self.border.bottom, *args, **kwargs)


    @property
    def top_border(self):
        return(self.border.top)

    @top_border.setter
    def top_border(self,  *args, **kwargs):
        self._set_border_attribs(self.border.top, *args, **kwargs)

    @property
    def right_border(self):
        return(self.border.right)

    @right_border.setter
    def right_border(self,  *args, **kwargs):
        self._set_border_attribs(self.border.right, *args, **kwargs)


    @property
    def left_border(self):
        return(self.border.left)

    @left_border.setter
    def left_border(self,  *args, **kwargs):
        self._set_border_attribs(self.border.left, *args, **kwargs)

    @property
    def border_color(self):
        return(self.border.color)

    @border_color.setter
    def border_color(self, value):
        self.border.color = value

    @property
    def border_style(self):
        return(self.border.styles)

    @border_style.setter
    def border_style(self, value):
        self.border.styles = value

    @property
    def number_format_type(self):
        return(self._number_format_type)

    @number_format_type.setter
    def number_format_type(self, value):

        if value not in self.number_format_types:
            raise Exception("Unknown number format for Google Sheets: " + str(value))
        self._number_format_type = value

    @property
    def number_format_pattern(self):
        return(self._number_format_pattern)

    @number_format_pattern.setter
    def number_format_pattern(self, pattern):
        self._number_format_pattern = pattern

    @property
    def background(self):
        return(self._background)

    @background.setter
    def background(self, color): # color should be a tuple of (r,g,b [a])
        self._background= color

    @property
    def foreground(self):
        return(self._foreground)

    @foreground.setter
    def foreground(self, color): # color should be a tuple of (r,g,b [a])
        self._foreground = color

    @property
    def border(self):
        if not self._border:
            self._border = CellBorder()
        return(self._border)

    @border.setter
    def border(self, cellborder):
        if type(cellborder) is dict:
            self._border = CellBorder(**cellborder)
        else:
            self._border = cellborder

    @property
    def padding(self):
        return(self._padding)

    @padding.setter
    def padding(self, data):
        self._padding = data

    @property
    def alignment(self):
        return(self._alignment)

    @alignment.setter
    def alignment(self, data):
        self._alignment = data

    @property
    def vertical_alignment(self):
        return(self._vertical_alignment)

    @vertical_alignment.setter
    def vertical_alignment(self, data):
        self._vertical_alignment = data

    @property
    def text_wrap(self):
        return(self._text_wrap)

    @text_wrap.setter
    def text_wrap(self, data):
        self._text_wrap = data

    @property
    def text_direction(self):
        return(self._text_direction)

    @text_direction.setter
    def text_direction(self, data):
        self._text_direction = data

    @property
    def text_format(self):
        return(self._text_format)

    @text_format.setter
    def text_format(self, data):
        self._text_format = data

    @property
    def text_rotation(self):
        return(self._text_rotation)

    @text_rotation.setter
    def text_rotation(self, data):
        self._text_rotation = data

    @property
    def hyperlink(self):
        return(self._hyperlink)

    @hyperlink.setter
    def hyperlink(self, data):
        self._hyperlink = data
