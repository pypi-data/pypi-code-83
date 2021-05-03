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
import googleapiclient.errors

import googleapps
from googleapps.serviceclient import CommitType
import copy
import datetime
import warnings
from pprint import pprint


"""
rows_available, columns_available: the boundary of spreadsheet: the number of rows or columns, regardless of whether any data is in them
nrow, ncol: the last row and column with any data in it.  Calling this requires a full data fetch. Calling last column furthermore requires iterating through every row.


"""

serial_number_base = datetime.datetime(1899,12,30)

#-------- Class-based decoratior functions
def rowcol_method(func):
    def wrapper(self, *args, **kwargs):
        if len(args) and type(args[0]) is str:
            # we expect this to be in A1:C3 format
            args = googleapps.sheets.a1_to_rowcol(args[0]) + list(args[1:])
        return(func(self, *args, **kwargs))
    return(wrapper)

def sheetrange_method(func):
    def wrapper(self, *args, **kwargs):
        if len(args) and type(args[0]) is str:
            # we expect this to be in A1:C3 format
            args = list(googleapps.sheets.parse_a1_range(args[0])) + list(args[1:])
        return(func(self, *args, **kwargs))
    return(wrapper)

def colspan_method(func):
    def wrapper(self, *args, **kwargs):
        if len(args) and type(args[0]) is str:
            # we expect this to be in A1:C3 format
            args = googleapps.sheets.parse_colspan(args[0]) + list(args[1:])
        return(func(self, *args, **kwargs))
    return(wrapper)




