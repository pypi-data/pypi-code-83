import datetime
import re

import googleapps

import warnings
from pprint import pprint

#from .. import Spreadsheet, Format 

class Workbook(googleapps.sheets.Spreadsheet):

    # set up some aliases to existing functions
    get_worksheet_by_name = googleapps.sheets.Spreadsheet.get_sheet
    close = googleapps.sheets.Spreadsheet.commit
    
    @property
    def worksheets(self):
        return(self.sheets)
    
    @property
    def filename(self):
        return(self.title)
    
    @filename.setter
    def filename(self, new_filename):
        return(self.title(new_filename))
    
    def __init__(self, filename):
        # eventually should support all of the extra params
        # see http://xlsxwriter.readthedocs.io/workbook.html
        super().__init__()
        self._title = filename
        self.add_request('spreadsheets', 'create', 
            callback=self.process_json, 
            body={ 'properties': {'title': filename} },
        )        
        #self.commit()
      
    def _add_uncommited_sheet(self, **kwargs):
        new_sheet = googleapps.sheets.xlsxwriter.Worksheet(self, **kwargs)        
        self._sheets.append(new_sheet)
        return(new_sheet)
    
    def add_worksheet(self, name=None):
        #Add a new worksheet to a workbook.
        # In theory we could just alias to the superclass.....?
        
        if not len(self.sheets):
            # this is the first worksheet, which is automatically created
            # by google when we do the spreadshseets().create method. 
            # so, we just generate the uncommited reference and update
            # the sheet name.
            first_sheet = self._add_uncommited_sheet(title='Sheet1', id=0, index=0)
            if name:
                # this triggers a updateSheet request to set the title. 
                # TODO: we could potentially save this step if we went back and updated
                # the create() request to set the sheet name at that time
                first_sheet.title = name
                
            return(first_sheet)
        
        return(super().add_sheet(name))
    
    xlsx_horizontal_alignments = {'JUSTIFY':'CENTER', 'CENTER_ACROSS':'CENTER'} # < these don't exist in google        
    xlsx_vertical_alignments = {'VCENTER': 'MIDDLE', 
                              'VJUSTIFY':'MIDDLE'} # < this doesn't exist in google
        
        
    xlsxwriter_border_styles = {
        0: {'style':'NONE'},
        1: {'style':'SOLID'},
        2: {'style':'SOLID_MEDIUM'},
        3: {'style':'DASHED'},
        4: {'style':'DOTTED'},
        5: {'style':'SOLID_THICK'},
        6: {'style':'DOUBLE'},
        # the rest of these are best-example but cannot be exactly duplicated by the Google Sheets API
        7: {'style':'SOLID'}, #solid, 0
        8: {'style':'DASHED'}, #dashed, 2
        9: {'style':'DOTTED'}, #dash dot
        10: {'style':'DOTTED'}, #dash dot, 2
        11: {'style':'DASHED'}, # dash dot dot
        12: {'style':'DASHED'}, # dash dot dot, 2
        13: {'style':'DASHED'}, #slant dash dot
        }

    def add_format(self, format):
        #Create a new Format object to formats cells in worksheets.
        same_params = ('bold', 'text_wrap', 'font_size', 'italic', 'foreground') 
        mapped_params = {'bg_color': 'background'} 
        
        fmt = googleapps.sheets.Format()
        for formatkey in format:
            if formatkey in same_params:
                setattr(fmt, formatkey, format[formatkey])
        
            if formatkey in mapped_params:
                setattr(fmt, mapped_params[formatkey], format[formatkey])
        
        if 'num_format' in format:
            nf = format['num_format']
            if type(nf) is int:
                raise Exception("Have not figured this out yet")
            #import pdb
            #pdb.set_trace()
            if re.search('%', nf):
                fmt.number_format_type = 'PERCENT'
                fmt.number_format_pattern = nf
            else:
                fmt.number_format_type = 'NUMBER'
                fmt.number_format_pattern = re.sub('0', '#', nf)
#            else:
#                raise Exception("Cannot handle num format '" + str(nf) + "' yet")
                    
        if 'align' in format:
            # in xlswriter, align can handle both horizontal and vertical
            value = format['align'].upper()
            if value in googleapps.sheets.Format.horizontal_alignments:
                fmt.align = value
            elif value in googleapps.sheets.Format.vertical_alignments:
                fmt.vertical_align = value
            elif value in self.xlsx_horizontal_alignments:
                fmt.align = self.xlsx_horizontal_alignments[value]
            elif value in self.xlsx_vertical_alignments:
                fmt.vertical_align = self.xlsx_vertical_alignments[value]
            else:
                raise Exception("Unknown alignment " + format['align'].upper())

        if 'valign' in format:
            value = format['valign'].upper()
            if value in self.xlsx_vertical_alignments:
                fmt.vertical_align = self.xlsx_vertical_alignments[value]
            else:
                fmt.vertical_align = value
    
        if 'border' in format:
            fmt.border = True
    
        if 'locked' in format:
            fmt.locked = format['locked']
        else:
            fmt.locked = None
        return(fmt)
        
        
    @classmethod
    def translate_border_style(cls, style=1):
        #TODO
        return(cls.render_border_json(**xlsxwriter_border_styles[style]))
        xlsxwriter_border_styles = {
        0: {'style':'NONE'},
        1: {'style':'SOLID'},
        2: {'style':'SOLID_MEDIUM'},
        3: {'style':'DASHED'},
        4: {'style':'DOTTED'},
        5: {'style':'SOLID_THICK'},
        6: {'style':'DOUBLE'},
        # the rest of these are best-example but cannot be exactly duplicated by the Google Sheets API
        7: {'style':'SOLID'}, #solid, 0
        8: {'style':'DASHED'}, #dashed, 2
        9: {'style':'DOTTED'}, #dash dot
        10: {'style':'DOTTED'}, #dash dot, 2
        11: {'style':'DASHED'}, # dash dot dot
        12: {'style':'DASHED'}, # dash dot dot, 2
        13: {'style':'DASHED'}, #slant dash dot
        }
    
           
                
                
                
                
                

   