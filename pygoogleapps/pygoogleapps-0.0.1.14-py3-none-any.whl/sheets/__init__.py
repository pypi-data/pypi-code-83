import re
import googleapps
from .spreadsheet import Spreadsheet
from .worksheet import Worksheet
from .format import Format
#import googleapps.sheets.xlsxwriter
#import googleapps.sheets.openpyxl


#------------- UTILITY FUNCTIONS -----------------------

ord_a = ord('A')
def column_letter_to_integer(col):
    col = col.upper()
    strlen = len(col)
    column = 0
    for offset in range(strlen):
        column += (ord(col[strlen-offset-1]) - ord_a + 1) * 26**offset
    column -= 1
    return(column)

def column_offset_to_letter(column):
    # this translates a 0-indexed column to the appropriate letter
    if column > 25:
        string = chr(ord_a + column % 26)
        column = int(column / 26)
        while column:
            string = chr(ord_a + (column-1) % 26) + string
            column = int((column-1) / 26)
        # this is the first digit, which needs 1 subtracted for it
        # because of the letter - number conversion issue
        return(string)
    return(chr(ord_a+column))


# Presently, we do allow 'a1' if people are lazy.
# Should it be constrained to only be uppercase? A1? AA1
a1re = re.compile(r'([A-Za-z]+)(\d+)$')
def a1_to_rowcol(a1cell):
    m = a1re.match(a1cell)
    if not m:
        raise Exception("'"+a1cell+"' does not appear to actually be in A1 notation. Cannot convert.")
    return(int(m.group(2)) - 1, column_letter_to_integer(m.group(1)))

a1rangere = re.compile(r'([A-Za-z]+)(\d+):([A-Za-z]+)(\d+)$')
def parse_a1_range(a1range):
    m = a1rangere.match(a1range)
    if not m:
        # to be resilient, we'll allow "A1" to be considered a range from [1,0,1,0]
        m = a1re.match(a1range)
        if not m:
            raise Exception("'" + a1range + "' does not appear to actually be in an A1:B2 notation. Cannot parse/convert.")
        return(int(m.group(2)) - 1, column_letter_to_integer(m.group(1)), int(m.group(2)) - 1, column_letter_to_integer(m.group(1)))
    return(int(m.group(2)) - 1, column_letter_to_integer(m.group(1)), int(m.group(4)) - 1, column_letter_to_integer(m.group(3)))

colspanre = re.compile(r'([A-Za-z]+):([A-Za-z]+)$')
def parse_colspan(colspan):
    if len(colspan) == 1:
        diff = ord(colspan) - ord_a
        return(diff, diff)
    m = colspanre.match(colspan)
    return (column_letter_to_integer(m.group(1)), column_letter_to_integer(m.group(2)))

def range_to_a1(row, column, last_row=None, last_column=None, worksheet=None):
    if worksheet:
        if type(worksheet) is str:
            result = worksheet + '!'
        else:
            result = worksheet.title + '!'
    else:
        result = ""

    result += chr(ord_a + column) + str(row+1)
    if last_row:
        result += ':' + column_offset_to_letter(last_column) + str(last_row+1)

    return(result)

def create(title, developer_metadata=None, worksheet_data=None, named_ranges=None, spreadsheet_params=None):
    # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets#SpreadsheetProperties
    if spreadsheet_params:
        spreadsheet_properties = spreadsheet_params.copy()
    else:
        spreadsheet_properties = {}

    spreadsheet_properties['title'] = title
    # now the actual create call
    self = Spreadsheet()
    self.add_request('spreadsheets', 'create',
        callback=self.process_json,
        body={
            'properties': spreadsheet_properties,
            'sheets': worksheet_data,
            'namedRanges': named_ranges,
            'developerMetadata': developer_metadata,
        })

    #---- At present, the first sheet always has index 0 and id 0
    #     So, we can create it in place without actually commiting the callback
    self._add_uncommited_worksheet(title='Sheet1', id=0, index=0)

    return(self)

urlre = re.compile(r'https://(www\.)?(docs.google.com/spreadsheets/d/([\w\-]+))?', re.I)
def get(id, ranges=None, include_grid=False):
    #-- we will manually process full urls instead of straight ids
    isurl = urlre.match(id)
    if isurl:
        actual_id = isurl.group(3)
        if not actual_id:
            raise ValueError("Call to googleapps.sheets.get provided a URL but not an expected url to a Google spreadsheet: " + id)
        id = actual_id

    self = Spreadsheet()
    self.make_request('spreadsheets', 'get',
        callback=self.process_json,
        spreadsheetId=id, ranges=ranges, includeGridData=include_grid
    )
    return(self)