@googleapps.serviceclient.googleappclient
class Worksheet(googleapps.ServiceClient):
    default_api = 'sheets'
    default_api_version = 'v4'
    commit_policy=CommitType.defer_commit
    colors = {
        'black': {'red':0, 'green':0, 'blue':0},
        'white': {'red':1, 'green':1, 'blue':1},
        'blue': {'red':0, 'green':0, 'blue':1},
        'red': {'red':1, 'green':0, 'blue':0},
        'green': {'red':0, 'green':1, 'blue':0},
        'purple': {'red':1, 'green':0, 'blue':1},
        }

    api_ro_properties = ('id',)
    api_properties = ('title', 'index', 'sheet_type', 'hidden', 'right_to_left', 'tab_color',
                        'rows_available', 'columns_available', 'frozen_rows_available', 'frozen_column_count', 'hide_gridlines')


    def clear(self):
        if self.nrows:
            # just in case ncol has never been calculated, becuase it is an expensive procedure,
            # we're going to use columns_available
            self.update_cells(0,0,[list(map(lambda x: None, range(self.columns_available))) for row in range(self.nrows)])
            self._celldata=None
        # if last row is 0, it's already clear

    def delete(self):
        #TODO: handle delete if this is not actually a committed sheet
        #self.spreadsheet.batch_update( 'deleteSheet', sheetId=lambda s: s.id )
        self.spreadsheet.batch_update( 'deleteSheet', sheetId=self.id )
        for i in range(len(self.spreadsheet._worksheets)):
            if self.spreadsheet._worksheets[i].id == self.id:
                self.spreadsheet._worksheets.pop(i)
                break

    def copy_to(self, spreadsheet, copy_protection=True, title=None, keep_title=False):
        """ Takes an ID or a googleapps.sheets.Spreadsheet object, copies this worksheet into it. This is done in real time, not deferred

        Args:
            spreadsheet (googleapps.spreadsheet|str): An object or ID for the spreadsheet to which this worksheet will be copied.
            copy_protection (bool): If this worksheet has protected ranges, should they be copied? The underlying API does not copy protected data. If the owner of the destination spreadsheet is not the same as the origin spreadsheet, there may be some differences in who has edit access as the owner can always edit the spreadsheet. Defaults to True.
            title (str, optional): Specify the title of the new worksheet.
            keep_title (bool): Indicates that the title of the new worksheet shoudl be the same as the source. By default, the underlying google API will call the spreadsheet "Copy of [original title]", possibly with an iterated number after it. This will replace that name with the original title of the source.  This should only be used if the destination spreadsheet is not the source as it will immediately create a duplicate name error. Default to False.
        """

        self.commit()
        if type(spreadsheet) is str:
            spreadsheet_id = spreadsheet
            spreadsheet = None
        else:
            spreadsheet_id = spreadsheet.id
        req = self.make_request(['spreadsheets', 'sheets'],
                          'copyTo',
                          spreadsheetId=self.spreadsheet.id,
                          sheetId=self.id,
                          body={'destination_spreadsheet_id': spreadsheet_id},
        )
        if not spreadsheet:
            spreadsheet = googleapps.sheets.get(spreadsheet_id)
        new_ws = Worksheet(spreadsheet, json={'properties':req})
        if self.protected_ranges and copy_protection:
            # for next stage debuging
            for protected_range in self.protected_ranges:
                copy_protection = {}
                if 'description' in protected_range:
                    copy_protection['description'] = protected_range['description']
                if 'warning_only' in protected_range:
                    copy_protection['warning_only'] = protected_range['warning_only']
                if 'editors' in protected_range:
                    if 'users' in protected_range['editors']:
                        copy_protection['user_editors'] = protected_range['editors']['users']
                    if 'groups' in protected_range['editors']:
                        copy_protection['group_editors'] = protected_range['editors']['groups']
                    if 'domain_users_can_edit' in protected_range['editors']:
                        copy_protection['domain_editors'] = protected_range['editors']['domain_users_can_edit']

                if 'start_row_index' in protected_range['range']:
                    copy_protection['start_row'] = protected_range['range']['start_row_index']
                if 'start_column_index' in protected_range['range']:
                    copy_protection['start_column'] = protected_range['range']['start_column_index']
                if 'end_row_index' in protected_range['range']:
                    copy_protection['last_row'] = protected_range['range']['end_row_index']-1
                if 'end_column_index' in protected_range['range']:
                    copy_protection['last_column'] = protected_range['range']['end_column_index']-1

                if 'unprotected_ranges' in protected_range:
                    copy_protection['unprotected_ranges'] = [
                        {
                            'row':  upr['start_row_index'],
                            'column':  upr['start_column_index'],
                            'last_row':  upr['end_row_index']-1,
                            'last_column':  upr['end_column_index']-1,
                        } for upr in protected_range['unprotected_ranges']
                    ]
                new_ws.protect(**copy_protection)
            new_ws.commit()

        if title:
            new_ws.title = title
            new_ws.commit()
        elif keep_title:
            new_ws.title = self.title
            new_ws.commit()
            #spreadsheet.commit()
        return(new_ws)

    def record_value_change(self, property, cleared=False):
        if cleared:
            del self.changes[property]
        elif property == 'tab_color':
            raise Exception("Not handled yet")
        elif property in ('frozen_row_count', 'frozen_column_count', 'hide_gridlines'):
            camelprop = googleapps.toCamel(property)
        elif property == 'rows_available':
            camelprop = 'row_count'
        elif property == 'columns_available':
            camelprop = 'column_count'

            self.batch_update(
                'updateSheetProperties',
                properties={'sheetId': lambda s: s.id, 'gridProperties': {camelprop, getattr(self, property)} },
                fields='gridProperties.' + camelprop,
            )
            raise Exception("Not handled yet")
        else:
            camelprop = googleapps.toCamel(property)
            self.batch_update(
                'updateSheetProperties',
                properties={'sheetId': lambda s: s.id, camelprop: getattr(self, property)},
                fields=camelprop,
            )

    def __init__(self, spreadsheet, json=None, **default_params):
        super().__init__()
        self.spreadsheet = spreadsheet

        for property, val in default_params.items():
            if property not in self.api_properties + self.api_ro_properties:
                raise Exception("Unknown parameter " + property)
            setattr(self, '_' + property, val)

        if json:
            self.process_json(json)

        self.protected_requests = []
        self._celldata = None
        self._celldata_type = None
        self._ncolumns = None
    #def process_spreadsheet_json_response(self, json):
        # this function is primarily used to extract the sheet-specific json from a full response from a spreadsheet get/create call
        #

    def process_new_worksheet_json(self, json):
        # this is broken as it doesn't allow for multiple batches
        return(self.process_json(json['replies'][0]['addSheet']))

    def process_json(self, json):

        # Note/TODO: This doesn't provide support to clear a field by setting to None.  Is that an issue?
        # -- first handle the properties
        json = googleapps.unCamel(json)
        self._original_json = json

        #-- first do properties
        params = googleapps.unCamel(json['properties'], flatten=True)

        self._id = params['sheet_id']
        self._columns_available = params['column_count']
        self._rows_available = params['row_count']
        for field in ('frozen_row_count', 'frozen_column_count', 'title', 'index'):
            if field in params and params[field] is not None:
                setattr(self, '_' + field, params[field])
            #TODO: unknown parameters are not being caught and killed
            # therea re at least red,green,blue that need to be accounted for
            # herd
            # if property not in self.api_properties:
            #    print("TODO: Ignoring unknown parameter " + param)
            #if params[param] is not None:
            #    setattr(self, '_' + property, params[param])

        # -- other core fields
        if 'merges' in json:
            self._merges = json['merges']
        if 'protected_ranges' in json:
            self._protected_ranges = json['protected_ranges']
        else:
            self._protected_ranges = None
        # -- then the data
        if 'data' in json:
            self._celldata = json['data'][0]
            self._celldata_type = 'grid'

    def process_spreadsheet_values_json(self, json):
        json = googleapps.unCamel(json)
        if json['major_dimension'] != 'ROWS':
            raise Exception("no logic to process columns yet")
        if 'values' in json:
            self._celldata = json['values']
        else:
            self._celldata = []
        self._celldata_type = 'values'

    @property
    def celldata_type(self):
        if not self._celldata_type:
            self.celldata
        return(self._celldata_type)

    @property
    def celldata(self):
        if self._celldata:
            return(self._celldata)

        # make the call
        # this can be a problem if the rows_available or columns_available is out of sync with the current sheet

        self.commit() #-- this is necessary in case we are refreshing.
        self.make_request(['spreadsheets', 'values'], 'get',
                          spreadsheetId=self.spreadsheet.id,
                          range=googleapps.sheets.range_to_a1(0,0,self.rows_available-1, self.columns_available-1, worksheet=self),
                          callback=self.process_spreadsheet_values_json
        )
        return(self._celldata)

    def refresh(self):
        self._celldata = None
        return(self.celldata)

    @property
    def protected_ranges(self):
        return(self._protected_ranges)


    def get_values(self):
        if self.celldata_type == 'values':
            # should this be a copy?
            return(copy.deepcopy(self.celldata))

        raise Exception("TODO: get_values from grid data")

    @sheetrange_method
    def get_range(self, start_row, start_col, end_row=None, end_col=None):

        if end_row is None:
            end_row = start_row
        if end_col is None:
            end_col = start_col

        result_data = []

        if self.celldata_type == 'values':

            rowdata = []
            for irow in range(start_row, end_row+1):
                if irow >= len(self.celldata):
                    break
                row = []
                for icol in range(start_col, end_col+1):
                    if icol >= len(self.celldata[irow]):
                        break
                    row.append(self.celldata[irow][icol])
                rowdata.append(row)
            return(rowdata)


        raise Exception("NEed to re-evaluate how ranges are done for grid data")

        for irow in range(start_row, end_row+1):

            if irow >= len(self.celldata['row_data']):
                # no more data
                # TODO: Verify this is the correct assumption
                # if it's the end of the sheet, we don't append blank rows
                # we could append(None) to have a matrix exactly as long as requested
                break
            for icol in range(start_col, end_col+1):
                if 'values' not in self._celldata['row_data'][irow]:
                    # this is a blank row.
                    rowdata.append(None)
                elif icol >= len(self._celldata['row_data'][irow]['values']):
                    # TODO: Verify this is the correct assumption
                    # same as the prior: if this is a column request past the point with information, we just break out
                    # and don't pad the array. This can lead to rows that have different lengths
                    # Alternatively, we could append(None) to have a matrix exactly as long as requested
                    break
                elif not 'effective_value' in self._celldata['row_data'][irow]['values'][icol]:
                    rowdata.append(None)
                else:
                    celldata = self._celldata['row_data'][irow]['values'][icol]['effective_value']

                    if 'string_value' in celldata:
                        rowdata.append(celldata['string_value'])
                    elif 'number_value' in celldata:
                        rowdata.append(celldata['number_value'])
                    elif 'boolean_value' in celldata:
                        rowdata.append(celldata['boolean_value'])
                    else:
                        print("Failed to append (" + str(irow) + "," + str(icol) + ")")
                        print('Cell data is :', celldata)
                        raise Exception("don't know the data in this cell!")

            result_data.append(rowdata)
        return(result_data)

    @sheetrange_method
    def get_row(self, *args):
        data = self.get_range(*args)
        if len(data) > 1:
            raise Exception("get_rows should be provided with a range that is just one row")
        return(data[0])

    @rowcol_method
    def get_cell(self, row, col):
        data = self.get_range(row,col,row,col)
        if len(data) > 1 or len(data[0]) > 1:
            raise Exception("get_cell should be provided with a range that is just one cell")
        if not data or not data[0]:
            return(None)
        return(data[0][0])





    def batch_update(self, request_type, **parameters):
        # this is an encapsulation failure
        # TODO: let the singleton service queue up the requests in order

        if self.last_request and self.last_request.function == 'batchUpdate' and not self.debug_commit:
            self.last_request.append('body', 'requests', {request_type: parameters})
        else:
            self.add_request('spreadsheets', 'batchUpdate',
                spreadsheetId=lambda s: s.spreadsheet.id,
                body={
                    'requests': [ {request_type: parameters} ]
                })

    def update_row(self, row, *args, **kwargs):
        self.update_dimension_properties('rows', row, row, *args, **kwargs)

    def update_rows(self, start_row, end_row, *args, **kwargs):
        self.update_dimension_properties('rows', start_row, end_row, *args, **kwargs)

    def update_column(self, column, *args, **kwargs):
        self.update_dimension_properties('columns', column, column, *args, **kwargs)

    def update_columns(self, start_column, end_column, *args, **kwargs):
        self.update_dimension_properties('columns', start_column, end_column, *args, **kwargs)

    def update_dimension_properties(self, dimension_type, start, end, size=None, hidden=None):
        properties = {}
        if size:
            properties['pixelSize'] = size
        if hidden is not None:
            properties['hiddenByUser'] = hidden

        if not properties:
            raise Exception("update dimension called for " + dimension_type + ", but no properties set/changed")

        self.batch_update(
            'updateDimensionProperties',
            range=self.dimension_range(dimension_type, start, end),
            properties=properties,
            fields='*',
        )


    def append_rows(self, count):
        return(self.append_dimension('rows', count))

    def append_columns(self, count):
        return(self.append_dimension('columns', count))

    def append_dimension(self, dimension_type, count):
        self.batch_update(
            'appendDimension',
            sheetId=lambda s: s.id,
            dimension=dimension_type.upper(),
            length=count
        )
        if dimension_type.lower() == 'rows':
            self._rows_available += count
        elif dimension_type.lower() == 'columns':
            self._columns_available += count
        else:
            raise Exception("Unknown dimension " + str(dimension_type))

    def delete_row(self, row): return(self.delete_dimension('ROWS', row))
    def delete_rows(self, start, end=None): return(self.delete_dimension('ROWS', start, end))
    def delete_column(self, column): return(self.delete_dimension('COLUMNS', column))
    def delete_columns(self, start, end=None): return(self.delete_dimension('COLUMNS', start, end))

    def delete_dimension(self, dimension_type, start, end=None):
        self.batch_update(
            'deleteDimension',
            range=self.dimension_range(dimension_type, start, end)
        )
        if end:
            count = end - start
        else:
            count = 1

        if dimension_type.lower() == 'rows':
            self._rows_available -= count
            # if this overlaps with rows with data, we need to update that too
            if start < self.nrows:
                # we need to remove these from the celldata array
                if start + count < self.nrows:
                    del self.celldata[start:(start+count)]
                else:
                    del self.celldata[start:self.nrows]
        elif dimension_type.lower() == 'columns':
            self._columns_available -= count

            # if ncolumns has been calculated, adjust it too
            if start < self.ncolumns:
                raise Exception('TODO: handle column deletes when data is present')
        else:
            raise Exception("Unknown dimension " + str(dimension_type))

    def _addif(self, ref, param, data):
        if param in data and data[param] is not None:
            ref[googleapps.toCamel(param)] = data[param]
            del data[param]



    def boolean_condition(self, condition_type, values=None):
        translate_condition = {
            '>': 'NUMBER_GREATER',
            '>=': 'NUMBER_GREATER_THAN_EQ',
            '<': 'NUMBER_LESS',
            '<=': 'NUMBER_LESS_THAN_EQ',
            '==': 'NUMBER_EQ',
            #HACK
            #            '=': 'NUMBER_EQ',
            '=': 'TEXT_EQ',
            '!=':'NUMBER_NOT_EQ',
            '<>':'NUMBER_NOT_EQ',
            'BETWEEN': 'NUMBER_BETWEEN',
            'NOT_BETWEEN': 'NUMBER_NOT_BETWEEN',
            'CONTAINS': 'TEXT_CONTAINS',
            'NOT_CONTAINS': 'TEXT_NOT_CONTAINS',
            'STARTS_WITH': 'TEXT_STARTS_WITH',
            'ENDS_WITH': 'TEXT_ENDS_WITH',
            'EQ': 'TEXT_EQ',
            'EMAIL': 'TEXT_IS_EMAIL',
            'URL': 'TEXT_IS_URL',
            'DATE_EQ': 'DATE_EQ',
            'DATE_BEFORE': 'DATE_BEFORE',
            'DATE_AFTER': 'DATE_AFTER',
            'DATE_ON_OR_BEFORE': 'DATE_ON_OR_BEFORE',
            'DATE_ON_OR_AFTER': 'DATE_ON_OR_AFTER',
            'DATE_BETWEEN': 'DATE_BETWEEN',
            'DATE_NOT_BETWEEN': 'DATE_NOT_BETWEEN',
            'DATE_IS_VALID': 'DATE_IS_VALID',
            'ONE_OF_RANGE': 'ONE_OF_RANGE',
            'ONE_OF_LIST': 'ONE_OF_LIST',
            'BLANK': 'BLANK',
            'NOT_BLANK': 'NOT_BLANK',
            'CUSTOM_FORMULA': 'CUSTOM_FORMULA',
        }

        condition = {}
        if values is not None:
            condition['values'] = list(map(lambda v:{'userEnteredValue':v}, values))
        # now for conditions
        condiition_type = condition_type.upper()
        if condition_type in translate_condition:
            condition['type'] = translate_condition[condition_type]
        else:
            raise Exception("Unknown condition type '" + condition_type + "'")
        return(condition)

    @sheetrange_method
    def add_conditional_formatting(self, start_row, start_column, last_row, last_column, rule_type, format, values=None):

        #TODO: GradientRule
        self.batch_update(
            'addConditionalFormatRule',
            rule={
                'ranges': [self.grid_range(start_row, start_column, last_row, last_column)],
                'booleanRule': {
                    'condition': self.boolean_condition(rule_type, values),
                    'format': format.cellformat_json(),
                },
            },
        )

    @sheetrange_method
    def add_data_validation(self, start_row, start_column, last_row, last_column, validation_type, values=None, required=True, input_message=None, show_dropdown=False):
        request = {
            'strict': required,
            'showCustomUi': show_dropdown,
            'condition': self.boolean_condition(validation_type, values),
        }

        if input_message is not None:
            request['inputMessage'] = input_message

        self.batch_update(
            'setDataValidation',
            range=self.grid_range(start_row, start_column, last_row, last_column),
            rule=request,
        )

    @sheetrange_method
    def unmerge_cells(self, start_row, start_column, last_row, last_column):
        self.batch_update(
            'unmergeCells',
            range=self.grid_range(start_row, start_column, last_row, last_column)
        )

    @sheetrange_method
    def merge_cells(self, start_row, start_column, last_row, last_column, merge_type='merge_all'):
        merge_type = merge_type.upper()
        if merge_type and merge_type not in ('MERGE_ALL', 'MERGE_ROWS', 'MERGE_COLUMNS'):
            raise Exception("Unknown merge_type '"+merge_type+"'")

        self.batch_update(
            'mergeCells',
            mergeType=merge_type,
            range=self.grid_range(start_row, start_column, last_row, last_column)
        )

    def freeze_rows(self, number_frozen):
        self.batch_update(
            'updateSheetProperties',
            properties={
                'sheetId': lambda s: s.id,
                'gridProperties': {'frozenRowCount': number_frozen},
                },
            fields='gridProperties.frozenRowCount'
        )

    def freeze_columns(self, number_frozen):
        self.batch_update(
            'updateSheetProperties',
            properties={
                'sheetId': lambda s: s.id,
                'gridProperties': {'frozenColumnCount': number_frozen},
            },
            fields='gridProperties.frozenColumnCount'
        )

    def freeze_panes(self, rows_frozen, columns_frozen):
        self.batch_update(
            'updateSheetProperties',
            properties={
                'sheetId': lambda s: s.id,
                'gridProperties': {
                    'frozenColumnCount': columns_frozen,
                    'frozenRowCount': rows_frozen},
            },
            fields='gridProperties.frozenColumnCount,gridProperties.frozenRowCount'
        )

    @sheetrange_method
    def autofilter(self, row=0, column=0, last_row=None, last_column=None, sort_specification=None, criteria=None):
        """ Apply the 'Basic Filter' to the sheet with the specified range.

        Args:
            range {GridRange}: the area to convert into a filter. By default, A1 to the last row and column. User can specify any set of parameters and the default will fill in the rest.
            sort_specification {dict} [optional]: a SortSpec json object. See https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#BasicFilter
            criteria {dict} [optional]: a FilterCriteria json object. See https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#BasicFilter
         """
        if last_row is None:
            last_row = self.nrows - 1
        if last_column is None:
            last_column = self.ncolumns - 1

        self.batch_update(
            'setBasicFilter',
            filter={
                'range':self.grid_range(row, column, last_row, last_column),
                'sortSpecs': sort_specification,
                'criteria': criteria,
            }
        )

    def clear_autofilter(self):
        """ Clears the existing autofilter. A sheet can only have on 'Basic Filter', so no parameters are needed. """

        self.batch_update(
            'clearBasicFilter',
            sheetId=lambda s: s.id,
        )


    @sheetrange_method
    def sort_range(self, row, column, last_row, last_column, *sort_specifications):
        """ sort a range in the spreadsheet.  sort specifications should be an array as follows:

            Empty array: sort the first column in the range, ascending
            {int}: A simple specification to indicate the column_offset to sort in ascending order
            {object of {'coloffset': int, 'reverse': bool}} reverse  is technically optional"""


        if not sort_specifications:
            specification = [{'dimensionIndex': 0}]
        else:
            specification = []
            for coldef in sort_specifications:
                if type(coldef) is int:
                    specification.append({'dimensionIndex': coldef, 'sortOrder': 'ASCENDING'})
                else:
                    sortdef = {'dimensionIndex': coldef['coloffset'], 'sortOrder': 'ASCENDING'}
                    if 'reverse' in coldef and coldef['reverse']:
                        sortdef['sortOrder'] = 'DESCENDING'
                    specification.append(sortdef)


        self.batch_update(
            'sortRange',
            range=self.grid_range(row, column, last_row, last_column),
            sortSpecs=specification
        )
        #
        # TODO: the result value returns the reordered data, so we should incorporate that more elegantly
        #
        self._celldata = None

    def protect(self, start_row=None, start_column=None, last_row=None, last_column=None, user_editors=None, group_editors=None, description=None, warning_only=False, unprotected_ranges=None, domain_editors=None):
        request = {'warningOnly':warning_only}
        if description:
            request['description'] = description

        if user_editors or group_editors:
            request['editors'] = {}
            if user_editors: request['editors']['users'] = user_editors
            if group_editors: request['editors']['groups'] = group_editors
        else:
            # TODO: the editors field needs to be restricted somehow, otherwise anyone with whom it is shared
            # can edit... Which is not what most people expect.
            # So a more elegant solution needs to be foound. Maybe adding self explicilty as the only editor?
            request['editors'] = {'domainUsersCanEdit':False}

        if domain_editors:
            request['editors']['domainUsersCanEdit'] = True

        if start_row is None and start_column is None and last_row  is None and last_column is None:
            #- sheet level protections
            request['range'] = {'sheetId': lambda s: s.id}
        elif start_row is not None and last_row:
            if start_column is not None and last_column:
                # full range
                request['range'] = self.grid_range(start_row, start_column, last_row, last_column)
            else:
                # just a set of rows
                request['range'] = self.grid_range(start_row, start_column, last_row, last_column)
        elif start_column is not None and last_column:
            # just a set of columns
            request['range'] = self.grid_range(start_row, start_column, last_row, last_column)

        else:
            raise Exception("Grid range not complete!")

        if unprotected_ranges:
            request['unprotectedRanges'] = list(map(lambda up: self.grid_range(**up), unprotected_ranges ))

        # TODO: what about domainUsersCanEdit
        # we can have multiple protected ranges, but only one sheet-level protection.
        # So die if that happens

        if 'startRowIndex' not in request['range'] and self.protected_requests:
            for prior in self.protected_requests:
                if 'startRowIndex' not in prior['request']['range']:
                    raise Exception("Can only protect a sheet one time")

        self.protected_requests.append({'request': request, 'type': 'new', 'unprotect': []})

        #if self.last_request and self.last_request.function == 'batchUpdate' and not self.debug_commit:
        #    self.last_request.append('body', 'requests', {request_type: parameters})
        #else:
        #self.batch_update('addProtectedRange',protectedRange=request)

    @sheetrange_method
    def unprotect(self, start_row, start_column, last_row, last_column, user_editors=None, group_editors=None, description=None, warning_only=False):

        request = {}
        # TODO: This is currently limited to sheets that have already been protected.
        # Also need to verify whether this is additive
        for protected_request in self.protected_requests:
            if 'start_row_index' not in protected_request['request']['range'] or (
                    # see if the unprotected request falls within here
                    start_row >= protected_request['request']['range']['start_row_index']
                    and last_row <= protected_request['request']['range']['end_row_index']
                    and start_column >= protected_request['request']['range']['end_column_index']
                    and last_column <= protected_request['request']['range']['end_column_index']
                    ):

                # TODO: this doesn't handle the istuation where we add a new protected range
                # and then try to unprotect cells in a different range
                protected_request['unprotect'].append(self.grid_range(start_row, start_column, last_row, last_column))
                return(True)
        else:
            # check to see if adding editors to an an existing protected range
            # if it is, we'll convert it to a request
            for protected in self.protected_ranges:
                if 'start_row_index' not in protected['range'] or (
                    # see if the unprotected request falls within here
                    start_row >= protected['range']['start_row_index']
                    and last_row <= protected['range']['end_row_index']
                    and start_column >= protected['range']['end_column_index']
                    and last_column <= protected['range']['end_column_index']
                    ):
                    #--- it would appear that this unprotected request
                    # falls within this range
                    # so we'll add the update request
                    # and return
                    if 'unprotected_ranges' in protected:
                        unprotected_ranges = protected['unprotected_ranges']
                    else:
                        unprotected_ranges = []

                    # add it here
                    unprotected_ranges.append(self.grid_range(start_row, start_column, last_row, last_column))

                    self.protected_requests.append({
                        'type': 'update',
                        'request': protected,
                        'unprotect': unprotected_ranges,
                    })
                    return(True)

        # if we got here, we couldn't find a protected range
        # that matches here
        raise Exception("Sheet not protected. Cannot add uprotected section.")

    #    if unprotected_ranges:
    #        request['unprotectedRanges'] = list(map(lambda up: self.grid_range(**up), unprotected_ranges ))

        # TODO: what about domainUsersCanEdit
