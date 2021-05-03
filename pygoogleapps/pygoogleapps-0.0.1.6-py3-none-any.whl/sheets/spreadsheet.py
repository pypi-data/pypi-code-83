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
from googleapps.serviceclient import CommitType

@googleapps.serviceclient.googleappclient
class Spreadsheet(googleapps.ServiceClient):
    default_api = 'sheets'
    default_api_version = 'v4'
    api_ro_properties = ('id',)
    api_properties = ('title', 'locale', 'auto_recalc', 'time_zone', 'default_format')
    commit_policy=CommitType.defer_commit


    def __init__(self):
        super().__init__()
        self._worksheets = []


    def commit(self):
        # TODO : let the singleton service handle commit.
        # This has problems with sync issues - what if spreadsheet things change
        # that are partly dependent on the underlying worksheettchanges?
        if self.debug:
            print("---------< COMMIT COMMIT COMMIT ")
        super().commit()
        if self.worksheets:
            for worksheet in self.worksheets:
                if self.debug:
                    print(" --------< Recursive Commit for Sheet " + worksheet.title)
                worksheet.commit()

    @property
    def active(self):
        return(self._worksheets[0])

    def add_worksheet(self, title=None, **kwargs):
        #we do the title like this so we can pass it in as an array  obj.add_worksheet("label")
        kwargs['title'] = title
        '''        json_definition = ('title', 'index', 'hidden', 'tab_color', 'right_to_left', 'sheet_id', 'sheet_type',)
        grid_properties = ('row_count', 'column_count', 'frozen_row_count', 'frozen_column_count','hide_gridlines',)
        request = self.process_api_definition('add_worksheet',
                                              kwargs,
                                              json_definition,
                                              {'grid_properties': grid_properties})
        '''
        new_worksheet = self._add_uncommited_worksheet(**kwargs)
        #TODO: This interface is not complete
        self.add_request('spreadsheets', 'batchUpdate',
                         spreadsheetId=lambda s: s.id,
                         body={
                             'requests': [{'addSheet': {'properties': {'title': new_worksheet.title }}}]
                         },
                         callback=new_worksheet.process_new_worksheet_json
                         )
        return(new_worksheet)

    def _add_uncommited_worksheet(self, **kwargs):
        new_worksheet = googleapps.sheets.Worksheet(self, rows_available=1000, columns_available=26, **kwargs)
        self._worksheets.append(new_worksheet)
        return(new_worksheet)

    def get_worksheet(self, title):
        for worksheet in self._worksheets:
            if worksheet.title == title:
                return(worksheet)
        return

    @property
    def url(self):
        return(self._url)

    @property
    def worksheets(self):
        return(self._worksheets)

    @property
    def worksheet_titles(self):
        return([ws.title for ws in self.worksheets])

    def batch_update(self, request_type, **parameters):
        if self.last_request and self.last_request.function == 'batchUpdate':
            self.last_request.append('body', 'requests', {request_type: parameters})
        else:
            self.add_request('spreadsheets', 'batchUpdate',
                spreadsheetId=lambda s: s.id,
                body={
                    'requests': [ {request_type: parameters} ]
                })


    def process_json(self, spreadsheet_json):
        self._id  = spreadsheet_json['spreadsheetId']
        self._url  = spreadsheet_json['spreadsheetUrl']
        for param in self.api_properties:
            setattr(self, '_' + param, spreadsheet_json['properties'][googleapps.toCamel(param)])

        # Process sheets
        for worksheetjson in spreadsheet_json['sheets']:
            # see if the worksheet already exists
            worksheet = self.get_worksheet_by_id(worksheetjson['properties']['sheetId'])
            if worksheet:
                # update anything that needs it
                worksheet.process_json(worksheetjson)
            else:
                # change name? Actually commited!
                worksheet = self._add_uncommited_worksheet(json=worksheetjson)
        # spreadsheet_json['sheets']
        return

    def get_worksheet_by_id(self, id):
        # encapsulated in case we ever want to move to a hashmap store
        for worksheet in self.worksheets:
            if worksheet.id == id:
                return(worksheet)
        return
