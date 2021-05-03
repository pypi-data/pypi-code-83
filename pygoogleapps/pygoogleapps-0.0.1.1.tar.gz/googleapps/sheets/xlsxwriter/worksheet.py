import re
import warnings
from pprint import pprint

import googleapps.sheets

POINT_HEIGHT_TO_INCH = 72
POINT_WIDTH_TO_INCH = 12
PIXEL_TO_INCH = 96

POINT_HEIGHT_TO_PIXEL = PIXEL_TO_INCH / POINT_HEIGHT_TO_INCH
POINT_WIDTH_TO_PIXEL = PIXEL_TO_INCH / POINT_WIDTH_TO_INCH

class Worksheet(googleapps.sheets.Worksheet):

    @googleapps.sheets.worksheet.rowcol_method
    def write(self, row, col, value, format=None):
        return(self.update_cells(row, col, value, format))
    
    @googleapps.sheets.worksheet.rowcol_method
    def write_row(self, row, col, data, format=None):
        self.update_cells(row, col, data, format)

    @googleapps.sheets.worksheet.rowcol_method
    def write_rows(self, row, col, dataset, format=None):
        self.update_cells(row, col, dataset, format)

    #---- All of these write methods could just alias write() above, but then they wouldn't 
    #     provide any typechecking
    
    @googleapps.sheets.worksheet.rowcol_method
    def write_formula(self, row, col, value, format=None):
        if type(value) is not str or value[0] != '=':
            raise Exception("Value sent to write_formula not a formula: " + str(value))
        self.update_cells(row, col, {'userEnteredValue': {'formulaValue': value}}, format)

    @googleapps.sheets.worksheet.rowcol_method
    def write_number(self, row, col, value, format=None):
        self.update_cells(row, col, {'userEnteredValue': {'numberValue': value}}, format)

    @googleapps.sheets.worksheet.rowcol_method
    def write_boolean(self, row, col, value, format=None):
        self.update_cells(row, col, {'userEnteredValue': {'booleanValue': value}}, format)

    @googleapps.sheets.worksheet.rowcol_method
    def write_url(self, row, col, url, format, string=None, tip=None):
        raise Exception("write_url not implemented yet")

    @googleapps.sheets.worksheet.rowcol_method
    def write_datetime(self, row, col, value, date_format=None):
        raise Exception("this requires some additional thought and testing")
        self._update_cells(row, col, {'numberValue': {'formulaValue': value}}, format)

    
    @googleapps.sheets.worksheet.sheetrange_method
    def merge_range(self, start_row, start_col, last_row, last_col, data=None, format=None):
        
        self.merge_cells(start_row, start_col, last_row, last_col)
        # Based on prior comments here, there can be issues here if the format includes a locked parameter
        # because the entire range has to be protected/unprotected, or the google client will throw an error

        #if 'locked' in format:
        if format.locked is not None:
            if format.locked:
                self.protect(start_row, start_col, last_row, last_col)
            else:
                self.unprotect(start_row, start_col, last_row, last_col)
            #format = format.copy()
            #del format['locked']
            
        # okay, now update the cells with the data and any additional format
        return(self.update_cells(start_row, start_col, data, format))
    
    
    def set_column(self, colspan, width):
        start,end = googleapps.sheets.parse_colspan(colspan)
        self.update_columns(start,end, size=width*POINT_WIDTH_TO_PIXEL)
        
    def set_row(self, row, height):
        self.update_rows(row,row, size=int(height*POINT_HEIGHT_TO_PIXEL))
        
    @googleapps.sheets.worksheet.sheetrange_method
    def data_validation(self, first_row, first_col, last_row, last_col, options):
        # TODO: This is only partially/minimally implemented
        val_type = options['validate']
        
        condition_params = {}
        if 'source' in options:
            condition_params['values'] = options['source']
            
        if 'error_type' in options:
            condition_params['required'] = options['error_type'].lower() == 'stop'
        
        if 'input_message' in options:
            condition_params['input_message'] = options['input_message']
#        if '' in options:
#            condition_params[''] = options['']
#        if '' in options:
#            condition_params[''] = options['']
#        if '' in options:
#            condition_params[''] = options['']
        
        
        if val_type == 'list':
            return(self.add_data_validation(
                first_row, first_col, last_row, last_col, 
                'ONE_OF_LIST', show_dropdown=True, **condition_params) 
            )
        else:
            raise Exception("Not implmented data validation of type " + str(val_type))
        
    @googleapps.sheets.worksheet.sheetrange_method
    def conditional_format(self, first_row, first_col, last_row, last_col, options):
        extra = {}
        if 'value' in options:
            extra['values'] = [options['value']] 
        elif 'values' in options:
            extra['values'] = options['values']
        
        self.add_conditional_formatting(
            first_row, first_col, last_row, last_col,
            options['criteria'], 
            format=options['format'],
            **extra             
        )
                
    @googleapps.sheets.worksheet.rowcol_method
    def freeze_panes(self, row, col, top_row=None, top_col=None):
        if top_row or top_col:
           warnings.warn('Note: Google sheets does not seem to support top_row/top_col')
        if not row:
            super().freeze_columns(col)
        elif not col:
            super().freeze_rows(row)
        else:
            super().freeze_panes(row, col)
        
    @googleapps.sheets.worksheet.rowcol_method
    def update_cells(self, row, column, values=None, format=None):
        result = super().update_cells(row, column, values, format)
        
        # the only thing extra we do is look to see if the format is locked,
        # which requires an additional call to proect the call      
        if format and format.locked is not None:
            if type(values) is list:
                if type(values[0]) is list:
                    last_row = row + len(values) - 1
                    last_column= column + len(values[0]) - 1
                else:
                    last_row = row
                    last_column= column + len(values) - 1
            else:
                last_row = row
                last_column = column
            if format.locked:
                self.protect(row, column, last_row, last_column)
            else:
                self.unprotect(row, column, last_row, last_column)
        return(result)
    
    def _process_format(self, ref):
        if type(ref) is dict:
            return 
        else:
            return ref.cellformat_json()