#        self.batch_update('addProtectedRange', protectedRange=request, fields='unprotectedRanges')


    def commit(self):
        # if there is a protection request, add it
        if self.protected_requests:
            for protected_request in self.protected_requests:
                request = protected_request['request']
                if len(protected_request['unprotect']):
                    request['unprotectedRanges'] = protected_request['unprotect']

                if protected_request['type'] == 'new':
                    self.batch_update('addProtectedRange', protectedRange=request)

                elif protected_request['type'] == 'update':
                    self.batch_update(
                        'updateProtectedRange',
                        protectedRange={
                            'protectedRangeId': protected_request['request']['protected_range_id'],
                            'unprotectedRanges': protected_request['unprotect'],
                        },
                        fields='unprotectedRanges',
                    )

            # clear this out so it doesn't get processed a second time on a second commit
            self.protected_requests = []
        try:
            result = super().commit()
        except googleapiclient.errors.HttpError as he:
            # catch and rethrow certain errors
            import sys
            exc_class, exc, tb = sys.exc_info()
            reason = he._get_reason()

            #
            # Recode errors that exceed the width or height of the spreadsheet to IndexError
            #
            update_out_of_bounds = re.match('Invalid requests\[\d+\].updateCells: GridCoordinate.(\w\w\w)\w*\[(\d+)\] is after last (row|col) in grid\[(\d+)\]', reason)
            if update_out_of_bounds:
                raise IndexError("Attempt to commit updates to Google Spreadsheet '"+self.spreadsheet.title+"', Worksheet '"+self.title+"': Cell specified to update in " + update_out_of_bounds.group(1) + " " + str(update_out_of_bounds.group(2)) + ", which is after the last "+update_out_of_bounds.group(3)+" ("+update_out_of_bounds.group(4)+")") from he

            #
            # default is to also modify the error message to add in information about the spreadsheet and worksheet
            #
            # This may be misguided, but I find the default HttpError messages to not be useful for large automations,
            # So I'm adding details here to at least reference the worksheet by name.
            #
            import json
            jsoncontent = json.loads(he.content)
            jsoncontent['error']['message'] += " (error occurred when commiting changes to Spreadsheet '"+self.spreadsheet.title+"', Worksheet '"+self.title+"')"
            he.content = json.dumps(jsoncontent).encode('utf-8')
            raise

        return(result)


    @property
    def nrows(self):
        if self.celldata is None:
            return(0)
        return(len(self.celldata))

    @property
    def ncolumns(self):
        # check if ncolumns is cached OR if there are no rows
        if self._ncolumns is not None or not self.nrows:
            return(self._ncolumns)

        self._ncolumns = 0
        for i in range(len(self.celldata[0])):
            if len(self._celldata[i]) > self._ncolumns:
                self._ncolumns = len(self._celldata[i])
        return(self._ncolumns)

    def insert_rows(self, index, count, data_matrix=None, inherit_prior_style=True, format=None):
        self.insert_dimensions('ROWS', index, count, data_matrix, inherit_prior_style, format)

    def insert_row(self, index, values=None, inherit_prior_style=True, format=None):
        self.insert_dimensions('ROWS', index, 1, values, inherit_prior_style, format)

    def insert_column(self, index, values=None, inherit_prior_style=True, format=None):
        self.insert_dimensions('COLUMNS', index, 1, values, inherit_prior_style, format)

    def insert_columns(self, index, count, data_matrix=None, inherit_prior_style=True, format=None):
        self.insert_dimensions('COLUMNS', index, count, data_matrix, inherit_prior_style, format)

    def insert_dimensions(self, dimension_type, index, count, value_matrix=None, inherit_prior_style=True, format=None):

        dimension_type = dimension_type.upper()

        if dimension_type == 'ROWS':
            if index > self.nrows:
                raise Exception("Attempt to insert new rows at index " + str(index) + " cannot be done because the worksheet does not have " + str(index) + " rows to begin with!")
        elif dimension_type == 'COLUMNS':
            if index > self.ncolumns:
                raise Exception("Attempt to insert new columns at index " + str(index) + " cannot be done because the worksheet does not have " + str(index) + " columns to begin with!")
        else:
            raise Exception("Unknown dimension " + str(dimension_type))

        self.batch_update(
            'insertDimension',
            range={
                'sheetId':lambda s: s.id,
                'dimension':dimension_type,
                'startIndex': index,
                'endIndex': index + count,
            },
            inherit_from_before=inherit_prior_style,
        )

        if dimension_type == 'ROWS':
            self._rows_available += count
        elif dimension_type == 'COLUMNS':
            self._columns_available += count
        else:
            raise Exception("Unknown dimension " + str(dimension_type))


        if value_matrix or format:
            self.update_cells(index, 0, value_matrix, format)


    def append(self, row, format=None):
        """ adds a single row to the end of the worksheet."""
        # last_row is not a variable, so we just need to add it to celldata

        if type(row[0]) in (list, tuple):
            raise Exception("Should not append a matrix - append is for a single row at a time. Use Extend")

        # add more rows if we have exceeded the sheet
        if self.nrows + 1 >= self.rows_available:
            self.append_rows(250)

        result = self.update_cells(self.nrows, 0, row, format=format)
        self._celldata.append(row)
        return(result)


    def extend(self, rows, format=None):
        """ adds a set of rows to the end of the worksheet."""
        # last_row is not a variable, so we just need to add it to celldata

        if type(rows[0]) not in (list, tuple):
            raise Exception("extend should be a matrix - e.g. a list of lists.")

        # add more rows if we have exceeded the sheet
        if self.nrows + len(rows) >= self.rows_available:
            nexthundred = (int((self.nrows + len(rows) - self.rows_available) / 100) + 2) * 100
            self.append_rows(nexthundred)

        result = self.update_cells(self.nrows, 0, rows, format=format)
        self._celldata.extend(rows)
        return(result)


    @sheetrange_method
    def update_format(self, row, column, last_row, last_column, cellformat):
        #if 'right_border' in cellformat:
        #    import pdb
        #    pdb.set_trace()

        if type(cellformat) is dict:
            cellformat = googleapps.sheets.Format(**cellformat)

        # normal formatting

        format_json = cellformat.cellformat_json()

        prepared_rows = []
        for valuerow in range(row,last_row+1):
            prepared_rows.append({'values': [ {'userEnteredFormat': format_json} for j in range(column, last_column+1) ]})

        fields = cellformat.fieldmask_fields()
        self.batch_update('updateCells',
                          rows=prepared_rows,
                          start=self.grid_coordinate(row, column),
                          #range=self.grid_range(row, column, last_row, last_column),
                          fields=','.join(['userEnteredFormat.' + f for f in fields]),
                          )

    @rowcol_method
    def update_cells(self, row, column, values=None, format=None):

        request = {}
        fields_active = ['userEnteredValue']
        #-----------------------------------
        # Process Formatting

        if format:
            if type(format) is dict:
                format = googleapps.sheets.Format(**format)
            # normal formatting
            format_json = format.cellformat_json()
            if format_json:
                fields_active.extend(googleapps.json_fieldmask({'userEnteredFormat':format_json}))
        else: format_json = None

        #-----------------------------------
        # TODO: Data Validation!
        # We can add it here!
        #

        #-----------------------------------
        # Actual Data! get everything into matrix format!
        if type(values) not in (list,tuple):
            values = [ values ]
        if len(values) and type(values[0]) not in (list,tuple):
            values = [ values ]

        prepared_rows = []
        for valuerow in values:
            prepared_row = []
            for cell in valuerow:
                # single cell value
                if type(cell) is dict:
                    prepared_row.append(cell)
                else:
                    celljson = {'userEnteredValue': self.extended_value(cell) }
                    if format_json:
                        celljson['userEnteredFormat'] = format_json
                    prepared_row.append(celljson)
            prepared_rows.append({'values': prepared_row})


        self.batch_update('updateCells',
                          start=self.grid_coordinate(row, column),
                          rows=prepared_rows,
                          fields=','.join(fields_active) # TODO < this isn't robust
        )

        '''
        don't do this now
        # now process the range/cell protection
        # it may eventually be more efficient to have this done after the fact, at the end of batch processing
        # but for now, we do it real time
        if format and format.locked is not None:
            meat = {}
            if format.locked:
                meat = {'protectedRange':self.grid_range(row, col, row+len(rows), col+len(rows[0]))}
            else:
                meat = {'unprotectedRanges':[self.grid_range(row, col, row+len(rows), col+len(rows[0]))]}

            self.services.add_request('spreadsheets', 'batchUpdate', {
            'spreadsheetId': self.workbook.id,
            'body': {
                'addProtectedRange': meat,
                }
            })
        '''

    @classmethod
    def extended_value(self, cell_value):

        if cell_value is dict or cell_value is None:
            # we assume they already processed this
            # None is the same as blank, won't update anything
            return(cell_value)

        # okay, it's something
        t = type(cell_value)
        if t is str:
            # is it a formula?
            if len(cell_value) and cell_value[0] == '=':
                return({'formulaValue': cell_value})
            else:
                return({'stringValue': cell_value})

        elif t is int or t is float:
            return({'numberValue': cell_value})

        elif t is bool:
            return({'boolValue': cell_value})

        # todo: should this be rendered as a number in SERIAL__NUMBER format
        # from the docs: The whole number portion of the value (left of the decimal) counts the days since December 30th 1899. The fractional portion (right of the decimal) counts the time as a fraction of the day. For example, January 1st 1900 at noon would be 2.5
        elif t is datetime.date:
            diff = cell_value - serial_number_base.date()
            return({'numberValue': diff.days})
        elif t is datetime.datetime:
            diff = cell_value - serial_number_base
            return({'numberValue': diff.total_seconds() / 60 / 60 / 24})

        raise TypeError("Unknown type '"+str(t)+"' cannot be processed by update cells for this value: " + str(cell_value))


    @sheetrange_method
    def grid_range(self, row, column, last_row, last_column):
        return ({
                'sheetId': lambda s: s.id,
                "startRowIndex": row,
                "endRowIndex": last_row+1 if last_row is not None else None,
                "startColumnIndex": column,
                "endColumnIndex": last_column+1 if last_column is not None else None,
        })

    @rowcol_method
    def grid_coordinate(self, row,column):
        return ({
                'sheetId': lambda s: s.id,
                'rowIndex': row,
                'columnIndex': column,
        })

    def dimension_range(self, type, start, end=None):
        type = type.upper()
        if type not in ('ROWS', 'COLUMNS'):
            raise Exception("Dimension type '" + type + "' is unknown")

        if not end:
            end=start
        return ({
                'sheetId': lambda s: s.id,
                'dimension': type,
                'startIndex': start,
                'endIndex': end+1,
        })
