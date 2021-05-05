import re
import warnings
from pprint import pprint

import googleapps

class XLSXWriterFormat(object):
    def __init__(self, **kwargs):
        for arg in kwargs:
            self.set(arg, kwargrs[arg])
    
    @classmethod 
    def render_border_json(cls, style=None, color=None):
        if style and style not in border_styles:
            raise Exception("Unknown border style '" + str(style) + "'")
        
        return ({
            'style': style,
            'color': cls.color_to_google_color(color)
            })
    
    
    @classmethod
    def translate_border_style(cls, style=1):
        return(cls.render_border_json(**xlsxwriter_border_styles[style]))
            
    
    def cellformat_json(self):
        json = {}
        raise Exception()
        
        #--------------------------------------------------------
        # numberFormat
        if self.number_format: 
            if type(sef.number_format) is int: # this is a hex value
                raise Exception("Have not implemented Excel's default formats yet")
                #json['numberFormat'] = {'format': self.number_format}
            else:
                json['numberFormat'] = {'pattern': self.number_format}
        
        #--------------------------------------------------------
        # backgroundColor    
        if self.background_color:
            if self.color_re(self.background_color):
                json['backgroundColor'] = self.render_colors(*self.bg_color)
            
        #--------------------------------------------------------
        # borders
        
        borders = {}
        if self.border_color:
            border_color = self.color_to_google_color(self.border_color)
        else: 
            # is this necessary? What happens if there is a border but no color?
            # is default black?
            border_color = self.color_to_google_color('black')

        # handle general/default border
        if self.border:
            # all borders
            border_def = {'style': self.translate_border_style(self.border),
                          'color': border_color}
            borders = {
                'top': border_def,
                'bottom': border_def,
                'left': border_def,
                'right': border_def,
            }
        
        # handle specific border data
        # Not sure if the color is/should be dependent on the style
        for border_type in ('top', 'bottom', 'left', 'right'):
            if getattr(self, border_type):
                borders.setdefault(border_type, {})
                borders[border_type]['style'] = self.translate_border_style(getattr(self, border_type))

                side_color = getattr(self, border_type_color)
                if side_color is None:
                    side_color = border_color    
                borders[border_type]['color'] = self.color_to_google_color(side_color)
                
                
        if borders:
            json['borders'] = borders            
            
        #--------------------------------------------------------
        # padding 
        # TODO 
         
         
        #--------------------------------------------------------
        # Alignment 
        if self.center_across or self.text_justlast:
            # these don't have google sheets equivalents, but we assume these are center-like
            # but if alignment is specifically specified, it will override this
            json["horizontalAlignment"] = 'center'
        
        if self.align:
            # in xlswriter, align can handle both horizontal and vertical
            if self.align in self.alignment_map:
                json["horizontalAlignment"] = self.alignment_map[self.align]
            else:
                json["verticalAlignment"] = self.vertical_alignment_map[self.align]
            
        if self.valign:
            # this can only be vertical - there is no setter in xlsxwriter for this
            json["verticalAlignment"] = self.vertical_alignment_map[self.vertical_align]

        if self.text_wrap is not None:
            if type(self.text_wrap) is bool:
                # this supports xlsxwriter, which is a boolean
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
            
        # this doesn't have an xlsxwriter equivalent        
        #    json["textDirection"] = self.
        #    json["hyperlinkDisplayType"] = self.


        text_format = {}
        if self.font_color:
            text_format['foregroundColor'] = self.color_to_google_color(self.font_color)
            
        if self.font_name:
            text_format["fontFamily"] = self.font_name

        if self.font_size:
            text_format["fontSize"] = self.font_size

        if self.bold:
            text_format["bold"] = self.bold

        if self.italic:
            text_format["italic"] = self.italic

        if self.font_strikeout:
            text_format["strikethrough"] = self.font_strikeout

        if self.underline:
            text_format["underline"] = self.underline


        if text_format:
            json["textFormat"] = text_format
        
        return( json )

        #--------------------------------------------------------
        
    wrap_strategies = ('OVERFLOW_CELL', 'LEGACY_WRAP', 'WRAP', 'CLIP')
        
    alignment_map = {'left':'LEFT', 'right':'RIGHT', 'center':'CENTER', None:'HORIZONTAL_ALIGN_UNSPECIFIED',
                     'justify':'center', 'center_across':'center'} # < these don't exist in google
        
    vertical_alignment_map = {'top':'TOP', 'vcenter': 'MIDDLE', 'bottom': 'BOTTOM', None:'VERTICAL_ALIGN_UNSPECIFIED',
                              'vjustify':'MIDDLE'} # < this doesn't exist in google
        
        #--------------------------------------------------------
                
    @property
    def font_name(self):
        return(self._font_name)

    @font_name.setter
    def set_font_name(self, value):
        self._font_name = value


    @property
    def font_size(self):
        return(self._font_size)

    @font_size.setter
    def set_font_size(self, value):
        self._font_size = value


    @property
    def font_color(self):
        return(self._font_color)

    @font_color.setter
    def set_font_color(self, value):
        self._font_color = value


    
    @property
    def bold(self):
        return(self._bold)

    @bold.setter
    def set_bold(self, value):
        self._bold = value


    @property
    def italic(self):
        return(self._italic)

    @italic.setter
    def set_italic(self, value):
        self._italic = value


    
    @property
    def underline(self):
        return(self._underline)

    @underline.setter
    def set_underline(self, value):
        self._underline = value


    @property
    def font_strikeout(self):
        return(self._font_strikeout)

    @font_strikeout.setter
    def set_font_strikeout(self, value):
        self._font_strikeout = value


    @property
    def font_script(self):
        return(self._font_script)

    @font_script.setter
    def set_font_script(self, value):
        self._font_script = value


    @property
    def num_format(self):
        return(self._num_format)

    @num_format.setter
    def set_num_format(self, value):
        self._num_format = value


    @property
    def locked(self):
        return(self._locked)

    @locked.setter
    def set_locked(self, value):
        self._locked = value


    @property
    def hidden(self):
        return(self._hidden)

    @hidden.setter
    def set_hidden(self, value):
        self._hidden = value


    @property
    def align(self):
        return(self._align)

    @align.setter
    def set_align(self, value):
        self._align = value


    @property
    def valign(self):
        return(self._valign)

    @valign.setter
    def set_valign(self, value):
        self._valign = value


    @property
    def rotation(self):
        return(self._rotation)

    @rotation.setter
    def set_rotation(self, value):
        self._rotation = value


    @property
    def text_wrap(self):
        return(self._text_wrap)

    @text_wrap.setter
    def set_text_wrap(self, value):
        self._text_wrap = value


    @property
    def text_justlast(self):
        return(self._text_justlast)

    @text_justlast.setter
    def set_text_justlast(self, value):
        self._text_justlast = value


    @property
    def center_across(self):
        return(self._center_across)

    @center_across.setter
    def set_center_across(self, value):
        self._center_across = value


    @property
    def indent(self):
        return(self._indent)

    @indent.setter
    def set_indent(self, value):
        self._indent = value


    @property
    def shrink(self):
        return(self._shrink)

    @shrink.setter
    def set_shrink(self, value):
        self._shrink = value


    @property
    def pattern(self):
        return(self._pattern)

    @pattern.setter
    def set_pattern(self, value):
        self._pattern = value


    @property
    def bg_color(self):
        return(self._bg_color)

    @bg_color.setter
    def set_bg_color(self, value):
        self._bg_color = value


    @property
    def fg_color(self):
        return(self._fg_color)

    @fg_color.setter
    def set_fg_color(self, value):
        self._fg_color = value


    @property
    def border(self):
        return(self._border)

    @border.setter
    def set_border(self, value):
        self._border = value


    @property
    def bottom(self):
        return(self._bottom)

    @bottom.setter
    def set_bottom(self, value):
        self._bottom = value


    @property
    def top(self):
        return(self._top)

    @top.setter
    def set_top(self, value):
        self._top = value


    @property
    def left(self):
        return(self._left)

    @left.setter
    def set_left(self, value):
        self._left = value


    @property
    def right(self):
        return(self._right)

    @right.setter
    def set_right(self, value):
        self._right = value


    @property
    def border_color(self):
        return(self._border_color)

    @border_color.setter
    def set_border_color(self, value):
        self._border_color = value


    @property
    def bottom_color(self):
        return(self._bottom_color)

    @bottom_color.setter
    def set_bottom_color(self, value):
        self._bottom_color = value


    @property
    def top_color(self):
        return(self._top_color)

    @top_color.setter
    def set_top_color(self, value):
        self._top_color = value


    @property
    def left_color(self):
        return(self._left_color)

    @left_color.setter
    def set_left_color(self, value):
        self._left_color = value


    @property
    def right_color(self):
        return(self._right_color)

    @right_color.setter
    def set_right_color(self, value):
        self._right_color = value

    @property
    def number_format_type(self):
        return(self._number_format_type)

    @number_format_type.setter
    def number_format_type(self, value):
        if type not in self.number_format_types:
            raise Exception("Unknown number format for Google Sheets: " + str(type))
        self._number_format_type = type
        
    @property
    def number_format_pattern(self):
        return(self._number_format_pattern)
    
    @number_format_pattern.setter
    def number_format_pattern(self, pattern):
        self._number_format_pattern = pattern
        
    @property
    def background_color(self):
        return(self._background_color)

    @background_color.setter
    def background_color(self, color): # color should be a tuple of (r,g,b [a])
        if type(color) is str:
            self._background_color = self.hex_to_color(color)
        else: self._background_color = color
            

    @property
    def borders(self):
        return(self._borders)

    @borders.setter
    def borders(self, data):
        self._borders = data

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

